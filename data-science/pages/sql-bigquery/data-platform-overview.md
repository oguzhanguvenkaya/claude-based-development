---
title: "Data Platform Overview"
domain: data-science
category: sql-bigquery
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/07-veri-platformu-genel-bakisi]]"
tags:
  - sql
  - data-platform
  - architecture
  - ingestion
  - bi
---

# Data Platform Overview

> One-line summary: A data platform is the central hub where an organization stores, transforms, and serves data to every team — combining ingestion, storage (warehouse / lake), transformation (ELT / dbt), and consumption (BI, ML, ops) into one coherent stack.

## Core Concept

Every department in a company produces or consumes data. Without a central platform, each team picks its own tools, copies data ad-hoc, and arrives at slightly different numbers for the same KPI. A **data platform** consolidates this — one source of truth, one set of pipelines, one place to query.

The platform is not a single product; it is a stack of components that work together. The shape of the stack has converged across most modern companies into a recognizable pattern, often called the "modern data stack."

## How It Works

### The five layers of a data platform

```
1. SOURCES           — SaaS apps (Salesforce, Stripe, HubSpot), product DBs, event streams
        │
        ▼
2. INGESTION         — Fivetran, Airbyte, custom connectors, streaming (Kafka, Pub/Sub)
        │
        ▼
3. STORAGE           — Data warehouse (BigQuery, Snowflake, Redshift) or lakehouse (Databricks)
        │
        ▼
4. TRANSFORMATION    — dbt, scheduled SQL, Spark jobs
        │
        ▼
5. CONSUMPTION       — BI tools (Looker, Tableau, Metabase), ML training, reverse-ETL back to ops
```

Each layer has its own tool category and vendors. The platform is the entire stack working together.

### Component details

**Sources.** Anything that produces data: operational databases, SaaS APIs, mobile apps, IoT sensors. The platform's job is to absorb all of them with minimal source-side impact.

**Ingestion.** Moves data from sources into storage. Two flavors:
- **Batch** (Fivetran / Airbyte): scheduled syncs, simple, the default
- **Streaming** (Kafka, Pub/Sub, Kinesis): for sub-minute freshness; complex, expensive

**Storage.** The warehouse or lakehouse — where queries actually run. See [[Modern Warehouse Comparison]]. BigQuery, Snowflake, Redshift, Databricks are the main contenders.

**Transformation.** Cleaning, joining, aggregating. Modern stacks run transformations **inside** the warehouse using SQL (ELT) rather than before loading (ETL). dbt is the leading orchestrator for SQL transformations; Airflow / Dagster wrap dbt for scheduling and broader workflows.

**Consumption.** The "last mile" — where humans and systems actually see the data:
- **BI dashboards** (Looker, Tableau, Mode, Metabase)
- **ML / data science** (Jupyter, training pipelines)
- **Reverse-ETL** (Hightouch, Census): push transformed data back to operational tools (Salesforce, Marketo)
- **Embedded analytics**: APIs that customer-facing products query

### How the layers communicate

Each layer exposes data to the next via tables or APIs:

- Sources → ingestion via connectors (read-only)
- Ingestion → storage via writes (typically bulk INSERT or COPY)
- Storage → transformation via SELECT (in-warehouse SQL)
- Transformation → consumption via tables/views (the [[Data Pipeline Architecture]] bronze/silver/gold layers)

The contracts between layers are the columns and row schemas. Documenting them is half the work of building a platform.

### A typical day on the platform

```
00:00  Fivetran syncs overnight: Salesforce, Stripe, mobile events → bronze tables
01:00  dbt runs: bronze → silver → gold (90 minutes for a mid-size warehouse)
03:00  Looker dashboards refresh against the new gold tables
08:00  Analysts start the day with fresh numbers
10:00  Marketing team launches campaign; reverse-ETL pushes target list back to Salesforce
14:00  Ad-hoc analysis hits silver tables for live questions
22:00  Lookback / model refresh; ML team trains on the day's data
```

The platform is what makes that timing work without anyone manually coordinating.

### Governance — the missing layer

Beyond the five technical layers, a real platform has:
- **Data catalog**: what tables exist, who owns them, what they mean (DataHub, Alation, Atlan)
- **Access control**: who can read what (warehouse IAM + tools like Immuta)
- **Quality monitoring**: tests on every pipeline run (see [[Testing Data Pipelines]])
- **Lineage**: which downstream depends on which upstream — for impact analysis when sources change
- **Cost tracking**: who is spending what on query compute (see [[Warehouse Storage vs Compute Cost]])

A small startup can get away with ad-hoc governance. A 500-person company cannot.

## Key Parameters

- **Single source of truth**: every metric defined once, computed once, exposed via gold layer
- **Schema contracts**: each layer's outputs are documented and tested
- **Cost ownership**: each team's queries should be attributable to track spend
- **Refresh cadence**: typically end-of-day for analytical use; real-time for operational use
- **Disaster recovery**: warehouses provide backup; reproducibility comes from dbt + git versioning

## When To Use

- **Any company with 3+ teams consuming data** — without a platform, definitions diverge
- **Any analytics function reporting metrics externally** — finance, regulatory, investor reporting
- **When data work blocks shipping** — building the platform unblocks every downstream team
- Anti-pattern: skipping the storage layer (querying directly against production OLTP — see [[OLTP vs OLAP]])
- Anti-pattern: spreadsheet-as-warehouse — does not scale past one team, one product line, one quarter

## Connections

- Related: [[Data Pipeline Architecture]] (the transformation layer inside the platform), [[OLTP vs OLAP]] (the platform sits on the OLAP side), [[Modern Warehouse Comparison]] (choosing the storage layer), [[Warehouse Storage vs Compute Cost]] (the economics)
- Builds on: every prior SQL lesson — the platform is the operating environment for everything you have learned
- Compare with: monolithic data systems (Oracle DW in 2005) vs modern composable stack (vendor-per-layer)
- Used by: every team beyond a one-analyst shop

## My Notes

- The "modern data stack" phrase encompasses the layers above plus the vendor mix; the layers themselves are universal.
- Practice: [BigQuery: Sorgu Maliyet Analizi ve Optimizasyonu](https://nextgen.workintech.com.tr/project/203/1?pid=7688) — draw your company's (or hypothetical) platform diagram with concrete vendors per layer.
- Building a platform is a multi-year endeavor for most organizations. New analysts often underestimate how long the storage + transformation layers take to stabilize.
- Interview tip: when discussing data infrastructure, mention specific tools per layer with reasoning — shows familiarity with the production landscape.
