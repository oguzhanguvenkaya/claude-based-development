---
title: "Value Preservation Test"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/11-deger-korunumu-testi]]"
tags:
  - sql
  - testing
  - data-quality
  - join-validation
  - reconciliation
---

# Value Preservation Test

> One-line summary: A SQL test that compares an aggregate total before and after a JOIN or transformation — if the totals do not match, the join silently dropped or duplicated rows.

## Core Concept

Joins are the highest-risk operation in SQL. A wrong join type drops rows; a fan-out (see [[Join Pitfalls Grain and Fan Out]]) multiplies them. Either way, your aggregate downstream is wrong, and the query runs without error.

The **Value Preservation Test** is the dedicated guard: take a known-correct aggregate (e.g., total shipping cost) from the source table, recompute it after the join, and verify the two match. If they don't, **the join changed the data** — investigate before trusting any downstream metric.

This is the test that catches the bugs no other test catches.

## How It Works

### The setup

You're joining `orders` with `shipping` on `order_id`. The finance team relies on total shipping cost. You need to prove the join preserved it.

```sql
-- Step 1: compute the total from the source
SELECT SUM(cost) AS source_total FROM shipping;
-- Suppose this returns 50000.00

-- Step 2: compute the same total after the join
SELECT SUM(s.cost) AS joined_total
FROM orders   o
JOIN shipping s ON o.id = s.order_id;
-- If this returns 50000.00 → safe to use
-- If this returns 75000.00 → fan-out; some shipping rows joined to multiple orders
-- If this returns 30000.00 → INNER drop; some shipping rows had no matching order
```

### As a single test query

```sql
WITH source AS (
  SELECT SUM(cost) AS total FROM shipping
),
joined AS (
  SELECT SUM(s.cost) AS total
  FROM orders   o
  JOIN shipping s ON o.id = s.order_id
)
SELECT
  source.total            AS source_total,
  joined.total            AS joined_total,
  joined.total - source.total AS diff
FROM source, joined
WHERE source.total != joined.total;
-- Empty result = pass; any row = totals diverged
```

### Multiple aggregates in one test

```sql
WITH expected AS (
  SELECT
    COUNT(*)   AS row_count,
    SUM(cost)  AS cost_total,
    AVG(cost)  AS cost_avg
  FROM shipping
),
actual AS (
  SELECT
    COUNT(DISTINCT s.id) AS row_count,   -- DISTINCT defends against fan-out
    SUM(s.cost)          AS cost_total,
    AVG(s.cost)          AS cost_avg
  FROM orders   o
  JOIN shipping s ON o.id = s.order_id
)
SELECT *
FROM expected, actual
WHERE expected.row_count != actual.row_count
   OR expected.cost_total != actual.cost_total;
```

The use of `COUNT(DISTINCT)` and pre-aggregating before joining are the two main defenses against fan-out — see [[Distinct and Deduplication]] and [[Join Pitfalls Grain and Fan Out]].

### Reconciliation across transformations

The same idea applies across longer pipelines:

```sql
-- Raw event count
SELECT COUNT(*) FROM raw_events;

-- After dedup
SELECT COUNT(*) FROM dedup_events;

-- After enrichment join
SELECT COUNT(*) FROM enriched_events;
```

Each step's count should be predictable. Dedup may reduce; enrichment should not change the count (with a proper LEFT JOIN). Unexplained jumps or drops = bug.

### Choosing the right "anchor" total

Pick a quantity the business already publishes externally — total monthly revenue, transaction count, unique users — and validate that every step of your pipeline preserves it. If your number diverges from finance's, you have a join (or filter) issue to find.

## Key Parameters

- **Pick anchor metrics carefully**: must be unambiguous and not subject to interpretation
- **Tolerance**: for floating-point sums, allow a tiny epsilon (`ABS(diff) < 0.01`) to avoid false positives
- **Granularity**: total across the table is the highest-level test; per-day or per-segment totals add finer-grained signal
- **Failure mode**: if the totals diverge, the next step is to find the rows responsible — anti-join queries help

## When To Use

- **After every JOIN** in a critical pipeline: the canonical defense against silent fan-out and row drops
- **After dedup or merge logic**: prove the dedup did not lose anything it shouldn't have
- **Reconciliation with external systems**: validate your warehouse total matches finance's, marketing's, ops' totals
- **Migration testing**: when moving from one schema to another, the totals should match exactly
- Anti-pattern: trusting that a row-count match implies a value match — fan-out can produce the right row count with wrong sums (especially with `COUNT(DISTINCT)`)
- Anti-pattern: skipping this test when "we already have a PK test" — they catch different bugs

## Connections

- Related: [[Testing Data Pipelines]] (parent), [[Primary Key Test]], [[Column Test]] — three complementary test families
- Builds on: [[Sum Avg Min Max]], [[Count and Countif]], [[Group By]], [[Joins Fundamentals]], [[Join Types]]
- Catches: [[Join Pitfalls Grain and Fan Out]] in a way no other test does — fan-out is invisible to PK tests on the source
- Compare with: dbt's `equal_rowcount` and `relationships` tests — narrower forms of the same idea
- Used by: every finance-grade data pipeline; reconciliation is non-negotiable when money is involved

## My Notes

- The single most valuable test for finance-related tables — when revenue is the metric, "off by 3%" is a fireable mistake.
- Practice: [Nova Finans Özeti Testi](https://nextgen.workintech.com.tr/project/202/3?pid=7600) — exactly this scenario; prove the summary table's totals match the source.
- Helpful pattern: when totals diverge, query `SELECT key, COUNT(*) FROM joined_table GROUP BY key HAVING COUNT(*) > 1` to find the duplicated keys. That is almost always the cause.
- Interview tip: when discussing data pipeline reliability, mention the three test families by name — PK, column, value preservation. Specificity signals seniority.
