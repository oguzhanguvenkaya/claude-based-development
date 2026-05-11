---
title: "Join vs Subquery"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/03-join-vs-nested-subquery]]"
tags:
  - sql
  - join
  - subquery
  - query-design
  - performance
---

# Join vs Subquery

> One-line summary: When two tables relate by a key, a JOIN is usually faster and clearer than a nested subquery — but subqueries (and CTEs) are better for filtering, one-shot lookups, and step-by-step composition.

## Core Concept

The same analytical question can usually be written multiple ways: with a JOIN, with a nested subquery, or with a CTE. They are often equivalent in result but differ in **readability and performance**. Choosing the right form is a small but consequential SQL skill.

The high-level rule:
- **Multiple related columns** from another table → **JOIN**
- **Single condition** based on another table's data → **subquery / CTE**
- **Multi-step pipeline** with reusable intermediates → **CTE**

## How It Works

### Scenario: get revenue + margin + carrier per order

The sales table has revenue and margin. The orders table has the carrier and order code. We need all four columns in one report.

### Subquery form (slow, painful)

```sql
SELECT
  s.order_id,
  s.revenue,
  s.margin,
  (SELECT order_code  FROM orders o WHERE o.id = s.order_id) AS order_code,
  (SELECT carrier     FROM orders o WHERE o.id = s.order_id) AS carrier
FROM sales s;
```

Each scalar subquery runs once per row of `sales`. If sales has 10 million rows, the orders table is scanned 20 million times (two subqueries × 10M rows). Result is right, performance is wrong.

### JOIN form (fast, clear)

```sql
SELECT
  s.order_id,
  s.revenue,
  s.margin,
  o.order_code,
  o.carrier
FROM sales s
JOIN orders o ON s.order_id = o.id;
```

Single pass over both tables, hash- or sort-merge join behind the scenes. Orders of magnitude faster, easier to read. See [[Joins Fundamentals]] and [[Join Types]].

### When subquery / CTE wins

Filtering — "give me X where the condition involves another table's data":

```sql
-- Subquery (clean): orders whose customer is in a target segment
SELECT * FROM orders
WHERE customer_id IN (
  SELECT id FROM customers WHERE segment = 'enterprise'
);

-- Or with EXISTS (often faster)
SELECT * FROM orders o
WHERE EXISTS (SELECT 1 FROM customers c WHERE c.id = o.customer_id AND c.segment = 'enterprise');

-- JOIN form (works but pulls in customer columns you do not need)
SELECT o.*
FROM orders    o
JOIN customers c ON o.customer_id = c.id
WHERE c.segment = 'enterprise';
```

For a pure filter (you only need rows from one side), `EXISTS` is canonical and often fastest. JOIN is fine but adds columns you might not want.

### When CTE wins

Multi-step pipelines:

```sql
WITH
  recent_orders AS (
    SELECT * FROM orders WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  ),
  by_customer AS (
    SELECT customer_id, COUNT(*) AS recent_count, SUM(amount) AS recent_revenue
    FROM recent_orders
    GROUP BY customer_id
  )
SELECT c.name, b.recent_count, b.recent_revenue
FROM customers c
JOIN by_customer b ON c.id = b.customer_id
WHERE b.recent_count >= 5;
```

A subquery or nested form would be hard to read. The CTE form reads top-to-bottom like documentation. See [[Common Table Expressions Cte]].

### Decision matrix

| Scenario | Best form |
|----------|-----------|
| Pull 2+ columns from another table | JOIN |
| Filter by existence in another table | EXISTS (preferred) or IN subquery |
| Filter by NOT existence | NOT EXISTS (avoid NOT IN) |
| Multi-step transformation, reused intermediate | CTE |
| Scalar value per row | LEFT JOIN with aggregation (avoid correlated subquery) |
| One-off ad hoc filter | Subquery (fast to write) |

## Key Parameters

- **Engine optimization**: modern engines (BigQuery, PostgreSQL, Snowflake) often rewrite IN-subqueries as semi-joins automatically; the textual form matters less than it once did
- **Correlated subquery cost**: per-row execution, slowest pattern; avoid on >1M rows
- **EXISTS short-circuits**: stops at first match per outer row, often faster than IN
- **Readability beats micro-optimization**: pick the clearest form; only optimize when you have measured slowness

## When To Use

- **JOIN**: structural combination of tables for analysis
- **Subquery / IN**: filtering by simple criteria from another table
- **EXISTS / NOT EXISTS**: existence checks, especially with NULL-safe semantics
- **CTE**: multi-step queries with named intermediate results
- Anti-pattern: correlated scalar subquery in SELECT on huge tables — use LEFT JOIN
- Anti-pattern: deeply nested subqueries when CTEs would read cleanly

## Connections

- Related: [[Common Table Expressions Cte]], [[Nested Subqueries]], [[Joins Fundamentals]], [[Join Types]], [[In and Not In]]
- Builds on: [[Select Statement]], [[Filtering Where]]
- Compare with: temp tables (real materialization, persists), views (saved across sessions)
- Used by: every multi-table analysis; the choice shapes both performance and maintainability

## My Notes

- A useful sanity check: run `EXPLAIN` (or BigQuery's query plan) on both forms — modern optimizers often plan them identically. When they don't, the explanation usually reveals which form is more efficient.
- Practice: rewrite one query in all three forms (subquery, JOIN, CTE) on a sample dataset and time each. Builds intuition.
- BigQuery tip: `SEMI JOIN` and `ANTI JOIN` are explicit syntax for EXISTS / NOT EXISTS patterns — clearer when supported.
- Interview tip: when given a join-vs-subquery question, mention both correctness AND performance — sets you apart from candidates who only argue style.
