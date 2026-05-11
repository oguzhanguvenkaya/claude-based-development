---
title: "Date Arithmetic Date Sub"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/11-date-sub-ile-zaman-araligi-cikarma]]"
tags:
  - sql
  - date-sub
  - date-add
  - date-diff
  - temporal-functions
---

# Date Arithmetic Date Sub

> One-line summary: DATE_SUB, DATE_ADD, and DATE_DIFF are the canonical BigQuery functions for moving forward/backward in time by a given interval or computing the distance between two dates.

## Core Concept

Every analytics question that mentions "last 7 days", "next month", "since signup", or "year-over-year" reduces to a date arithmetic problem. SQL has no `-` operator that works directly on dates — instead, dedicated functions ensure you specify the **unit** (day, week, month, year) and avoid accidental millisecond math.

DATE_SUB shifts a date backward; DATE_ADD shifts forward; DATE_DIFF returns the distance. Together they cover almost every temporal need short of timezone arithmetic.

## How It Works

### DATE_SUB — go back in time

```sql
SELECT DATE_SUB(DATE '2025-06-20', INTERVAL 5 DAY) AS five_days_before;
-- 2025-06-15

SELECT DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH) AS one_month_ago;
-- e.g., 2026-04-11 if today is 2026-05-11
```

Signature: `DATE_SUB(date_value, INTERVAL n unit)`. Units: DAY, WEEK, MONTH, QUARTER, YEAR.

### DATE_ADD — go forward in time

```sql
SELECT DATE_ADD(order_date, INTERVAL 30 DAY) AS return_deadline
FROM orders;
```

### DATE_DIFF — distance between two dates

```sql
SELECT
  signup_date,
  CURRENT_DATE() AS today,
  DATE_DIFF(CURRENT_DATE(), signup_date, DAY) AS days_since_signup
FROM customers;
```

Signature: `DATE_DIFF(later_date, earlier_date, unit)`. Result is signed — negative if `later_date < earlier_date`.

### Filtering "last N days"

```sql
SELECT *
FROM orders
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY);
```

The canonical pattern for rolling-window queries. Combined with date partitioning, this can be the single fastest filter on a huge table.

### TIMESTAMP equivalents

For finer-grained time (seconds, milliseconds), BigQuery uses `TIMESTAMP_SUB`, `TIMESTAMP_ADD`, `TIMESTAMP_DIFF`:

```sql
SELECT TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 HOUR);
SELECT TIMESTAMP_DIFF(end_ts, start_ts, SECOND) AS duration_seconds FROM sessions;
```

### Building age buckets

```sql
SELECT
  customer_id,
  CASE
    WHEN DATE_DIFF(CURRENT_DATE(), signup_date, DAY) < 30 THEN 'new'
    WHEN DATE_DIFF(CURRENT_DATE(), signup_date, DAY) < 365 THEN 'active'
    ELSE 'veteran'
  END AS lifecycle_stage
FROM customers;
```

A common cohort-labeling pattern combining DATE_DIFF and [[Conditional Expressions SQL]].

## Key Parameters

- **Units**: DAY, WEEK, MONTH, QUARTER, YEAR for DATE; add HOUR, MINUTE, SECOND, MILLISECOND for TIMESTAMP
- **Argument order in DATE_DIFF**: `(later, earlier, unit)` — easy to flip, returns negative number if reversed
- **Month math caveats**: `DATE_ADD(DATE '2025-01-31', INTERVAL 1 MONTH)` = 2025-02-28 (clamped to last day of February). Edge cases at month ends are engine-specific.
- **DATE vs DATETIME vs TIMESTAMP**: pick the type that matches your data's precision and timezone needs (see [[SQL Data Types and Casting]])

## When To Use

- Rolling windows: "last 7 / 30 / 90 days"
- Cohort definitions: bucket customers by signup recency
- Recency/frequency calculations in RFM analysis
- Date-based join keys: "match purchases to campaigns active on that date"
- Anti-pattern: subtracting dates with `-` operator in BigQuery — errors; use DATE_DIFF
- Anti-pattern: filtering with `WHERE EXTRACT(YEAR FROM date_col) = 2025` — disables partition pruning; use `WHERE date_col BETWEEN '2025-01-01' AND '2025-12-31'` instead

## Connections

- Related: [[Filtering Where]] (date arithmetic almost always lives in WHERE), [[Conditional Expressions SQL]] (cohort buckets), [[SQL Data Types and Casting]] (parse strings to dates before arithmetic)
- Builds on: temporal type semantics
- Compare with: `EXTRACT(part FROM date)` for getting year/month/quarter from a date; `DATE_TRUNC(date, unit)` for snapping to start of period
- Used by: every time-series report, cohort analysis, lifecycle marketing

## My Notes

- Personal habit: always use `CURRENT_DATE()` in queries, never hard-coded "today" strings — keeps the query reusable.
- Practice: [Greenweez Satışlar](https://nextgen.workintech.com.tr/project/202/2?pid=7597) — compute week-over-week revenue, days-since-last-purchase per customer.
- BigQuery tip: combine `DATE_TRUNC` with `DATE_DIFF` for "complete weeks since" — `DATE_DIFF(DATE_TRUNC(today, WEEK), DATE_TRUNC(start, WEEK), WEEK)`.
- Interview tip: when discussing time-window queries on partitioned tables, emphasize that `WHERE partition_date >= DATE_SUB(...)` allows partition pruning while function wrappers on the column do not.
