---
title: "String Concatenation Concat"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/08-concat-ile-sutunlari-birlestirme]]"
tags:
  - sql
  - concat
  - string-building
  - composite-keys
---

# String Concatenation Concat

> One-line summary: CONCAT joins multiple string columns or literals into one — building full names, composite keys, ISO date strings, and any value made from smaller text parts.

## Core Concept

Tables store atomic values: first name, last name, year, month, day. Reports and joins often need composites: "Alice Wang", "2025-01-15", "user_12345". `CONCAT` is the SQL string assembler — it stitches inputs together in order.

In modern SQL engines, CONCAT is NULL-safe in BigQuery (NULL inputs produce NULL output), but in some engines you must use `COALESCE` first or risk an entire concatenated string going NULL because of one missing column.

## How It Works

### Basic concatenation

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;
-- "Alice Wang"
```

CONCAT takes 2 or more arguments. Any literal (`' '`, `'-'`, `':'`) can be a separator.

### Building composite keys

```sql
SELECT
  CONCAT(customer_id, '-', order_id) AS purchase_key
FROM orders;
-- "1001-50231"
```

Composite keys let you join on a single field where multiple columns identify a record. Useful but lossy — once concatenated, you cannot easily split back without REGEXP or `SPLIT`.

### Building ISO date strings from parts

```sql
SELECT
  CONCAT(year, '-', LPAD(CAST(month AS STRING), 2, '0'), '-', LPAD(CAST(day AS STRING), 2, '0')) AS iso_date
FROM events;
-- "2025-01-05"
```

`LPAD` left-pads with zeros so months/days always have two digits. Without LPAD, `2025-1-5` is not a valid ISO date and parsing breaks. See [[SQL Data Types and Casting]].

### NULL handling

```sql
-- BigQuery: NULL input → NULL output
SELECT CONCAT('Mr. ', NULL, ' Smith');
-- Returns NULL

-- Defensive concat using COALESCE
SELECT CONCAT('Mr. ', COALESCE(middle_name, ''), ' Smith');
-- Returns 'Mr.  Smith' if middle_name is NULL
```

See [[Null Handling SQL]] for the broader rule.

### The `||` operator (standard SQL)

```sql
SELECT first_name || ' ' || last_name FROM customers;
-- PostgreSQL/Snowflake; not BigQuery
```

`||` is the SQL-standard concatenation operator but is not available in BigQuery — stick with CONCAT in BQ.

### Combining with FORMAT for templated strings

```sql
SELECT FORMAT('Order #%d totals $%.2f', order_id, amount) AS receipt_line
FROM orders;
-- "Order #50231 totals $99.99"
```

`FORMAT` is closer to printf — cleaner than chaining many CONCATs.

## Key Parameters

- **Argument count**: at least 2 in standard usage; BigQuery accepts variadic
- **Types**: arguments are auto-cast to STRING (in BigQuery). Other engines require explicit CAST.
- **NULL behavior**: BigQuery propagates NULL; PostgreSQL with `||` propagates NULL too unless using `CONCAT()` which ignores NULL
- **`STRING_AGG`**: a related aggregate that joins strings from many rows into one (`STRING_AGG(name, ', ')`)

## When To Use

- Building display names ("First Last", "Last, First")
- Composite keys for joins, dedup, or pivoting (`CONCAT(category, '_', subcategory)`)
- Assembling ISO date / timestamp strings from parts
- Formatting CSV-style exports inside SQL
- Anti-pattern: heavy concatenation inside the SELECT of a billion-row query — slow because it allocates new strings; consider precomputing in a CTE or view
- Anti-pattern: building keys that you immediately need to split apart again — keep the original columns

## Connections

- Related: [[String Cleaning Replace and Case]] (clean first, then concat), [[SQL Data Types and Casting]] (CAST other types to STRING before concat in non-BQ engines), [[Null Handling SQL]] (NULL propagation through CONCAT)
- Builds on: string handling fundamentals
- Compare with: `FORMAT()` for printf-style templating; `STRING_AGG` for cross-row concatenation
- Used by: dashboard label generation, join key construction, log formatting

## My Notes

- Convention: separate parts of a composite key with a character that **cannot** appear in any part (often `|` or `~`). `-` is risky because it appears in many natural strings.
- Practice: [Circle Stok Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7593) — build readable product labels by concatenating SKU, category, and size.
- BigQuery tip: `||` does **not** work; always use `CONCAT()`. Porting from PostgreSQL bites here.
- Interview tip: when asked "how would you build a unique row identifier?", answer with CONCAT plus a separator — but mention that hash functions (`FARM_FINGERPRINT(...)`) are better for large keyspaces.
