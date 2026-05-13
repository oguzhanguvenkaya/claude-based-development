---
title: "Finance KPIs"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/11-finans-kpilari]]"
tags:
  - data-analysis
  - kpi
  - finance
  - profitability
  - margin
---

# Finance KPIs

> One-line summary: The finance team's headline KPIs measure profitability — gross margin (revenue minus direct costs) and net margin (gross margin minus marketing + operational costs) — both expressed as percentages so they normalize across business sizes and time periods.

## Core Concept

For the finance team, "KPI" equals **profit control**. Revenue without profitability is vanity; growing 50% while losing money is a path to bankruptcy. The two margin KPIs answer the central question: **"are we making money, and is that improving?"**

Margins are percentages, not absolute dollars. A $1M revenue business with 40% gross margin is healthier than a $10M revenue business with 5% gross margin. Reporting margins instead of raw revenue forces the business to optimize efficiency, not just scale.

## How It Works

### Gross margin

```
Gross Margin = (Revenue − Cost of Goods Sold) / Revenue × 100
```

- **Revenue**: total sales in the period
- **Cost of Goods Sold (COGS)**: the direct cost of producing what was sold
  - For a retailer: wholesale cost of inventory + shipping in
  - For a SaaS company: cloud infrastructure + customer success delivery
  - For a manufacturer: raw materials + factory labor + factory overhead

Gross margin tells you: **out of every dollar of revenue, how much is left after paying for the product itself?**

A 60% gross margin means you keep 60 cents on every dollar before any marketing, salaries, or office rent. That 60 cents pays for everything else and (ideally) leaves a profit.

### Net margin

```
Net Margin = (Revenue − COGS − OpEx − Marketing) / Revenue × 100
            = Gross Margin × (1 − OpEx_ratio − Marketing_ratio)
```

OpEx = operational expenses (salaries, rent, software, overhead). Marketing = ad spend, content, sales team commissions.

Net margin tells you: **out of every dollar of revenue, how much actual profit is left at the very end?**

- Industry benchmarks (rough): software ~20%, e-commerce ~5%, grocery retail ~2%, luxury goods ~15%

### A worked example — GreenFit

GreenFit's daily P&L for April 5:

| Line item | Amount |
|-----------|--------|
| Revenue | $50,000 |
| COGS (product cost) | $20,000 |
| **Gross margin** | **$30,000 (60%)** |
| Marketing spend | $8,000 |
| Operating expenses (split daily) | $12,000 |
| **Net margin** | **$10,000 (20%)** |

If on April 5 marketing spiked to $20,000 (due to a campaign error), the math becomes:

| Line item | Amount |
|-----------|--------|
| Revenue | $50,000 |
| COGS | $20,000 |
| Gross margin | $30,000 (60%) — **unchanged** |
| Marketing | $20,000 — spiked |
| OpEx | $12,000 |
| Net margin | **-$2,000 (-4%)** — bleeding |

This illustrates why both KPIs matter: gross margin shows production efficiency; net margin shows whether the business model overall is sustainable.

### Supporting metrics finance tracks

Around the two KPI headlines, finance dashboards typically include:

- **Revenue** (absolute) — by region, by channel, by product line
- **COGS breakdown** — product cost vs shipping in vs returns processing
- **Marketing spend** — by channel, by campaign
- **Customer Acquisition Cost (CAC)** = marketing spend / new customers
- **Customer Lifetime Value (LTV)** — expected revenue from one customer over their relationship
- **LTV / CAC ratio** — health check, should be > 3 for sustainable growth
- **Operating cash flow** — actual cash in vs out (different from accounting profit)

These metrics explain *why* margins moved; the margins themselves are the headline.

### Daily vs monthly vs quarterly

| Cadence | Use case |
|---------|----------|
| **Daily** | Operational margin tracking — catch issues like the April 5 spike fast |
| **Weekly** | Trend monitoring — smooth out daily noise |
| **Monthly** | Reporting to leadership |
| **Quarterly** | Board / investor reporting; long-cycle decisions |

Most finance teams maintain dashboards at all four cadences. The seven-step analysis framework ([[Seven Step Framework in Practice]]) defines when to dig deeper.

### Common analyst questions on finance KPIs

- "Why did gross margin drop 2pp last month?" → drill into COGS breakdown
- "Are we acquiring profitably?" → check CAC payback period and LTV/CAC
- "Is this campaign worth running?" → marketing efficiency = revenue uplift / spend
- "What is the break-even point for this product?" → unit economics modeling

Each answer requires the same workflow ([[Data Analysis Workflow]]) applied to a different question.

### Computing in SQL

```sql
-- Daily gross margin
SELECT
  DATE(order_date) AS day,
  SUM(revenue)                        AS revenue,
  SUM(cogs)                           AS cogs,
  SAFE_DIVIDE(SUM(revenue) - SUM(cogs), SUM(revenue)) AS gross_margin_pct
FROM orders
GROUP BY day
ORDER BY day DESC;
```

See [[Sum Avg Min Max]], [[Group By]], [[Safe Divide]] for the building blocks.

## Key Parameters

- **Margin definition consistency**: every team must agree on what's in COGS vs OpEx; argue once, document, then enforce
- **Time period alignment**: margin for April includes April-attributable costs only — accruals matter for monthly reporting
- **Inflation / FX adjustment**: when comparing year-over-year, factor in inflation and currency moves
- **Cohort vs blended**: blended margin can mask that new customers are unprofitable; cohort views reveal this

## When To Use

- **Finance team's primary dashboard** — gross + net margin headline always
- **Investor / board reporting** — quarterly margin trends
- **Pricing decisions** — set prices to hit target margin
- **Cost-cutting analyses** — find the line items eating margin
- Anti-pattern: reporting absolute profit without margin context — hides efficiency trends
- Anti-pattern: optimizing one KPI at the expense of the other — slashing marketing improves net margin short-term but kills growth

## Connections

- Related: [[KPI Fundamentals]] (this page is one of three department examples), [[Inventory KPIs]] (the operations side), [[Quality KPIs]] (the product side), [[Seven Step Framework in Practice]] (the methodology that computes these KPIs), [[Customer Acquisition and Expansion Funnels]] (CAC, LTV, NRR — the growth-related finance KPIs)
- Builds on: basic accounting, [[Sum Avg Min Max]] (SQL aggregates), [[Pivot Tables Sheets]] (Sheets equivalent)
- Compare with: cash-flow KPIs (timing of money, not just profitability); contribution margin (unit-level economics)
- Used by: every finance team; every executive review meeting

## My Notes

- Margins are the single most universal business KPI — every for-profit organization tracks some flavor of them.
- Practice: [Amazon Books Kalite Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7281) — compute gross and net margin from a sample P&L, identify which line item is driving variance.
- The hardest part of margin work is **definition agreement** across teams, not the math. Push hard to document COGS / OpEx boundaries.
- Interview tip: when discussing impact of an analytical project, framing it as "moved gross margin from X% to Y%" is the most universally understandable metric. Use it.
