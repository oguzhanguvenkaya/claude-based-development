---
title: "Customer Segmentation Rfm"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/09-segmentasyon-nedir]]"
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/10-segmentasyon-rfm-yontemi]]"
tags:
  - data-analysis
  - segmentation
  - rfm
  - customer-analytics
  - personalization
---

# Customer Segmentation Rfm

> One-line summary: Customer segmentation groups customers into actionable cohorts based on shared behavior — and **RFM** (Recency, Frequency, Monetary) is the canonical scoring method that ranks customers on how recently, how often, and how much they buy, producing segments like "champions," "at-risk," and "lost."

## Core Concept

Henry Ford famously said customers could have his Model T "in any color, as long as it's black." That worked for an early mass market. It does not work today. Modern markets reward businesses that understand and respond to **customer differences** — and the analytical practice that captures those differences is **segmentation**.

Segmentation groups customers by shared characteristics (behavior, demographics, value) so that each group can be served, marketed to, and retained differently. **RFM** is the most widely-adopted behavioral segmentation framework: it scores every customer on three axes and combines those scores into named segments that drive concrete marketing and product decisions.

## How It Works

### Why segment at all?

A flat customer list hides important variation:
- Your top 10% of customers might generate 60% of revenue (Pareto pattern)
- New customers behave differently from long-time loyalists
- At-risk customers signal churn before they leave

Treating them all identically means under-serving the most valuable and over-spending on the least likely to convert. Segmentation lets each group get the right message, offer, and product experience.

### The RFM framework

Three behavioral signals, scored 1–5 each:

| Letter | Stands for | Captures |
|--------|-----------|----------|
| **R** | Recency | How recently did they buy? (last week = high, last year = low) |
| **F** | Frequency | How often do they buy? (10 orders/year = high, 1 = low) |
| **M** | Monetary | How much do they spend? (total or average) |

Each customer gets a 3-digit score: `RFM = 555` (best — bought yesterday, often, lots) to `RFM = 111` (worst — bought long ago, rarely, little).

### Computing RFM scores

```sql
WITH customer_metrics AS (
  SELECT
    customer_id,
    DATE_DIFF(CURRENT_DATE(), MAX(order_date), DAY) AS days_since_last_order,
    COUNT(*)                                        AS order_count,
    SUM(amount)                                     AS total_spend
  FROM orders
  GROUP BY customer_id
),
rfm_scores AS (
  SELECT
    customer_id,
    NTILE(5) OVER (ORDER BY days_since_last_order ASC) AS r_score,  -- lowest = best
    NTILE(5) OVER (ORDER BY order_count DESC)          AS f_score,  -- highest = best
    NTILE(5) OVER (ORDER BY total_spend DESC)          AS m_score   -- highest = best
  FROM customer_metrics
)
SELECT
  customer_id,
  r_score, f_score, m_score,
  CONCAT(r_score, f_score, m_score) AS rfm_code
FROM rfm_scores;
```

`NTILE(5)` (see [[Window Functions Fundamentals]]) splits customers into 5 equal quintiles — the standard RFM scoring.

### Naming the segments

The 125 possible RFM codes group into named segments:

| Segment | RFM signature | Description | Action |
|---------|---------------|-------------|--------|
| **Champions** | 555, 554 | Recent, frequent, high-spend | VIP treatment, referral asks |
| **Loyal customers** | 543, 444 | Frequent + high-value | Loyalty programs, retain |
| **Potential loyalists** | 534, 524 | Recent + frequent, lower spend | Cross-sell, upgrade offers |
| **New customers** | 511, 512 | Recently bought, low frequency | Onboarding, second purchase nudges |
| **Promising** | 412, 411 | Some recency, low frequency/spend | Engagement campaigns |
| **At risk** | 145, 244 | Used to buy often, dropped off | Win-back campaigns |
| **Cannot lose them** | 155, 145 | High-value but inactive | Personal outreach |
| **About to sleep** | 222 | Mid-range across all dimensions | General re-engagement |
| **Hibernating** | 111, 121 | Old, low-frequency, low-spend | Low-cost win-back or accept the loss |

The labels vary by company; the structure is universal.

### The transcript's BrightCart example

> "BrightCart's sales are flat. Leadership asks: should we focus on loyalists, new customers, or those drifting away?"

The RFM analysis reveals:
- 8% of customers are Champions, generating 45% of revenue → invest in retention
- 30% are At-risk, generating 25% of revenue → urgent win-back campaign
- 40% are Hibernating, generating 5% of revenue → low-priority

The answer: focus most effort on Champions (cheap retention) and At-risk (high recovery potential). Hibernating gets a final automated campaign and is then accepted as churned.

### Beyond RFM — other segmentation axes

RFM is behavioral. Other useful segmentations:

| Axis | Examples | Use case |
|------|----------|----------|
| **Demographic** | Age, gender, location | Brand positioning |
| **Firmographic** (B2B) | Company size, industry | Sales targeting |
| **Psychographic** | Lifestyle, values | Brand messaging |
| **Behavioral** | Usage frequency, feature adoption | Product, retention |
| **Journey stage** | Awareness → activation → expansion → churn | Lifecycle marketing |
| **Value tier** | Top 10% / mid 40% / bottom 50% by revenue | Resource allocation |

Sophisticated teams combine multiple axes (e.g., "high-value B2B customers in the financial sector who have used Feature X but not Feature Y").

### Updating segments

Segments are not static — customers move between them. A "Champion" who stops buying becomes "At-risk" three months later. Recompute segments on a regular cadence:

- **Weekly** for retail / e-commerce with fast-moving customers
- **Monthly** for SaaS subscriptions
- **Quarterly** for B2B with longer sales cycles

Each customer's segment changes; the action they trigger should adapt.

### Segment-driven personalization

Once segments are defined, downstream systems can:
- **Email marketing**: different campaigns per segment
- **Pricing**: discount strategies aligned to segment (loyalty rewards for Champions, recovery offers for At-risk)
- **Product**: feature prioritization by segment usage
- **Sales**: account managers prioritize Champions and Cannot-lose
- **Customer success**: proactive outreach to At-risk

The KPI tied to each segment differs: Champions optimize for expansion revenue; At-risk for recovery rate; Hibernating for low-cost re-engagement.

## Key Parameters

- **Quintile method**: NTILE(5) is standard; some teams use 4 (quartiles) for simpler segments
- **Time window**: define "recency" against a fixed window (last 90 days, last year) — using all-history dilutes recent signal
- **Refresh cadence**: weekly to quarterly depending on industry
- **Score weighting**: by default each of R/F/M is equal; some industries weight M heavier (B2B) or F heavier (subscription)
- **Segment count**: 8–12 named segments is the sweet spot; more dilutes; fewer loses nuance

## When To Use

- **Personalized marketing**: campaign design by segment
- **Retention strategy**: identify At-risk early, intervene
- **Revenue concentration analysis**: how much of revenue comes from the top segments
- **Product prioritization**: which segment's needs to prioritize
- Anti-pattern: building segments and not acting on them — segmentation is mid-funnel work; the value is in downstream activation
- Anti-pattern: too many segments (50+) — operationally impossible to serve each

## Connections

- Related: [[Customer Acquisition and Expansion Funnels]] (segmentation often gets applied within the expansion funnel), [[Cohort Analysis]] (cohort views over time complement segment snapshots), [[KPI by Business Model]] (segmentation strategies shift by model)
- Builds on: [[Window Functions Fundamentals]] (NTILE for scoring), [[Group By]], [[Joins Fundamentals]]
- Compare with: K-means clustering (ML-based segmentation; useful for unsupervised discovery), persona-based segmentation (qualitative; lower precision but useful for design)
- Used by: every CRM-driven team; every personalization initiative

## My Notes

- RFM is the highest-ROI segmentation technique because it's behavioral (real signal) and simple to compute (single query). Start here before exploring ML-based clustering.
- Practice: [Amazon Books NPS Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7292) — compute RFM scores, name the segments, propose one action per segment.
- The hardest part of segmentation is not computing — it's operationalizing. Tie each segment to a downstream system (email, sales handoff, product flag) before declaring victory.
- Interview tip: when discussing customer analytics, mention RFM specifically with the segment-to-action mapping. Many candidates know "segmentation"; fewer can walk through the operational use.
