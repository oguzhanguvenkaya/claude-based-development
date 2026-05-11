---
title: "Window Functions Across Grain"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/05-window-ile-farkli-detay-seviyelerinde-join]]"
tags:
  - sql
  - window-functions
  - join-pitfalls
  - grain
  - advanced
---

# Window Functions Across Grain

> One-line summary: When joining tables at different grain levels (e.g., order-level shipping costs vs line-item sales), direct joins cause fan-out that corrupts totals — window functions let you distribute order-level totals across line items without changing the sum.

## Core Concept

[[Join Pitfalls Grain and Fan Out]] explained the bug: joining a fine-grained table (line items) with a coarse-grained table (orders) multiplies the coarse side's rows. If you SUM the order-level shipping cost after the join, you get N× the real total, where N is the average number of line items per order.

Pre-aggregating is one fix. **Window functions are another, often more elegant fix:** keep the row detail, divide the coarse total across the partition, and the SUM stays correct.

This is one of the most useful "intermediate-to-senior" SQL techniques. Most analysts know window functions for ranking; fewer use them to navigate grain mismatches.

## How It Works

### The setup

```
orders                  order_lines
─────────────           ──────────────────
order_id (PK)           order_id (FK)
shipping_cost           product_id
                        quantity
                        unit_price

Goal: a per-product report that includes the order's shipping cost, without
inflating the total shipping cost.
```

### The fan-out bug (recap)

```sql
SELECT
  l.product_id,
  l.quantity,
  o.shipping_cost
FROM order_lines o_l AS l
JOIN orders             o ON l.order_id = o.order_id;
```

If order 42 has 3 line items and `shipping_cost = $12`, the join produces 3 rows each showing `$12`. SUM-ing shipping_cost from this result gives `$36` — three times the truth. See [[Join Pitfalls Grain and Fan Out]].

### Window function fix: distribute the cost

```sql
WITH joined AS (
  SELECT
    l.order_id,
    l.product_id,
    l.quantity,
    o.shipping_cost,
    COUNT(*) OVER (PARTITION BY l.order_id) AS lines_per_order
  FROM order_lines AS l
  JOIN orders      AS o ON l.order_id = o.order_id
)
SELECT
  order_id,
  product_id,
  quantity,
  shipping_cost / lines_per_order AS allocated_shipping_cost
FROM joined;
```

For order 42 with 3 lines: each row now shows `$4`. SUM of `allocated_shipping_cost` across all three lines = `$12`. Total is preserved; the per-row detail is preserved.

This is **proportional allocation** — splitting a coarse-grained total across the rows of its fine-grained group.

### Variation: allocate by weight, not equally

```sql
WITH joined AS (
  SELECT
    l.order_id,
    l.product_id,
    l.quantity,
    l.unit_price,
    o.shipping_cost,
    SUM(l.quantity * l.unit_price) OVER (PARTITION BY l.order_id) AS order_total_value
  FROM order_lines AS l
  JOIN orders      AS o ON l.order_id = o.order_id
)
SELECT
  product_id,
  shipping_cost * SAFE_DIVIDE(quantity * unit_price, order_total_value) AS allocated_shipping_cost
FROM joined;
```

Now shipping cost is split proportionally to each line's contribution to the order's total value. More expensive line items absorb more of the shipping cost. See [[Safe Divide]] for the SAFE_DIVIDE guard.

### Preserving aggregates: the test

After applying the allocation, run [[Value Preservation Test]] to confirm:

```sql
-- Source total
SELECT SUM(shipping_cost) AS source FROM orders;
-- Allocated total
SELECT SUM(allocated_shipping_cost) AS allocated FROM the_allocated_view;
-- These must match (modulo floating-point tolerance)
```

If they don't match, allocation is wrong somewhere — usually a misplaced PARTITION BY or a NULL denominator.

### Window vs pre-aggregate: which to choose

| Situation | Use |
|-----------|-----|
| You need both fine-grained rows AND coarse-grained context | Window |
| You only need the coarse-grained summary | Pre-aggregate (CTE + GROUP BY) |
| Allocation by weight | Window with proportional formula |
| Simple sum that must not double-count | Either; pre-aggregate is usually clearer |

Window approach is most valuable when downstream needs per-row detail AND correct totals — e.g., a "product profitability" report that needs to charge each line its share of order-level overhead.

### Combining with rank/lag

```sql
-- Top product per order by allocated shipping cost
SELECT *
FROM (
  SELECT
    order_id,
    product_id,
    allocated_shipping_cost,
    RANK() OVER (PARTITION BY order_id ORDER BY allocated_shipping_cost DESC) AS rank_in_order
  FROM allocated_data
)
WHERE rank_in_order = 1;
```

Window functions compose. Once you have the per-row allocation, rank/lag/lead within the partition all work without further joins.

## Key Parameters

- **PARTITION BY = the coarse-grained ID**: the column whose total you are spreading
- **Denominator computation**: use `COUNT(*)` for equal split, `SUM(weight)` for weighted
- **NULL safety**: wrap divisions in [[Safe Divide]] — partitions with zero rows or NULL weights will error otherwise
- **Performance**: window functions trigger a sort; on huge tables, partition cardinality matters

## When To Use

- **Order-level cost allocated to line items**: shipping, tax, discounts, overhead
- **Channel cost allocated to events**: marketing spend allocated to attributed conversions
- **Department headcount allocated to project hours**: org-level totals distributed across project rows
- **Any "coarse total + fine detail" report** where the per-row breakdown must sum to the original total
- Anti-pattern: simple SUM after a fan-out join — produces multiplied totals; this is the bug allocation solves
- Anti-pattern: using a window allocation when a pre-aggregated CTE would suffice — adds complexity without benefit

## Connections

- Related: [[Window Functions Fundamentals]] (the syntax base), [[Join Pitfalls Grain and Fan Out]] (the bug this solves), [[Joins with Group By]] (the alternative pre-aggregate approach), [[Value Preservation Test]] (the test that proves allocation preserved totals)
- Builds on: [[Safe Divide]] (for proportional formulas), [[Common Table Expressions Cte]] (CTE often holds the joined-with-windows intermediate)
- Compare with: pre-aggregating before join — simpler when you do not need row detail
- Used by: cost allocation, attribution modeling, multi-grain reporting in finance and operations

## My Notes

- This is the technique that separates analysts who "know windows" from those who can solve real reporting problems. It is the most "senior" window-function pattern in everyday BI work.
- Practice: [Pencere (window) Fonksiyonları - 2](https://nextgen.workintech.com.tr/project/202/5?pid=7607) — allocate an order-level cost across line items and prove the total is preserved.
- BigQuery tip: when allocation formulas get complex, materialize the intermediate via a temp table — debugging is much easier than chasing through 4 nested CTEs with window functions.
- Interview gotcha: be ready to walk through the order/line-item allocation example. It tests both window-function syntax and grain awareness — high signal in interviews.
