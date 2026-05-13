---
title: "Cohort Analysis"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/11-cohort-analizi]]"
tags:
  - data-analysis
  - cohort
  - retention
  - customer-analytics
  - time-series
---

# Cohort Analysis

> One-line summary: Cohort analysis groups customers by a shared starting event (signup month, first purchase date) and tracks each group's behavior over time — revealing retention, churn timing, and trend differences that averages over the whole customer base hide.

## Core Concept

"Average customer retention is 60%" feels meaningful but is misleading. It mixes customers who signed up yesterday with customers who signed up 3 years ago, hiding whether your business is improving or declining. **Cohort analysis** breaks the average apart: it groups customers by when they started, then tracks each group's behavior separately. The pattern across cohorts tells the story.

A January cohort of 100 customers might lose 30 in month 1. A March cohort of 100 might lose only 20 — direct evidence that something improved (a better onboarding flow, perhaps). The aggregate retention rate would never reveal this.

## How It Works

### Building a basic cohort

```
Step 1 — Define the cohort criterion: signup month
Step 2 — Group customers by signup month
Step 3 — For each cohort, measure behavior in each subsequent period (month 1, month 2, ...)
Step 4 — Compare cohorts side by side
```

The output is a **cohort table**:

| Cohort | M0 | M1 | M2 | M3 | M4 | M5 |
|--------|-----|-----|-----|-----|-----|-----|
| 2026-01 | 100 | 70 | 55 | 45 | 38 | 32 |
| 2026-02 | 120 | 90 | 72 | 60 | 50 | — |
| 2026-03 | 90  | 68 | 56 | 48 | — | — |
| 2026-04 | 110 | 88 | 75 | — | — | — |
| 2026-05 | 130 | 105 | — | — | — | — |

- **M0** = month of signup (100% by definition)
- **M1** = customers from that cohort still active in month 1
- The diagonal becomes shorter for newer cohorts (less history)

Convert to percentages and the picture sharpens:

| Cohort | M0 | M1 | M2 | M3 | M4 | M5 |
|--------|-----|-----|-----|-----|-----|-----|
| 2026-01 | 100% | 70% | 55% | 45% | 38% | 32% |
| 2026-02 | 100% | 75% | 60% | 50% | 42% | — |
| 2026-03 | 100% | 76% | 62% | 53% | — | — |
| 2026-04 | 100% | 80% | 68% | — | — | — |
| 2026-05 | 100% | 81% | — | — | — | — |

**Month 1 retention** improved from 70% → 81% across five cohorts. That's a real signal — something changed in onboarding around February, and it's working.

### Cohort analysis in SQL

```sql
WITH cohorts AS (
  SELECT
    customer_id,
    DATE_TRUNC(MIN(order_date), MONTH) AS cohort_month
  FROM orders
  GROUP BY customer_id
),
activity AS (
  SELECT
    o.customer_id,
    c.cohort_month,
    DATE_DIFF(DATE_TRUNC(o.order_date, MONTH), c.cohort_month, MONTH) AS months_since_cohort
  FROM orders   o
  JOIN cohorts  c USING (customer_id)
)
SELECT
  cohort_month,
  months_since_cohort,
  COUNT(DISTINCT customer_id) AS active_customers
FROM activity
GROUP BY cohort_month, months_since_cohort
ORDER BY cohort_month, months_since_cohort;
```

See [[Common Table Expressions Cte]], [[Joins Fundamentals]], [[Date Arithmetic Date Sub]], [[Count and Countif]].

### Visualizing cohorts

The classic cohort visualization is the **retention curve** (one line per cohort, time-since-signup on x-axis, retention % on y-axis):

```
100% │■■■
 80% │  ■■■
 60% │     ■■■■
 40% │         ■■■■■
 20% │              ■■■■■■■
  0% └────────────────────────
     M0  M1  M2  M3  M4  M5  M6  M7  M8
```

Multiple cohorts plotted together reveal:
- **Improving cohorts**: each new line stays above the previous → product/onboarding improving
- **Declining cohorts**: each new line falls below → something broke or competition increased
- **Flat across cohorts**: stable performance, neither improving nor degrading

Alternative visualization: a **heatmap** of the cohort table — colors indicate retention strength, easy to scan for patterns.

### What cohort analysis reveals

| Pattern | Interpretation |
|---------|----------------|
| Steep month-1 drop | Activation problem; onboarding does not connect users to value |
| Gradual decline | Natural churn; minimize by retention work |
| Plateau (flat after month N) | Reached "engaged core"; remaining customers stable |
| Improvement in newer cohorts | Recent product/marketing change is working |
| Regression in newer cohorts | Recent change broke something |
| Spike in a specific cohort | Often a campaign or acquisition channel that brought wrong-fit customers |

The diagonal pattern matters more than absolute numbers. Even slow-growing businesses with bad absolute retention can be healthy if cohorts are improving over time.

### Beyond retention — other cohort metrics

Cohorts can track any metric, not just retention:

- **Revenue per cohort over time**: cumulative spend curve per signup month
- **Feature adoption per cohort**: which cohort tried Feature X first?
- **Support ticket rate per cohort**: are newer cohorts easier to support?
- **NPS per cohort**: do newer customers like the product more or less?

Anything where the question "is this changing over time, controlling for tenure?" matters benefits from a cohort view.

### Cohort vs segment

Cohorts and segments are complementary:

- **Cohort**: groups by *when* customers started (time-based)
- **Segment**: groups by *what kind* of customers they are (behavior, value, demographic — see [[Customer Segmentation Rfm]])

A "champions in the January cohort" view combines both — tracking a specific high-value segment within a specific time-based cohort.

### Common pitfalls

- **Comparing cohorts with different exposure time**: the most recent cohort has less history, do not interpret its absolute drop-off vs older cohorts directly
- **Survivorship bias**: customers in M5 are the survivors of M1, M2, M3, M4. Their behavior is not representative of "average customers."
- **Cohort size confounding**: a small cohort can show extreme percentages just from variance — always sanity-check with absolute numbers alongside
- **External event contamination**: holidays, promotions, COVID-style disruptions shift cohort behavior independent of product changes

## Key Parameters

- **Cohort dimension**: usually signup or first-purchase date; can also be acquisition channel, geography, plan tier
- **Cohort grain**: monthly is standard; weekly for fast-moving products; daily for high-volume consumer apps
- **Time horizon**: 6–24 months; longer reveals lifetime patterns
- **Minimum cohort size**: avoid cohorts with < 50 customers (variance dominates)
- **Activity definition**: "active" can mean logged in, purchased, completed task — define carefully

## When To Use

- **Retention investigations**: where is the drop-off, and is it improving?
- **A/B test rollups over time**: separate treatment vs control as cohorts
- **Channel quality assessment**: do customers from referrals retain better than paid ads?
- **Pricing change impact**: cohort before vs after the price change
- **Investor reporting**: cohort retention is the SaaS gold standard for showing health
- Anti-pattern: reporting a blended retention number when cohort trends contradict each other
- Anti-pattern: presenting cohort charts without a clear takeaway annotation

## Connections

- Related: [[Customer Segmentation Rfm]] (cohorts + segments combine powerfully), [[Customer Acquisition and Expansion Funnels]] (cohorts track funnel behavior over time), [[KPI Fundamentals]] (retention is a key KPI), [[Vanity Metrics Anti Patterns]] (cohort analysis is the antidote to many vanity patterns)
- Builds on: [[Group By]], [[Date Arithmetic Date Sub]], [[Window Functions Fundamentals]], [[Common Table Expressions Cte]]
- Compare with: cross-sectional analysis (snapshot of everyone today — misses time variation), longitudinal individual tracking (cohort views are aggregated longitudinal)
- Used by: every retention-focused team; every investor pitch for subscription businesses

## My Notes

- Cohort analysis is the most undervalued analytics technique. Most teams underuse it. Push for it whenever someone asks "is retention improving?"
- Practice: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283) — build a monthly retention cohort table, identify the inflection point.
- A useful framing: "the diagonal is the story." When pitching cohort findings, point at the diagonal of the table — improvements show there.
- Interview tip: when discussing retention, mention cohort analysis explicitly. Bonus if you can verbalize the SQL pattern (DATE_DIFF + GROUP BY cohort_month + months_since).
