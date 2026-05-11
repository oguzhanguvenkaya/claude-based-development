---
title: "Data Pipeline Architecture"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/01-veri-hatti-genel-bakis]]"
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/02-donusum-asamalari-ve-veri-modelleme]]"
tags:
  - sql
  - data-pipeline
  - medallion-architecture
  - data-modeling
  - bronze-silver-gold
---

# Data Pipeline Architecture

> One-line summary: A data pipeline transforms raw source data through staged layers — bronze (raw), silver (cleaned), and gold (business-ready) — turning messy operational inputs into consistent, analytics-ready models that dashboards and reports can rely on.

## Core Concept

When a company's data lives across many systems — CRM, billing, product event logs, third-party integrations — every dashboard query that joins them lives in pain. Schemas drift. Definitions diverge. The same "revenue" number means three different things to three teams.

A **data pipeline** solves this by funneling all sources through a predictable transformation chain. Each layer has a clear job, a clear contract, and clear consumers. The most widely adopted convention is the **medallion architecture** (bronze → silver → gold) popularized by Databricks and now standard across modern warehouses.

## How It Works

### The three layers

| Layer | Contents | Purpose | Updated |
|-------|----------|---------|---------|
| **Bronze** (raw) | Ingested as-is from source | Capture everything, lossless | Continuously / batch |
| **Silver** (cleaned) | Typed, deduplicated, validated | One canonical version per entity | Daily / hourly |
| **Gold** (modeled) | Aggregated, business-friendly | Direct dashboard / ML feed | Daily / on-demand |

Each layer's output is the next layer's input. A query against gold tables should never reference bronze; that would bypass the cleaning logic and risk inconsistency.

### A concrete pipeline

```
Salesforce (CRM)        ──┐
Stripe (billing)        ──┼──> bronze.raw_*  ──> silver.dim_*, silver.fact_*  ──> gold.metric_*
Product event logs      ──┘     (typed copy)    (cleaned + joined)               (business KPIs)
```

- **Bronze**: `bronze.raw_salesforce_accounts`, `bronze.raw_stripe_invoices`, `bronze.raw_events`
- **Silver**: `silver.dim_customers` (unified customer entity), `silver.fact_subscriptions`
- **Gold**: `gold.weekly_revenue`, `gold.churn_rate_by_cohort`, `gold.trial_to_paid_conversion`

### Four transformation stages

Within the pipeline, every step does one of four jobs:

1. **Clean** — fix types, deduplicate, drop garbage rows, handle NULLs ([[Null Handling SQL]], [[SQL Data Types and Casting]])
2. **Enrich** — join lookup tables, derive new fields, attach categorizations
3. **Aggregate** — collapse to coarser grain (per-day, per-customer summaries) using [[Group By]]
4. **Join** — combine entities into the wider tables that dashboards consume ([[Joins Fundamentals]])

A silver model is typically one or two of these; a gold model is usually all four.

### Why staging matters

Going directly from bronze to gold in one massive query would:
- Be unmaintainable (a 200-line CTE chain)
- Make testing impossible (no intermediate to inspect)
- Force every consumer to recompute the cleaning logic
- Break when a source schema changes (one bad column propagates everywhere)

Layers create **contracts** — silver promises clean data to gold; gold promises business-ready data to dashboards. Each layer can be tested independently. See [[Testing Data Pipelines]].

### Modeling within each layer

- Bronze tables: usually one-to-one with the source (raw_stripe_invoices ↔ Stripe's `invoices` endpoint)
- Silver tables: follow [[Relational Data Model]] norms — `dim_*` for slowly-changing entities, `fact_*` for events; one row per business object at the grain of that object
- Gold tables: denormalized for query speed, often star-schema; sometimes one mart per consumer team (`gold_marketing.*`, `gold_finance.*`)

This is the same dimensional modeling discipline data warehouses have used since Kimball's books in the 90s — recast for the cloud era.

### Orchestration

Pipelines do not run themselves. Tools like **dbt**, **Airflow**, and **Dagster** schedule each layer's refresh, track lineage between models, and surface failures. dbt is the lingua franca for the SQL-side transformations covered in this curriculum.

## Key Parameters

- **Refresh cadence per layer**: bronze near-real-time, silver hourly/daily, gold daily/weekly — depends on freshness needs and cost (see [[Views vs Tables Tradeoffs]])
- **Schema contract**: each layer's columns are documented and tested; downstream consumers code against the contract, not the implementation
- **Lineage**: which gold table depends on which silver, which silver depends on which bronze — tools auto-generate this
- **Storage cost vs recompute cost**: materializing each layer (table) costs storage; views skip storage but recompute every read (see [[Warehouse Storage vs Compute Cost]])

## When To Use

- **Any time multiple sources feed dashboards or ML** — even a 2-source startup benefits from bronze/silver/gold
- **When the team grows past 1 analyst** — without staging, every analyst rediscovers cleaning logic
- **When data quality matters** — staging makes testing tractable
- Anti-pattern: skipping silver and going bronze → gold for "simplicity" — every gold query duplicates cleaning, drift inevitable
- Anti-pattern: dozens of gold marts with no shared silver layer — the same entity defined 10 different ways

## Connections

- Related: [[SQL Views in Pipelines]] (how individual pipeline steps are implemented), [[Views vs Tables Tradeoffs]] (materialization choices per layer), [[Hybrid Table View Pipeline Pattern]] (mixing both), [[Testing Data Pipelines]] (validating contracts)
- Builds on: [[Relational Data Model]] (dimensional modeling), [[Joins Fundamentals]], [[Group By]], [[OLTP vs OLAP]] (pipelines move OLTP → OLAP)
- Compare with: ETL (Extract-Transform-Load: transform before warehouse) vs ELT (Extract-Load-Transform: warehouse does the work) — modern stack is ELT
- Used by: every data team beyond a one-person shop; the foundation of analytics engineering

## My Notes

- Bronze/silver/gold terminology comes from Databricks but the concept is older — Kimball used "staging / integration / presentation," same idea.
- Practice: [Greenweez Finans - Veri Kökeni & Orkestrasyon](https://nextgen.workintech.com.tr/project/203/1?pid=7608) — map a real source-to-dashboard data flow into bronze/silver/gold layers.
- Anti-pattern I have personally hit: bronze tables with no documentation. Six months later, no one remembers what `raw_v2_old_v3_final` was meant to capture. Always document at ingestion.
- Interview tip: when discussing pipeline design, name the layers and the four transformation stages — signals serious data engineering experience.
