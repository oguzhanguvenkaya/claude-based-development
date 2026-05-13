---
title: "Warehouse Storage vs Compute Cost"
domain: data-science
category: sql-bigquery
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/08-depolama-ve-isleme-ucretleri]]"
tags:
  - sql
  - cost-model
  - storage
  - compute
  - bigquery
---

# Warehouse Storage vs Compute Cost

> One-line summary: Modern data warehouses charge on two independent meters — storage (cheap, paid per GB of data at rest) and compute (expensive, paid per query that scans those bytes) — and the right architecture balances the two for each workload.

## Core Concept

The cost of running a warehouse is not a single number — it is the sum of two very different meters. **Storage** is cheap and grows linearly with data volume. **Compute** is expensive and grows with query frequency × bytes scanned per query.

A workload that costs $50/month in storage can easily cost $5000/month in compute if the same heavy query runs hundreds of times per day. Conversely, a workload that materializes everything pays storage fees on data nobody reads. Knowing which meter dominates for each workload is the foundation of cost optimization.

## How It Works

### The two meters

| Meter | Charged on | BigQuery default rate | Optimization lever |
|-------|-----------|----------------------|---------------------|
| **Storage** | GB stored per month | $0.02/GB active, $0.01/GB long-term | Delete unused data, partition, archive |
| **Compute (on-demand)** | TB scanned per query | $6.25/TB | Select fewer columns, filter partition, materialize hot aggregates |

(Rates vary by region and pricing model — see [[Warehouse Pricing Models]].)

### Independent scaling

In BigQuery (and Snowflake), storage and compute are **decoupled** — you can have 100 TB stored but zero compute usage in a month (and pay only storage), or vice versa. Older warehouses (Redshift legacy) coupled them, forcing you to size the cluster for the bigger of the two.

This decoupling is the architectural breakthrough of the modern warehouse era. It enables the [[Hybrid Table View Pipeline Pattern]]: you can materialize hot data (storage cost) to slash query cost, without buying a bigger server.

### Workload patterns

**Read-heavy, query-bound:** A dashboard that runs the same aggregation 1000 times per day. Storage is small (the result table); compute is the dominant cost. Solution: materialize the hot table, scan minimal columns per query.

**Write-heavy, storage-bound:** An event-logging table receiving 1 billion rows per day. Storage grows fast; queries are infrequent (analysts run ad-hoc analyses occasionally). Solution: partition by date, set long-term archival, drop old data, accept that occasional analytical queries are cheap.

**Cold archive:** A regulatory backup that may never be queried. Storage only; compute is zero. Solution: long-term storage tier (50% cheaper after 90 days untouched).

### How BigQuery prices a query

```sql
SELECT order_id, amount FROM orders WHERE order_date = '2026-05-12';
```

BigQuery prices this query on:
1. **Columns scanned**: `order_id` + `amount` only (it skips other columns entirely — see [[Bigquery Query Cost Model]])
2. **Rows scanned**: depends on partitioning — if `orders` is partitioned by `order_date`, only the one partition is scanned
3. **Bytes per row**: the type-size of `order_id` (INT64 = 8 bytes) + `amount` (NUMERIC = ~16 bytes)
4. **Min charge**: 10 MB minimum per query

So a properly partitioned `SELECT order_id, amount` over one day might scan 50 MB; the same `SELECT *` without partitioning could scan 500 GB. **Same data, 10,000× cost difference.**

### Storage tiers (BigQuery example)

- **Active storage** ($0.02/GB-month): tables modified in the last 90 days
- **Long-term storage** ($0.01/GB-month): tables untouched for 90+ days — automatic, no action needed
- **Time travel** (free, 7-day default): point-in-time snapshots; queryable for accidental recovery

You do not pay separately for time travel within the default window — it is included.

### Compute pricing (BigQuery example)

- **On-demand**: $6.25/TB scanned, no commitment, no idle cost
- **Reservations** (flat-rate): buy slots in $200/100-slot/month chunks; predictable cost; idle slots wasted
- **Enterprise editions**: tiered pricing for organizations with SLA needs

See [[Warehouse Pricing Models]] for the on-demand vs flat-rate decision.

### Cost shifting via materialization

The hybrid pattern is essentially **trading compute for storage**:

```
Without materialization:
   Each query scans 100 GB of silver tables × 1000 queries/day = 100 TB/day
   Cost: 100 × $6.25 = $625/day compute, $0 incremental storage

With materialization (10 GB gold table refreshed daily):
   Refresh job scans 100 GB once = $0.625/day
   Each dashboard query scans 10 GB × 1000 queries/day = 10 TB/day
   Cost: 10 × $6.25 = $62.50/day compute + $0.20/day storage
```

The materialized table saves ~$560/day in compute for a ~$0.20/day storage cost. The ROI is obvious. See [[Views vs Tables Tradeoffs]].

## Key Parameters

- **Active vs long-term storage**: automatic in BigQuery; manual archival policies in Snowflake/Redshift
- **Bytes-scanned attribution**: BigQuery shows estimated cost before running a query (dry-run via `--dry_run` flag or Console)
- **Slot reservations**: when query volume is predictable, slot reservations cost less than on-demand
- **Idle cost**: in BigQuery on-demand, zero idle cost; in slot reservations, idle slots are wasted
- **Cost monitoring**: every warehouse exposes per-query and per-user cost metrics; export to dashboards

## When To Use

- **Before optimizing**: run dry-runs to see what each query costs; the worst offenders are usually obvious
- **When designing new pipelines**: choose materialization with cost in mind (see [[Hybrid Table View Pipeline Pattern]])
- **Periodic review**: monthly bill spike investigations; quarterly audits of top queries
- Anti-pattern: optimizing storage on a query-heavy workload — you save pennies while compute drains dollars
- Anti-pattern: optimizing compute on a write-heavy archive workload — opposite problem
- Anti-pattern: choosing a warehouse without modeling expected workload — costs vary 5× across platforms for the same workload

## Connections

- Related: [[Warehouse Pricing Models]] (on-demand vs flat-rate), [[Bigquery Query Cost Model]] (BigQuery-specific details including why column selection matters), [[Partitioning and Clustering]] (the main compute-side optimization), [[Views vs Tables Tradeoffs]]
- Builds on: [[Data Platform Overview]], [[Data Pipeline Architecture]]
- Compare with: traditional databases (storage + compute coupled to a single server's resources)
- Used by: every cost-conscious data team; warehouse spend is often a top-3 line item in tech budgets

## My Notes

- A useful first move when joining a new team: pull the warehouse cost dashboard and identify the top 5 most-expensive recurring queries. Optimizing them usually pays back the time investment in a week.
- Practice: [BigQuery: Sorgu Maliyet Analizi ve Optimizasyonu](https://nextgen.workintech.com.tr/project/203/1?pid=7688) — run a dry-run on three different queries and compute their relative costs.
- BigQuery tip: the editor shows estimated scan size before query execution — train your eye to read it every time.
- Interview tip: discussing decoupled storage + compute signals understanding of modern warehouse architecture, distinguishes you from candidates who only know Postgres-style coupled systems.
