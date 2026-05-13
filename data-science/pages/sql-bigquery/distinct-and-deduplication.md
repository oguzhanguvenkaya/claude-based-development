---
title: "Distinct and Deduplication"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/06-distinct]]"
tags:
  - sql
  - distinct
  - deduplication
  - data-quality
---

# Distinct and Deduplication

> One-line summary: The DISTINCT keyword collapses duplicate rows in a query result, returning only unique combinations of the selected columns.

## Core Concept

When you `SELECT city FROM customers`, the result repeats every city as many times as it appears in the table — once per customer. If the goal is "what cities do we serve?", you do not want that. `DISTINCT` removes the duplicates and returns each unique value once.

`DISTINCT` operates on the **combination** of all columns in the SELECT clause, not on a single column. This subtlety is the source of most DISTINCT mistakes.

## How It Works

### Single column

```sql
SELECT DISTINCT city
FROM customers;
```

If 10,000 customers live across 50 cities, this returns 50 rows.

### Multiple columns

```sql
SELECT DISTINCT city, country
FROM customers;
```

This returns unique `(city, country)` **pairs**. New York USA and New York Canada are two different rows. A common mistake is expecting DISTINCT to apply to only the first column listed.

### DISTINCT vs GROUP BY

These two queries are equivalent:

```sql
SELECT DISTINCT city FROM customers;

SELECT city FROM customers GROUP BY city;
```

`GROUP BY` is more flexible because you can add aggregations (`COUNT(*)`, `SUM(amount)`) in the same query, while `DISTINCT` only deduplicates. Use `DISTINCT` for pure deduplication, `GROUP BY` when you also want to compute per-group metrics.

### Counting distinct values

```sql
SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```

This answers: "how many unique customers placed at least one order?" Different from `COUNT(*)`, which counts all rows including repeats.

## Key Parameters

- **All columns matter**: DISTINCT considers every column in the SELECT list — adding or removing a column changes the result set entirely
- **NULL handling**: DISTINCT treats NULLs as equal to each other, so multiple NULL rows collapse to one
- **Performance**: DISTINCT requires the engine to sort or hash the data — on large tables it can be expensive
- **`COUNT(DISTINCT ...)`**: a common aggregate, but in BigQuery it can be slow; `APPROX_COUNT_DISTINCT` trades exactness for speed

## When To Use

- "What unique values exist in this column?" — DISTINCT on one column
- "What unique combinations exist?" — DISTINCT on multiple columns
- Building a lookup or dimension table from a fact table
- Anti-pattern: using `SELECT DISTINCT *` to "clean up" a table — it hides the real duplication problem instead of fixing the source data ([[Null Handling SQL]] and proper [[Relational Data Model]] design are usually the cure)
- Anti-pattern: combining DISTINCT with `ORDER BY` on a column not in the SELECT list — some engines reject it, others silently change behavior

## Connections

- Related: [[Select Statement]] (DISTINCT is a SELECT modifier), [[Conditional Expressions SQL]] (often used together for cohort lists), [[Count and Countif]] (`COUNT(DISTINCT col)` is the most common DISTINCT pattern)
- Builds on: set theory — DISTINCT enforces the mathematical definition of a set
- Compare with: [[Group By]] (more flexible, allows aggregations); `ROW_NUMBER() OVER (...)` (for keeping the first occurrence of duplicates instead of collapsing them — see [[Window Functions Fundamentals]])
- Used by: [[Measures of Central Tendency]] (counting unique values is a basic descriptive statistic); a common workaround for [[Join Pitfalls Grain and Fan Out]] (though pre-aggregation is usually cleaner). The spreadsheet equivalent is the UNIQUE function — see [[Filter Query Unique Sheets]].

## My Notes

- A surprising number of "data quality" tasks start with `SELECT DISTINCT key_column` to find unexpected duplicates.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), use DISTINCT to find unique campaign IDs or customer segments.
- BigQuery tip: prefer `APPROX_COUNT_DISTINCT(col)` over `COUNT(DISTINCT col)` for large tables when ±1% accuracy is acceptable — orders of magnitude faster.
- Interview gotcha: "Does `SELECT DISTINCT col1, col2` deduplicate on col1 only?" No — on the pair.
