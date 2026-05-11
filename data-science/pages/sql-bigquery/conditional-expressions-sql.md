---
title: "Conditional Expressions SQL"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/13-kosullu-sutunlar]]"
tags:
  - sql
  - case-when
  - if-statement
  - row-level-logic
---

# Conditional Expressions SQL

> One-line summary: CASE WHEN and IF let you compute a value per row based on conditions, adding branching logic directly inside SELECT or other clauses.

## Core Concept

Sometimes you need a column that does not exist in the source table — a label, a bucket, a derived flag. **Conditional expressions** let you compute one inline. For each row, the engine evaluates the conditions in order and returns the first matching value.

Two forms exist: the universal **`CASE WHEN`** (works in every SQL engine) and the shorter **`IF`** (BigQuery, MySQL — not standard SQL). They produce the same result.

## How It Works

### Simple IF (BigQuery / MySQL)

```sql
SELECT
  order_id,
  amount,
  IF(amount > 100, 'HIGH', 'LOW') AS value_tier
FROM orders;
```

Reads: "if amount > 100 return 'HIGH', else return 'LOW'." Three arguments: condition, value_if_true, value_if_false.

### CASE WHEN — two flavors

**Searched form** (more flexible):

```sql
SELECT
  order_id,
  amount,
  CASE
    WHEN amount > 1000 THEN 'enterprise'
    WHEN amount > 100  THEN 'mid'
    WHEN amount > 10   THEN 'small'
    ELSE                    'micro'
  END AS deal_size
FROM orders;
```

The engine evaluates each `WHEN` top to bottom and returns the value of the first matching branch. If no branch matches and there is no `ELSE`, the result is NULL.

**Simple form** (when comparing one column to literal values):

```sql
SELECT
  order_status,
  CASE order_status
    WHEN 'paid'      THEN 'success'
    WHEN 'shipped'   THEN 'success'
    WHEN 'delivered' THEN 'success'
    WHEN 'refunded'  THEN 'failure'
    ELSE                  'in_progress'
  END AS status_group
FROM orders;
```

Less flexible but more compact when all branches compare the same column.

### Combined with aggregation

```sql
SELECT
  COUNT(*)                                    AS total_orders,
  SUM(CASE WHEN amount > 100 THEN 1 ELSE 0 END) AS high_value_orders,
  AVG(CASE WHEN city = 'New York' THEN amount END) AS nyc_avg_amount
FROM orders;
```

`CASE WHEN ... THEN 1 ELSE 0 END` inside SUM is the canonical "count rows that match this condition" pattern. The second example — using `CASE` inside `AVG` without `ELSE` — averages only the matching rows because NULLs are excluded from `AVG`.

## Key Parameters

- **Evaluation order**: top to bottom; the first matching `WHEN` wins
- **ELSE is optional**: missing ELSE means NULL when nothing matches — almost always include ELSE
- **Type consistency**: all branches must return the same type (or be implicitly castable); mixing strings and integers fails
- **IF vs CASE**: `IF` for two-way branching, `CASE` for three or more branches

## When To Use

- Labeling rows for reports (low/mid/high, paid/unpaid, active/churned)
- Building derived flags before aggregation
- Pivoting wide tables (CASE inside SUM is the SQL pivot pattern before window functions)
- "Counting if" queries: `SUM(CASE WHEN cond THEN 1 ELSE 0 END)` — equivalent to `COUNT(*) FILTER (WHERE cond)` in PostgreSQL
- Anti-pattern: nesting CASE 5+ levels deep — pull the logic into a lookup table or a CTE for readability

## Connections

- Related: [[Filtering Where]] (similar boolean logic, but WHERE filters rows while CASE projects values), [[Null Handling SQL]] (CASE often handles NULL fallbacks), [[Count and Countif]] (COUNTIF is sugar over `COUNT(CASE WHEN ...)`)
- Builds on: boolean expressions and basic typing
- Compare with: `COALESCE` (specific to "first non-null"), `NULLIF` (specific to "null if equal")
- Used by: [[Distinct and Deduplication]] for cohort labeling, [[Sum Avg Min Max]] (conditional aggregates), [[Group By]] (CASE inside SELECT for pivot patterns)

## My Notes

- Always include `ELSE` — silent NULLs from missing branches cause confusing downstream bugs.
- The `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` pattern is the bread and butter of analytics SQL. Memorize it.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), bucket customers into segments (high/mid/low value) using CASE WHEN.
- Interview tip: when asked to "label every row based on multiple thresholds," reach for searched CASE — clearer than nested IFs.
- BigQuery tip: `IFNULL(col, default)` and `COALESCE(col1, col2, col3)` are special-purpose conditionals that are clearer than the equivalent CASE.
