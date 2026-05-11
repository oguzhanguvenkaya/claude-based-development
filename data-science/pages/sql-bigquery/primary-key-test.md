---
title: "Primary Key Test"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/09-primary-key-testi]]"
tags:
  - sql
  - testing
  - primary-key
  - uniqueness
  - data-quality
---

# Primary Key Test

> One-line summary: A SQL test that verifies the primary key column uniquely identifies every row — returns the duplicate keys when broken, an empty result when healthy.

## Core Concept

Almost every analytical bug downstream traces back to one upstream cause: a column that was supposed to be unique was not. A duplicate `customer_id` doubles a revenue total. A duplicate `order_id` after a join fans out into 4x line counts. A duplicate `transaction_id` makes a refund report show two entries for one event.

The **Primary Key Test** is the single most valuable SQL data quality check. It is short, fast, and catches a wide class of data corruption. Run it on every PK of every table that downstream queries depend on.

## How It Works

### The canonical test

```sql
-- Test: customer_id should be unique in customers
SELECT
  customer_id,
  COUNT(*) AS row_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

GROUP BY collapses rows by `customer_id`; HAVING keeps only the keys whose count is >1. See [[Group By]] and [[Where vs Having]].

- **Healthy**: 0 rows returned
- **Broken**: each duplicate key returned with its count

### Composite key test

When a single column is not unique but a combination is (common in junction tables):

```sql
-- Test: (order_id, line_number) should be unique in order_line_items
SELECT
  order_id,
  line_number,
  COUNT(*) AS row_count
FROM order_line_items
GROUP BY order_id, line_number
HAVING COUNT(*) > 1;
```

### Strict version: every row identifiable

Sometimes the PK is implicit (no column declared as PRIMARY KEY in DDL) but you know what it should be. The test enforces what the schema does not.

### Inspecting failures

```sql
-- When the basic test fails, drill into duplicates
SELECT *
FROM customers
WHERE customer_id IN (
  SELECT customer_id FROM customers GROUP BY customer_id HAVING COUNT(*) > 1
)
ORDER BY customer_id;
```

This returns every row in every duplicate group, so you can see what fields differ — often a sign of broken deduplication upstream.

### dbt's built-in version

```yaml
# In dbt_project: declarative test
models:
  - name: customers
    columns:
      - name: customer_id
        tests:
          - unique          # ≡ the PK test above
          - not_null
```

dbt compiles `unique` into exactly the SQL shown earlier. Most production data teams use dbt for this; the underlying SQL is what's important to understand.

### When the test legitimately allows duplicates

Some tables — event logs, audit trails — intentionally allow duplicate keys. The "PK test" then runs against a different column or composite, like `(event_id, occurred_at)` for idempotent event streams. The principle is the same; the columns change.

## Key Parameters

- **One PK per table**: the test runs against the declared (or assumed) PK
- **Composite keys**: list all columns in GROUP BY
- **NULL handling**: NULLs are treated as their own group in GROUP BY, so multiple NULL rows collapse — usually NULL PKs are themselves a bug
- **Performance**: GROUP BY + HAVING on a PK is fast — the engine has likely indexed or clustered it

## When To Use

- **Every fact table**: the PK of a fact table is sacred
- **Every dimension/lookup table** used in a JOIN: duplicate dimension keys cause fan-out (see [[Join Pitfalls Grain and Fan Out]])
- **After ingestion**: catch duplicate inserts immediately, not three transforms downstream
- **After dedup logic**: prove the dedup actually worked
- Anti-pattern: skipping the PK test because "it's obviously unique" — production data routinely surprises analysts
- Anti-pattern: declaring the PK in DDL but not testing it — many engines (BigQuery, Snowflake) do not enforce PK constraints

## Connections

- Related: [[Testing Data Pipelines]] (this is one of three test families), [[Column Test]] (the other column-level tests), [[Value Preservation Test]] (the join-safety test), [[Join Pitfalls Grain and Fan Out]] (this test catches the right-side uniqueness assumption)
- Builds on: [[Group By]], [[Count and Countif]], [[Where vs Having]]
- Compare with: dbt's `unique` test (declarative wrapper around the same SQL); `assert_unique` in pandas-like tools
- Used by: every production data quality framework

## My Notes

- A surprisingly common failure: PK test passes on the source table, fails on the staging table after a transformation introduced a duplicate from a bad JOIN. Always test after each transformation.
- Practice: [Nova Finans Özeti Testi](https://nextgen.workintech.com.tr/project/202/3?pid=7600) — run the PK test on the summary table; if it fails, your aggregation logic is wrong.
- BigQuery / Snowflake do not enforce PK constraints at the engine level (unlike PostgreSQL). The test is your only line of defense.
- Interview tip: when asked "how would you validate data after a complex transformation?", the PK test should be the first thing you mention.
