---
title: "SQL Fundamentals Overview"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
next_lesson: "[[SQL Computed Data Overview]]"
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/01-tanitim-ve-amaci]]"
tags:
  - sql
  - overview
  - umbrella
  - getting-started
---

# SQL Fundamentals Overview

> One-line summary: A map of the foundational SQL concepts — from the relational data model to query mechanics — that every data analyst needs before tackling joins, aggregations, and advanced analytics.

## Core Concept

SQL is the **lingua franca of structured data**. When spreadsheets break under the weight of millions of rows, multiple users, and live updates, SQL takes over. It is the language of relational databases, data warehouses, and most modern BI tools.

The lesson this page summarizes covers the irreducible foundation: how data is stored (model + types), how to read it (SELECT + WHERE + ORDER BY), and how to write it back (DDL + DML). Master these and most of analytics is downstream composition.

Why SQL won: declarative. You describe *what* you want, the engine figures out *how* to get it. That is what lets you query terabytes from your laptop.

## How It Works — The Concept Map

### Foundation — how data is structured

- [[Relational Data Model]] — tables, rows, columns, primary keys, foreign keys
- [[OLTP vs OLAP]] — operational vs analytical databases, the two worlds an analyst inhabits
- [[Entity Relationship Diagrams]] — the visual notation that turns a schema into a map
- [[SQL Data Types and Casting]] — types as contracts; CAST/SAFE_CAST for conversions

### Reading — projection, filter, sort

- [[Select Statement]] — the verb of every query; choose columns and tables
- [[Distinct and Deduplication]] — collapse duplicates with DISTINCT
- [[Filtering Where]] — restrict rows with WHERE, AND, OR, NOT, BETWEEN
- [[Pattern Matching SQL]] — fuzzy text search with LIKE and REGEXP
- [[In and Not In]] — set membership; replaces long OR chains
- [[Column Aliasing and Ordering]] — AS for renaming, ORDER BY for sorting

### Branching — per-row logic

- [[Conditional Expressions SQL]] — CASE WHEN and IF for derived columns and bucket labels
- [[Null Handling SQL]] — three-valued logic, IS NULL, COALESCE, SAFE_CAST

### Writing — mutating the database

- [[Create Update Delete]] — DDL (CREATE/ALTER/DROP) and DML (INSERT/UPDATE/DELETE)

## How They Fit Together

A typical analyst session moves through the concepts in roughly this order:

```
1. Explore the schema           → [[Entity Relationship Diagrams]]
2. Pick the right table          → [[Relational Data Model]]
3. Read a sample                 → [[Select Statement]]
4. Filter to a segment           → [[Filtering Where]], [[In and Not In]], [[Pattern Matching SQL]]
5. Handle missing data           → [[Null Handling SQL]], [[SQL Data Types and Casting]]
6. Bucket or label               → [[Conditional Expressions SQL]]
7. Dedupe and sort               → [[Distinct and Deduplication]], [[Column Aliasing and Ordering]]
8. Materialize if recurring      → [[Create Update Delete]] (CTAS)
```

Every later lesson (joins, aggregations, window functions, CTEs) **assumes** fluency with these. Skipping fundamentals creates debt that surfaces as confusing bugs months later.

## Key Parameters

- **SQL dialect**: this lesson uses BigQuery (Google Cloud) Standard SQL — most syntax also works in PostgreSQL, Snowflake, Redshift
- **Case-sensitivity**: keywords are case-insensitive (`SELECT` == `select`), but identifiers and string comparisons usually are case-sensitive
- **Execution order**: written `SELECT … FROM … WHERE`, but executed `FROM → WHERE → SELECT → ORDER BY` — explains why aliases work in ORDER BY but not WHERE

## When To Use

- **New analyst onboarding**: read this page first, then drill into each linked concept
- **Reviewing for an interview**: the page list is the curriculum
- **Building muscle memory**: rewrite every example from each linked page until you can recall them without looking

## Connections

- Builds on: spreadsheet thinking (rows, columns, formulas) — SQL extends it to billions of rows. See [[Google Sheets Analytics Overview]] for the Sheets ↔ SQL concept bridge.
- Related: [[Descriptive Statistics]] (analytics often starts with SQL aggregates that compute these), [[Measures of Central Tendency]] (COUNT, AVG, MIN, MAX are descriptive stats)
- Compare with: pandas in Python (similar operations, imperative syntax); spreadsheets (limited scale)
- Used by: every other SQL lesson — aggregations, joins, window functions, CTEs, advanced SQL

## My Notes

- The biggest beginner trap: thinking SQL is "easy because it reads like English." It is declarative and the engine does heavy work — that means subtle mistakes can produce wrong but plausible-looking results. Always sanity-check row counts.
- Practice projects for this lesson:
  - [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523) — basic SELECT/WHERE/DISTINCT workout
  - [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556) — slightly broader analytical requests
- Recommended ordering for self-study: [[Select Statement]] → [[Filtering Where]] → [[Conditional Expressions SQL]] → [[Null Handling SQL]] → then everything else.
- Returning to this overview after each later lesson reinforces the mental map — the concept graph compounds.
- **Next lesson:** [[SQL Computed Data Overview]] — aggregation (COUNT, SUM, AVG, GROUP BY, HAVING) plus scalar functions (ROUND, CONCAT, REPLACE, DATE_SUB).
