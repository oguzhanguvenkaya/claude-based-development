---
title: "Nested Subqueries"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/02-ic-ice-query-nested-query]]"
tags:
  - sql
  - subquery
  - nested-query
  - query-composition
---

# Nested Subqueries

> One-line summary: A subquery is a SELECT that lives inside another SELECT — used to filter one table by the result of another (`WHERE col IN (SELECT ...)`) or to use a computed value inside a larger query.

## Core Concept

The subquery is the most basic form of query composition: take a SELECT, wrap it in parentheses, and use its result as an input to another SELECT. The inner query runs first; the outer query consumes its output.

Subqueries pre-date CTEs in SQL history and remain the right tool for short, one-shot composition. For multi-step pipelines or repeated computations, [[Common Table Expressions Cte]] are usually cleaner.

## How It Works

### Subquery in WHERE — set membership

```sql
-- Sales where the order used the "happy_hour" promotion code
SELECT *
FROM sales
WHERE order_id IN (
  SELECT order_id FROM orders WHERE promo_code = 'happy_hour'
);
```

The inner query returns a set of `order_id` values. The outer query keeps sales rows whose `order_id` is in that set. See [[In and Not In]].

### Subquery in FROM — derived table

```sql
SELECT segment, AVG(monthly_revenue) AS avg_rev
FROM (
  SELECT
    customer_id,
    segment,
    SUM(amount) AS monthly_revenue
  FROM orders
  WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
  GROUP BY customer_id, segment
)
GROUP BY segment;
```

The inner SELECT computes per-customer monthly revenue, and the outer SELECT averages by segment. The subquery acts as a temporary table for the outer query.

### Subquery in SELECT — scalar value

```sql
SELECT
  c.customer_id,
  c.name,
  (SELECT MAX(order_date) FROM orders WHERE customer_id = c.customer_id) AS last_order
FROM customers c;
```

A **correlated subquery**: it references the outer query (`c.customer_id`) and runs once per outer row. Powerful but slow on large tables — usually rewritable as a LEFT JOIN.

### NOT IN — the NULL trap

```sql
-- DANGER: if the subquery returns any NULL, the whole NOT IN returns no rows
SELECT * FROM customers WHERE id NOT IN (SELECT customer_id FROM excluded_list);
```

This is the same NULL trap covered in [[In and Not In]]. Safer:

```sql
SELECT * FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM excluded_list e WHERE e.customer_id = c.id);
```

### EXISTS / NOT EXISTS — yes/no subqueries

```sql
-- Customers who placed at least one order
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);

-- Customers with no orders
SELECT * FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

EXISTS only checks whether any row matches; it does not return the matching rows. Faster than `IN` for large lookup tables and immune to the NULL trap.

## Key Parameters

- **Parentheses required**: every subquery is wrapped in `()`
- **Aliases on FROM subqueries**: most engines (including BigQuery) require an alias when a subquery is in FROM
- **Correlated subqueries**: reference outer columns, run once per outer row — can be slow
- **Scalar subqueries in SELECT**: must return one row, one column, or you get an error
- **Performance**: a flat subquery + outer query is usually as fast as the equivalent JOIN; correlated subqueries are typically slower

## When To Use

- **Quick filter by another table's result**: `WHERE id IN (SELECT ...)`
- **Per-row lookups**: scalar subqueries in SELECT (consider LEFT JOIN for performance)
- **Existence checks**: `EXISTS / NOT EXISTS` for "does any match exist?"
- **Derived tables in FROM**: when one-step pre-aggregation is needed and a CTE would be overkill
- Anti-pattern: deeply nesting subqueries 3+ levels — refactor to CTEs for readability
- Anti-pattern: correlated subqueries inside SELECT on million-row tables — almost always rewrite as JOIN

## Connections

- Related: [[Common Table Expressions Cte]] (the modern alternative), [[Join vs Subquery]] (when to choose each), [[In and Not In]] (subqueries as IN sources), [[Null Handling SQL]] (the NOT IN NULL trap)
- Builds on: [[Select Statement]], [[Filtering Where]]
- Compare with: `EXISTS` (faster than IN for large sets), JOIN (often equivalent and clearer)
- Used by: nearly every multi-table analytical query in some form

## My Notes

- Mental model: a subquery is one SELECT inside another. A CTE is one SELECT named before another. The mechanics are similar; the readability differs.
- Practice: pick a query you wrote with subqueries and rewrite it with CTEs — feel the difference.
- BigQuery tip: scalar subqueries in SELECT can use partition filters but cost more than equivalent LEFT JOIN aggregations on huge tables.
- Interview gotcha: be ready to explain why `WHERE x NOT IN (SELECT y FROM ...)` returns no rows when the subquery contains NULL — it is the #1 silent-bug SQL question.
