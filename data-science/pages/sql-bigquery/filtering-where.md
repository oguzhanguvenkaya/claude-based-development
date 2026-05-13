---
title: "Filtering Where"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/07-verileri-filtreleme-where]]"
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/08-diger-anahtar-kelimelerle-filtreleme]]"
tags:
  - sql
  - where
  - filtering
  - boolean-logic
---

# Filtering Where

> One-line summary: The WHERE clause restricts a query to rows matching a boolean condition, supporting comparison operators (=, <, >), range filters (BETWEEN), and boolean combinators (AND, OR, NOT).

## Core Concept

Most queries do not want every row — they want a subset. `WHERE` is the gate. The database evaluates the condition against each row and keeps only the rows where it returns `TRUE`. Rows where the condition is `FALSE` or `NULL` are excluded.

WHERE turns SQL from "show me everything" to "show me what matters." Every nontrivial analysis depends on it.

## How It Works

### Basic comparison operators

```sql
SELECT * FROM customers
WHERE city = 'New York';

SELECT * FROM orders
WHERE amount > 10000;

SELECT * FROM products
WHERE stock <= 5;
```

Operators: `=`, `!=` (or `<>`), `<`, `<=`, `>`, `>=`.

### Combining conditions: AND, OR, NOT

```sql
-- All three must be true
SELECT * FROM customers
WHERE city = 'New York' AND signup_date >= '2024-01-01' AND is_active = TRUE;

-- At least one must be true
SELECT * FROM products
WHERE category = 'electronics' OR price > 1000;

-- NOT inverts the condition
SELECT * FROM customers
WHERE NOT city = 'Boston';  -- equivalent to city != 'Boston'
```

`AND` binds tighter than `OR`. Use parentheses when mixing them:

```sql
-- Customers in NY who either spent >$1000 OR signed up recently
WHERE city = 'New York' AND (lifetime_spend > 1000 OR signup_date >= '2025-01-01');
```

Without parentheses, the engine reads `A AND B OR C` as `(A AND B) OR C`, which is almost never what you mean.

### Range filtering: BETWEEN

```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31';
```

Inclusive on both ends. Equivalent to `order_date >= '2025-01-01' AND order_date <= '2025-01-31'`. Cleaner for date ranges.

### NULL caveat

`WHERE column = NULL` does **not** work. NULL is "unknown" — comparing to it always returns NULL, which excludes the row. Use `IS NULL` / `IS NOT NULL` instead (see [[Null Handling SQL]]).

## Key Parameters

- **WHERE runs before SELECT**: you cannot reference a column alias defined in SELECT inside WHERE
- **Short-circuit evaluation**: most engines stop evaluating an AND chain after the first FALSE — order conditions cheapest first
- **Indexes**: if the column in WHERE has an index, the query is fast; without an index, it scans the whole table
- **String literals**: use single quotes `'New York'`, not double quotes (which mean identifiers in standard SQL)

## When To Use

- **Always**, except for full-table exports
- Restricting to a date range, a customer segment, a geography, an active status
- Excluding nulls, outliers, or sentinel values before aggregating
- Anti-pattern: filtering after aggregating when you could have filtered before — moves more data through GROUP BY than necessary. Filter early; aggregate late.
- Anti-pattern: `WHERE date_col > NOW() - INTERVAL '7 day'` when an indexed column exists — wraps the column in a function and disables index use in some engines

## Connections

- Related: [[Select Statement]] (WHERE filters the rows that SELECT projects), [[In And Not In]] (cleaner alternative to long OR chains)
- Builds on: boolean algebra (AND/OR/NOT), three-valued logic (TRUE/FALSE/NULL)
- Compare with: [[Where vs Having]] — HAVING filters **after** GROUP BY, on aggregates instead of rows
- Used by: [[Conditional Expressions SQL]], [[Pattern Matching SQL]], [[Group By]], [[Date Arithmetic Date Sub]] (date range filters), every analytical query. The spreadsheet equivalent is [[Filter Query Unique Sheets]] (FILTER / QUERY).

## My Notes

- Three-valued logic catches people: `NULL = NULL` returns NULL, not TRUE. Always use IS NULL.
- Practice: [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523) — practice combining filters for segment definitions.
- Interview tip: when asked "what's the difference between WHERE and HAVING?", answer with execution order — WHERE is pre-aggregation, HAVING is post-aggregation.
- In BigQuery, WHERE on a partitioned column reduces cost dramatically. Always include the partition filter when querying large tables. See [[Partitioning and Clustering]].
