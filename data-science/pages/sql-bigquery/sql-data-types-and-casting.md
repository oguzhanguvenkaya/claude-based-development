---
title: "SQL Data Types and Casting"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/15-veri-turleri]]"
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/16-veri-turu-donusturme-casting]]"
tags:
  - sql
  - data-types
  - cast
  - safe-cast
  - bigquery
---

# SQL Data Types and Casting

> One-line summary: Every SQL column has a fixed data type — numeric, text, boolean, date, or temporal — and CAST/SAFE_CAST convert between types when calculations need a different shape.

## Core Concept

A column's **data type** declares the kind of value it can store and how the engine should treat operations on it. If `order_amount` is stored as TEXT, you cannot `SUM` it without first converting it to a number. If `signup_date` is stored as STRING, you cannot compute "days since signup" without casting to DATE.

Type discipline is what makes relational databases reliable and fast. Pick the wrong type and your query either errors out or, worse, silently returns wrong results.

## How It Works

### Common BigQuery / standard SQL types

| Type | Purpose | Example |
|------|---------|---------|
| `INT64` / `INTEGER` | Whole numbers | `42`, `-1`, `1000000` |
| `FLOAT64` / `NUMERIC` | Decimals (NUMERIC for exact, FLOAT for approximate) | `3.14`, `0.0001` |
| `STRING` | Text of any length | `'Alice'`, `'12345'` |
| `BOOL` | True/False | `TRUE`, `FALSE` |
| `DATE` | Calendar date, no time | `DATE '2026-05-11'` |
| `DATETIME` | Date + time, no timezone | `DATETIME '2026-05-11 14:30:00'` |
| `TIMESTAMP` | Date + time, UTC | `TIMESTAMP '2026-05-11 14:30:00 UTC'` |
| `ARRAY` | Ordered list of values | `[1, 2, 3]` |
| `STRUCT` | Named bundle of fields | `STRUCT('Alice' AS name, 30 AS age)` |
| `BYTES`, `GEOGRAPHY`, `JSON` | Specialized | binary, geo, semi-structured |

### Why type matters

```sql
-- If amount is STRING '100', this returns '50100' (string concat in some engines)
-- If amount is INT64, this returns 150
SELECT amount + 50 FROM orders;

-- If signup_date is STRING '2024-01-15', date functions fail
SELECT DATE_DIFF(CURRENT_DATE(), signup_date, DAY) FROM customers;
-- Must cast first:
SELECT DATE_DIFF(CURRENT_DATE(), CAST(signup_date AS DATE), DAY) FROM customers;
```

### CAST — explicit conversion

```sql
-- String to date
SELECT CAST('2024-12-31' AS DATE);

-- Number to string (for concatenation or formatting)
SELECT CAST(amount AS STRING);

-- String to number
SELECT CAST('3.14' AS FLOAT64);

-- Combined: parse, compute, present
SELECT CAST(CAST(date_str AS DATE) + INTERVAL 30 DAY AS STRING) AS end_date_str
FROM subscriptions;
```

CAST raises an **error** if the conversion fails. `CAST('hello' AS INT64)` crashes the query.

### SAFE_CAST — graceful conversion

```sql
SELECT SAFE_CAST(amount_str AS FLOAT64) AS amount FROM raw_data;
-- Returns NULL when conversion fails, no error
```

`SAFE_CAST` is essential for messy ingestion data where some rows have invalid values. Pair with [[Null Handling SQL]] to deal with the resulting NULLs.

### Implicit casting

Some engines implicitly cast between compatible types (`INT64` ↔ `FLOAT64`), but **never rely on it**. Be explicit; the next person reading your query will thank you.

## Key Parameters

- **`CAST(expr AS TYPE)`**: errors on failure
- **`SAFE_CAST(expr AS TYPE)`**: returns NULL on failure (BigQuery)
- **`NUMERIC` vs `FLOAT64`**: NUMERIC is exact (no rounding), FLOAT is approximate — use NUMERIC for money
- **`DATE` vs `TIMESTAMP`**: DATE has no time; TIMESTAMP is timezone-aware (always UTC in BigQuery)
- **Storage cost**: in BigQuery, types have different per-byte costs — STRING is ~2 bytes per char, INT64 is 8 bytes, DATE is 8 bytes

## When To Use

- **Always declare types correctly at table creation**; downstream queries depend on it
- **CAST** when you control the data and know conversion will succeed
- **SAFE_CAST** when reading external or user-generated data
- **Cast dates from strings** — common ingestion task; CSV imports often store dates as strings
- Anti-pattern: storing numbers as strings to avoid type errors — you push the problem downstream and lose math/sort capabilities
- Anti-pattern: using FLOAT for money — rounding errors compound (use NUMERIC)
- Anti-pattern: comparing `STRING '10'` with `INT64 10` — engine behavior varies; cast explicitly

## Connections

- Related: [[Null Handling SQL]] (SAFE_CAST produces NULLs you must handle), [[Conditional Expressions SQL]] (CASE often paired with casts), [[Relational Data Model]] (types are declared in CREATE TABLE)
- Builds on: programming language type systems — same concepts, SQL-specific syntax
- Compare with: pandas `dtype`, Python `int()/str()/float()` — different ecosystems, same idea
- Used by: every analytic computation that consumes ingestion or BI data; the canonical ingestion application is [[Bigquery Insert with Cast Workflow]]

## My Notes

- Date-parsing bugs are the most common SQL gotcha for new analysts. Always inspect the type before computing on a date column: `SELECT column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'X'`.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), check whether date and amount columns are stored in the right types before computing metrics.
- BigQuery tip: use `PARSE_DATE('%Y-%m-%d', date_str)` for nonstandard string formats; `CAST` only handles ISO format.
- For money, default to `NUMERIC(38, 9)` in BigQuery — exact decimal, sufficient precision for financial calculations.
