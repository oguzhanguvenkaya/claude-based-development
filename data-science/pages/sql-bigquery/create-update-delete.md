---
title: "Create Update Delete"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/17-create-update-delete]]"
tags:
  - sql
  - ddl
  - dml
  - data-mutation
---

# Create Update Delete

> One-line summary: SQL commands that modify the database itself — CREATE makes new tables/columns (DDL), UPDATE changes existing rows, DELETE removes rows (DML). Unlike SELECT, these are irreversible without a backup.

## Core Concept

So far every SQL command we have looked at — `SELECT`, `WHERE`, `ORDER BY` — only **reads** data. The database stays untouched. The commands in this page **mutate** state.

They split into two families:

- **DDL** (Data Definition Language): CREATE, ALTER, DROP — change the **schema** (tables, columns, types)
- **DML** (Data Manipulation Language): INSERT, UPDATE, DELETE, MERGE — change the **data** (rows)

Mutations are powerful and dangerous. A misplaced `UPDATE` without a WHERE clause modifies every row in the table. A `DROP TABLE` is instant and (in most engines) not recoverable from within SQL.

## How It Works

### CREATE — make a new table

```sql
CREATE TABLE customers (
  customer_id INT64    NOT NULL,
  first_name  STRING,
  last_name   STRING,
  city        STRING,
  signup_date DATE,
  is_active   BOOL     DEFAULT TRUE
);
```

You declare each column's name, type, and any constraints. The result is an empty table ready to receive rows.

### CREATE TABLE AS SELECT (CTAS)

```sql
-- Build a new table from a query — common in data warehouses
CREATE TABLE premium_customers AS
SELECT * FROM customers
WHERE membership_tier = 'premium';
```

CTAS is the workhorse of ELT pipelines: it materializes a query as a new table, types inferred from the SELECT.

### INSERT — add rows

```sql
INSERT INTO customers (customer_id, first_name, last_name, city)
VALUES (1001, 'Alice', 'Wang', 'New York');

-- Multi-row insert
INSERT INTO customers (customer_id, first_name, last_name, city)
VALUES
  (1002, 'Bob', 'Smith', 'Boston'),
  (1003, 'Carol', 'Lee', 'Chicago');

-- INSERT from another query
INSERT INTO archive_customers
SELECT * FROM customers WHERE last_active < '2023-01-01';
```

### UPDATE — change existing rows

```sql
-- Update a single row
UPDATE customers
SET city = 'Brooklyn'
WHERE customer_id = 1001;

-- Update many rows
UPDATE orders
SET status = 'expired'
WHERE order_date < CURRENT_DATE() - INTERVAL 365 DAY
  AND status = 'pending';

-- DANGER — no WHERE clause: updates every row
UPDATE customers SET city = 'Default';
```

**Rule:** before running UPDATE, always run the same query as `SELECT * FROM table WHERE <same condition>` to preview which rows will change.

### DELETE — remove rows

```sql
-- Delete specific rows
DELETE FROM customers
WHERE last_active < '2020-01-01';

-- DANGER — no WHERE: empties the table
DELETE FROM customers;
```

`DELETE` removes rows but keeps the table structure. To remove the table entirely: `DROP TABLE customers`.

### ALTER — change schema

```sql
-- Add a column
ALTER TABLE customers ADD COLUMN phone STRING;

-- Drop a column (BigQuery)
ALTER TABLE customers DROP COLUMN phone;

-- Rename a column
ALTER TABLE customers RENAME COLUMN city TO city_name;
```

## Key Parameters

- **NOT NULL** constraint: declared at CREATE time; INSERTs without that column will fail
- **DEFAULT** value: applied when a row is inserted without specifying that column
- **WHERE in UPDATE/DELETE**: omitting it affects every row — almost never intended
- **Transactions**: in OLTP databases, wrap mutations in BEGIN/COMMIT/ROLLBACK; in BigQuery, mutations on DML are atomic per statement
- **TRUNCATE vs DELETE**: TRUNCATE empties the table faster but cannot use WHERE; DELETE is slower but precise

## When To Use

- **CREATE TABLE / CTAS**: building intermediate tables in an ELT pipeline; setting up new datasets
- **INSERT**: loading data into a warehouse (often via batch tools, not raw INSERTs in BigQuery)
- **UPDATE**: correcting bad data, backfilling new columns
- **DELETE**: removing test data, archiving old rows
- Anti-pattern: running UPDATE/DELETE without first writing the equivalent SELECT to preview
- Anti-pattern: using DML (UPDATE/DELETE) heavily in OLAP warehouses — they are optimized for append-only writes; prefer rebuilding the table via CTAS
- Anti-pattern: bare `DROP TABLE` on production data — restore from backup is a long road

## Connections

- Related: [[Relational Data Model]] (CREATE materializes the model), [[Select Statement]] (CTAS combines SELECT and CREATE), [[Oltp Vs Olap]] (DDL/DML cost profile differs by system)
- Builds on: schema design and transaction theory
- Compare with: dbt (modern data warehouses prefer declarative model files over imperative DDL); SQLAlchemy ORM (programmatic schema management)
- Used by: every production data pipeline; the ingestion-specific pattern lives at [[Bigquery Insert with Cast Workflow]]

## My Notes

- Personal rule: never run UPDATE or DELETE in production without first running the equivalent SELECT and inspecting the row count.
- Practice: in [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523), use CREATE TABLE AS SELECT to build a campaign-specific aggregation.
- BigQuery tip: mutations cost more than reads. INSERT/UPDATE/DELETE bills the entire affected partition.
- Interview tip: discuss undo strategies — backups, time travel (BigQuery supports 7-day undelete via `FOR SYSTEM_TIME AS OF`), versioned tables — when asked about destructive operations.
