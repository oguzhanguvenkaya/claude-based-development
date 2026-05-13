---
title: "Null Handling SQL"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/14-null-degerleri]]"
tags:
  - sql
  - null
  - missing-data
  - three-valued-logic
---

# Null Handling SQL

> One-line summary: NULL in SQL represents "unknown" — not zero, not empty string — and requires special operators (IS NULL, COALESCE) because comparisons against NULL always return NULL.

## Core Concept

`NULL` is one of the most misunderstood concepts in SQL. It does **not** mean zero, blank, or false. It means **"value unknown"** — the database has no information about that cell. A customer whose phone number is NULL is not a customer with phone `0` or phone `""`; it is a customer whose phone we simply do not know.

This semantic forces SQL into **three-valued logic**: every boolean condition can be `TRUE`, `FALSE`, or `NULL`. Operations involving NULL almost always propagate NULL, which is why naive `WHERE col = NULL` queries return nothing.

## How It Works

### NULL vs zero vs empty string

| Value | Meaning |
|-------|---------|
| `NULL` | Unknown / missing |
| `0` | Known to be zero |
| `''` | Known to be empty string |

These are three different things. A column that stores call duration in minutes: NULL means "we never called this customer"; 0 means "we called and hung up immediately."

### Comparison fails: use IS NULL

```sql
-- WRONG — returns zero rows
WHERE phone = NULL;
WHERE phone != NULL;

-- RIGHT
WHERE phone IS NULL;
WHERE phone IS NOT NULL;
```

`NULL = anything` returns NULL, and the WHERE clause excludes rows whose condition is not strictly TRUE.

### NULL in arithmetic and concatenation

```sql
SELECT 5 + NULL;            -- NULL
SELECT 'Hello' || NULL;     -- NULL (in standard SQL)
SELECT NULL * 100;          -- NULL
```

Any arithmetic involving NULL is NULL. This propagates surprisingly: a calculated column that adds an optional bonus to salary becomes NULL for every employee with no bonus, even though salary itself is known.

### NULL in aggregates

```sql
SELECT
  COUNT(*)         AS total_rows,         -- counts all rows
  COUNT(phone)     AS phone_filled,       -- counts non-NULL rows
  AVG(amount)      AS avg_amount          -- excludes NULL rows
FROM customers;
```

`COUNT(*)` includes NULL rows. `COUNT(column)` and other aggregates ignore NULL — except `COUNT(*)`.

### Handling NULLs explicitly

```sql
-- Replace NULL with a default
SELECT COALESCE(phone, 'no phone') FROM customers;
-- COALESCE returns the first non-NULL argument

SELECT IFNULL(amount, 0) FROM orders;
-- BigQuery / MySQL — same idea, two arguments only

-- Turn a specific value into NULL
SELECT NULLIF(rating, -1) FROM reviews;
-- Returns NULL if rating = -1, else rating
```

### The NOT IN NULL trap

```sql
-- If 'excluded_ids' contains NULL:
WHERE customer_id NOT IN (SELECT id FROM excluded_ids)
-- Returns ZERO rows. See [[In and Not In]].
```

Use `NOT EXISTS` to be safe.

## Key Parameters

- **`IS NULL` / `IS NOT NULL`**: the only correct way to test for NULL
- **`COALESCE(a, b, c)`**: returns first non-NULL argument; replaces NULL with a default
- **`IFNULL(a, b)`**: two-argument shorthand
- **`NULLIF(a, b)`**: returns NULL if a = b, otherwise returns a — useful for converting sentinel values
- **`NOT NULL` constraint**: prevents NULLs at the schema level (see [[Relational Data Model]])

## When To Use

- Detect missing data: `WHERE col IS NULL`
- Provide defaults for display: `COALESCE(name, 'Unknown')`
- Convert sentinel codes (`-1`, `'N/A'`) to proper NULLs: `NULLIF`
- Aggregate only known values: aggregate functions auto-skip NULL — usually what you want
- Anti-pattern: storing `'N/A'` or `-1` instead of NULL — makes filtering and aggregation harder
- Anti-pattern: comparing to NULL with `=` or `!=`
- Anti-pattern: assuming `WHERE col != 'x'` excludes NULLs — it does not (NULL is excluded silently)

## Connections

- Related: [[Filtering Where]] (NULL handling rules apply in WHERE), [[In and Not In]] (NULL trap with NOT IN), [[Conditional Expressions SQL]] (CASE WHEN often handles NULLs), [[Safe Divide]] (a NULL-aware division operator from the same family)
- Builds on: three-valued logic (TRUE / FALSE / NULL)
- Compare with: Python's `None`, R's `NA`, pandas' `NaN` — same conceptual problem, different APIs
- Used by: every realistic dataset (real data is messy and full of NULLs); [[Count and Countif]] (the gap between COUNT(*) and COUNT(col) equals the NULL count)

## My Notes

- "Why is my COUNT off by 5?" — because 5 rows had NULL in the counted column.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), audit which columns have NULLs and decide whether to filter, fill, or flag them.
- BigQuery tip: `SAFE_DIVIDE(a, b)` returns NULL on division by zero instead of error — a NULL-aware variant of `/`.
- Interview question: "How would you find customers with no orders?" Answer: `LEFT JOIN ... WHERE orders.id IS NULL` (anti-join pattern).
- A NULL is not a value — it is the absence of a value. Treat it as missing information, not as a special number.
