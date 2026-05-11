---
title: "Numeric Functions Round"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/07-sayisal-fonksiyonlar-round]]"
tags:
  - sql
  - round
  - ceil
  - floor
  - numeric-formatting
---

# Numeric Functions Round

> One-line summary: ROUND, CEIL, FLOOR, TRUNC, and ABS shape numbers for display — rounding to a decimal place, taking the integer above or below, dropping the fractional part, or removing the sign.

## Core Concept

Aggregates often produce ugly numbers — `AVG(amount)` returns `47.823184729...` when the user wants `$47.82`. Numeric functions let you reshape numbers without changing their underlying type, so dashboards and reports look professional.

These functions are **scalar** — they transform one number to another, row by row. They do not aggregate.

## How It Works

### ROUND — to a decimal place

```sql
SELECT
  ROUND(47.8231)        AS to_integer,        -- 48
  ROUND(47.8231, 2)     AS to_two_decimals,   -- 47.82
  ROUND(47.8231, 0)     AS same_as_first,     -- 48
  ROUND(47.85, 1)       AS half_up_or_even    -- 47.9 (banker's rounding in some engines)
;
```

Second argument: decimal places. Positive means after the decimal point; negative means before (rounding to tens, hundreds, etc.).

```sql
-- Round to nearest 100
SELECT ROUND(12345, -2);  -- 12300
```

### CEIL / CEILING — always up

```sql
SELECT CEIL(47.1);   -- 48
SELECT CEIL(-3.5);   -- -3 (toward positive infinity)
```

Used when you need to "round up to the next whole unit" — number of pages for pagination, ceil(total / page_size).

### FLOOR — always down

```sql
SELECT FLOOR(47.9);  -- 47
SELECT FLOOR(-3.5);  -- -4 (toward negative infinity)
```

### TRUNC — drop the fractional part

```sql
SELECT TRUNC(47.9);    -- 47  (toward zero)
SELECT TRUNC(-47.9);   -- -47 (toward zero, NOT -48)
```

TRUNC differs from FLOOR for negative numbers. TRUNC always moves toward zero; FLOOR always moves toward minus infinity.

### ABS — absolute value

```sql
SELECT ABS(-47.8);   -- 47.8
SELECT ABS(47.8);    -- 47.8
```

Useful for distance / deviation calculations and for filtering "anything off by more than X."

### Putting them together

```sql
SELECT
  product_id,
  ROUND(AVG(price), 2)            AS avg_price_display,
  CEIL(SUM(quantity) / 100.0)     AS pallets_needed,
  ABS(MAX(price) - MIN(price))    AS price_range
FROM products
GROUP BY product_id;
```

## Key Parameters

- **ROUND default**: rounds half-away-from-zero in BigQuery; some engines use banker's rounding (half-to-even) — check the docs of your engine for monetary calculations
- **Negative second argument**: rounds to tens/hundreds/thousands
- **TRUNC vs FLOOR**: identical for positive numbers; differ for negatives (TRUNC → zero, FLOOR → -infinity)
- **Type preservation**: rounding a NUMERIC stays NUMERIC; rounding a FLOAT stays FLOAT
- **NULL behavior**: any input NULL → output NULL

## When To Use

- **ROUND**: displaying money, percentages, and rates in dashboards
- **CEIL**: capacity calculations (pages, batches, pallets)
- **FLOOR**: bucket assignment (`FLOOR(age / 10) * 10` for age buckets)
- **TRUNC**: dropping noise from imprecise floats; converting datetime to date in some engines (`TRUNC(ts)`)
- **ABS**: distance, deviation, difference magnitude
- Anti-pattern: rounding before aggregating when small errors compound — round only at the final display step
- Anti-pattern: using FLOAT for money — rounding errors accumulate; use NUMERIC (see [[SQL Data Types and Casting]])

## Connections

- Related: [[Sum Avg Min Max]] (rounding usually applied to aggregate output), [[SQL Data Types and Casting]] (NUMERIC vs FLOAT matters for rounding precision)
- Builds on: basic floating-point arithmetic
- Compare with: `FORMAT()` for string-formatted output (different goal: numeric→string vs numeric→numeric); locale-aware formatting in BI tools
- Used by: every dashboard formatting query, KPI display

## My Notes

- Always round **last** — after every aggregate and computation — otherwise small per-row errors snowball.
- Practice: [Greenweez Satışlar](https://nextgen.workintech.com.tr/project/202/2?pid=7597) — produce AOV (Average Order Value) and conversion rate rounded for executive display.
- BigQuery tip: `FORMAT('%.2f', col)` returns a string with exactly 2 decimals — better than ROUND when you need consistent decimal display (e.g., `1.50` not `1.5`).
- Interview gotcha: `ROUND(0.5)` may be 0 or 1 depending on engine — banker's rounding rounds to even. Check before using in tests.
