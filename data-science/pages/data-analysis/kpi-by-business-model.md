---
title: "KPI by Business Model"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/01-farkli-sirketler-farkli-kpilar]]"
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/02-is-modeli-ve-kpi]]"
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/03-ticari-model-ve-olgunluk-seviyesi]]"
tags:
  - data-analysis
  - kpi
  - business-model
  - b2c
  - b2b
  - saas
---

# KPI by Business Model

> One-line summary: A KPI that's vital for one company can be meaningless for another — what to measure depends on whether the business is B2C or B2B, transactional or subscription, and on its stage of maturity. Research suggests ~70% of corporate KPIs do not reflect actual strategy because this matching step is skipped.

## Core Concept

The same number can be brilliant or worthless depending on the business model behind it. **Foot traffic** is critical for a physical retailer but irrelevant for a SaaS company. **Monthly Recurring Revenue (MRR)** is the lifeblood of a subscription business but meaningless for a one-time product seller. The error is treating KPIs as universal when they are deeply contextual.

The selection task has three layers, in order:

1. **Business model** — B2C vs B2B, transactional vs subscription
2. **Commercial model** — one-time purchase, subscription, marketplace, freemium
3. **Maturity stage** — growth (acquisition focus), scale (efficiency focus), mature (retention focus)

Get these three right and the KPI list almost writes itself. Get them wrong and your dashboard tracks vanity ([[Vanity Metrics Anti Patterns]]).

## How It Works

### Layer 1 — B2C vs B2B

| Aspect | B2C | B2B |
|--------|-----|-----|
| **Decision cycle** | Seconds to days | Weeks to months |
| **Deal size** | Small (avg $10–500) | Large (avg $5K–$500K) |
| **Volume** | High frequency | Low frequency |
| **Key KPIs** | Conversion rate, CAC, AOV, repeat purchase | Pipeline value, win rate, sales cycle length |
| **Funnel stages** | Awareness → click → purchase | Lead → MQL → SQL → opportunity → close |

A B2C coffee shop optimizes for "many customers, fast transactions." A B2B SaaS company optimizes for "fewer accounts, deeper engagement, longer retention." Same word ("customer") means very different operational realities.

### Layer 2 — Commercial model

| Model | Key KPIs |
|-------|----------|
| **One-time purchase** (e-commerce) | Conversion rate, AOV, repeat purchase rate |
| **Subscription** (SaaS, streaming) | MRR/ARR, churn rate, LTV, expansion revenue |
| **Marketplace** (Airbnb, Uber) | GMV, take rate, supply/demand balance |
| **Freemium** (Spotify, Dropbox) | Free-to-paid conversion, paid retention |
| **Advertising** (media, social) | DAU/MAU, time spent, CPM, fill rate |

Even within "SaaS" the KPIs shift: a usage-based pricing model emphasizes **expansion revenue** more than seat-based models. The commercial model determines which dial moves the bottom line.

### Layer 3 — Maturity stage

| Stage | What matters | Headline KPI |
|-------|--------------|--------------|
| **Pre-PMF** | Are users finding value? | Activation rate, engagement |
| **Growth** | Are we acquiring efficiently? | CAC payback, conversion rate |
| **Scale** | Are we expanding profitably? | LTV / CAC ratio, gross margin |
| **Mature** | Are we keeping customers? | Net retention, churn rate |
| **Decline** | Can we extend? | Win-back rate, cost reduction |

The mistake: tracking acquisition KPIs in a mature business or retention KPIs in a pre-PMF startup. The framework shifts as the company evolves.

### A worked example — two dashboards for one analyst

A data analyst at a holding company that owns:
1. **A chain of coffee shops** (B2C, transactional, mature)
2. **A SaaS workforce-management product** (B2B, subscription, growth stage)

Building one dashboard for "the company" is the trap. The right move is **two separate dashboards**:

**Coffee shop dashboard:**
- Daily customer count
- Average transaction value
- Repeat customer rate (loyalty card)
- Hour-of-day demand pattern
- Inventory waste rate

**SaaS dashboard:**
- New ARR added this month
- Customer churn rate (logo + revenue)
- Expansion revenue (upsells, seat additions)
- Free-trial-to-paid conversion
- Net Promoter Score

Even the *vocabulary* of "customer" means different things in each. No single dashboard can serve both.

### The "70% of KPIs are wrong" statistic

Research suggests roughly 70% of corporate KPIs do not actually reflect strategy. The common failure modes:

- **Copy-paste from another industry** (a B2B firm tracking foot traffic)
- **Frozen since startup days** (still tracking signups when growth has matured)
- **Easy-to-measure-but-irrelevant** (visitors instead of buyers)
- **Stakeholder-flattering** (CMO favorites that do not link to revenue)

The fix is methodical: revisit each KPI annually, ask "does this map to a strategic objective, given our current model and stage?", and prune ruthlessly.

### Connecting back to first principles

The discipline matches [[KPI Fundamentals]] but adds context-awareness. The selection question is not "what could we measure?" but "what should we measure, given who we are right now?"

The result: bespoke KPI sets per business unit. The data analyst's job is to build them.

## Key Parameters

- **Annual KPI review**: revisit the KPI list every 12 months at minimum; companies evolve
- **One dashboard per business unit**: do not multiplex across models
- **Vocabulary alignment**: define "customer," "active user," "engagement" precisely per unit
- **Stage transition flags**: when growth slows, the KPI list should shift from acquisition to retention focus
- **Document the rationale**: write down why each KPI was chosen — context for the next analyst

## When To Use

- **New analytics role at a company**: map the business model + maturity before defining KPIs
- **Major business shift**: pivot, new product line, IPO prep — KPIs should refresh
- **Cross-team alignment**: when sales and product disagree on what matters, the business model lens reconciles
- **Mergers and acquisitions**: each acquired unit needs its own KPI set
- Anti-pattern: applying the same dashboard template across diverse business units
- Anti-pattern: treating KPIs as permanent — they should evolve with the business

## Connections

- Related: [[KPI Fundamentals]] (the basic concept), [[KPI by Team and Function]] (the team layer of selection), [[Vanity Metrics Anti Patterns]] (what to avoid), [[Customer Acquisition and Expansion Funnels]] (the customer-side KPIs)
- Builds on: [[Seven Step Framework in Practice]] (the analytical workflow that builds these KPIs)
- Compare with: OKRs (goal-setting framework that often defines the headline KPIs)
- Used by: every analytics leader; every quarterly business review

## My Notes

- The "70% of KPIs are wrong" statistic is sobering. Use it to justify pruning bloated dashboards.
- Practice: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283) — sketch a KPI set for a fictional company, then critique it against the three layers.
- A useful exercise: pick a public company (Netflix, Shopify, Etsy) and write down what its 3 headline KPIs probably are based on its business model. Compare against their public investor presentations.
- Interview tip: when asked "what KPIs would you build for X?", lead with the business model + maturity context before listing numbers. Shows strategic thinking, not just metric-naming.
