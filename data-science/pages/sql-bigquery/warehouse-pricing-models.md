---
title: "Warehouse Pricing Models"
domain: data-science
category: sql-bigquery
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/09-fiyatlandirma-modelleri]]"
tags:
  - sql
  - pricing
  - cost-model
  - on-demand
  - flat-rate
---

# Warehouse Pricing Models

> One-line summary: Modern warehouses bill compute in two main ways — on-demand (pay per query / byte scanned, no commitment) and flat-rate (reserve fixed capacity for a predictable monthly fee) — and choosing between them depends on workload size, predictability, and team tolerance for cost spikes.

## Core Concept

Once a workload outgrows trial usage, the warehouse bill becomes a real line item. Every major warehouse offers two pricing styles for compute:

- **On-demand (pay-as-you-go):** each query is metered; the bill scales with usage; no minimum
- **Flat-rate (reservations / commitments):** buy a slot capacity for a fixed monthly fee; usage within the capacity is free

The right choice depends on whether your usage is **predictable** (favor flat-rate) or **bursty** (favor on-demand).

## How It Works

### On-demand pricing (BigQuery default)

```
Charge = sum over queries of (TB scanned × $6.25)
```

- Each query costs based on bytes scanned
- No idle cost — if you do not query, you pay nothing for compute
- No setup, no commitment
- Cost spikes when someone writes an expensive query (a `SELECT *` on a TB-scale table)

Best for:
- Small to mid teams (< $5K/month compute spend)
- Unpredictable query volume (project work, exploration-heavy teams)
- New deployments where workload is unknown

### Flat-rate (slot reservations)

```
Charge = slots reserved × $monthly rate
```

A "slot" is a unit of parallel processing capacity. You buy a chunk (e.g., 100 slots for $2,000/month) and queries run within that capacity. If you saturate it, queries queue. If you under-use it, slots sit idle.

- Predictable bill regardless of query count
- Caps the maximum spend
- Encourages efficient queries (a wasteful query slows other queries instead of inflating the bill)
- Wastes money if average utilization is low (e.g., heavy night, idle day)

Best for:
- Mid-to-large teams with consistent daily/hourly load
- Cost-predictability needs (procurement / finance wants a fixed line item)
- Workloads dominated by scheduled refreshes (predictable, plannable)

### Decision rubric

```
1. What is your current on-demand monthly spend?
   < $1K   → stay on-demand
   $1-5K   → on-demand or small reservation
   > $5K   → likely a reservation saves money
   > $20K  → almost certainly reservation, with auto-scaling

2. How spiky is the workload?
   Heavy spikes, idle valleys → on-demand (avoid paying for idle slots)
   Steady throughout day      → flat-rate (high utilization → cheap per query)

3. Cost predictability requirement?
   Need fixed monthly cost     → flat-rate
   Variable spend acceptable   → on-demand
```

### Hybrid: reservations + on-demand overflow

Most large teams use both:
- **Baseline workload** (scheduled refreshes, BI dashboards): flat-rate reservation
- **Overflow** (analyst ad-hoc queries during peak): on-demand spillover

BigQuery's "auto-scaling reservations" provide this directly. Snowflake's multi-cluster warehouses are conceptually similar.

### A worked example

**Scenario:** A 20-person data team. Monthly load:
- 60 GB scanned per day during business hours
- 200 GB scanned per night by scheduled jobs
- ~30 days/month operating

**On-demand cost:**
- Daily total: 260 GB × $6.25/TB = $1.63/day
- Monthly: $1.63 × 30 = **~$49/month**

For this team, on-demand is dirt cheap. Reservations would waste money.

**Same team, scaled 100×** (a real mid-size company):
- 26 TB scanned per day × 30 days = 780 TB/month
- On-demand: 780 × $6.25 = **$4,875/month**

At this scale, an annual reservation around 1,000 slots ($20K/month if you commit annual) might match the workload. The break-even depends on slot utilization patterns.

### Snowflake's model is virtual warehouses

Snowflake bills compute via **virtual warehouses** — sized clusters that you start, run queries on, and stop. Each warehouse has a per-second rate (XS = $1/hour up to 6XL = $256/hour). You pay only when the warehouse is running.

Same concept, different mechanics: Snowflake's "start the warehouse, pay per second" is conceptually halfway between on-demand and flat-rate.

### Redshift's coupled storage + compute (legacy)

Older Redshift requires sizing a cluster that includes both storage and compute. You pay for the cluster whether it is busy or idle. Newer "Redshift Serverless" mirrors BigQuery's on-demand model.

### Costs that surprise teams

- **Streaming inserts** (BigQuery): priced separately from on-demand or reservations; per row, not per byte
- **Materialized view refreshes**: BigQuery charges for the refresh compute
- **Cross-region data transfer**: substantial; co-locate workloads
- **Failed queries**: BigQuery does NOT charge for failed queries (rare upside of stupid mistakes)

## Key Parameters

- **Slot capacity** (flat-rate): determines max concurrency; under-sized → queueing, over-sized → waste
- **Commitment term**: annual vs monthly reservation pricing differ — annual is 20–40% cheaper
- **Auto-scaling**: BigQuery and Snowflake offer it; eliminates the "reserve enough for peak" problem
- **Cost attribution**: tag queries by team / project to enable charge-back accounting

## When To Use

- **On-demand**: any new or small workload; exploratory teams; unpredictable usage
- **Flat-rate / reservations**: predictable enterprise workloads with steady utilization
- **Hybrid**: medium-to-large teams with both baseline and overflow needs
- **Snowflake virtual warehouses**: per-job sizing; pause when idle
- Anti-pattern: reserving capacity for peak without auto-scaling — you pay for idle slots
- Anti-pattern: staying on on-demand at $20K/month — almost always a reservation is cheaper

## Connections

- Related: [[Warehouse Storage vs Compute Cost]] (storage is separate from compute pricing), [[Bigquery Query Cost Model]] (the per-query specifics), [[Modern Warehouse Comparison]] (each vendor's pricing model), [[Hybrid Table View Pipeline Pattern]] (materialization shifts cost between the two meters)
- Builds on: workload modeling, basic accounting
- Compare with: cloud compute pricing (EC2 on-demand vs reserved vs spot) — same conceptual model
- Used by: every finance team negotiating warehouse contracts; every data leader planning annual budgets

## My Notes

- The "should we move to flat-rate?" question usually surfaces at $5K–10K/month on-demand spend. Run the math; cloud rep can help but always model it independently.
- Practice: estimate annual on-demand cost for your team's current daily scan volume — does it justify exploring reservations?
- Pricing changes — these rates were current as of 2026 BigQuery on-demand pricing; check the vendor's current page before quoting numbers.
- Interview tip: when asked about warehouse cost optimization, distinguish "reduce bytes scanned" (compute) from "reduce data stored" (storage) from "switch pricing model" (commercial) — three different levers.
