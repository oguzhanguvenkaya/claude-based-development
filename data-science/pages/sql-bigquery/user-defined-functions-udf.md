---
title: "User Defined Functions Udf"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/02-sqlde-fonksiyon-tanimlama-ve-cagirma]]"
tags:
  - sql
  - udf
  - create-function
  - code-reuse
  - bigquery
---

# User Defined Functions Udf

> One-line summary: A user-defined function (UDF) lets you wrap a repeatable calculation or classification in a named, parameterized function that any query can call — standardizing logic, reducing duplication, and lowering the chance of inconsistent definitions across reports.

## Core Concept

The same calculation often appears in many queries: profit margin (`revenue - cost`), age bucket from a date, formatted phone numbers, currency conversion. Every analyst who writes it from scratch invites a typo or a slightly different definition. A UDF solves this: write the logic once, give it a name, call it everywhere.

In BigQuery, UDFs come in two flavors: **persistent** (stored in a dataset, available across sessions, sharable with the team) and **temporary** (only lives in the current query/session, no permission to create persistent UDFs needed).

## How It Works

### Persistent UDF — define once, reuse forever

```sql
CREATE OR REPLACE FUNCTION analytics.margin(revenue NUMERIC, cost NUMERIC)
RETURNS NUMERIC
AS (
  SAFE_DIVIDE(revenue - cost, revenue)
);
```

Now any query in any dataset can call it:

```sql
SELECT
  order_id,
  analytics.margin(revenue, cost) AS margin_pct
FROM sales.orders;
```

Stored in the `analytics` dataset, owned by whoever has CREATE FUNCTION permission there.

### Temporary UDF — defined inline in a query

```sql
CREATE TEMP FUNCTION age_bucket(age INT64) AS (
  CASE
    WHEN age < 18 THEN 'minor'
    WHEN age < 35 THEN 'young_adult'
    WHEN age < 55 THEN 'middle'
    ELSE             'senior'
  END
);

SELECT user_id, age_bucket(age) AS bucket FROM users;
```

Temporary UDFs live only for the duration of the script. Great for one-off scripts; no persistent permission needed.

### Parameters and return types

```sql
CREATE TEMP FUNCTION discount_price(
  original_price NUMERIC,
  discount_pct   NUMERIC,
  min_floor      NUMERIC
)
RETURNS NUMERIC
AS (
  GREATEST(original_price * (1 - discount_pct / 100), min_floor)
);
```

Parameters are typed. The return type is declared explicitly (`RETURNS NUMERIC`) or inferred from the SQL body if omitted.

### SQL UDF vs JavaScript UDF

BigQuery supports two implementations:

```sql
-- SQL UDF: body is a SQL expression
CREATE TEMP FUNCTION double_it(x INT64) AS (x * 2);

-- JavaScript UDF: body is JS code
CREATE TEMP FUNCTION reverse_str(s STRING)
RETURNS STRING
LANGUAGE js AS """
  return s.split('').reverse().join('');
""";
```

SQL UDFs are faster and engine-optimizable. JS UDFs run in a sandbox and are slower but handle things SQL cannot (regex with backreferences, complex string manipulation, custom hashing).

### UDF inside a window function

UDFs combine cleanly with window logic:

```sql
CREATE TEMP FUNCTION margin(rev NUMERIC, cost NUMERIC) AS (
  SAFE_DIVIDE(rev - cost, rev)
);

SELECT
  order_id,
  margin(revenue, cost)                                            AS row_margin,
  AVG(margin(revenue, cost)) OVER (PARTITION BY category)         AS category_avg_margin
FROM orders;
```

See [[Window Functions Fundamentals]].

### Limitations

- BigQuery SQL UDFs **cannot** contain a SELECT — only scalar expressions. For row-returning logic, use a view or table-valued function (TVF).
- JS UDFs are slow on huge tables; benchmark before using widely.
- UDFs cannot be used to enforce row-level security; permissions live at the table/dataset level.

## Key Parameters

- **`CREATE FUNCTION` vs `CREATE OR REPLACE FUNCTION`**: use OR REPLACE to update without first dropping
- **`TEMP`** prefix: scoped to current session; no persistent permissions required
- **`RETURNS type`**: optional but recommended — makes the interface explicit
- **Naming**: same conventions as tables — `snake_case`, descriptive
- **Dataset for persistent UDFs**: pick a dedicated one (`utils`, `udf`, `analytics`) so they are easy to find

## When To Use

- **Repeated logic across queries**: margin, age bucket, geo lookup, currency conversion
- **Standardizing business definitions**: "what does 'active customer' mean" — encode it in one UDF
- **Encapsulating ugly expressions**: nested CASE WHEN or COALESCE chains become one clean call
- Anti-pattern: a UDF used in only one query — keep it inline; UDFs are for reuse
- Anti-pattern: UDFs for things every analyst should write from scratch (basic arithmetic) — hides simple logic
- Anti-pattern: JS UDFs called on every row of a billion-row table — slow; use SQL UDFs or pre-compute

## Connections

- Related: [[Functions in SQL Overview]] (the family taxonomy), [[Window Functions Fundamentals]] (UDFs work inside window functions), [[Clean Sql Style Guide]] (UDFs are a code-reuse mechanism)
- Builds on: every scalar function used inside the UDF body
- Compare with: views (return rows, materialized differently); macros in dbt (compile-time text substitution); stored procedures (multi-statement, side effects)
- Used by: any team with a shared business-logic library — UDFs are the canonical way to standardize definitions

## My Notes

- A team's `utils` dataset full of well-named UDFs is a cultural marker — it means the team values consistency over individual flair.
- Practice: [Fonksiyonlar - Satış](https://nextgen.workintech.com.tr/project/202/5?pid=7605) — extract a recurring calculation in your sales analysis into a UDF.
- BigQuery tip: persistent UDFs require BigQuery Admin or DataEditor role on the destination dataset. Confirm permissions before assuming you can CREATE.
- Interview tip: discussing UDFs in interviews signals you have worked on production analytics — most pure-junior candidates know nothing about UDFs.
