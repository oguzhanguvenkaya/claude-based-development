---
title: "Sum Avg Min Max"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/03-sum-avg-min-max]]"
tags:
  - sql
  - sum
  - avg
  - min
  - max
  - aggregation
---

# Sum Avg Min Max

> One-line summary: The four canonical numeric aggregates that reduce a column of values into a single number — total (SUM), average (AVG), smallest (MIN), largest (MAX).

## Core Concept

Once you can [count rows](count-and-countif.md), the next step is asking what those numbers add up to, what the typical value is, and what the extremes look like. `SUM`, `AVG`, `MIN`, and `MAX` answer those four questions in one line each. They are the four most common aggregates in any analytical query.

All four ignore NULL values automatically — they aggregate only the known data. This is usually what you want; if it is not, fill NULLs first with COALESCE (see [[Null Handling SQL]]).

## How It Works

### Basic syntax

```sql
SELECT
  SUM(amount)   AS total_revenue,
  AVG(amount)   AS avg_order_value,
  MIN(amount)   AS smallest_order,
  MAX(amount)   AS largest_order,
  COUNT(*)      AS order_count
FROM orders;
```

One row out. Each aggregate scans the whole `amount` column and reduces it to a single value.

### With GROUP BY — one row per group

```sql
SELECT
  product_category,
  SUM(amount) AS revenue,
  AVG(amount) AS avg_order,
  MIN(order_date) AS first_order_date,
  MAX(order_date) AS last_order_date
FROM orders
GROUP BY product_category;
```

See [[Group By]]. MIN and MAX also work on dates and strings — returning the earliest date or the alphabetically smallest string.

### AVG nuances

```sql
-- Average ignoring NULL
SELECT AVG(rating) FROM reviews;
-- If 100 reviews exist and 10 have NULL rating, the average is sum / 90, not sum / 100.

-- Average treating NULL as zero (rarely what you want)
SELECT AVG(COALESCE(rating, 0)) FROM reviews;
```

The default (NULL-ignoring) behavior matches how a human would compute an average — "of the ratings I have, what's typical?" The COALESCE version answers a different question.

### MIN and MAX on dates and strings

```sql
SELECT
  MIN(signup_date) AS earliest_signup,
  MAX(signup_date) AS latest_signup,
  MIN(name)        AS alphabetically_first
FROM customers;
```

For dates: earliest / latest. For strings: lexicographic min/max.

### Combining with COUNTIF for conditional sums

```sql
SELECT
  SUM(IF(amount > 100, amount, 0)) AS high_value_revenue,
  COUNTIF(amount > 100)            AS high_value_orders
FROM orders;
```

Conditional aggregates are the SQL idiom for "show me the slice without splitting the query."

## Key Parameters

- **NULL handling**: all four aggregates skip NULL. `AVG` divides by the non-NULL count, not the total row count.
- **Integer overflow**: SUM on a huge INT64 column can overflow. BigQuery handles this with arbitrary-precision NUMERIC if needed.
- **MIN/MAX on STRING**: lexicographic comparison — `'10'` is less than `'2'` because '1' < '2'. Cast to INT64 first if you want numeric order.
- **Type widening**: AVG of INT64 returns FLOAT64 (because the result has a decimal part).

## When To Use

- Any "total / average / extremes" question
- Daily revenue, average ticket size, minimum stock, maximum delay
- Combined with GROUP BY for breakdowns by category, day, region
- With CASE WHEN for conditional aggregates (revenue from a specific segment)
- Anti-pattern: AVG of percentages stored as separate column values — you usually want a weighted average, not a simple mean of percentages
- Anti-pattern: MIN/MAX on a column that should be unique — use a key lookup; aggregating a PK is confusing

## Connections

- Related: [[Count and Countif]] (counts rows; SUM aggregates values), [[Safe Divide]] (avg = sum/count; safe division avoids div-by-zero), [[Group By]], [[Where vs Having]]
- Builds on: [[SQL Data Types and Casting]] (aggregates require numeric types — cast strings first), [[Null Handling SQL]]
- Compare with: [[Measures of Central Tendency]] (AVG = mean; median needs APPROX_QUANTILES, not built-in)
- Used by: every analytics dashboard, every KPI computation

## My Notes

- The classic "average misleads" lesson: SQL AVG is the arithmetic mean, sensitive to outliers. For skewed data, also report median with APPROX_QUANTILES.
- Practice: [Greenweez Satışlar](https://nextgen.workintech.com.tr/project/202/2?pid=7597) — compute daily/weekly revenue summaries with SUM, AVG.
- BigQuery tip: `STDDEV(col)` and `VARIANCE(col)` are also built-in — see [[Measures of Spread]].
- Interview tip: when the interviewer says "what's the daily average revenue per customer?", they want `SUM(revenue) / COUNT(DISTINCT customer_id)`, not `AVG(revenue)` (which is per-order average).
