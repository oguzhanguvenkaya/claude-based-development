---
title: "Common Table Expressions Cte"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/01-with-as-ile-query-tanimlama]]"
tags:
  - sql
  - cte
  - with-clause
  - query-composition
---

# Common Table Expressions Cte

> One-line summary: A Common Table Expression (CTE), written with `WITH name AS (...)`, defines a named, query-scoped temporary result you can reference like a table — used for pre-aggregations, breaking complex queries into readable steps, and avoiding repeated subqueries.

## Core Concept

When a query grows beyond a single SELECT, two strategies fight for clarity: deeply nested subqueries or temporary tables. CTEs are the third — and usually best — option. They let you **name** an intermediate result, then use that name in the main query as if it were a real table. The CTE exists only for the duration of the query; no schema changes, no cleanup.

Functionally, a CTE is roughly equivalent to a subquery you could have written inline. Practically, it transforms long queries into a top-down narrative: each CTE is a paragraph that says "first, compute this," and the main SELECT is the conclusion.

## How It Works

### Basic syntax

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS month,
    SUM(amount)                   AS revenue
  FROM orders
  GROUP BY month
)
SELECT *
FROM monthly_revenue
ORDER BY month DESC;
```

The CTE `monthly_revenue` is defined once, then queried like a table. The aggregation logic lives in one place.

### Multiple CTEs in one query

```sql
WITH
  monthly_revenue AS (
    SELECT DATE_TRUNC(order_date, MONTH) AS month, SUM(amount) AS revenue
    FROM orders
    GROUP BY month
  ),
  monthly_customers AS (
    SELECT DATE_TRUNC(order_date, MONTH) AS month, COUNT(DISTINCT customer_id) AS customers
    FROM orders
    GROUP BY month
  )
SELECT
  r.month,
  r.revenue,
  c.customers,
  SAFE_DIVIDE(r.revenue, c.customers) AS revenue_per_customer
FROM monthly_revenue   r
JOIN monthly_customers c USING (month)
ORDER BY r.month DESC;
```

Each CTE is a clear, isolated step. The final SELECT just composes them. See [[Safe Divide]] for the SAFE_DIVIDE pattern.

### A CTE can reference earlier CTEs

```sql
WITH
  raw_clean AS (
    SELECT * FROM raw_orders WHERE order_date IS NOT NULL
  ),
  by_month AS (
    SELECT DATE_TRUNC(order_date, MONTH) AS month, SUM(amount) AS revenue
    FROM raw_clean
    GROUP BY month
  )
SELECT * FROM by_month;
```

This produces a top-down pipeline within a single query — each step builds on the previous.

### CTE vs nested subquery

These two queries are equivalent in result:

```sql
-- Nested subquery (harder to read)
SELECT month, revenue / customers AS rpc
FROM (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS month,
    SUM(amount) AS revenue,
    COUNT(DISTINCT customer_id) AS customers
  FROM orders
  GROUP BY month
);

-- CTE (easier to read, especially when reused)
WITH monthly AS (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS month,
    SUM(amount) AS revenue,
    COUNT(DISTINCT customer_id) AS customers
  FROM orders
  GROUP BY month
)
SELECT month, revenue / customers AS rpc FROM monthly;
```

Same answer. The CTE form scales: when a new metric is added, you do not have to repeat the GROUP BY logic.

### Recursive CTEs (advanced)

BigQuery and most engines support recursive CTEs for hierarchical data (org charts, category trees):

```sql
WITH RECURSIVE org AS (
  SELECT employee_id, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.manager_id, o.level + 1
  FROM employees e JOIN org o ON e.manager_id = o.employee_id
)
SELECT * FROM org;
```

Advanced topic — usually you do not need it unless modeling hierarchies.

## Key Parameters

- **Scope**: a CTE lives only within the query that defines it; the next query starts fresh
- **Naming**: each CTE has a name like a table — short, snake_case, descriptive of what the step computes
- **Materialization**: in BigQuery, CTEs are typically inlined (re-evaluated each time referenced); reference a heavy CTE twice and it runs twice. Use a temp table or `CREATE TABLE` for true caching
- **Composition**: each CTE can reference earlier CTEs but not later ones

## When To Use

- **Multi-step transformations**: pre-aggregate, then join, then filter — each step its own CTE
- **Reused intermediate results**: when the same subquery appears 3+ times, refactor into a CTE
- **Readable SQL**: making a 50-line query into a top-down narrative of named steps
- **Replacing repeated subqueries**: a CTE referenced twice is one source of truth
- Anti-pattern: defining a CTE used only once and only inline — adds indirection without benefit (some still prefer it for readability)
- Anti-pattern: heavy CTEs referenced multiple times in BigQuery — each reference re-evaluates; consider materializing

## Connections

- Related: [[Nested Subqueries]] (the alternative form), [[Join vs Subquery]] (when to compose with CTEs vs joins), [[Joins with Group By]] (CTEs often hold the pre-aggregation)
- Builds on: [[Select Statement]], [[Group By]]
- Compare with: temp tables (real materialization, persist longer), views (saved across sessions), [[Create Update Delete]] CREATE TABLE AS (full materialization)
- Used by: every nontrivial analytical query; dbt models are essentially named CTEs at a project level

## My Notes

- Rule of thumb: when a query exceeds ~15 lines, refactor with CTEs. Almost always pays for itself in maintenance.
- Practice: rewrite a deeply nested query you have written before using CTEs — the gain in readability is usually dramatic.
- BigQuery tip: if a CTE is referenced more than once and is expensive, materialize it: `CREATE TEMP TABLE x AS SELECT ...` is sometimes the right choice over `WITH x AS ...`.
- Interview tip: when asked to write multi-step analysis, lead with CTEs; demonstrates clean coding instinct.
