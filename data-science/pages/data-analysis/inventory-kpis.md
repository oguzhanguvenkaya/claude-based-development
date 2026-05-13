---
title: "Inventory KPIs"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/12-envanter-kpilari]]"
tags:
  - data-analysis
  - kpi
  - inventory
  - supply-chain
  - stockout
---

# Inventory KPIs

> One-line summary: For inventory teams, the headline KPI is the **stockout rate** — the percentage of SKUs out of stock when customers want them — because no stock means no sale, even with everything else working.

## Core Concept

In retail and e-commerce, "KPI" for the inventory team translates to **product availability**. No matter how brilliant the marketing campaign, no matter how good the price, if the shelf is empty when a customer arrives, the sale does not happen. **Stockout rate** is the inventory team's profit equivalent — the single number that says whether they are doing their job.

Around stockout rate, inventory teams maintain a stack of supporting metrics (average stock, total stock, fulfillment time, days of supply) that diagnose **why** stockouts happen and how to prevent them.

## How It Works

### The headline KPI: stockout rate

```
Stockout Rate = (SKUs out of stock during period / Total SKUs) × 100
```

A 5% stockout rate means 1 in 20 products is unavailable when a customer wants it. For e-commerce, anything above 3% is concerning; above 10% is crisis.

Measured at a fixed cadence (typically daily at 9 AM):
- Snapshot the inventory database
- Count SKUs where stock_quantity = 0 (or below safety threshold)
- Divide by total active SKUs

### Supporting metrics

| Metric | What it measures |
|--------|------------------|
| **Average stock** | Mean inventory level across all SKUs |
| **Total stock** | Aggregate units on hand |
| **Days of supply** | Average stock / average daily demand — how long until you run out |
| **Stockout duration** | Average hours per stockout — how fast you recover |
| **Reorder cycle time** | Time from "place order with supplier" to "stock available" |
| **Safety stock buffer** | Extra inventory held to absorb demand spikes |
| **Inventory turnover** | COGS / average inventory — how many times stock cycles per year |
| **Carrying cost** | Storage + insurance + obsolescence as % of stock value |

### Two dashboards for two audiences

**Executive dashboard (overview):**
- Today's stockout rate
- 30-day trend
- Top 5 categories with highest stockouts
- Total inventory value

The exec dashboard answers: "are we hitting our availability target?"

**Operational dashboard (interactive):**
- SKU-level stockout list (sortable, filterable)
- Reorder recommendations (which SKUs to restock now)
- Supplier lead times
- Per-warehouse stock levels

The ops dashboard answers: "what should we do right now?"

This separation — high-level summary for execs, drill-down for operators — is a universal pattern in KPI dashboard design.

### Why stockouts happen

| Cause | Diagnostic metric |
|-------|-------------------|
| Underforecasting demand | Forecast accuracy, sudden spike in orders |
| Supplier delays | Lead time variance |
| Operational errors | Receiving discrepancies, miscounts |
| Promo-induced spikes | Marketing schedule correlation |
| Seasonality | Year-over-year stockout patterns |

A good analyst correlates the stockout KPI with the right supporting metric to identify the cause. Then operations acts: reorder, change supplier, increase safety stock.

### The cost of stockouts

The hidden cost is significant:
- **Direct**: lost sale (customer buys elsewhere)
- **Indirect**: customer switches to a competitor permanently
- **Reputation**: "they're always out of stock" damages brand

Industry rule: every 1% increase in stockout rate corresponds to ~1.5–2.5% revenue loss for retail. The leverage is high — improving from 8% to 5% stockout can recover 5%+ of total revenue.

### Computing in SQL

```sql
-- Daily stockout rate
SELECT
  DATE(snapshot_at) AS day,
  COUNTIF(stock_qty = 0) AS sku_out_of_stock,
  COUNT(*)               AS total_skus,
  SAFE_DIVIDE(COUNTIF(stock_qty = 0), COUNT(*)) AS stockout_rate
FROM inventory_snapshots
WHERE is_active = TRUE
GROUP BY day
ORDER BY day DESC;
```

See [[Count and Countif]], [[Safe Divide]], [[Group By]], [[Date Arithmetic Date Sub]].

### The trade-off: stockout vs carrying cost

Holding more inventory reduces stockout rate but raises **carrying cost** (storage, capital tied up, obsolescence). The right balance depends on the product:

- **Fast-moving, low-margin** (groceries, basic apparel): high stockout cost; carry more
- **Slow-moving, high-margin** (luxury watches, rare books): low stockout cost; carry less
- **Perishable** (fresh food, fashion): aggressive forecasting; minimize carry

Optimization is per-SKU, not blanket-policy. Analysts often segment SKUs by ABC analysis (top 20% by revenue, mid 30%, bottom 50%) and apply different safety stock policies per tier.

### Linking to finance KPIs

Inventory KPIs feed into [[Finance KPIs]] via two paths:
- **Stockout cost** → lost revenue → lower gross margin (in absolute dollars)
- **Carrying cost** → operational expense → lower net margin

The inventory team's job is to minimize the *sum* of stockout cost + carrying cost. Either extreme hurts profitability.

## Key Parameters

- **Snapshot frequency**: daily for most retail; hourly for fast-moving SKUs; real-time for high-stakes (e.g., grocery)
- **SKU definition**: a "SKU" can mean different things (product variant vs base product vs region-specific) — define carefully
- **Active vs discontinued**: stockouts on discontinued items shouldn't count
- **Safety stock**: usually set at 1.65 × standard deviation of demand for ~95% service level

## When To Use

- **Inventory team's primary dashboard** — stockout rate front and center
- **Supply chain reviews** — root-cause analysis when stockout rate spikes
- **Pre-promo planning** — pull supporting metrics to ensure inventory matches expected demand
- **Supplier negotiations** — lead time variance is a key supplier KPI
- Anti-pattern: optimizing stockout rate alone without considering carrying cost — leads to over-investment in inventory
- Anti-pattern: blanket safety stock policy across all SKUs — high-margin items should carry more; low-margin less

## Connections

- Related: [[KPI Fundamentals]], [[Finance KPIs]] (the cost trade-off), [[Quality KPIs]] (a different operational lens), [[Seven Step Framework in Practice]] (the methodology)
- Builds on: [[Sum Avg Min Max]] (SQL aggregates), [[Pivot Tables Sheets]], [[Conditional Expressions SQL]] (CASE for stockout flags)
- Compare with: SaaS uptime KPIs (% of time service is available) — same conceptual structure (availability rate)
- Used by: every retail / e-commerce / manufacturing analytics team

## My Notes

- Stockout rate is one of the highest-leverage KPIs in retail — a percentage-point improvement can mean millions in recovered revenue.
- Practice: [Amazon Books Tedarik Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7269) — compute stockout rate for a sample inventory dataset; segment by category.
- The "two dashboards" pattern (exec overview + ops drill-down) is reusable for almost every operational KPI — replicate it for quality, fulfillment, etc.
- Interview tip: when discussing inventory analytics, mention the stockout-vs-carrying-cost trade-off — shows you understand the economic balance, not just the metric.
