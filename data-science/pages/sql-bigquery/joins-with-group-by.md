---
title: "Joins with Group By"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/06-join-ve-group-by]]"
tags:
  - sql
  - join
  - group-by
  - aggregation
  - common-mistakes
---

# Joins with Group By

> One-line summary: When you aggregate a joined result, every non-aggregate column must appear in GROUP BY — the rule of [[Group By]] applied to the wider, joined virtual table.

## Core Concept

Once two or three tables are stitched together with JOIN, the next step is usually "summarize." Sum the revenue per customer. Count purchases per product category. Average order value per region. These all combine **JOIN** (which wide row do I want?) and **GROUP BY** (which dimensions do I bucket by?).

The error mode is universal: putting a non-aggregate column from the joined result in SELECT without listing it in GROUP BY. The engine rejects the query, but new analysts often misread the error and try increasingly wrong fixes.

## How It Works

### The setup

```
purchases   products   buyers
─────────   ────────   ──────
id          id         id
product_id  name       name
buyer_id    price      email
quantity    category
```

Question: "How much did each buyer spend on each product?"

### The query

```sql
SELECT
  b.name       AS buyer_name,
  pr.name      AS product_name,
  SUM(pu.quantity * pr.price) AS total_spend
FROM purchases pu
JOIN products  pr ON pu.product_id = pr.id
JOIN buyers    b  ON pu.buyer_id   = b.id
GROUP BY b.name, pr.name;
```

Three tables joined → one wide virtual row per purchase. Then GROUP BY collapses those wide rows into (buyer, product) buckets, summing `quantity * price` within each.

### The common error

```sql
-- ERROR: pu.id is not in GROUP BY and not aggregated
SELECT
  b.name,
  pr.name,
  pu.id,                            -- ← orphan column
  SUM(pu.quantity * pr.price)
FROM purchases pu
JOIN products pr ON pu.product_id = pr.id
JOIN buyers   b  ON pu.buyer_id   = b.id
GROUP BY b.name, pr.name;
```

The engine cannot decide which `pu.id` to show for each (buyer, product) group — there might be many purchases. Fix one of three ways:

1. **Add the column to GROUP BY** — if you want one row per (buyer, product, purchase_id), which usually means you do not want aggregation at all
2. **Aggregate the column** — `MIN(pu.id)`, `MAX(pu.id)`, or `ARRAY_AGG(pu.id)` if you want to keep the values
3. **Drop the column** — usually the right answer; if it does not survive a GROUP BY, you probably did not need it

### Pre-aggregating to keep things sane

```sql
-- Pre-aggregate purchases by buyer + product, THEN join
WITH purchase_summary AS (
  SELECT
    buyer_id,
    product_id,
    SUM(quantity) AS qty
  FROM purchases
  GROUP BY buyer_id, product_id
)
SELECT
  b.name,
  pr.name,
  ps.qty * pr.price AS total_spend
FROM purchase_summary ps
JOIN products pr ON ps.product_id = pr.id
JOIN buyers   b  ON ps.buyer_id   = b.id;
```

Aggregating before joining is often clearer than aggregating after — fewer columns to think about in the GROUP BY.

### COUNT(DISTINCT) after a join — watch out

```sql
-- "How many unique customers bought each product?"
SELECT
  pr.id,
  pr.name,
  COUNT(DISTINCT pu.buyer_id) AS unique_buyers
FROM products pr
LEFT JOIN purchases pu ON pr.id = pu.product_id
GROUP BY pr.id, pr.name;
```

A naive `COUNT(*)` here would count purchases, not unique buyers. DISTINCT is essential when joins introduce fan-out. See [[Distinct and Deduplication]] and [[Count and Countif]].

## Key Parameters

- **Every non-aggregate goes into GROUP BY**: applies to columns from any joined table
- **`SELECT col, COUNT(*)`** without GROUP BY: error
- **`GROUP BY id` plus other columns of the same table**: many engines (BigQuery, MySQL) allow this if `id` functionally determines the others (called *functional dependency*); most engines do not
- **`GROUP BY ALL`** (BigQuery): groups by every non-aggregate SELECT column automatically — useful when columns are many

## When To Use

- Per-category metrics: revenue per buyer, count per product, average per region
- Cohort or segment summaries that pull dimensions from joined tables
- Fact + dimension star-schema queries with totals
- Anti-pattern: forgetting that an aggregate after a fan-out join (one-to-many) double-counts — see [[Join Pitfalls Grain and Fan Out]]
- Anti-pattern: SUM on a foreign-key column — meaningless arithmetic on identifiers

## Connections

- Related: [[Group By]] (the underlying rule), [[Where vs Having]] (filter joined rows before grouping), [[Joins Fundamentals]], [[Multiple Joins]], [[Join Pitfalls Grain and Fan Out]]
- Builds on: [[Sum Avg Min Max]] (the aggregates you usually apply), [[Count and Countif]]
- Compare with: [[Window Functions Fundamentals]] (`SUM(x) OVER (PARTITION BY y)`) — same grouping idea but rows are preserved. [[Window Functions Across Grain]] is the canonical fix for fan-out without sacrificing row detail.
- Used by: virtually every dashboard SQL query

## My Notes

- Defensive workflow: write the JOINs first, run a `SELECT *` with `LIMIT 100` to verify the joined shape, **then** add the aggregations.
- Practice: [Greenweez Finans - JOIN](https://nextgen.workintech.com.tr/project/202/3?pid=7599) — produce a per-buyer or per-product revenue summary using 2-3 joined tables.
- The "I keep getting an error about GROUP BY" feeling is almost always solved by re-reading every SELECT column and asking: is this a grouping column or an aggregate?
- BigQuery tip: when prototyping, `GROUP BY ALL` lets you focus on the SELECT list and worry about grouping mechanically. Switch to explicit GROUP BY columns in production for clarity.
