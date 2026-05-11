---
title: "Bigquery Query Cost Model"
domain: data-science
category: sql-bigquery
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/11-bigquery-sorgu-maliyetleri]]"
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/12-sutun-ve-satir-bazli-maliyetler]]"
tags:
  - sql
  - bigquery
  - cost-model
  - columnar-storage
  - query-optimization
---

# Bigquery Query Cost Model

> One-line summary: BigQuery prices queries by bytes scanned — driven primarily by the **columns selected** (not rows touched) thanks to columnar storage — with a 10 MB minimum per query; select fewer columns, filter by partitions, and most cost problems disappear.

## Core Concept

BigQuery's on-demand pricing reduces to one number: **bytes scanned per query**. The minimum is 10 MB. The rate is $6.25/TB scanned. Everything else — performance, optimization, query rewriting — flows from that single dial.

The non-obvious part: bytes scanned is determined by the **columns** in your SELECT, not the rows. This is the consequence of **columnar storage**, where each column is stored physically separate. A query that touches one column from a 1 TB table might scan only 10 GB, even though it returns the same number of rows as `SELECT *` (which would scan all 1 TB).

Mastering this single fact is the single highest-ROI BigQuery skill.

## How It Works

### The cost formula

```
bytes_scanned = sum of byte sizes of the columns referenced × rows in partitions read
cost          = max(10 MB, bytes_scanned) × $6.25/TB
```

References include columns in SELECT, WHERE, GROUP BY, JOIN ON, ORDER BY — anywhere a column is touched.

### Why columnar storage matters

```
Row-oriented (OLTP):           Column-oriented (BigQuery, all OLAP):
[id|name|email|age|...]        Column 1: [id, id, id, id, ...]
[id|name|email|age|...]        Column 2: [name, name, name, ...]
[id|name|email|age|...]        Column 3: [email, email, email, ...]
...                            Column 4: [age, age, age, age, ...]
```

In row storage, reading any column means reading the whole row. In column storage, reading one column means reading only that column's bytes. For analytical queries that touch 2–5 columns out of 50, this is a 10–25× scan reduction.

### Practical example

A `customers` table with 100M rows and 20 columns, total 100 GB.

```sql
-- Scans only 8 GB (the email and signup_date columns)
SELECT email, signup_date FROM customers;

-- Scans 100 GB (every column)
SELECT * FROM customers;

-- Same 8 GB scan as the first query — WHERE filter doesn't change scan size
SELECT email, signup_date FROM customers WHERE country = 'US';
-- (But: WHERE country = 'US' DOES add `country` to the scan, making it ~10 GB)
```

The cost difference: 8 GB × $6.25/TB ≈ $0.05; 100 GB × $6.25/TB ≈ $0.63. **12× cheaper** for the same row count.

### The 10 MB minimum

Every query is billed for at least 10 MB. Even `SELECT 1` costs $0.00006 because of this floor. For tiny tables, the minimum dominates — the 100-row config table costs the same to scan as a 1 MB scan would.

### Why WHERE without partitioning does NOT save scan cost

A common surprise:

```sql
-- Even though only 1000 rows match, BigQuery still scans the whole `country` column
SELECT email FROM customers WHERE country = 'US';
```

WHERE is a row filter, not a scan filter. The engine still reads the whole `country` column to find which rows match. Both `email` and `country` are scanned.

The exception: if `customers` is **partitioned** or **clustered** by `country`, BigQuery can skip irrelevant partitions/blocks entirely. See [[Partitioning and Clustering]].

### How partitioning reduces scan cost

```sql
-- Unpartitioned: scans the full date column over 5 years of data
SELECT amount FROM orders WHERE order_date = '2026-05-12';

-- Same query, but `orders` partitioned by order_date:
-- scans only the 2026-05-12 partition (1/1825 of total data)
SELECT amount FROM orders WHERE order_date = '2026-05-12';
```

Partition pruning is the single biggest BigQuery cost optimization. Always include partition filters when the table is partitioned.

### Estimating cost before running

```
-- In the BigQuery Console: the editor shows "This query will process X.X GB"
-- Via CLI:
bq query --dry_run --use_legacy_sql=false 'SELECT email FROM customers'
```

The dry run returns the byte estimate without executing. Train yourself to read it before running heavy queries.

### Per-query optimization checklist

1. **SELECT only needed columns** — never `SELECT *` in production
2. **Filter on partitioned column** — `WHERE date_col >= 'X'`
3. **Filter on clustered column** — narrows blocks within partitions
4. **Use APPROX_COUNT_DISTINCT instead of COUNT(DISTINCT)** when ±1% accuracy is acceptable
5. **Use INT64 instead of STRING for high-cardinality keys** — smaller per-row bytes
6. **Avoid SELECT * in CTEs** — even unused columns are scanned
7. **Materialize hot aggregates** — turn 1 TB scans into 10 MB scans (see [[Views vs Tables Tradeoffs]])

### What is NOT charged

- **Failed queries** — if a query errors, you pay nothing
- **Query result caching** — re-running an identical query within 24 hours returns the cached result, no scan
- **Time travel within 7 days** — included
- **Storage of query results** — temp tables expire after 24 hours; do not count toward storage

### Slot mechanics (advanced)

Under the hood, each query consumes **slots** (parallel processing units). On-demand pricing converts the slot usage to bytes scanned. With reservations, you pay for slot capacity directly. The two pricing models settle the same underlying compute — different commercial wrappers.

## Key Parameters

- **Bytes per column type**: INT64 = 8 bytes/row, FLOAT64 = 8, NUMERIC = 16, STRING ≈ 2 × char count + 2, DATE = 8, TIMESTAMP = 8, BOOL = 1
- **Minimum charge**: 10 MB per query
- **On-demand rate**: $6.25/TB (US regions; varies by region)
- **Query result cache TTL**: 24 hours; deterministic results cached automatically
- **dry-run flag**: free; returns byte estimate without execution

## When To Use

- **Before every heavy query**: read the byte estimate
- **When investigating a bill spike**: query the `INFORMATION_SCHEMA.JOBS` view for top-cost queries
- **When designing dashboards**: pre-aggregate; do not let BI tools issue `SELECT *` against TB tables
- **When onboarding new analysts**: the dollar-amount feedback is the fastest teacher of efficient SQL
- Anti-pattern: ignoring the byte estimate "for speed of iteration" — one bad query can cost more than a week's coffee budget
- Anti-pattern: using `SELECT *` to "see all columns" on a TB table — use `LIMIT 10` or query INFORMATION_SCHEMA for the schema

## Connections

- Related: [[Warehouse Storage vs Compute Cost]] (the two-meter model), [[Partitioning and Clustering]] (the main scan-reducer), [[Warehouse Pricing Models]] (on-demand vs flat-rate), [[Modern Warehouse Comparison]] (BigQuery's pricing in context)
- Builds on: [[Select Statement]] (column selection matters), [[Filtering Where]], [[Joins Fundamentals]]
- Compare with: Snowflake (per-second virtual warehouse, not per-byte), Redshift (cluster-based)
- Used by: every cost-conscious BigQuery user; FinOps teams; performance engineers

## My Notes

- The single most important habit: **glance at the byte estimate before every run.** Make it muscle memory.
- Practice: [BigQuery: Sorgu Maliyet Analizi ve Optimizasyonu](https://nextgen.workintech.com.tr/project/203/1?pid=7688) — run dry-run on three of your worst queries; rewrite to reduce scan size.
- BigQuery tip: `INFORMATION_SCHEMA.JOBS_BY_PROJECT` shows every query's bytes scanned and cost for the last 6 months — use it to find runaway queries.
- Interview tip: when asked "how would you reduce BigQuery cost?", lead with column pruning, then partitioning, then materialization, then pricing model — in that order, biggest impact first.
