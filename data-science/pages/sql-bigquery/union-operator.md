---
title: "Union Operator"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/04-union]]"
tags:
  - sql
  - union
  - union-all
  - set-operators
---

# Union Operator

> One-line summary: UNION stacks the rows of two SELECTs vertically into one result, requiring matching column counts and types — used for combining data from "old + new" systems, identical-schema tables, or alternative branches of a query.

## Core Concept

JOINs combine tables **horizontally** (matching keys → wider rows). UNION combines tables **vertically** (same columns → more rows). When two tables hold the same kind of data — orders from an old system and a new one, sales from different regions stored in separate tables — UNION stitches them into a single logical dataset to query.

UNION has a strict requirement: the SELECTs being unioned must have the **same number of columns** in the **same order** with **compatible types**. If schemas drifted, you cast or rename until they align.

## How It Works

### Basic UNION (removes duplicates)

```sql
SELECT order_id, customer_id, amount FROM orders_legacy
UNION
SELECT order_id, customer_id, amount FROM orders_new;
```

Result: every distinct `(order_id, customer_id, amount)` row from both tables. Identical rows appear once — UNION implicitly deduplicates.

### UNION ALL (keeps duplicates, faster)

```sql
SELECT order_id, customer_id, amount FROM orders_legacy
UNION ALL
SELECT order_id, customer_id, amount FROM orders_new;
```

`UNION ALL` skips the deduplication step. Faster, especially on large tables. Use unless you specifically need to deduplicate.

**Default to UNION ALL** unless you have a reason to dedupe — the silent deduplication of UNION is a frequent source of "where did my rows go?" confusion.

### Aligning schemas with explicit column lists

```sql
-- Old table has (id, cust, amt); new table has (order_id, customer_id, amount, currency)
SELECT id          AS order_id,
       cust        AS customer_id,
       amt         AS amount,
       'USD'       AS currency   -- pad with literal for missing column
FROM orders_legacy

UNION ALL

SELECT order_id,
       customer_id,
       amount,
       currency
FROM orders_new;
```

UNION matches columns by position, not name. Always list columns explicitly so you control the alignment.

### Marking the source

```sql
SELECT order_id, customer_id, amount, 'legacy' AS source FROM orders_legacy
UNION ALL
SELECT order_id, customer_id, amount, 'new'    AS source FROM orders_new;
```

Adding a `source` column lets downstream consumers tell which system the row came from — essential during migrations.

### UNION'd CTEs in a larger query

```sql
WITH all_orders AS (
  SELECT order_id, customer_id, amount, order_date FROM orders_legacy
  UNION ALL
  SELECT order_id, customer_id, amount, order_date FROM orders_new
)
SELECT
  DATE_TRUNC(order_date, MONTH) AS month,
  SUM(amount)                   AS revenue
FROM all_orders
GROUP BY month
ORDER BY month;
```

The CTE makes the union a logical table; the rest of the query treats it as one source.

### Set operators family

| Operator | Behavior |
|----------|----------|
| `UNION` | Union of two SELECTs, deduplicated |
| `UNION ALL` | Union of two SELECTs, all rows kept |
| `INTERSECT` | Rows that appear in both SELECTs |
| `EXCEPT` (or `MINUS`) | Rows in first SELECT that do not appear in second |

INTERSECT and EXCEPT are less commonly used but valuable for data quality checks: "which IDs are in source A but missing from B?" → `SELECT id FROM A EXCEPT SELECT id FROM B`.

## Key Parameters

- **Column count and order must match**: SQL aligns by position, not name; verify columns in each SELECT
- **Types must be compatible**: use [[SQL Data Types and Casting]] CAST/SAFE_CAST to align
- **UNION vs UNION ALL**: ALL is faster and almost always what you want; UNION dedupes
- **First SELECT names the columns**: the result column names come from the first SELECT
- **ORDER BY at the end**: applies to the unioned result, not each individual SELECT

## When To Use

- **System migrations**: legacy + new tables holding the same kind of data
- **Multi-source ingestion**: regional tables, partner-specific tables, multi-vendor data combined
- **Branching queries**: when one SELECT covers one segment and another SELECT covers a different segment with different logic
- **Set-difference data quality checks**: `EXCEPT` to find missing IDs between two sources
- Anti-pattern: using UNION (with dedupe) by habit when UNION ALL would do — pays a sort/hash cost for nothing
- Anti-pattern: relying on column-name matching — SQL goes by position, not name

## Connections

- Related: [[Joins Fundamentals]] (joins combine horizontally; UNION combines vertically), [[Common Table Expressions Cte]] (CTEs often wrap UNIONs), [[Distinct and Deduplication]] (UNION's implicit dedup is the same DISTINCT logic)
- Builds on: [[Select Statement]], [[SQL Data Types and Casting]] (aligning types)
- Compare with: INSERT INTO ... SELECT (persists the result; UNION is ephemeral); INTERSECT and EXCEPT (other set operators)
- Used by: ETL pipelines combining sources, migrations, data audits

## My Notes

- Habit: default to `UNION ALL`. Only escalate to `UNION` when you explicitly want dedup.
- Practice: write a UNION that combines two sales tables with slightly different schemas. Force yourself to handle the column alignment explicitly.
- BigQuery tip: `UNION ALL` is essentially free; `UNION` triggers a deduplication that scans both sides — measurable cost on large tables.
- Interview tip: be ready to explain the deduplication difference. It's a frequent SQL gotcha.
