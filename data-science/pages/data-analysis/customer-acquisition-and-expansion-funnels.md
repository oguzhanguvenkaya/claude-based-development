---
title: "Customer Acquisition and Expansion Funnels"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/07-musteri-kazanim-kanallari]]"
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/08-genisleme-hunisi]]"
tags:
  - data-analysis
  - funnel
  - customer-acquisition
  - retention
  - ltv
  - cac
---

# Customer Acquisition and Expansion Funnels

> One-line summary: Two complementary funnels frame the customer lifecycle — the **acquisition funnel** measures how prospects become paying customers (channels, conversion rates, CAC) and the **expansion funnel** measures what happens after (retention, satisfaction, LTV) — together they answer "are we growing and keeping the right customers?"

## Core Concept

The customer journey has two halves, and analytics treats them as separate funnels:

1. **Acquisition funnel**: from "never heard of us" → "paid for the first time"
2. **Expansion funnel**: from "first payment" → "long-term valuable customer"

A healthy business has both funnels flowing — strong acquisition without retention is a leaky bucket; strong retention without acquisition is stagnation. The data analyst's job is to measure each, identify where customers drop, and feed the marketing / customer success teams actionable insights.

## How It Works

### Acquisition funnel — the channel view

The acquisition funnel asks: **where do customers come from, and how efficiently?**

```
Awareness (saw an ad)
   │
   ▼
Interest (clicked / visited site)
   │
   ▼
Consideration (signed up / opened the app)
   │
   ▼
Activation (took the first valuable action)
   │
   ▼
Purchase / Subscription (paid)
```

At each stage, some prospects drop off. Conversion rate stage-to-stage reveals where the leaks are.

### Acquisition channels

Customers enter the funnel through different channels:

| Channel | Examples | Typical strengths |
|---------|----------|-------------------|
| **Paid search** | Google Ads, Bing Ads | High intent, scalable |
| **Paid social** | Meta, TikTok, LinkedIn | Targeted, lower intent |
| **Organic search** | SEO traffic | High intent, slow to build |
| **Email** | Newsletter, drip campaigns | High ROI for existing audience |
| **Referral** | Friend invites, partner integrations | Best LTV, hardest to scale |
| **Direct / Brand** | Typing the URL, brand search | Indicates brand strength |
| **Content / Social organic** | Blog, YouTube, podcast | Long-term, hard to attribute |

> Think of channels as highways into a city. The analyst identifies which highway is busiest, fastest, and cheapest.

### Channel KPIs

For each channel, the canonical metrics:

- **CAC (Customer Acquisition Cost)** = channel spend / customers acquired
- **CPC (Cost Per Click)** = channel spend / clicks (intermediate)
- **Conversion rate** = customers / clicks
- **LTV / CAC ratio** = lifetime value of acquired customers / CAC
- **Payback period** = months until the customer's revenue covers CAC

The headline KPI is **LTV / CAC** — should be > 3 for sustainable growth. Below 1 means you lose money on every customer.

### Channel attribution — the hard problem

A single customer rarely enters through one channel. A typical journey:

```
Saw a YouTube ad → didn't click
Two weeks later, searched on Google → visited site
Read a blog post → bookmarked
A week later, saw a Meta retargeting ad → clicked
Signed up → paid
```

Which channel gets credit? Last-click attribution (the convention for years) credits Meta. But the YouTube ad started the journey; the blog convinced them. **Multi-touch attribution** models distribute credit across channels.

Common models:
- **Last click**: simple, biased toward bottom-funnel channels
- **First click**: biased toward top-funnel awareness channels
- **Linear**: equal credit across all touchpoints
- **Time decay**: more credit to touchpoints near the conversion
- **Data-driven (ML)**: GA4's algorithmic model

Attribution is among the hardest analytics problems. Pick a model, document the choice, accept imperfection.

### Expansion funnel — the post-purchase view

After the first sale, the expansion funnel asks: **do they stay, grow, and refer?**

```
First purchase / activation
   │
   ▼
Repeat purchase / continued use
   │
   ▼
Expansion (upsell, larger plan, more seats)
   │
   ▼
Advocacy (referrals, reviews, case studies)
```

### Expansion KPIs

- **Retention rate** = % of customers still active after N days/months
- **Churn rate** = 1 − retention rate
- **Net Revenue Retention (NRR)** = revenue from existing customers (with expansion) / revenue from same customers a year ago
- **Lifetime Value (LTV)** = total revenue per customer over their relationship
- **NPS (Net Promoter Score)** = survey-based likelihood to recommend
- **Expansion revenue** = upsells + cross-sells + plan upgrades

The headline KPI is **NRR** for subscription businesses (> 100% means you grow revenue from existing customers without acquiring new ones — the holy grail) or **repeat purchase rate** for transactional.

### The two funnels are linked

The two funnels are not independent:

- **High-CAC channels often have higher LTV**: customers who came from a friend's recommendation retain better than impulse-purchase ad clicks
- **Wrong-fit customers acquired cheaply churn fast**: low CAC, low LTV = no real growth
- **Expansion potential informs acquisition spend**: if NRR is 120%, you can spend more on acquisition because existing customers grow themselves

A common mistake: optimizing acquisition cost (CAC) alone without considering the LTV of customers acquired through each channel.

### The leaky bucket diagnosis

When growth stalls, the diagnostic question is: **acquisition problem or retention problem?**

| Symptom | Diagnosis | Action |
|---------|-----------|--------|
| New customers flat, existing customers happy | Acquisition problem | Marketing investment, new channels |
| New customers growing, total revenue flat | Retention problem | Customer success, product fixes |
| Both growing, but slower than expected | Activation problem | Onboarding, time-to-value |
| Activation strong, expansion weak | Product / pricing problem | Tier design, upsell flows |

The combined funnel view reveals which half of the business needs attention.

### Connecting to other KPIs

- Acquisition channel performance feeds into [[KPI by Team and Function]] (Marketing's CAC)
- Retention KPIs feed into [[KPI by Business Model]] (subscription companies live or die by NRR)
- Avoiding vanity (total signups, total downloads) — see [[Vanity Metrics Anti Patterns]]
- The deeper customer-level analysis lives in [[Customer Segmentation Rfm]] and [[Cohort Analysis]]

## Key Parameters

- **CAC payback target**: < 12 months is healthy for most SaaS; < 6 months for consumer
- **LTV / CAC ratio target**: > 3 sustainable, > 5 excellent, < 1 unsustainable
- **NRR target**: > 100% is the SaaS gold standard
- **Retention window**: define the period (day-7, day-30, day-90) consistently across reports
- **Attribution model documented**: every channel-performance number should cite which model produced it

## When To Use

- **Marketing performance reviews** — channel-by-channel CAC and conversion
- **Investor presentations** — LTV / CAC and NRR are universally expected
- **Annual planning** — acquisition vs retention investment trade-off
- **Diagnosing growth stalls** — which half of the funnel is leaking
- Anti-pattern: optimizing acquisition without measuring retention quality — leaky bucket
- Anti-pattern: ignoring attribution and crediting only the last-click channel — over-invests in bottom-funnel channels

## Connections

- Related: [[KPI Fundamentals]], [[KPI by Team and Function]] (marketing's KPIs), [[Vanity Metrics Anti Patterns]], [[Customer Segmentation Rfm]] (segment customers within the funnel), [[Cohort Analysis]] (track funnel cohorts over time)
- Builds on: [[Seven Step Framework in Practice]], [[Data Pipeline Architecture]] (acquisition data comes from multiple sources)
- Compare with: AARRR pirate metrics (Acquisition, Activation, Retention, Referral, Revenue) — same concept, different vocabulary
- Used by: every growth team; every CMO dashboard; every investor pitch

## My Notes

- The two-funnel view is the conceptual frame that makes growth math make sense. Internalize it before diving into specific metrics.
- Practice: [Amazon Books NPS Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7292) — build acquisition channel and retention dashboards for a fictional e-commerce.
- A useful anchor question: "if we doubled marketing spend tomorrow, would LTV / CAC hold?" Forces honest evaluation of channel scalability.
- Interview tip: when discussing growth analytics, mention both halves explicitly — "we tracked CAC at the top, NRR at the bottom, and used cohort views to tie them together." Signals end-to-end thinking.
