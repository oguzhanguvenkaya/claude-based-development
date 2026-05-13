---
title: "Quality KPIs"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/13-kalite-kpilari]]"
tags:
  - data-analysis
  - kpi
  - quality
  - returns
  - customer-satisfaction
---

# Quality KPIs

> One-line summary: For quality teams, the headline KPI is the **return rate** — the percentage of orders returned by customers — because returns are the most direct signal that product quality or expectations failed; supporting metrics decompose returns by reason and quantify their financial impact.

## Core Concept

For the quality team, "KPI" equals **product quality** as experienced by customers. Internal tests catch some defects; the rest surface through customer behavior. **Return rate** is the universal signal: when customers send products back, something failed — quality, fit, expectations, packaging.

Fewer returns mean happier customers. They also mean fewer logistics costs, less inventory write-off, and a reputation that does not bleed. Quality KPIs sit at the intersection of customer satisfaction and operational cost.

## How It Works

### The headline KPI: return rate

```
Return Rate = (Number of orders returned / Number of orders shipped) × 100
```

A 5% return rate means 1 in 20 orders is sent back. Industry benchmarks:
- **Online apparel**: 20–40% (high — fit issues)
- **Online electronics**: 8–15%
- **In-store retail**: 5–10%
- **Industrial / B2B**: 1–3%

Measured weekly or monthly; daily is too noisy for most categories.

### Supporting metrics

| Metric | What it measures |
|--------|------------------|
| **Returns by reason** | Categorical breakdown: damaged, wrong item, didn't fit, didn't like |
| **Return rate by category** | Apparel vs electronics vs accessories |
| **Refund payout** | Direct financial cost of returns |
| **Restocking cost** | Logistics + inspection + repackaging |
| **Time to refund** | How fast customers get their money back |
| **Repeat-return customers** | Customers who return frequently (sometimes intentional behavior) |
| **NPS** | Net Promoter Score — willingness to recommend |
| **Review rating** | Average star rating per product |

These metrics explain *why* returns happen and what to act on.

### Return reasons — the diagnostic pivot

When return rate spikes, the first analytical step is: **break down by reason**.

| Reason | What it tells you | Action |
|--------|-------------------|--------|
| **Damaged in transit** | Packaging or carrier issue | Improve packaging; review carrier performance |
| **Wrong item shipped** | Fulfillment error | Audit picking/packing process |
| **Didn't fit** (apparel) | Sizing chart / model accuracy | Improve product photos, size guides |
| **Didn't match description** | Listing accuracy | Update product copy / photos |
| **Changed mind** | Customer-side; harder to influence | Friction in checkout? Wishlist features? |
| **Quality defect** | Manufacturing issue | Engage supplier; QC sampling |

A pivot table of return rate × reason × product category is the canonical first analysis.

### Financial impact of returns

A return is not just a refunded sale — it carries real costs:

| Cost component | Typical magnitude |
|----------------|-------------------|
| Direct refund | 100% of sale price |
| Return shipping (if paid) | 5–15% of sale price |
| Inspection + restocking | 10–20% of product cost |
| Product write-off (damaged/unsellable) | 30–100% of product cost |
| Customer support time | 5–10 min per return |

A returned $50 order can cost the company $20–30 in handling. At scale, this is a material P&L line ([[Finance KPIs]] connection — returns directly hit gross margin).

### A worked example — GreenFit returns

GreenFit tracks these per category for April:

| Category | Orders shipped | Returns | Return rate | Top reason |
|----------|----------------|---------|-------------|------------|
| Apparel | 8,000 | 1,600 | 20% | Didn't fit (45%) |
| Footwear | 3,200 | 480 | 15% | Didn't fit (60%) |
| Accessories | 2,000 | 80 | 4% | Damaged (50%) |
| Equipment | 800 | 24 | 3% | Quality defect (40%) |

Insight: apparel + footwear are dominated by fit issues — investment in better size charts and 3D fit visualization would have the highest leverage.

### Returns and customer LTV

Counterintuitively, a generous return policy can *increase* customer lifetime value. Customers who feel safe to return are more willing to buy again. The optimal return rate is not zero — it is whatever level maximizes long-term revenue.

The data team's job: model the relationship between return policy strictness and repeat purchase rate.

### Computing in SQL

```sql
-- Monthly return rate by category
WITH monthly_orders AS (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS month,
    category,
    COUNT(*)                     AS orders
  FROM orders
  GROUP BY month, category
),
monthly_returns AS (
  SELECT
    DATE_TRUNC(return_date, MONTH) AS month,
    category,
    COUNT(*)                       AS returns
  FROM returns
  GROUP BY month, category
)
SELECT
  o.month,
  o.category,
  o.orders,
  COALESCE(r.returns, 0) AS returns,
  SAFE_DIVIDE(COALESCE(r.returns, 0), o.orders) AS return_rate
FROM monthly_orders   o
LEFT JOIN monthly_returns r USING (month, category)
ORDER BY o.month DESC, return_rate DESC;
```

See [[Common Table Expressions Cte]], [[Joins Fundamentals]], [[Join Types]] (LEFT JOIN to keep all order months), [[Null Handling SQL]] (COALESCE for zero returns).

### Quality dashboards — the two-audience pattern

Like inventory, quality dashboards split:

**Executive view:** overall return rate, trend, biggest categories of concern.

**Operational view:** drill into a category, see returns by reason, by SKU, by week — find the specific product to fix.

This pattern (executive overview + operational drill-down) recurs across operational KPIs — see [[Inventory KPIs]] for the parallel.

### The reverse logistics layer

For high-return categories (apparel), the **reverse logistics** flow is its own operations:
- Receive return → inspect → restock OR repair OR destroy → refund
- Each step has its own time and cost KPIs
- Sometimes "return centers" are physically separate from outbound fulfillment

A mature operation tracks the *cost per return* alongside the return rate.

## Key Parameters

- **Measurement window**: monthly is standard; weekly for fast-moving fashion; quarterly for B2B
- **Numerator definition**: "returned orders" or "returned items" — orders can be partial returns
- **Time lag**: a customer can return up to 30 days (or 60, 90) after purchase — be careful with denominator alignment
- **Refund vs exchange**: exchanges are sometimes excluded from "returns" depending on policy; document the choice

## When To Use

- **Quality team's primary dashboard** — return rate at the top
- **Category-level analysis** — which products drive the most returns
- **Supplier conversations** — high return rate is a supplier scorecard item
- **Pricing decisions** — products with high returns may need price adjustment or discontinuation
- Anti-pattern: blanket return policy ignoring per-category cost — strict on $5 t-shirts wastes effort; lenient on $500 electronics burns money
- Anti-pattern: optimizing return rate to zero — usually means making customers feel unsafe, hurting LTV

## Connections

- Related: [[KPI Fundamentals]], [[Finance KPIs]] (returns hit gross margin directly), [[Inventory KPIs]] (returned items affect stock), [[Seven Step Framework in Practice]] (the methodology)
- Builds on: [[Common Table Expressions Cte]] (multi-source aggregation), [[Joins Fundamentals]], [[Sum Avg Min Max]]
- Compare with: NPS (Net Promoter Score) — a survey-based satisfaction KPI; complementary to behavior-based return rate
- Used by: every consumer-facing retailer; quality teams across manufacturing, e-commerce, services

## My Notes

- Return rate is one of the most universally tracked retail KPIs — every retailer measures some flavor of it.
- Practice: [Amazon Books Kalite Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7281) — compute return rate, decompose by reason, identify the single product category to focus quality investment on.
- The relationship between return policy strictness and customer LTV is counterintuitive — generous policies often pay off. Be ready to defend this in stakeholder discussions.
- Interview tip: framing analytics impact as "reduced return rate from X% to Y%, saving $Z in handling costs" is high-signal — it ties analysis to a measurable business outcome.
