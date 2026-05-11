---
title: "Bigquery Insert with Cast Workflow"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/05-bigquery-insert-ve-cast-islemleri]]"
tags:
  - sql
  - bigquery
  - insert
  - cast
  - data-ingestion
---

# Bigquery Insert with Cast Workflow

> One-line summary: The canonical BigQuery pattern for moving data from a raw staging table to a typed production table — INSERT INTO + SELECT with CAST/SAFE_CAST to clean and convert types in one pass.

## Core Concept

Raw data lands ugly. CSVs import everything as STRING; APIs return mixed types; vendor exports come with dates in odd formats. The first transformation step in any pipeline is **typing** — converting STRING columns into INT64, DATE, TIMESTAMP, BOOL — and storing the cleaned result in a production-ready table.

In BigQuery this is done with `INSERT INTO production_table SELECT ... FROM staging_table`, where the SELECT does the type conversions inline. `SAFE_CAST` handles malformed rows by emitting NULL instead of failing the whole load.

## How It Works

### The pipeline shape

```
raw_leads (STRING everywhere)
     │
     ▼  INSERT INTO ... SELECT ... CAST/SAFE_CAST
clean_leads (typed: INT64, DATE, BOOL, etc.)
```

### Basic INSERT INTO ... SELECT

```sql
INSERT INTO marketing.clean_leads (
  lead_id,
  signup_date,
  age,
  is_qualified
)
SELECT
  SAFE_CAST(lead_id      AS INT64)  AS lead_id,
  SAFE_CAST(signup_date  AS DATE)   AS signup_date,
  SAFE_CAST(age          AS INT64)  AS age,
  SAFE_CAST(is_qualified AS BOOL)   AS is_qualified
FROM raw.leads;
```

Every column is cast explicitly. Malformed values become NULL (thanks to SAFE_CAST) instead of crashing the entire INSERT.

### CAST vs SAFE_CAST in INSERT

```sql
-- CAST: any bad row crashes the load
INSERT INTO clean.orders
SELECT CAST(amount AS NUMERIC) FROM raw.orders;
-- ERROR: Invalid cast on row 4287: '$1,200.00' to NUMERIC

-- SAFE_CAST: bad rows become NULL; load completes
INSERT INTO clean.orders
SELECT SAFE_CAST(REPLACE(REPLACE(amount, '$', ''), ',', '') AS NUMERIC)
FROM raw.orders;
```

Combining `REPLACE` (see [[String Cleaning Replace and Case]]) and `SAFE_CAST` is the standard "parse a messy number" idiom.

### Date parsing — PARSE_DATE for nonstandard formats

```sql
-- SAFE_CAST handles ISO format (YYYY-MM-DD)
SELECT SAFE_CAST('2024-12-31' AS DATE);  -- works

-- For other formats, use PARSE_DATE
SELECT PARSE_DATE('%m/%d/%Y', '12/31/2024');           -- 2024-12-31
SELECT PARSE_DATE('%d %b %Y', '31 Dec 2024');          -- 2024-12-31
SELECT SAFE.PARSE_DATE('%m/%d/%Y', 'not a date');      -- NULL (SAFE prefix)
```

See [[SQL Data Types and Casting]] for the broader type system, and [[Date Arithmetic Date Sub]] for date operations after parsing.

### CREATE TABLE AS SELECT (CTAS) — when starting fresh

If the destination table does not yet exist, CTAS is often cleaner:

```sql
CREATE TABLE marketing.clean_leads AS
SELECT
  SAFE_CAST(lead_id      AS INT64)  AS lead_id,
  SAFE_CAST(signup_date  AS DATE)   AS signup_date,
  SAFE_CAST(age          AS INT64)  AS age,
  SAFE_CAST(is_qualified AS BOOL)   AS is_qualified
FROM raw.leads;
```

BigQuery infers types from the SELECT. Use INSERT INTO when the table already exists with a defined schema; use CTAS to create + populate in one step. See [[Create Update Delete]].

### MERGE — upsert from staging to production

```sql
MERGE marketing.clean_leads AS target
USING (
  SELECT
    SAFE_CAST(lead_id     AS INT64) AS lead_id,
    SAFE_CAST(signup_date AS DATE)  AS signup_date
  FROM raw.leads
) AS source
ON target.lead_id = source.lead_id
WHEN MATCHED THEN
  UPDATE SET signup_date = source.signup_date
WHEN NOT MATCHED THEN
  INSERT (lead_id, signup_date) VALUES (source.lead_id, source.signup_date);
```

MERGE is the BigQuery upsert pattern: insert new rows, update existing ones, all in one atomic statement.

### Validating the load with tests

After the INSERT, run [[Primary Key Test]], [[Column Test]], and [[Value Preservation Test]] against the destination. If `raw.leads` had 10,000 rows but `clean.leads` has 9,847 after SAFE_CAST, you know 153 rows had at least one bad column.

## Key Parameters

- **SAFE_CAST**: returns NULL on failed conversion; essential for ingestion of untrusted data
- **SAFE. prefix**: SAFE_CAST, SAFE.PARSE_DATE, SAFE.PARSE_TIMESTAMP — same idea for related functions
- **Destination schema**: must be defined either by an existing table or by CTAS inference
- **Streaming inserts**: a different API for low-latency ingestion (`tabledata.insertAll`), beyond the SQL-only scope
- **Cost**: INSERT bills for the bytes inserted plus the bytes scanned by the SELECT

## When To Use

- **Initial type conversion** from raw STRING staging to typed production tables
- **Periodic batch loads** from CSV / external sources via raw staging
- **Schema migrations**: load old data into a new schema with renamed/recast columns
- **Filtering during load**: INSERT only valid rows by adding a WHERE clause
- Anti-pattern: bypassing staging and trying to load directly into typed tables — one bad row fails the whole load
- Anti-pattern: chained CASTs without SAFE_ — schedule one nightly load to fail and discover this the hard way
- Anti-pattern: production INSERTs without follow-up tests — silent corruption goes unnoticed

## Connections

- Related: [[Create Update Delete]] (INSERT is a DML; CTAS is DDL+DML), [[SQL Data Types and Casting]] (the type system underlying CAST), [[String Cleaning Replace and Case]] (clean before cast), [[Null Handling SQL]] (SAFE_CAST emits NULLs)
- Tested by: [[Primary Key Test]], [[Column Test]], [[Value Preservation Test]] — the tests that follow every load
- Compare with: dbt models (declarative, source-controlled), Dataflow (streaming ingestion), Cloud Composer / Airflow (orchestration)
- Used by: every BigQuery ingestion pipeline

## My Notes

- Defensive default: every CAST in ingestion code starts as SAFE_CAST. Promote to CAST only when you have a hard guarantee that the input cannot be malformed.
- Practice: load a CSV with intentionally messy data (mixed date formats, dollar signs in numbers, "N/A" in numeric columns) into a typed table. Count rows with NULLs after the load.
- BigQuery tip: `INSERT INTO ... SELECT ... LIMIT 0` is a no-op that can validate the SELECT plan and types without actually loading — useful for testing.
- Interview tip: when discussing data ingestion, name the SAFE_ family explicitly. It signals familiarity with real-world dirty-data handling.
