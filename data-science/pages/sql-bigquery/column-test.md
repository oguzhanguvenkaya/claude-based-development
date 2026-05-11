---
title: "Column Test"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/10-column-testi]]"
tags:
  - sql
  - testing
  - data-quality
  - null-check
  - range-check
  - accepted-values
---

# Column Test

> One-line summary: SQL tests that validate per-column rules — no unexpected NULLs, values within a range, only accepted categorical values, valid data types — returning offending rows when violations occur.

## Core Concept

If a table is a building, each column is a load-bearing pillar. A cracked pillar may not be visible from outside, but the whole structure is unsound. **Column tests** are inspections of individual pillars: is this column allowed to be NULL? Are its values in the expected range? Do its categorical values match an approved list?

Where [[Primary Key Test]] asks "is this row identifiable?", column tests ask "is the data inside the row plausible?" They catch ingest bugs, broken transformations, schema drift, and upstream data corruption.

## How It Works

### NULL check — column should never be NULL

```sql
-- Test: email should never be NULL in customers
SELECT *
FROM customers
WHERE email IS NULL;
```

Empty result = pass. Any row = a customer missing their email. Combine with HAVING for thresholds:

```sql
SELECT COUNT(*) AS null_emails
FROM customers
WHERE email IS NULL
HAVING COUNT(*) > 10;  -- tolerate up to 10 missing
```

See [[Null Handling SQL]].

### Range check — values within a sensible window

```sql
-- Test: order amount must be between $0 and $100,000
SELECT *
FROM orders
WHERE amount < 0 OR amount > 100000;
```

Catches negative orders (returns? bugs?) and ridiculous values (data entry typos, currency unit mistakes).

```sql
-- Test: order_date must not be in the future
SELECT *
FROM orders
WHERE order_date > CURRENT_DATE();
```

### Accepted values check — only allowed categories

```sql
-- Test: status must be one of a known set
SELECT *
FROM orders
WHERE status NOT IN ('pending', 'paid', 'shipped', 'delivered', 'cancelled');
```

Catches typos (`'shipped '` with a trailing space, `'PAID'` in wrong case) and unexpected new states from upstream that the report does not handle yet. See [[In and Not In]] and [[String Cleaning Replace and Case]].

### Type / format check — strings that should parse

```sql
-- Test: email should look like an email
SELECT *
FROM customers
WHERE NOT REGEXP_CONTAINS(email, r'^[^@]+@[^@]+\.[^@]+$');
```

See [[Pattern Matching SQL]] for REGEXP details.

### Referential integrity (a column test on FK)

```sql
-- Test: every order's customer_id must exist in customers
SELECT o.id, o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;
```

The anti-join pattern from [[Join Types]]. Catches orphaned foreign keys.

### dbt's declarative version

```yaml
columns:
  - name: email
    tests:
      - not_null
  - name: status
    tests:
      - accepted_values:
          values: ['pending', 'paid', 'shipped', 'delivered', 'cancelled']
  - name: amount
    tests:
      - dbt_utils.expression_is_true:
          expression: ">= 0"
```

Same underlying SQL; declarative syntax keeps tests readable next to the model definition.

## Key Parameters

- **Severity tiers**: hard fail (PK NULL) vs soft warning (a few missing optional values)
- **Thresholds**: HAVING COUNT(*) > N to tolerate small failure counts
- **Combined predicates**: one test can cover multiple rules (`WHERE col IS NULL OR col < 0 OR col > 100000`)
- **Scope**: column tests target single columns; cross-column rules (sum equals total) are [[Value Preservation Test]] territory

## When To Use

- **Required columns**: NULL check on any column the downstream layer treats as guaranteed
- **Numeric columns**: range check on amounts, durations, counts, percentages
- **Status / category columns**: accepted-values check to catch upstream changes
- **Foreign keys**: referential integrity check to catch orphans
- Anti-pattern: testing every column for every rule "just in case" — bloats the test suite without adding signal
- Anti-pattern: setting tolerance thresholds so high they never fire — defeats the point

## Connections

- Related: [[Testing Data Pipelines]] (parent — why we test), [[Primary Key Test]] (the row-level test), [[Value Preservation Test]] (the aggregate-level test)
- Builds on: [[Null Handling SQL]], [[In and Not In]], [[Pattern Matching SQL]], [[Filtering Where]]
- Compare with: schema enforcement (NOT NULL, CHECK constraints) — catches the same bugs at write time in OLTP; rare in OLAP warehouses
- Used by: every dbt project's `tests:` block, every production data quality framework

## My Notes

- Personal rule: every required column gets a `not_null` test. Every categorical column gets an `accepted_values` test. These two cover ~80% of column-level bugs.
- Practice: [Nova Finans Özeti Testi](https://nextgen.workintech.com.tr/project/202/3?pid=7600) — write NULL, range, and accepted-values tests for the summary's key columns.
- When a column test fails after a deploy, the bug is usually upstream — a new ingest source, a vendor format change, a typo in a CASE WHEN. Check the source first, not the test.
- BigQuery tip: schema "REQUIRED" mode prevents NULLs at write time — declare critical columns this way as belt + suspenders alongside the SQL test.
