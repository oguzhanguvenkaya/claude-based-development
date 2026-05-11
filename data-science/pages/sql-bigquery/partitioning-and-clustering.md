---
title: "Partitioning and Clustering"
domain: data-science
category: sql-bigquery
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/13-veri-bolumlendirme-partitioning]]"
tags:
  - sql
  - bigquery
  - partitioning
  - clustering
  - performance
  - cost-optimization
---

# Partitioning and Clustering

> One-line summary: Partitioning splits a table into independent slices by a column (usually date) so queries scan only the relevant partitions; clustering sorts rows within each partition by other columns to skip irrelevant blocks — together they cut scan cost by orders of magnitude on large tables.

## Core Concept

A 1 TB unpartitioned table scans 1 TB on every query, no matter how narrow the filter. Same query against a daily-partitioned version scans only the day's slice — typically 1 GB or less. The compute savings are 1000×. This is why **partitioning is the most important BigQuery cost optimization**.

Clustering refines further: within each partition, rows are sorted by additional columns, so the engine can skip blocks that do not contain matching values. Partitioning prunes at the partition level; clustering prunes at the block level.

## How It Works

### Partitioning by date (most common)

```sql
-- Create a date-partitioned table
CREATE TABLE analytics.orders (
  order_id INT64,
  customer_id INT64,
  amount NUMERIC,
  order_date DATE
)
PARTITION BY order_date;

-- Query that benefits: scans only one day's partition
SELECT SUM(amount) FROM analytics.orders WHERE order_date = '2026-05-12';
```

Behind the scenes, BigQuery stores each day's rows in a separate physical partition. A WHERE clause on the partition column lets the engine skip every other partition entirely. Over 5 years of data, that is ~1825 partitions — most queries touch only 1–30 of them.

### Partition types

| Type | Use case | Example |
|------|----------|---------|
| **Time-unit column** | Most common — partition by a DATE / TIMESTAMP column | `PARTITION BY order_date` |
| **Ingestion time** | Auto-partition by load time when no date column exists | `PARTITION BY _PARTITIONTIME` |
| **Integer range** | Partition by an integer bucket | `PARTITION BY RANGE_BUCKET(customer_id, GENERATE_ARRAY(0, 10000, 100))` |

Date-column partitioning dominates real-world use; the other two are niche.

### The partition filter requirement

```sql
-- BAD: no partition filter, scans the entire table
SELECT * FROM analytics.orders WHERE customer_id = 12345;

-- GOOD: includes partition filter
SELECT * FROM analytics.orders
WHERE order_date >= '2026-01-01'   -- partition filter
  AND customer_id = 12345;
```

BigQuery has a `require_partition_filter` option that makes the engine refuse queries without a partition filter — a safety net for shared tables.

### Clustering — second-level optimization

```sql
CREATE TABLE analytics.orders (
  order_id INT64,
  customer_id INT64,
  amount NUMERIC,
  order_date DATE
)
PARTITION BY order_date
CLUSTER BY customer_id, status;
```

Within each daily partition, rows are sorted by `customer_id` then `status`. When you filter by either, the engine reads only the relevant blocks within the partition.

```sql
SELECT * FROM analytics.orders
WHERE order_date = '2026-05-12'    -- partition pruning
  AND customer_id = 12345;          -- clustering block pruning
```

Result: scans a fraction of a single day's partition. For a 100M-row table partitioned by date and clustered by customer, this query might scan 50 MB instead of 1 TB. **~20,000× savings.**

### When to partition vs cluster

| Pattern | Best for |
|---------|----------|
| **Partition only** | Time-series with date filters | Standard for fact tables |
| **Partition + cluster** | Time-series with secondary filters (customer, region) | KPI dashboard data |
| **Cluster only** | Small lookup tables that need fast WHERE | Dimensional tables under 1 GB |
| **Neither** | Tiny tables (< 1 GB) | Config tables, role lookups |

### Partition limits and behaviors

- BigQuery supports up to 4000 partitions per table — daily partitioning over 11 years
- For longer histories, partition by month or year
- Partitions can be deleted independently (clean up old data without rewriting the table)
- Streaming inserts allocate to today's partition by ingestion time
- Schema changes apply to all partitions atomically

### Clustering details

- Up to 4 cluster columns per table
- Clustering columns must be at the start of the row physical layout
- Adding/removing clustering requires recreating the table
- BigQuery automatically reorganizes clusters in the background; no manual maintenance needed

### Cost of partitioning itself

- Partitioning **adds no storage cost** — same bytes, just organized differently
- Partition pruning is **free** (it happens before the scan is billed)
- Clustering also adds no storage or compute cost beyond the initial setup

### A common mistake: filtering by a function on the partition column

```sql
-- BAD: function wraps the partition column → partition pruning DISABLED
SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2026;

-- GOOD: filter directly on the partition column
SELECT * FROM orders WHERE order_date BETWEEN '2026-01-01' AND '2026-12-31';
```

The engine cannot use partition pruning if the partition column is inside a function call. Always write the filter as a direct comparison.

### Combining with [[Bigquery Query Cost Model]] best practices

A well-optimized query combines:
1. **Select only needed columns** (column pruning)
2. **Filter on partition column** (partition pruning)
3. **Filter on cluster column** (block pruning)
4. **Materialize hot aggregates** (avoid recomputing — see [[Views vs Tables Tradeoffs]])

Each multiplies the savings. A 1 TB table optimally queried might scan 10 MB — five orders of magnitude smaller.

## Key Parameters

- **`PARTITION BY column`**: usually a DATE; can be TIMESTAMP, INT, or `_PARTITIONTIME`
- **`CLUSTER BY col1, col2, col3, col4`**: up to four columns, sorted by leftmost first
- **`require_partition_filter`**: BigQuery option to enforce partition filter on queries (default: false)
- **Partition expiration**: auto-delete partitions older than N days (saves storage on rolling data)
- **Reorg**: BigQuery handles cluster reorg automatically

## When To Use

- **Always partition fact tables on date** — orders, events, transactions, logs
- **Cluster on secondary filter columns** — customer_id, region, status
- **Always include partition filter in queries** — biggest single cost-saving habit
- **Set partition expiration on rolling tables** — automatic data retention
- Anti-pattern: partitioning a small table (< 1 GB) — overhead exceeds benefit
- Anti-pattern: clustering on a high-cardinality column that nobody filters on — wasted setup
- Anti-pattern: querying partitioned table without partition filter — scans entire table, defeats the purpose

## Connections

- Related: [[Bigquery Query Cost Model]] (partitioning is the main cost lever), [[Warehouse Storage vs Compute Cost]], [[Data Pipeline Architecture]] (silver/gold tables almost always partitioned), [[Filtering Where]] (where the partition filter lives)
- Builds on: [[SQL Data Types and Casting]] (DATE column needed for date partitioning), [[Create Update Delete]] (CREATE TABLE syntax)
- Compare with: Snowflake (uses micropartitions automatically — different model), Redshift (sort keys play a similar role to clustering)
- Used by: every production BigQuery deployment; absolutely standard for fact tables

## My Notes

- Partitioning is binary: either you have it and your queries are cheap, or you do not and they are expensive. The middle ground is rare.
- Practice: [BigQuery: Sorgu Maliyet Analizi ve Optimizasyonu](https://nextgen.workintech.com.tr/project/203/1?pid=7688) — partition an unpartitioned table; measure the cost difference on a typical query.
- BigQuery tip: when ingesting historical data, use the `_PARTITIONTIME` pseudo-column to populate the right partition: `INSERT INTO orders (...) SELECT *, DATE '2024-01-15' FROM staging`.
- Interview tip: when asked about query optimization, lead with "partition the table and include the partition filter" — it is the #1 BigQuery answer and most candidates miss it.
