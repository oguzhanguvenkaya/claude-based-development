---
title: "KPI by Team and Function"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/04-farkli-takimlar-farkli-kpilar]]"
tags:
  - data-analysis
  - kpi
  - team-design
  - cross-functional
  - dashboard
---

# KPI by Team and Function

> One-line summary: Beyond the business-model layer, each team within a company has its own mission and own KPIs — marketing optimizes for acquisition, sales for conversion, customer success for retention — and the analyst's job is to build a per-team KPI set that aligns each team's metric to its mission.

## Core Concept

A coffee shop and a SaaS company need different KPIs ([[KPI by Business Model]]). But even *within one company*, every team has its own mission and therefore its own KPIs. Lumping all teams into one dashboard creates a wall of numbers nobody can act on.

The analyst's job is to **define per-team KPI sets** that connect each team's work directly to its mission. This requires understanding team responsibilities and the data sources each team relies on, then designing a small headline KPI plus supporting metrics that the team can actually move.

## How It Works

### Step 1 — Understand each team's mission

Before designing KPIs, learn what each team is paid to do:

| Team | Mission | Primary lever they pull |
|------|---------|-------------------------|
| **Marketing** | Bring qualified prospects | Channel spend allocation, messaging |
| **Sales** | Convert prospects to revenue | Sales process, pricing, qualification |
| **Customer Success** | Keep and grow customers | Onboarding, support, account management |
| **Product** | Build features users love | Roadmap prioritization, UX |
| **Engineering** | Ship and maintain reliably | Code quality, deployment cadence |
| **Operations** | Deliver products / services | Fulfillment, logistics, supplier mgmt |
| **Finance** | Maintain profitability | Cost control, capital allocation |
| **HR / People** | Hire and retain talent | Recruiting funnel, culture, comp |

Each team's KPI must connect to *their* lever. Tracking marketing's spend efficiency does not help engineering ship faster.

### Step 2 — Identify the data sources each team owns

Per team, ask: where does the data come from?

| Team | Typical data sources |
|------|----------------------|
| Marketing | Google Ads, Meta Ads, GA4, email platform |
| Sales | CRM (Salesforce, HubSpot), call recordings |
| Customer Success | Support ticketing (Zendesk), NPS surveys, product usage |
| Product | Product analytics (Amplitude, Mixpanel), feature flags |
| Engineering | Monitoring (Datadog), CI/CD, GitHub |
| Operations | ERP, warehouse management, shipping |
| Finance | Accounting software, payment processors |

Without integrating these sources, you cannot build cross-team views. The data pipeline ([[Data Pipeline Architecture]]) becomes the foundation for cross-team KPI work.

### Step 3 — Define the headline KPI per team

One KPI per team, aligned to the mission:

| Team | Headline KPI | Why this one |
|------|--------------|--------------|
| Marketing | **Customer Acquisition Cost (CAC)** | How efficiently they buy customers |
| Sales | **Win rate** | How well they close qualified deals |
| Customer Success | **Net Revenue Retention** | Keeping + growing accounts |
| Product | **Activation rate** | Are users getting value? |
| Engineering | **Uptime** or **Deployment frequency** | System reliability + velocity |
| Operations | **Fulfillment time** | Service delivery speed |
| Finance | **Gross margin** | Profitability ([[Finance KPIs]]) |
| HR | **Time to hire** + **Retention rate** | Talent pipeline health |

Each is *one number* the team is accountable for moving. Supporting metrics decompose the KPI ([[KPI Fundamentals]]).

### Step 4 — The unified North Star dashboard

Many companies aspire to a single "North Star" dashboard where leadership can see every team's KPI in one view. The standard pattern:

```
EXECUTIVE NORTH STAR
├── Revenue (overall)
├── Marketing → CAC trend
├── Sales → Win rate trend
├── Customer Success → Net retention trend
├── Product → Activation rate trend
├── Engineering → Uptime + deployment freq
├── Operations → Fulfillment time
├── Finance → Gross margin trend
└── HR → Time to hire + retention
```

One row per team, one chart per row. Clicking a row drills into the team's own deeper dashboard with supporting metrics.

This is the **"NorthStar Koda Yönetim"** pattern from the course transcript — a leadership view that respects team autonomy while enabling cross-team visibility.

### Misalignment as a diagnostic

When team KPIs are misaligned, predictable failure modes appear:

| Symptom | Likely misalignment |
|---------|---------------------|
| Marketing wins, sales loses | Marketing optimizes lead volume, not lead quality |
| Sales hits quota, churn spikes | Sales pushes bad-fit deals to close |
| Engineering ships fast, prod incidents rise | Speed KPI without reliability KPI |
| Customer Success high satisfaction, expansion flat | Optimizing for survey scores, not revenue growth |

The analyst's job: spot these patterns and propose KPI changes that align team incentives toward business outcomes.

### Cross-team KPIs — the integrative layer

Some KPIs span teams and force coordination:

- **LTV / CAC ratio**: marketing buys customers; customer success retains them; finance sets discount rates
- **Time to value**: sales sets expectations; product ships features; customer success onboards
- **Churn root cause**: customer success notices; product fixes; engineering deploys

Cross-team KPIs are typically reviewed in cross-functional meetings (weekly business review, quarterly OKR sync).

## Key Parameters

- **One headline KPI per team**: 2 max; more dilutes focus
- **Supporting metric count**: 5–15 per team; enough to diagnose movement
- **Refresh cadence per team**: marketing daily, product weekly, finance monthly — varies with operational tempo
- **Ownership**: name the person (not just the team) accountable for each KPI
- **Definition consistency**: "customer" should mean the same thing across all team dashboards — write the canonical definition once

## When To Use

- **New team formation**: define the KPI before the team builds processes
- **Annual planning**: revisit each team's KPI list as part of yearly strategy
- **Cross-functional friction**: KPI misalignment often explains why two teams disagree
- **Organizational design**: combining or splitting teams requires re-thinking KPIs
- Anti-pattern: one giant dashboard with everyone's metrics — leadership cannot focus, teams ignore it
- Anti-pattern: KPIs designed by HR for compensation that distort actual behavior (Goodhart's Law)

## Connections

- Related: [[KPI Fundamentals]] (definition + KPI vs metric), [[KPI by Business Model]] (the company-level layer), [[Vanity Metrics Anti Patterns]] (what to avoid), [[Finance KPIs]], [[Inventory KPIs]], [[Quality KPIs]] (department-specific examples), [[Data Team Roles and Responsibilities]] (who builds the team-level dashboards)
- Builds on: [[Data Platform Overview]] (the data pipeline that integrates each team's sources)
- Compare with: OKRs (the goal-setting framework where team-level Key Results often become KPIs)
- Used by: every executive team building their company-wide reporting layer

## My Notes

- The hardest part of cross-team KPI design is **definition consistency**. Sales and marketing will define "lead" differently if you let them. Force a single definition.
- Practice: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283) — design a 5-team dashboard for a fictional retailer; justify each KPI choice.
- A useful artifact: a one-page "KPI registry" listing every KPI, its owner, its definition, and the source query. New analysts onboard in days instead of weeks.
- Interview tip: when discussing past analytics work, frame impact in terms of moving a team-specific KPI ("reduced CAC by 18%", "lifted activation by 12%"). Specificity signals real ownership.
