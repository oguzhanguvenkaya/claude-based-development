---
title: "Functions in SQL Overview"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak]]"
tags:
  - sql
  - functions
  - overview
  - taxonomy
---

# Functions in SQL Overview

> One-line summary: SQL functions take inputs (parameters), do something with them, and return a result — the same mental model as functions in any programming language, organized in SQL into four families: scalar, aggregate, window, and user-defined.

## Core Concept

A function is a little machine: feed it inputs, get back an output. SQL leans on functions heavily — every nontrivial query uses several. Once you internalize the four families and how they interact with rows, the rest of SQL is mostly remembering which function name does which thing.

The families differ in how many rows they take in and how many they produce:

| Family | Input | Output |
|--------|-------|--------|
| **Scalar** | 1 value per row | 1 value per row |
| **Aggregate** | many rows (a group) | 1 value per group |
| **Window** | many rows (a window) | 1 value per row (preserves rows) |
| **User-defined (UDF)** | any (you define) | any (you define) |

Each family solves a different category of problem. Aggregates summarize; scalars reshape; window functions add summary context without losing detail; UDFs reuse your own logic.

## How It Works

### Scalar functions — one row in, one row out

Already covered in earlier lessons. The most common scalar functions:

- Numeric: `ROUND`, `CEIL`, `FLOOR`, `ABS` — see [[Numeric Functions Round]]
- String: `CONCAT`, `REPLACE`, `LOWER`, `UPPER` — see [[String Concatenation Concat]] and [[String Cleaning Replace and Case]]
- Date: `DATE_SUB`, `DATE_ADD`, `DATE_DIFF` — see [[Date Arithmetic Date Sub]]
- Conditional: `IF`, `CASE WHEN`, `COALESCE` — see [[Conditional Expressions SQL]] and [[Null Handling SQL]]
- Type conversion: `CAST`, `SAFE_CAST`, `PARSE_DATE` — see [[SQL Data Types and Casting]]

```sql
SELECT
  ROUND(price * 1.18, 2)        AS price_with_tax,   -- scalar
  UPPER(country)                AS country_norm,    -- scalar
  DATE_DIFF(today, signup, DAY) AS days_since_join  -- scalar
FROM customers;
```

### Aggregate functions — many rows in, one row out

Already covered. The five most common:

- `COUNT`, `COUNTIF` — see [[Count and Countif]]
- `SUM`, `AVG`, `MIN`, `MAX` — see [[Sum Avg Min Max]]
- `STDDEV`, `VARIANCE` — for spread (referenced in [[Measures of Spread]])

```sql
SELECT
  category,
  COUNT(*)           AS items,
  AVG(price)         AS avg_price,
  SUM(stock_qty)     AS total_stock
FROM products
GROUP BY category;   -- aggregates require GROUP BY when paired with non-aggregate columns
```

See [[Group By]] for the grouping mechanics.

### Window functions — many rows in, one row out per source row

The third family is the focus of this lesson. Aggregates collapse rows; window functions compute the same summary but keep every original row intact. See [[Window Functions Fundamentals]].

```sql
SELECT
  category,
  product_name,
  stock_qty,
  SUM(stock_qty) OVER (PARTITION BY category) AS category_total_stock,
  stock_qty / SUM(stock_qty) OVER (PARTITION BY category) AS share_of_category
FROM products;
-- One row per product, with the category total visible on every row.
```

### User-defined functions (UDFs)

When the same logic appears in many queries, define it once as a function. See [[User Defined Functions Udf]].

```sql
CREATE FUNCTION margin(revenue NUMERIC, cost NUMERIC)
RETURNS NUMERIC
AS (
  SAFE_DIVIDE(revenue - cost, revenue)
);

SELECT order_id, margin(revenue, cost) AS margin_pct FROM orders;
```

UDFs do not invent new abilities; they package existing scalar logic for reuse and consistency.

## Key Parameters

- **Function family fits problem**: ask "how many rows in, how many rows out?" — that tells you which family
- **Built-in vs UDF**: prefer built-in when one exists; UDFs add overhead and reduce engine optimization
- **NULL propagation**: most scalars and aggregates handle NULL by returning NULL or skipping — see [[Null Handling SQL]]
- **SAFE_ variants** (`SAFE_CAST`, `SAFE_DIVIDE`, `SAFE.PARSE_DATE`): return NULL on failure instead of crashing — essential for ingestion

## When To Use

- **Scalar**: any per-row computation (formatting, parsing, arithmetic)
- **Aggregate**: any summary (KPIs, totals, averages, counts)
- **Window**: when you need a summary alongside row detail (ratios, ranks, running totals)
- **UDF**: when one logic appears 3+ times across queries — package it
- Anti-pattern: nesting 5+ scalars instead of writing a UDF — opaque and untested
- Anti-pattern: using a window function when an aggregate suffices — wastes compute on row preservation you do not need

## Connections

- Related: [[User Defined Functions Udf]], [[Window Functions Fundamentals]], [[Window Functions Across Grain]] — the deep dives on each topic in this lesson
- Builds on: every prior SQL lesson's individual function pages
- Compare with: Python/pandas function ecosystem (similar split: scalar vectorized ops, aggregates, rolling windows)
- Used by: every meaningful SQL query

## My Notes

- The "rows in / rows out" mental model is the cleanest way to learn SQL functions. Memorize it.
- Practice: [Fonksiyonlar](https://nextgen.workintech.com.tr/project/202/5?pid=7604) — sample the four families in a single project.
- BigQuery tip: hover over any function in the editor — inline docs show signature, types, return value, and example.
- Interview tip: when asked "what's the difference between an aggregate and a window function?", answer with "both summarize, but aggregates collapse rows; windows keep rows and add the summary per row."
