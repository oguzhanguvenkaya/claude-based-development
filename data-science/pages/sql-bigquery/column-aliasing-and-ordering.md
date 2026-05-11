---
title: "Column Aliasing and Ordering"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/11-takma-adlar-aliasing]]"
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/12-order-by-ile-siralama]]"
tags:
  - sql
  - alias
  - order-by
  - presentation
---

# Column Aliasing and Ordering

> One-line summary: AS renames columns and tables in the output for readability, while ORDER BY sorts the result rows; together they form the presentation layer of SQL.

## Core Concept

Raw SQL output often looks ugly — column names like `cust_first_nm` or `tot_amt_usd_cents` are great for storage but terrible for stakeholders. **Aliasing** with `AS` lets you rename columns (and tables) in the result. **ORDER BY** controls row order, which SQL does not guarantee by default.

Both clauses are about communication, not computation: they do not change what data is returned, only how it is labeled and arranged.

## How It Works

### Column aliases

```sql
SELECT
  first_name AS name,
  last_name AS surname,
  customer_id AS id,
  signup_date AS member_since
FROM customers;
```

`AS` is optional in most engines:

```sql
SELECT first_name name, last_name surname FROM customers;
-- Works, but `AS` is clearer.
```

### Aliasing computed columns (required, not optional)

```sql
SELECT
  first_name,
  last_name,
  CONCAT(first_name, ' ', last_name) AS full_name,
  amount * 1.18 AS amount_with_tax
FROM customers;
```

Without the alias, the column header would be the entire expression, which is unusable downstream.

### Table aliases

In multi-table queries, table aliases shorten references:

```sql
SELECT c.first_name, o.amount
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id;
```

### ORDER BY — basic sort

```sql
SELECT * FROM customers
ORDER BY last_name;            -- ascending (default)

SELECT * FROM customers
ORDER BY signup_date DESC;     -- newest first
```

### Multi-column sort

```sql
SELECT * FROM customers
ORDER BY country ASC, last_name ASC, first_name ASC;
```

Sorted by country first, then last name within each country, then first name within each (country, last name) pair.

### Sort by computed column

```sql
SELECT
  customer_id,
  amount * 1.18 AS total_with_tax
FROM orders
ORDER BY total_with_tax DESC;
```

You can reference the alias in ORDER BY because ORDER BY runs **after** SELECT.

### Sort by position (avoid)

```sql
SELECT first_name, last_name FROM customers ORDER BY 2;
-- Sorts by the 2nd column. Fragile — breaks if you reorder SELECT.
```

## Key Parameters

- **AS keyword**: optional for columns and tables in most engines; required only when you want clarity
- **ASC / DESC**: per-column, defaults to ASC
- **NULLS FIRST / NULLS LAST**: explicit control over where NULLs sort (not all engines support this)
- **ORDER BY in subqueries**: usually ignored — only the outermost ORDER BY of a query matters
- **Performance**: ORDER BY on a large unindexed column is expensive; in BigQuery, prefer `ORDER BY` only on the final result set, not inside CTEs

## When To Use

- **Always alias computed columns** — without an alias, the column name is the expression
- **Always alias tables in multi-table queries** — keeps queries readable
- **ORDER BY** for any output a human will read (reports, dashboards, CSV exports)
- **ORDER BY** to control "top N" results (`ORDER BY revenue DESC LIMIT 10`)
- Anti-pattern: ordering by column position (`ORDER BY 2`) in shared SQL — fragile to refactors
- Anti-pattern: ORDER BY inside a subquery — most engines discard it

## Connections

- Related: [[Select Statement]] (aliasing is part of SELECT), [[Distinct and Deduplication]] (DISTINCT + ORDER BY interact carefully)
- Builds on: nothing — pure presentation
- Compare with: doing the same sort in a downstream tool (BI dashboard, pandas) — usually better in SQL when the result set is small
- Used by: [[Conditional Expressions SQL]] (computed columns from CASE WHEN typically need aliases), every report query

## My Notes

- Convention: use snake_case aliases that are valid identifiers (`full_name`, not `Full Name`). Saves headaches when chaining queries.
- Practice: present a clean report in [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523) — rename columns to business-friendly names.
- BigQuery tip: in the Console, you can sort by clicking column headers — useful for exploration but the underlying query has no ORDER BY, so the original engine order applies on export.
- Interview gotcha: "Can you ORDER BY an alias defined in SELECT?" Yes (ORDER BY runs after SELECT). Can you do it in WHERE? No (WHERE runs before SELECT).
