---
title: "Join Pitfalls Grain and Fan Out"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/07-join-dikkat-edilmesi-gerekenler]]"
tags:
  - sql
  - join
  - grain
  - fan-out
  - data-quality
  - anti-patterns
---

# Join Pitfalls Grain and Fan Out

> One-line summary: Most join bugs come from mismatched grain (one side has finer-grained rows than the other), causing fan-out (row multiplication) or the wrong join type silently dropping or duplicating data.

## Core Concept

Two tables are safe to join when they share the **same grain** — the same conceptual level of detail. Orders and customers share grain via `customer_id` (one customer ↔ many orders, that is fine). Orders and order_line_items do not: each order has multiple line items, so joining without aggregation **fans out** — every order row gets duplicated by its line count.

Fan-out is the silent killer of join-based aggregates. Revenue suddenly looks 3x what it should. Stock counts triple. Customer counts inflate. The query runs without error; the result is just wrong.

This page collects the patterns to detect and prevent it.

## How It Works

### What "grain" means

A table's grain is the question "**what does one row represent?**"

| Table | Grain |
|-------|-------|
| `customers` | One customer |
| `orders` | One order |
| `order_line_items` | One product within one order |
| `daily_sales` | One day per store |
| `events` | One user action |

If you join two tables of different grain, the coarser side gets multiplied by the finer side. Joining `orders` to `order_line_items` on `order_id` produces one row per line item — and any column from `orders` (like `total_amount`) now appears multiple times.

### The fan-out bug

```sql
-- WRONG — total_amount is double-counted because each order has multiple line items
SELECT
  o.customer_id,
  SUM(o.total_amount) AS lifetime_value
FROM orders            o
JOIN order_line_items  li ON o.id = li.order_id
GROUP BY o.customer_id;
```

If an order has 3 line items, `o.total_amount` appears 3 times in the joined result and gets summed 3 times. The fix is either:
- Do not join `order_line_items` at all (you do not need it)
- Pre-aggregate `order_line_items` to one row per order before joining
- Use `SELECT DISTINCT` carefully — see [[Distinct and Deduplication]]

### Pre-aggregating to match grain

```sql
WITH line_summary AS (
  SELECT
    order_id,
    SUM(quantity * unit_price) AS line_total,
    COUNT(*)                    AS line_count
  FROM order_line_items
  GROUP BY order_id
)
SELECT
  o.customer_id,
  SUM(o.total_amount) AS lifetime_value,
  SUM(ls.line_count)  AS total_lines_purchased
FROM orders       o
JOIN line_summary ls ON o.id = ls.order_id
GROUP BY o.customer_id;
```

Now both sides of the join have grain = "one order" → no fan-out, no double-counting.

### Wrong join type silently drops data

```sql
-- INNER drops orders without shipments — undercounts revenue
SELECT SUM(o.total_amount) AS revenue
FROM orders     o
JOIN shipments  s ON o.id = s.order_id;

-- LEFT keeps all orders — correct revenue
SELECT SUM(o.total_amount) AS revenue
FROM orders     o
LEFT JOIN shipments s ON o.id = s.order_id;
```

The first looks innocent but quietly drops every unshipped order. Always ask: do I need rows from the right side, or only when matched?

### NULL keys silently drop rows in INNER

```sql
-- INNER JOIN drops rows where order.customer_id IS NULL (guest checkouts)
SELECT COUNT(*) FROM orders o INNER JOIN customers c ON o.customer_id = c.id;
```

NULL never equals anything. Guest orders disappear from this count. Fix by switching to LEFT JOIN or filtering NULLs upstream.

### Duplicate keys on the "lookup" side

```sql
-- If countries table has 2 rows for the same code (data quality bug), every order joining to it doubles
SELECT o.id, c.name
FROM orders   o
JOIN countries c ON o.country_code = c.code;
```

Always verify the lookup side has unique join keys — that is exactly what the [[Primary Key Test]] is for.

## Key Parameters

- **Grain check**: before joining, verify which side is finer and decide whether to aggregate it first
- **Row count sanity**: result row count should equal the larger side for one-to-many, or stay flat for one-to-one
- **Join key uniqueness**: the right side's join key should be unique unless fan-out is intended
- **Anti-join pattern**: LEFT JOIN + WHERE right.id IS NULL for "find the missing"

## When To Use

- **Always run a row-count check** after any JOIN before aggregating
- **Pre-aggregate the finer-grained side** when you only need its summary
- **Switch from INNER to LEFT** when the right side is allowed to be missing
- Anti-pattern: trusting that the join "looks right" because it returns rows — wrong joins return rows too
- Anti-pattern: chaining 5+ JOINs without checking row counts at each step

## Connections

- Related: [[Joins Fundamentals]], [[Join Types]] (the wrong type is half the pitfall), [[Multiple Joins]] (fan-out compounds in chains), [[Joins with Group By]] (aggregating after fan-out double-counts), [[Distinct and Deduplication]] (a workaround for fan-out, not a fix), [[Window Functions Across Grain]] (the elegant per-row allocation fix)
- Builds on: [[Relational Data Model]] (PK/FK uniqueness assumptions), [[Null Handling SQL]] (NULL in join keys)
- Tested by: [[Primary Key Test]], [[Value Preservation Test]] — the dedicated tests for these exact bugs
- Used by: every analytical query that aggregates joined data

## My Notes

- **Number one defensive habit**: after every JOIN in a draft query, run `SELECT COUNT(*) FROM …` and sanity-check the row count.
- Practice: [Nova Finans Özeti Testi](https://nextgen.workintech.com.tr/project/202/3?pid=7600) — build a finance summary, then verify totals match a known reference (this is exactly the value preservation test).
- The hardest join bug to spot is "everything looks fine, totals are slightly off." Symptom: revenue is 2.7x what it should be, not 2.0x — fan-out from a many-to-many join.
- Interview tip: when discussing a tricky SQL bug, mention "grain" explicitly — interviewers love hearing the word from a candidate.
