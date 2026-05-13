---
title: "KPI Fundamentals"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/09-kpi-nedir]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/10-kpi-metrik-farki]]"
tags:
  - data-analysis
  - kpi
  - metrics
  - business-analytics
---

# KPI Fundamentals

> One-line summary: A KPI (Key Performance Indicator) is a single measurable value tied directly to a business goal — the headline number that says whether you are winning — while supporting metrics describe the underlying activity but do not, by themselves, indicate success or failure.

## Core Concept

Every team in a business has goals. Marketing wants conversions. Finance wants profit. Operations wants uptime. **KPIs translate goals into measurable numbers**: one or two headline indicators per goal that say, at a glance, whether the team is succeeding.

Every other number on the dashboard is a **metric** — supporting context that helps explain the KPI's movement but is not itself the success criterion. The discipline of separating KPIs from metrics is the difference between a dashboard that drives action and one that drives confusion.

## How It Works

### KPI vs metric — the key distinction

| Aspect | KPI | Metric |
|--------|-----|--------|
| **Tied to a goal** | Yes (one specific business outcome) | Not directly |
| **Action-triggering** | If it moves, you act | Provides context |
| **Count per team** | 1–3 max | Many (5–20) |
| **Stakeholder focus** | What executives ask about | What analysts dig into |
| **Example (marketing)** | Conversion rate | Click-through rate, impressions, bounce rate |
| **Example (inventory)** | Stockout rate | Average stock, total stock |

A useful test: **"if this number moves, do we change behavior?"** If yes, it's a KPI candidate. If no (it's just descriptive), it's a metric.

### The case for fewer KPIs

A dashboard with 30 numbers gets ignored. The same dashboard with 3 KPIs and 27 supporting metrics gets used. Stakeholders need to know what to look at first.

> Emma at GreenFit once built a dashboard with 30 numbers. Stakeholders saw the chaos and ignored it. She rebuilt it with one KPI (stockout rate) and supporting metrics, and the operations team started checking it daily.

This is the **vital few** principle (Pareto applied to dashboards): 1–3 KPIs drive 80% of the decision value.

### Anatomy of a good KPI

A well-designed KPI has:

- **Clear definition**: "stockout rate = number of SKUs out of stock / total SKUs, measured daily at 9 AM"
- **Numeric and measurable**: not "customer satisfaction" but "NPS score" or "% of orders with 5-star rating"
- **Goal-aligned**: there is a target number (>X or <Y)
- **Owned**: one team is responsible for moving it
- **Cadence**: tracked at a fixed interval (daily, weekly, monthly)

Without these, "KPI" devolves into "any number we report."

### Vanity metrics — the anti-KPI

Some popular numbers fail the KPI test:

- **Total signups** (vanity): goes up over time naturally; says nothing about whether growth is working
- **Total page views** (vanity): same — directional but not goal-aligned
- **Twitter followers** (vanity): grows unless you do nothing; not action-triggering

KPI equivalents:
- Total signups → **conversion rate** (% of visitors who sign up)
- Total page views → **engagement** (% of visitors who view 3+ pages)
- Twitter followers → **engagement rate** (% of followers who interact per post)

Vanity metrics flatter the team; real KPIs reveal whether the team is succeeding.

### KPI design by team

| Team | Typical KPI | What it measures |
|------|-------------|------------------|
| Marketing | Conversion rate, CAC, CTR | Acquiring users efficiently |
| Sales | Win rate, ACV, quota attainment | Closing revenue |
| Customer Success | NPS, churn rate, expansion revenue | Keeping and growing accounts |
| Finance | Gross margin, operating margin | Profitability |
| Operations | Stockout rate, fulfillment time | Reliable delivery |
| Engineering | Uptime, deployment frequency, MTTR | System reliability |
| Product | Activation rate, retention curve | User value |

See [[Finance KPIs]], [[Inventory KPIs]], [[Quality KPIs]] for the GreenFit examples.

### Lead vs lag indicators

**Lag indicator**: measures the outcome after it happens (revenue, churn rate). You can see if you won but cannot change it.

**Lead indicator**: measures the activity that drives the outcome (sales calls, signups, customer support response time). You can act on it before the lag indicator moves.

Good KPI systems include both: lag KPIs for accountability ("did we win?") and lead KPIs for steering ("are we on track to win?").

### Why a KPI is not just a metric you stared at

The transition from "metric we report" to "KPI we manage" is cultural:

- A meeting agenda item dedicated to the KPI
- A target set ahead of the period
- A reflection on movement after the period
- An owner accountable for it
- Action plans when it moves outside acceptable range

Without those, a "KPI" is just another number on a slide.

## Key Parameters

- **Count**: 1–3 KPIs per team; more dilutes attention
- **Cadence**: daily / weekly / monthly depending on volatility
- **Target**: every KPI needs a target (>X or <Y) — without one, you cannot know if you are succeeding
- **Definition**: written down, single-source-of-truth — fragmenting "what does conversion rate mean?" across teams is a common failure
- **Ownership**: one named person or team accountable

## When To Use

- **Every team should have 1–3 KPIs** — the foundation of accountability
- **Quarterly business reviews** — KPI trends are the agenda
- **OKR / Goal-setting** — KPIs are how you measure goal attainment
- **Dashboard design** — KPIs at the top, metrics below
- Anti-pattern: "let me show you 30 metrics" — leadership disengages
- Anti-pattern: KPIs without targets — directionless, cannot diagnose under/overperformance
- Anti-pattern: vanity metrics promoted as KPIs — flatters team, hides problems

## Connections

- Related: [[Seven Step Framework in Practice]] (step 6 — KPIs are the typical output of analysis), [[Finance KPIs]], [[Inventory KPIs]], [[Quality KPIs]], [[Data Visualization Sheets]] (KPI dashboards), [[KPI by Business Model]], [[KPI by Team and Function]], [[Vanity Metrics Anti Patterns]]
- Builds on: [[Data Analysis Workflow]] — KPIs require the full workflow to compute and validate
- Compare with: OKRs (Objectives and Key Results — a goal-setting framework where KPIs become the "Key Results")
- Used by: every business team; the universal output of analytics work

## My Notes

- The "fewer KPIs" rule is hard to enforce in practice — every stakeholder wants their favorite number elevated. Push back; quality of attention beats quantity of metrics.
- Practice: [Amazon Books Kalite Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7281) — pick 1 KPI for the quality team, justify why, list 3-5 supporting metrics.
- A clean definition: "If this number moves, we do something differently." If no, it's a metric. If yes, KPI candidate.
- Interview tip: when asked about analytics impact, frame in terms of moving a named KPI ("conversion rate from 2.1% to 2.7%"). Specificity signals real ownership.
