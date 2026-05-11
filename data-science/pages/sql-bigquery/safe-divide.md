---
title: "Safe Divide"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/04-safe-divide-fonksiyonu]]"
tags:
  - sql
  - safe-divide
  - division-by-zero
  - null-handling
  - bigquery
---

# Safe Divide

> One-line summary: SAFE_DIVIDE(a, b) returns NULL instead of crashing when b is zero — the standard BigQuery idiom for any ratio whose denominator might be zero.

## Core Concept

Division by zero is the most common runtime error in numeric SQL. A single bad row — a customer with zero sessions, a category with zero items — kills the entire query. `SAFE_DIVIDE` solves this by substituting NULL for the error.

The trade-off: you no longer get an error pointing at the bad input. Instead, you get a NULL that you must handle downstream. In analytics this is almost always preferable — one NULL is recoverable, a failed query is not.

## How It Works

### Basic usage

```sql
SELECT
  customer_id,
  SAFE_DIVIDE(total_spend, session_count) AS spend_per_session
FROM customer_metrics;
```

- If `session_count > 0`: returns `total_spend / session_count`
- If `session_count = 0`: returns NULL
- If either is NULL: returns NULL

No error, no crash.

### Compare with regular division

```sql
-- Regular division: errors out on any zero denominator
SELECT total_spend / session_count FROM customer_metrics;
-- ERROR: division by zero

-- SAFE_DIVIDE: gracefully returns NULL for zero rows
SELECT SAFE_DIVIDE(total_spend, session_count) FROM customer_metrics;
-- Runs to completion; bad rows become NULL
```

### Combined with aggregates

```sql
-- Conversion rate: orders divided by sessions
SELECT
  campaign_id,
  SAFE_DIVIDE(SUM(orders), SUM(sessions)) AS conversion_rate
FROM analytics
GROUP BY campaign_id;
```

If a campaign has zero sessions, the conversion rate is NULL — not an error, not a misleading zero, not infinity.

### Handling the resulting NULL

```sql
-- Show 0% for zero-session rows
SELECT
  campaign_id,
  COALESCE(SAFE_DIVIDE(orders, sessions), 0) AS conversion_rate_or_zero
FROM analytics;

-- Filter out the NULL rows
SELECT * FROM (
  SELECT
    campaign_id,
    SAFE_DIVIDE(orders, sessions) AS rate
  FROM analytics
)
WHERE rate IS NOT NULL;
```

See [[Null Handling SQL]] for the full toolkit.

## Key Parameters

- **Exactly two arguments**: numerator and denominator
- **NULL inputs**: if either argument is NULL, the result is NULL (consistent with three-valued logic)
- **Type rules**: both arguments must be numeric (INT64, FLOAT64, NUMERIC); result is FLOAT64 if either is FLOAT, NUMERIC otherwise
- **Cousins**: `SAFE_ADD`, `SAFE_SUBTRACT`, `SAFE_MULTIPLY` — same pattern for overflow protection; `SAFE_CAST` for casting failures (see [[SQL Data Types and Casting]])

## When To Use

- Any percentage or rate computation where the denominator could be zero (conversion rate, fill rate, error rate)
- KPI dashboards that must not break when a category has zero activity
- Per-user / per-session metrics where some users may have zero sessions
- Anti-pattern: wrapping a guaranteed-non-zero denominator in SAFE_DIVIDE — adds noise without value
- Anti-pattern: silently swallowing zero-denominator rows that should be investigated — sometimes the zero is a bug upstream, and a NULL hides it

## Connections

- Related: [[Null Handling SQL]] (SAFE_DIVIDE generates NULLs you must handle), [[Sum Avg Min Max]] (often used inside ratio aggregates), [[SQL Data Types and Casting]] (SAFE_CAST is the same family)
- Builds on: division semantics, the principle of fail-soft computation
- Compare with: `NULLIF(denominator, 0)` then divide — same effect, more portable across engines; `CASE WHEN denominator = 0 THEN NULL ELSE numerator/denominator END` — verbose but explicit
- Used by: every ratio in a dashboard query

## My Notes

- Rule of thumb: **default to SAFE_DIVIDE for any computed ratio in analytics**. Switch back to `/` only when you have proven the denominator cannot be zero.
- Practice: [Circle Teslimat Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7596) — compute on-time delivery rates without crashing on zero-delivery days.
- Portable equivalent (PostgreSQL, Snowflake): `numerator * 1.0 / NULLIF(denominator, 0)` — same NULL-on-zero behavior using standard SQL.
- Watch out for "NULL means zero" misreadings in reports. A dashboard showing NULL for conversion rate could be either "no data" or "data with zero denominator" — annotate clearly.
