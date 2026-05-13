---
title: "Joins Fundamentals"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/01-joine-giris]]"
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/02-join-kullanimi]]"
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/03-table-aliasing]]"
tags:
  - sql
  - join
  - on-clause
  - table-aliasing
---

# Joins Fundamentals

> One-line summary: JOIN combines rows from two tables using a matching condition (typically primary-key to foreign-key), letting you query related data as one virtual table — and table aliases keep the syntax readable.

## Core Concept

Relational databases split data across tables on purpose ([[Relational Data Model]]). Customers live in `customers`, their orders in `orders`, the products they bought in `products`. To answer "what did Alice buy?", you must **stitch** rows back together using the keys that link the tables. That stitching is JOIN.

A JOIN is not a copy — it is a virtual combination of rows that share a matching key. The result is a new wider table, computed on the fly, that you then SELECT from like any other source.

## How It Works

### Syntax: SELECT … FROM A JOIN B ON condition

```sql
SELECT
  purchases.id        AS purchase_id,
  purchases.quantity,
  products.name       AS product_name,
  products.price
FROM purchases
JOIN products
  ON purchases.product_id = products.id;
```

Reading: "for each row in `purchases`, find the `products` row whose `id` matches `purchases.product_id`, and combine them."

The `ON` clause is the join condition. Typical pattern: the foreign key of one table equals the primary key of the other. The FK ↔ PK relationship is exactly what [[Entity Relationship Diagrams]] document.

### Why qualify column names

Once two tables are joined, both contribute columns. If both have an `id` column, plain `SELECT id` is ambiguous and errors out. You must qualify with the table name:

```sql
SELECT purchases.id, products.id FROM purchases JOIN products ON ...;
```

This is correct but verbose. In any real query, the next step is to give tables short aliases.

### Table aliases — AS for tables

```sql
SELECT
  p.id         AS purchase_id,
  p.quantity,
  pr.name      AS product_name,
  pr.price
FROM purchases AS p
JOIN products  AS pr
  ON p.product_id = pr.id;
```

`AS` after the table name gives it a short alias. From that point on, every reference to the table — in SELECT, ON, WHERE, GROUP BY — uses the alias.

Conventions:
- Use 1–3 letter aliases meaningful to the reader (`p` for purchases, `c` for customers, `o` for orders)
- Once a table has an alias, you **must** use it; the original name is no longer in scope in most engines
- `AS` is optional (`FROM purchases p` works) but recommended for clarity

### Default join type: INNER

When you write `JOIN` without specifying a type, you get **INNER JOIN** — only rows that match in **both** tables. Rows in either table with no match are dropped. See [[Join Types]] for the four variants (INNER, LEFT, RIGHT, FULL OUTER).

### Joining without the keys table

```sql
-- Cross join (Cartesian product) — every combination
SELECT * FROM colors CROSS JOIN sizes;
-- If colors has 10 rows and sizes has 5, result has 50 rows
```

Rarely intentional, often a bug — when ON conditions are missing or wrong, the join behaves like CROSS and explodes row counts.

## Key Parameters

- **ON clause**: the matching condition; almost always FK = PK, but any boolean expression is valid
- **USING (col)**: shorthand when both tables have a column with the same name — `JOIN products USING (id)`
- **Table aliases**: required for self-joins; recommended for any multi-table query
- **NULL in join keys**: NULL never equals anything (even NULL), so rows with NULL keys are silently dropped by INNER JOIN

## When To Use

- Combining related data living in different tables (customers + orders + products)
- Enriching a fact table with dimensional data (a sales row + the store / region / product details)
- Looking up reference values (status codes, country names, currency conversions)
- Anti-pattern: joining without an ON clause — produces a CROSS JOIN; usually a bug
- Anti-pattern: long table names without aliases — queries become unreadable past 2 tables

## Connections

- Related: [[Join Types]] (which rows survive the join), [[Multiple Joins]] (chaining 3+ tables), [[Joins with Group By]] (aggregating joined data), [[Join Pitfalls Grain and Fan Out]] (what to watch for)
- Builds on: [[Relational Data Model]] (PK/FK relationships), [[Entity Relationship Diagrams]] (the join path you follow), [[Select Statement]] (JOIN sits between FROM and WHERE)
- Compare with: [[Nested Subqueries]] and [[Common Table Expressions Cte]] (often a JOIN can be rewritten as a subquery; see [[Join vs Subquery]] for when to pick each). The spreadsheet equivalent is [[Lookup Functions Sheets]] (VLOOKUP / XLOOKUP).
- Used by: every multi-table analytical query

## My Notes

- The single most common JOIN error: a typo in the ON clause that always evaluates true, producing a CROSS JOIN sized result. Always verify the result row count is sensible.
- Practice: [Greenweez Finans - JOIN](https://nextgen.workintech.com.tr/project/202/3?pid=7599) — combine sales and finance tables, watch the row count.
- Aliasing convention: lowercase one-letter aliases for top-level tables, two-letter for less-common ones. `c` for customers, `o` for orders, `pr` for products, `pi` for product_inventory.
- Interview tip: ask "what's the difference between USING(col) and ON a.col = b.col?" — USING auto-deduplicates the column in the result; ON keeps both.
