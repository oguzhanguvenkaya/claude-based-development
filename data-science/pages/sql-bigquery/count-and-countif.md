---
title: "Count and Countif"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/02-count-countif]]"
tags:
  - sql
  - count
  - countif
  - aggregation
  - row-counting
---

# Count and Countif

> One-line summary: COUNT counts rows (all, non-NULL, or distinct); COUNTIF (BigQuery) counts rows satisfying a boolean condition — the canonical building block for "how many of X?" questions.

## Core Concept

Every analytical question that begins with "how many" maps to some form of COUNT. The flavors differ in what gets counted: every row, only rows where a column is filled in, only unique values, or only rows that match a condition.

Think of each variant as a different click counter placed at a different checkpoint in the data pipeline.

## How It Works

### COUNT(*) — every row

```sql
SELECT COUNT(*) AS total_orders FROM orders;
```

Counts every row, including those with all NULLs. This is "how big is this table?"

### COUNT(column) — non-NULL rows

```sql
SELECT COUNT(phone) AS phone_filled FROM customers;
```

Counts only rows where `phone` is not NULL. Useful for data completeness audits. The gap between `COUNT(*)` and `COUNT(column)` equals the NULL count — see [[Null Handling SQL]].

### COUNT(DISTINCT column) — unique values

```sql
SELECT COUNT(DISTINCT customer_id) AS unique_customers FROM orders;
```

How many different customers placed at least one order? Note: NULLs are excluded from `COUNT(DISTINCT ...)`. See [[Distinct and Deduplication]].

### COUNTIF — count rows matching a condition (BigQuery)

```sql
SELECT
  COUNTIF(amount > 100)              AS high_value_orders,
  COUNTIF(status = 'cancelled')      AS cancellations,
  COUNTIF(amount > 100 AND status = 'paid') AS paid_high_value
FROM orders;
```

`COUNTIF(condition)` is sugar for `COUNT(CASE WHEN condition THEN 1 END)` — see [[Conditional Expressions SQL]]. Cleaner and the same performance.

### Combining with GROUP BY

```sql
SELECT
  city,
  COUNT(*)                    AS total_customers,
  COUNTIF(is_premium)         AS premium_customers,
  COUNT(DISTINCT signup_year) AS distinct_signup_years
FROM customers
GROUP BY city;
```

One row per city, three counts per row. This is the bread-and-butter aggregate query. See [[Group By]].

## Key Parameters

- **`*` vs column**: `*` counts rows; a column counts non-NULL values
- **DISTINCT modifier**: deduplicates before counting
- **COUNTIF condition**: any boolean expression — comparisons, AND/OR, function calls
- **APPROX_COUNT_DISTINCT**: BigQuery fast approximate variant (±1% error, orders of magnitude faster on huge tables)
- **Performance**: COUNT(*) is the fastest aggregate; COUNT(DISTINCT col) can be slow on billion-row tables

## When To Use

- "How many X are there?" → COUNT(*)
- "How many of them have Y filled in?" → COUNT(Y)
- "How many distinct values of Z?" → COUNT(DISTINCT Z)
- "How many match condition C?" → COUNTIF(C)
- Combined with GROUP BY for "how many per category"
- Anti-pattern: `COUNT(1)` vs `COUNT(*)` — identical in modern engines; the "performance trick" is folklore
- Anti-pattern: `COUNT(DISTINCT col)` on billion-row tables when ±1% is acceptable — use APPROX_COUNT_DISTINCT

## Connections

- Related: [[Sum Avg Min Max]] (other aggregates), [[Group By]] (split COUNTs by category), [[Conditional Expressions SQL]] (COUNTIF is sugar over CASE WHEN)
- Builds on: [[Distinct and Deduplication]] (COUNT DISTINCT uses the same set logic), [[Null Handling SQL]] (NULL handling drives the difference between COUNT(*) and COUNT(col))
- Compare with: `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` — equivalent to COUNTIF, more portable across engines
- Used by: [[Measures of Central Tendency]] (the n in mean = sum / n)

## My Notes

- The single most useful diagnostic query: `SELECT COUNT(*), COUNT(col) FROM table` — instantly tells you the NULL rate of a column.
- Practice: [Circle Stok Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7593) — count inventory rows by various conditions.
- BigQuery tip: `COUNT(*) OVER (PARTITION BY col)` is the window-function variant — see [[Window Functions Fundamentals]].
- Interview tip: be ready to explain why `COUNT(*) > COUNT(col)` when `col` has NULLs.
