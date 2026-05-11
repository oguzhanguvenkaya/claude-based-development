---
title: "SQL Computed Data Overview"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/01-aggregate-fonksiyonu-nedir]]"
tags:
  - sql
  - aggregation
  - scalar-functions
  - overview
  - umbrella
---

# SQL Computed Data Overview

> One-line summary: A map of the SQL building blocks that produce *new* values from existing ones — aggregates that reduce many rows to one, and scalar functions that reshape single values per row.

## Core Concept

The first SQL lesson ([[SQL Fundamentals Overview]]) covered *reading* data: SELECT, WHERE, ORDER BY. This lesson is about *computing* new data: turning many rows into summaries (aggregates) or transforming each row into a cleaner / friendlier form (scalar functions).

The split matters because the two families behave differently:

- **Aggregates** (SUM, COUNT, AVG, MIN, MAX, COUNTIF) collapse N rows into 1 row per group — they require GROUP BY when used with non-aggregate columns.
- **Scalar functions** (ROUND, CONCAT, REPLACE, LOWER, DATE_SUB) operate row-by-row — the result still has N rows, just with transformed values.

An analyst's daily SQL almost always combines both: clean the strings, normalize the case, parse the dates (scalars), then sum the amounts and count the customers per group (aggregates).

## How It Works — The Concept Map

### Aggregate Functions (rows → summary)

- [[Count and Countif]] — COUNT, COUNT(DISTINCT), COUNTIF for row tallies
- [[Sum Avg Min Max]] — the four canonical numeric aggregates
- [[Safe Divide]] — SAFE_DIVIDE for ratios where the denominator might be zero

### Grouping and Group-Level Filters

- [[Group By]] — split rows into buckets so aggregates compute per category
- [[Where vs Having]] — WHERE filters rows before grouping; HAVING filters groups after

### Scalar Functions (per-row reshaping)

- [[Numeric Functions Round]] — ROUND, CEIL, FLOOR, TRUNC, ABS for number formatting
- [[String Concatenation Concat]] — CONCAT for building composite strings
- [[String Cleaning Replace and Case]] — REPLACE + LOWER/UPPER/INITCAP for text normalization
- [[Date Arithmetic Date Sub]] — DATE_SUB / DATE_ADD / DATE_DIFF for time-window logic

## How They Fit Together

A typical "computed report" query layers them like this:

```sql
SELECT
  -- 1. Bucket: scalar function on a raw column
  DATE_TRUNC(order_date, MONTH) AS month,                 -- scalar (date)
  LOWER(country) AS country_norm,                          -- scalar (string clean)

  -- 2. Aggregate: reduce rows within each bucket
  COUNT(*) AS order_count,                                 -- aggregate
  SUM(amount) AS revenue,                                  -- aggregate
  ROUND(AVG(amount), 2) AS avg_order_value,               -- aggregate + scalar
  SAFE_DIVIDE(COUNTIF(status = 'refunded'), COUNT(*)) AS refund_rate
                                                           -- aggregate (COUNTIF + COUNT) + scalar (SAFE_DIVIDE)
FROM orders

-- 3. Pre-aggregate row filter
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)  -- scalar inside WHERE

-- 4. Bucket definition
GROUP BY month, country_norm

-- 5. Post-aggregate filter
HAVING COUNT(*) > 100

-- 6. Sort
ORDER BY month DESC, revenue DESC;
```

This single query touches every page in the lesson. Reading these layers top to bottom is exactly how the engine runs them (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY).

## Key Parameters

- **Aggregates require GROUP BY** when mixed with non-aggregate columns
- **Scalar functions do not change row count** — they transform values one row at a time
- **NULL is universal**: aggregates skip NULL; scalars usually propagate NULL
- **Order of operations**: scalars in WHERE happen before aggregates; scalars in SELECT happen after

## When To Use

- **New to the lesson**: read [[Count and Countif]] → [[Sum Avg Min Max]] → [[Group By]] → [[Where vs Having]] first; scalars later
- **Reviewing for an interview**: master the differences between WHERE/HAVING and SUM/COUNT/COUNTIF — those are the most common SQL aggregation interview topics
- **Cleaning a messy dataset**: start with [[String Cleaning Replace and Case]] before joining
- **Building a dashboard query**: combine scalars (for formatting) and aggregates (for metrics) in one SELECT

## Connections

- Builds on: [[SQL Fundamentals Overview]] (all foundation concepts assumed)
- Related: [[Descriptive Statistics]] (SQL aggregates **are** the descriptive statistics), [[Measures of Central Tendency]] (AVG, MIN, MAX), [[Measures of Spread]] (STDDEV is the SQL counterpart)
- Compare with: pandas `.groupby().agg()` (same model, imperative syntax); Excel pivot tables (same idea, GUI-driven)
- Used by: every analytical dashboard query, every KPI computation, every cohort analysis

## My Notes

- The "aggregate vs scalar" distinction is the conceptual divide that, once internalized, makes most SQL errors obvious. Most "I keep getting an error about GROUP BY" frustration is a mismatch between the two.
- Practice projects for this lesson:
  - [Circle Stok Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7593) — counts and sums on inventory
  - [Circle Stok/Ürün Takipleri - 2](https://nextgen.workintech.com.tr/project/202/2?pid=7595) — more aggregations
  - [Circle Teslimat Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7596) — date arithmetic on delivery times
  - [Greenweez Satışlar](https://nextgen.workintech.com.tr/project/202/2?pid=7597) — full sales report with grouping and ratios
- Returning to this overview after future lessons (joins, window functions) keeps the foundation visible while the wiki grows.
- **Next lesson:** [[Joins Fundamentals]] (combining tables) and [[Testing Data Pipelines]] (validating the result).
- **Sprint 3 follows:** [[Data Warehouse Economics Overview]] — architecture and cost of running SQL at production scale.
