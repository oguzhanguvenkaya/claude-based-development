---
title: "Testing Data Pipelines"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/08-neden-test-ediyoruz]]"
tags:
  - sql
  - testing
  - data-quality
  - dbt
  - assertions
---

# Testing Data Pipelines

> One-line summary: SQL data tests are assertions you run against your tables — like unit tests for analysts — catching bad data at the source instead of letting it spread into dashboards and decisions.

## Core Concept

Data errors almost never surface at the dashboard. They surface during extraction, transformation, or join — long before anyone notices the wrong number. A small bug ("two rows for the same customer ID") can silently double a metric, and by the time someone questions the number, the corruption has propagated through dozens of downstream tables.

The fix is the same idea software engineers have used for decades: **write tests**. SQL data tests are queries that return 0 rows when the data is healthy and >0 rows when it is broken. Run them on every pipeline run; fail loudly when they break.

This page is the **hub** of the SQL testing family — it explains why and how to test. The specific test types live in their own pages.

## How It Works

### The basic shape of a SQL test

A SQL test is a query that returns the **bad rows**. Healthy → empty result. Broken → rows you can inspect.

```sql
-- Test: customer_id should be unique
SELECT customer_id, COUNT(*) AS dup_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
-- Empty result = pass; any row = fail
```

The pipeline runner checks: `if rows > 0 then alert`. That's it.

### Three families of tests

| Test type | What it asserts | Catches |
|-----------|----------------|---------|
| [[Primary Key Test]] | Each row uniquely identified | Duplicate rows, ingest bugs, fan-out from upstream joins |
| [[Column Test]] | Per-column rules (no NULLs, in range, valid set) | Bad inputs, broken transformations, schema drift |
| [[Value Preservation Test]] | Aggregate totals unchanged across transformations | Silent row drops, accidental fan-out, ETL bugs |

Most teams write all three for any critical table.

### Where tests run

- **Inline in dbt models**: dbt's `tests:` block declaratively defines tests next to model definitions. Failures break the build.
- **As scheduled queries**: BigQuery / Snowflake scheduled queries run tests on a cadence and post failures to Slack / email
- **In CI/CD before deploy**: validate the new pipeline against a sample dataset before promoting to production
- **In manual review**: copy-paste a test query into the BigQuery console while debugging

### The "0 rows = pass" contract

Why return failing rows instead of a boolean?
- When a test fails, you want to **see what failed** immediately, not just be told "something broke"
- Aggregations summarize the damage: how many duplicates, how many NULLs, how big the gap
- The test query is itself the debugger

### Test-driven analytics

The pattern that mature data teams converge on:
1. Define the table's contract (PK, required columns, expected totals)
2. Write the tests **before or alongside** the production query
3. Every code change runs the tests; failures block the merge
4. Production runs the tests after each refresh; failures page on-call

dbt, Great Expectations, and Soda are the popular tools that operationalize this.

## Key Parameters

- **Test as a single query**: keep tests simple — one assertion per query, easy to debug
- **Frequency**: run after every transformation that touches the table
- **Severity**: not all failures are equal — a duplicate PK is a hard fail; a few NULLs in an optional column may be a warning
- **Threshold**: some tests tolerate small failure counts (e.g., "fewer than 10 NULLs in a 1M-row column is acceptable")
- **Documentation**: a test without a one-line explanation of what it asserts is a future debugging burden

## When To Use

- **Always** for primary keys of tables that downstream queries depend on
- **Always** for any totals that the business reports externally (revenue, user counts)
- **Before joins**: validate uniqueness on the right side of any LEFT JOIN to avoid fan-out (see [[Join Pitfalls Grain and Fan Out]])
- **After ingestion**: catch ingest bugs before they propagate
- Anti-pattern: writing tests that always pass — they catch nothing; review each test's failure mode
- Anti-pattern: 1000 tests no one reads when they fail — keep tests few, loud, and meaningful

## Connections

- Related: [[Primary Key Test]] (uniqueness), [[Column Test]] (per-column rules), [[Value Preservation Test]] (totals across joins), [[Join Pitfalls Grain and Fan Out]] (the bugs tests are designed to catch)
- Builds on: [[Group By]] (most tests use GROUP BY + HAVING), [[Count and Countif]] (test queries are mostly counting queries)
- Compare with: software unit tests (same mindset, different domain); Great Expectations (Python-based data quality framework)
- Used by: every production analytical pipeline; dbt's testing layer is the de facto industry standard

## My Notes

- The mindset shift that separates senior from junior analysts: **assume your data is broken until tests prove it isn't**. Treat the absence of tests as "we have no idea if this is right."
- Practice: [Nova Finans Özeti Testi](https://nextgen.workintech.com.tr/project/202/3?pid=7600) — write each of the three test types against the finance summary table.
- A useful first test for any new table: "Does the row count match what I expected?" — it is one line of SQL and catches a lot.
- Interview tip: when discussing data pipeline reliability, mention specific test types ("PK uniqueness, column NULLs, value preservation across joins") — shows you've thought about failure modes concretely.
