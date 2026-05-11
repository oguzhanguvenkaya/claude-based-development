---
title: "Views vs Tables Tradeoffs"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/03-cok-tablo-maliyet-etkileri]]"
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/05-gorunumler-ve-tablolar-arti-eksi]]"
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/06-karma-tablo-ve-gorunum-yaklasimi]]"
tags:
  - sql
  - views
  - tables
  - materialization
  - cost-optimization
---

# Views vs Tables Tradeoffs

> One-line summary: Choose views for live freshness and minimal storage, tables for query speed and predictable cost — the tradeoff is between recompute cost on every query (views) versus storage cost plus staleness (tables).

## Core Concept

Every pipeline step has the same materialization choice: should this intermediate result be a **view** (computed live each time) or a **table** (computed once, stored)? The answer is not universal — it depends on query frequency, freshness requirements, storage cost, and compute cost.

Getting it wrong is expensive. Materializing everything inflates the storage bill (and propagates staleness through chained tables); materializing nothing slows queries to a crawl. The skill is recognizing where each makes sense.

## How It Works

### The two extremes

```
View-only pipeline:                    Table-only pipeline:
bronze tables                          bronze tables
   │                                      │
   ▼ (live view)                          ▼ (scheduled INSERT)
silver views                          silver tables (stored)
   │                                      │
   ▼ (live view)                          ▼ (scheduled INSERT)
gold views                            gold tables (stored)
   │                                      │
   ▼ (live query)                         ▼ (live query)
dashboards                            dashboards

Cost: compute every query              Cost: storage + scheduled refreshes
Freshness: always live                 Freshness: lags by refresh interval
```

### Side-by-side comparison

| Aspect | View | Table |
|--------|------|-------|
| **Storage** | None (just SQL definition) | Full result stored |
| **Compute per query** | Re-runs the underlying SQL | Just reads stored bytes |
| **Freshness** | Always reflects current source | Stale until next refresh |
| **First-query latency** | Pays full pipeline cost | Fast |
| **Repeated-query cost** | Pays full pipeline cost again | Free (after the build) |
| **Permission model** | Can hide source data | Same permissions as a regular table |
| **Easy to update logic** | Edit `CREATE VIEW` and refresh; no rebuild | Must drop + recreate, or schedule a refresh |

### The "too many tables" anti-pattern (transcript 03)

A common bug: every CTE in a pipeline is converted into a CREATE TABLE step. Storage triples. Refresh latency stacks. The bill spikes.

```
bronze.raw_orders        → CREATE TABLE silver.cleaned_orders
silver.cleaned_orders    → CREATE TABLE silver.enriched_orders
silver.enriched_orders   → CREATE TABLE gold.daily_revenue
gold.daily_revenue       → query
```

Each layer pays storage costs even though only the final `gold.daily_revenue` is dashboard-bound. The intermediate layers could be views — same logic, no storage.

**Fix**: materialize the layer that **consumers actually query directly**; everything upstream that exists only to feed it can be a view.

### When freshness drives the choice (transcript 05)

> "Marketing wants the new-signups dashboard updated hourly. Finance wants weekly reports."

Two different consumers, two different freshness needs:

- **Marketing dashboard** → built on **views** (always live, hourly variance acceptable since the underlying source updates real-time)
- **Finance weekly report** → built on a **table** refreshed Monday morning (saves recompute cost since the same data is queried many times during the week)

Same source, different materialization for different downstream contracts.

### The hybrid approach (transcript 06)

The mature pattern:
- **Heavy, reusable transformations** → tables (materialized once, queried many times)
- **Light, query-time logic** → views on top of those tables
- **Live ad-hoc analysis** → views chained to the materialized base

```
bronze.raw_*                        (storage: original)
   │
   ▼ (table — refreshed daily, expensive cleaning step)
silver.cleaned_dim_customers        (storage: full)
silver.cleaned_fact_orders          (storage: full)
   │
   ▼ (view — cheap join, always fresh)
gold.orders_with_customer_segment   (storage: none)
   │
   ▼ (materialized view — for dashboard speed)
gold.daily_revenue_mv               (storage: full but small)
```

Each layer's choice is deliberate: the heavy ELT cost is paid once (silver tables); the cheap join is live (gold view); the hot dashboard query is fast (materialized view).

### Decision rubric

Ask, in order:

1. **Does query frequency × pipeline cost > storage cost?** → Table
2. **Do consumers tolerate any staleness?** → If no → view; if yes → table
3. **Does the SQL fit materialized-view restrictions?** → If yes, consider MV (best of both)
4. **Is the result hot enough that latency matters?** → Table
5. **Is the underlying source changing constantly?** → View (avoids stale data)

For most pipelines, **50–80% of intermediate steps should be views** and **gold-layer hot tables should be materialized**.

### Cost intuition (BigQuery example)

For a 1 TB silver table queried 1000× per day at $5/TB scanned:
- **As a view**: 1 TB × 1000 = 1 PB scanned per day = $5,000/day in query cost
- **As a table**: 1 TB stored at ~$20/month = $0.65/day + small query cost on cached scans

For high-traffic tables, materializing pays back in days. For rarely-queried logic, views are clearly cheaper.

## Key Parameters

- **Storage cost** (BigQuery): roughly $0.02/GB/month for active, $0.01/GB/month for long-term
- **Query cost** (BigQuery): $6.25/TB scanned (on-demand pricing)
- **Refresh cost**: every table rebuild pays full compute; materialized views auto-incremental (cheaper)
- **Refresh frequency**: how stale is acceptable for this consumer?

## When To Use

- **View**: low-frequency queries, live freshness, light SQL
- **Table (scheduled refresh)**: dashboard-grade tables, heavy SQL, predictable refresh window
- **Materialized view**: high-frequency aggregates with auto-refresh (when allowed)
- **Hybrid**: combine all three across the pipeline layers
- Anti-pattern: materializing every layer "for performance" — quadruples storage cost, propagates staleness
- Anti-pattern: only views for hot dashboards — every dashboard refresh pays the full pipeline cost
- Anti-pattern: choosing materialization without measuring — instrument queries before deciding

## Connections

- Related: [[Data Pipeline Architecture]] (where in the pipeline the choice applies), [[SQL Views in Pipelines]] (view mechanics), [[Hybrid Table View Pipeline Pattern]] (the canonical mix), [[Warehouse Storage vs Compute Cost]] (the underlying cost model)
- Builds on: [[Create Update Delete]] (CTAS for tables), [[Select Statement]]
- Compare with: dbt model materializations (view / table / incremental / ephemeral / materialized_view) — dbt encodes exactly this decision
- Used by: every production warehouse; the materialization strategy is a top-3 architectural decision

## My Notes

- Rule of thumb: in dbt, default new models to `view`, promote to `table` only when measured cost or latency demands it.
- Practice: [BigQuery: Sorgu Maliyet Analizi ve Optimizasyonu](https://nextgen.workintech.com.tr/project/203/1?pid=7688) — find one view that should be a table and one table that should be a view in a sample project.
- The phrase "everything is a view" is romantic but rarely survives a real workload. Measure.
- Interview gotcha: when asked "view vs table?", do not give a binary answer — give a decision rubric (frequency, freshness, cost, refresh tolerance).
