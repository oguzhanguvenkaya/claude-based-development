---
title: "Group By"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/05-group-by]]"
tags:
  - sql
  - group-by
  - aggregation
  - breakdown
---

# Group By

> One-line summary: GROUP BY collapses rows that share the same values in one or more columns into a single row per group, letting aggregates (SUM, COUNT, AVG) compute per category instead of globally.

## Core Concept

A bare aggregate like `SELECT SUM(amount) FROM orders` returns one number for the whole table — total revenue. But the more useful question is almost always "total revenue **per category**." That is what `GROUP BY` does: it splits the table into buckets defined by the grouping columns, then runs the aggregate inside each bucket.

The result has one row per distinct combination of grouping column values. Each non-aggregate column in the SELECT clause must either appear in the GROUP BY or itself be wrapped in an aggregate — this is the **single most enforced SQL rule** by database engines.

## How It Works

### Basic syntax

```sql
SELECT
  city,
  COUNT(*)       AS customer_count,
  AVG(spend)     AS avg_spend
FROM customers
GROUP BY city;
```

Output: one row per city. The grouping column (`city`) appears as-is; everything else is aggregated.

### Group by multiple columns

```sql
SELECT
  country,
  city,
  COUNT(*) AS customer_count
FROM customers
GROUP BY country, city;
```

One row per `(country, city)` combination. Order in GROUP BY does not matter for the result, but it can matter for query plans.

### Group by expression

```sql
SELECT
  EXTRACT(MONTH FROM order_date) AS order_month,
  SUM(amount)                    AS revenue
FROM orders
GROUP BY order_month;
```

You can group by computed values, not just raw columns. BigQuery allows referencing the SELECT alias in GROUP BY (more portable: repeat the expression).

### The single rule

Every column in SELECT must be either:
1. A grouping column (listed in GROUP BY), or
2. Inside an aggregate function (`SUM`, `COUNT`, `AVG`, `MIN`, `MAX`)

```sql
-- WRONG — first_name is neither grouped nor aggregated
SELECT city, first_name, COUNT(*)
FROM customers
GROUP BY city;
-- ERROR

-- RIGHT — first_name is aggregated (we pick one)
SELECT city, ANY_VALUE(first_name), COUNT(*)
FROM customers
GROUP BY city;
```

`ANY_VALUE(col)` returns an unspecified value from the group — useful when you know all values in the group are the same.

### Order of execution

```
FROM        → read source
WHERE       → filter rows
GROUP BY    → bucket rows
HAVING      → filter groups
SELECT      → compute aggregates and project
ORDER BY    → sort final result
```

WHERE filters **before** GROUP BY; HAVING filters **after**. See [[Where vs Having]].

## Key Parameters

- **Grouping columns**: any number; combination defines the granularity
- **Aggregates allowed in SELECT**: SUM, COUNT, AVG, MIN, MAX, STDDEV, ARRAY_AGG, STRING_AGG, etc.
- **NULL behavior**: NULL is treated as its own group — all rows with NULL in the grouping column collapse together
- **`GROUP BY ALL`** (BigQuery): groups by every non-aggregate column in SELECT automatically — convenient shorthand
- **GROUPING SETS / ROLLUP / CUBE**: produce multiple grouping levels in one query (advanced)

## When To Use

- Any "per category" breakdown — per day, per region, per product
- Cohort summaries (sign-up month vs revenue)
- Quality audits — count rows per status, per source, per error_code
- Pivot-style reports (combined with [[Conditional Expressions SQL]])
- Anti-pattern: GROUP BY on a column that is unique per row (like primary key) — produces N groups of 1 row each, identical to no GROUP BY but slower
- Anti-pattern: forgetting that NULL groups together — silently merges rows you may not want merged

## Connections

- Related: [[Count and Countif]], [[Sum Avg Min Max]] (the aggregates GROUP BY enables), [[Where vs Having]] (pre vs post filter), [[Distinct and Deduplication]] (DISTINCT is equivalent to GROUP BY without aggregates)
- Builds on: [[Select Statement]], [[Filtering Where]]
- Compare with: [[Window Functions Fundamentals]] (`SUM(x) OVER (PARTITION BY y)`) — same partitioning idea but every original row is preserved
- Used by: every dashboard query, every cohort analysis, every per-segment KPI; especially relevant after joins — see [[Joins with Group By]] and [[Join Pitfalls Grain and Fan Out]]. The spreadsheet equivalent is [[Pivot Tables Sheets]].

## My Notes

- Rule of thumb: if your SELECT has any aggregate function, you almost certainly need GROUP BY.
- Practice: [Greenweez Satışlar](https://nextgen.workintech.com.tr/project/202/2?pid=7597) — break down sales by region, by month, by product category.
- BigQuery tip: `GROUP BY ALL` is great for exploration; once the query stabilizes, list the columns explicitly for readability.
- Interview gotcha: "what does GROUP BY do with NULL?" Answer: NULL is its own group; all NULL-grouping rows collapse into one.
- Performance: in BigQuery, GROUP BY on a clustered column is fast; on an unclustered high-cardinality column, it triggers a shuffle.
