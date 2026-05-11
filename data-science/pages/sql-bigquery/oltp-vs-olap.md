---
title: "OLTP vs OLAP"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/03-oltp-ve-olap-sistemleri]]"
tags:
  - sql
  - oltp
  - olap
  - data-warehouse
  - system-architecture
---

# OLTP vs OLAP

> One-line summary: Two database paradigms — OLTP for fast small transactions in operational systems, OLAP for heavy analytical queries on aggregated historical data.

## Core Concept

Not all databases are designed for the same workload. **OLTP** (Online Transaction Processing) systems power day-to-day operations: an ATM withdrawal, a flight booking, an e-commerce checkout. They handle many small, fast reads and writes. **OLAP** (Online Analytical Processing) systems power analytics: revenue trends, cohort analysis, executive dashboards. They handle few, very large queries over historical data.

As a data analyst, you should almost never query OLTP directly — your big aggregations would slow down the operational system. You query OLAP (typically a data warehouse) instead, which receives data from OLTP via ETL/ELT pipelines.

## How It Works

| Aspect | OLTP | OLAP |
|--------|------|------|
| **Workload** | Many small reads/writes per second | Few large analytical reads |
| **Typical query** | Single row lookup or update | Aggregations across millions of rows |
| **Data freshness** | Real-time (live state) | Hours to days behind (batch loaded) |
| **Schema** | Highly normalized, many tables | Denormalized, fewer wider tables (star/snowflake schema) |
| **Storage layout** | Row-oriented | Column-oriented |
| **Example systems** | PostgreSQL, MySQL, Oracle, SQL Server | BigQuery, Snowflake, Redshift, Databricks |
| **Concurrency** | High (thousands of concurrent users) | Lower (data team + dashboards) |
| **Updates** | Frequent UPDATE/DELETE | Append-mostly, rarely updated |

### Why two systems, not one?

If you ran a 5-minute aggregation query on the operational database while customers are checking out, the checkout latency would spike. Splitting workloads means each system can be tuned for its purpose: OLTP for write speed and row locks, OLAP for compression and parallel scanning.

### The pipeline that connects them

```
OLTP database (live)
     │
     ▼  ETL/ELT (overnight or streaming)
OLAP warehouse (analytical)
     │
     ▼
Reports / dashboards / ML features
```

## Key Parameters

- **Row-oriented storage** (OLTP): all columns of a row stored together → fast single-row reads and writes
- **Column-oriented storage** (OLAP): all values of a column stored together → fast aggregations, high compression
- **Normalization level**: OLTP uses 3NF or higher; OLAP often uses denormalized star schemas for query speed
- **Latency tolerance**: OLTP must respond in milliseconds; OLAP can take seconds to minutes

## When To Use

- **OLTP**: any app that records live business transactions (orders, payments, user actions)
- **OLAP**: analytics, BI, reporting, ML feature engineering, customer segmentation
- **Anti-pattern**: Running heavy analytical SQL directly on the production database — even read-only queries can degrade write performance via lock contention or cache pollution
- **Anti-pattern**: Using a data warehouse as a transactional store — most warehouses do not support row-level updates efficiently

## Connections

- Related: [[Relational Data Model]] (used by both, applied differently), [[Entity Relationship Diagrams]]
- Builds on: Operating system I/O patterns, indexing concepts
- Compare with: NoSQL paradigms (key-value, document, graph) which solve different problems
- Used by: Data warehouse design, [[Descriptive Statistics]] (analytics often run on OLAP)

## My Notes

- BigQuery is OLAP. Every SQL example in this course assumes an OLAP-style backend.
- An analyst should know which side they are on — if a query takes 30 seconds and you are in OLTP, you are doing it wrong.
- Hybrid systems exist (HTAP — Hybrid Transactional/Analytical Processing) but are rare in practice.
- Practice: [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556) — analytical workload typical of OLAP.
