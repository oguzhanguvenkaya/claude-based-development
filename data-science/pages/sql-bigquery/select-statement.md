---
title: "Select Statement"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/05-select]]"
tags:
  - sql
  - select
  - projection
  - query-basics
---

# Select Statement

> One-line summary: The fundamental SQL command that retrieves data from one or more tables, controlling which columns appear in the result.

## Core Concept

`SELECT` is the verb of SQL. Every read query begins with it. The clause tells the database **which columns** to return, while `FROM` tells it **which table** to read from. Together they form the minimum viable query: "show me these columns from that table."

Think of a database table as a closet full of clothes. `SELECT *` is "show me everything." `SELECT shirts` is "only show me shirts." The flexibility of choosing what to project is what separates SQL from a flat data dump.

## How It Works

### Minimum query

```sql
SELECT * FROM customers;
```

`*` means "all columns." Useful for quickly inspecting a table, but rarely what you want in production reports — it returns every byte, including columns you don't need.

### Selecting specific columns

```sql
SELECT first_name, last_name, email
FROM customers;
```

Only the listed columns are returned, in the order you list them. The order can matter for downstream consumers (CSV exports, dashboards).

### Computed columns

You can include expressions, not just column names:

```sql
SELECT
  first_name,
  last_name,
  CONCAT(first_name, ' ', last_name) AS full_name,
  signup_date,
  DATE_DIFF(CURRENT_DATE(), signup_date, DAY) AS days_since_signup
FROM customers;
```

The result becomes a virtual table that did not exist on disk — SQL computes it on the fly. Aliases (`AS full_name`) name these computed columns. See [[Column Aliasing and Ordering]].

### Order of execution vs order of writing

SQL is written `SELECT ... FROM ... WHERE ...` but the engine **executes in a different order**:

1. `FROM` (read the source)
2. `WHERE` (filter rows)
3. `GROUP BY`, `HAVING` (aggregate)
4. `SELECT` (project columns)
5. `ORDER BY` (sort)
6. `LIMIT` (cut)

This matters: you cannot reference a `SELECT` alias inside `WHERE` because `WHERE` runs first.

## Key Parameters

- **`*` (asterisk)**: all columns. Convenient for exploration, wasteful in production.
- **Column order in SELECT**: determines output column order — important for downstream consumers
- **Computed expressions**: any function or operator can appear in a SELECT list — `ROUND()`, `CONCAT()`, arithmetic, etc.
- **Subqueries in SELECT**: scalar subqueries can return one value per row (advanced; see [[Ctes and Subqueries]] in later lessons)

## When To Use

- **Always** — every analytical question starts with a SELECT
- **Exploration**: `SELECT * FROM table LIMIT 10` is the universal first move in a new dataset
- **Reports**: SELECT only the columns the stakeholder asked for; reducing output saves cost in BigQuery (column scanning is billed)
- **Anti-pattern**: `SELECT *` in production queries — it inflates compute cost, breaks if columns are added or removed, and leaks columns the consumer should not see (PII, internal flags)

## Connections

- Related: [[Distinct and Deduplication]] (modifier to SELECT), [[Filtering Where]] (next clause in pipeline), [[Column Aliasing and Ordering]] (the presentation layer on top of SELECT)
- Builds on: [[Relational Data Model]] (you select from tables)
- Compare with: spreadsheet "hide column" — the same effect, but SQL is composable and scalable
- Used by: every other SQL operation — [[Group By]], aggregates ([[Count and Countif]], [[Sum Avg Min Max]]), JOINs and window functions all start with SELECT

## My Notes

- In BigQuery, **column pruning** is a real cost concern. `SELECT *` from a 1 TB table can cost $5+; `SELECT one_column` from the same table might cost $0.10. See [[Bigquery Query Cost Model]] for the full cost mechanics.
- Practice: [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523) — practice listing columns explicitly.
- Interview tip: when asked "how do you debug a slow query?", an early answer is "remove SELECT * and project only the columns I need."
- Tooling tip: most SQL IDEs auto-complete column names after `SELECT` — learn the keyboard shortcut.
