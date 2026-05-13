---
title: "Data Lifecycle"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/04-data-analiz-ekosistemi/transcripts/06-veri-yasam-dongusu]]"
tags:
  - data-analysis
  - lifecycle
  - data-infrastructure
  - etl
  - elt
---

# Data Lifecycle

> One-line summary: Data has a lifecycle — collect, store, clean, transform, analyze, feed insights back to business tools — that turns scattered raw inputs into operational decisions; modern data infrastructure automates each stage so analysts focus on the analysis, not the plumbing.

## Core Concept

Raw data is messy and useless on its own. Modern data infrastructure exists to manage the full **lifecycle** that turns it into business value. Each stage in the lifecycle has its own tools, owners, and quality concerns. The lifecycle view is essential because:

- Skipping a stage produces broken downstream analytics
- Investing in earlier stages compounds (clean data feeds clean analysis, broken data feeds broken analysis)
- Understanding where data lives in the lifecycle clarifies which team is responsible

The lifecycle is the operational counterpart to the seven-step [[Seven Step Framework in Practice]] analyst workflow — the framework describes the analyst's process; the lifecycle describes the data's journey.

## How It Works

### The six stages

```
1. COLLECTION   →  gather data from sources
        │
        ▼
2. STORAGE      →  persist it durably
        │
        ▼
3. CLEANING     →  fix quality issues
        │
        ▼
4. TRANSFORMATION → shape for analysis
        │
        ▼
5. ANALYSIS     →  produce insights and KPIs
        │
        ▼
6. FEEDBACK     →  pipe insights back into business tools
```

Each stage feeds the next. A failure at any stage propagates: bad collection → bad storage → bad analysis → bad decisions.

### Stage 1 — Collection

**Bring data together from disparate sources.**

Sources typically include:
- SaaS apps (Salesforce, HubSpot, Stripe, Mailchimp)
- Product databases (operational PostgreSQL, MySQL)
- Event streams (web/mobile clickstreams, IoT)
- Third-party APIs (Google Analytics, Meta Ads, weather, exchange rates)
- Spreadsheets (legacy data, vendor exports)

**Tools**: Fivetran, Airbyte, Stitch (batch); Kafka, Kinesis, Pub/Sub (streaming).

Quality concerns at this stage: missing fields, schema drift (vendor changes their API), authentication failures, rate limits.

### Stage 2 — Storage

**Persist data in a queryable system.**

Two main paradigms:
- **Data warehouse**: structured, columnar storage optimized for SQL analytics (BigQuery, Snowflake, Redshift)
- **Data lake / lakehouse**: cheaper storage for raw + semi-structured data (S3, Databricks, Iceberg)

Most modern stacks use both: lake for raw bronze data, warehouse for transformed silver/gold layers (see [[Data Pipeline Architecture]]).

Storage cost characteristics: see [[Warehouse Storage vs Compute Cost]] for the cost model.

### Stage 3 — Cleaning

**Fix quality issues before downstream analysis touches the data.**

Cleaning operations:
- Fix data types (text-stored numbers, malformed dates)
- Deduplicate
- Handle missing values
- Normalize text (case, whitespace, encoding)
- Flag outliers
- Validate referential integrity

See [[String Cleaning Replace and Case]], [[Null Handling SQL]], [[Data Exploration and Cleaning Sheets]] for the techniques.

Without cleaning, every downstream query reproduces the same fixes. With cleaning at the silver layer, all consumers benefit from one source of truth.

### Stage 4 — Transformation

**Shape clean data into analytical models.**

Activities:
- Joining tables to build wider analytical views
- Aggregating to the right grain (per-customer, per-day, per-region)
- Computing derived columns (margin, age bucket, RFM score)
- Building cohort, funnel, and trend tables

**Tools**: dbt, Spark, scheduled SQL. dbt has become the industry standard for SQL-based transformation, encoding the transformation logic as version-controlled models.

The output of transformation is the **gold layer**: tables ready to be queried directly by dashboards and ML pipelines.

### Stage 5 — Analysis

**Extract insights and produce KPIs.**

This is the data analyst's primary day-to-day: building dashboards, running ad-hoc analyses, computing the headline KPIs, identifying trends and anomalies. Tools include BI platforms (Looker, Tableau, Metabase, Looker Studio) and the SQL / Python environment for deep dives.

Outputs: dashboards, slide decks, Slack-bot alerts, KPI tracking, segment definitions, A/B test reports.

### Stage 6 — Feedback (the often-missing stage)

**Pipe analytical insights back into operational tools.**

Sometimes called "reverse ETL" or "operational analytics." Examples:
- Update Salesforce account scores based on product usage data
- Trigger marketing automation when a customer hits an RFM segment
- Push churn-risk flags to customer success tooling
- Sync inventory forecasts to the warehouse management system

**Tools**: Hightouch, Census, custom scripts.

Without the feedback stage, analytics produces insights but operational systems do not act on them. The feedback stage closes the loop.

### The lifecycle in numbers

For a mid-sized data team, typical effort split:

| Stage | % of team time | Why |
|-------|---------------:|-----|
| Collection | 5% | Mostly automated by ingestion tools |
| Storage | 5% | Mostly automated by warehouse |
| Cleaning | 25% | Hardest to automate; data quality is messy |
| Transformation | 30% | The core of analytics engineering work |
| Analysis | 25% | The visible "analyst" work |
| Feedback | 10% | Often under-invested |

Junior analysts often see only stage 5 (analysis). Senior analysts and analytics engineers see the whole pipeline.

### Failure modes per stage

| Stage | Common failure | Symptom |
|-------|---------------|---------|
| Collection | Vendor schema change | Daily ingest breaks, no data lands |
| Storage | No partition strategy | Query costs balloon ([[Partitioning and Clustering]]) |
| Cleaning | Skipped at silver layer | Same bugs reappear in every downstream query |
| Transformation | No tests | Silent corruption, wrong numbers in dashboards ([[Testing Data Pipelines]]) |
| Analysis | Vanity metrics | Pretty dashboards, no decisions ([[Vanity Metrics Anti Patterns]]) |
| Feedback | Missing | Insights produced but never acted on operationally |

Diagnosing slow / wrong analytics often means tracing through the lifecycle and finding which stage broke.

## Key Parameters

- **Ownership per stage**: collection often DevOps / data engineering; storage = engineering; cleaning + transformation = analytics engineers; analysis = analysts; feedback = often unstaffed
- **Tool standardization**: one ingestion tool, one warehouse, one transformation framework — vendor sprawl creates lifecycle gaps
- **SLA per stage**: define expected delivery time (ingestion within 24h, transformation runs nightly, dashboards refresh hourly)
- **Cost attribution**: trace cost back through stages — ingestion, storage, query — to attribute spend per business unit

## When To Use

- **Onboarding to a new data team**: map the existing lifecycle and find the gaps
- **Bill investigations**: trace cost through the lifecycle stages
- **Strategic planning**: invest in the weakest stage first
- **Architectural decisions**: vendor choices, build vs buy
- Anti-pattern: investing heavily in stage 5 (analysis) without solid 3 and 4 — analyses constantly hit data quality issues
- Anti-pattern: no stage 6 — insights generated but not connected to operations

## Connections

- Related: [[Data Platform Overview]] (the technical realization of the lifecycle), [[Data Pipeline Architecture]] (medallion structure within stages 2-4), [[Data Professional Role and Collaboration]] (who owns which stage), [[Testing Data Pipelines]] (validates stages 3-4), [[Seven Step Framework in Practice]] (the analyst's workflow inside stage 5)
- Builds on: [[OLTP vs OLAP]], [[Bigquery Insert with Cast Workflow]]
- Compare with: software dev lifecycle (similar staged thinking), MLOps lifecycle (extends through model training and deployment)
- Used by: every data team's architectural planning; every analytics engineer's mental model

## My Notes

- The lifecycle view is what distinguishes "analyst who runs queries" from "analytics engineer who owns the pipeline." Career trajectory often follows expanding lifecycle ownership.
- Practice: [Amazon Books NPS Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7292) — for a fictional company, sketch the lifecycle: where each data type lives at each stage.
- The feedback stage (reverse ETL) is genuinely undervalued. Many teams have 90% of analytics value locked in dashboards that no one reads. Pipe it back.
- Interview tip: when discussing architecture, narrate the lifecycle stages in order — signals systemic thinking vs piecemeal analyst skills.
