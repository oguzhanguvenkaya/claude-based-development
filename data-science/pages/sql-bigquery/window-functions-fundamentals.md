---
title: "Window Functions Fundamentals"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/03-neden-window-fonksiyonlarina-ihtiyacimiz-var]]"
  - "[[raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/04-partition-by-ve-over-kullanimi]]"
tags:
  - sql
  - window-functions
  - partition-by
  - over-clause
  - running-totals
---

# Window Functions Fundamentals

> One-line summary: A window function computes an aggregate (or rank) over a "window" of rows defined by `PARTITION BY` and applies it per row — letting you see totals, ratios, ranks, or running sums alongside the original row detail, without collapsing rows like GROUP BY would.

## Core Concept

A regular aggregate with `GROUP BY` collapses many rows into one summary row per group. That works when you want only the summary. But often you want both:
- The detail (every product, with its model, color, size, price, stock)
- The summary alongside it (this product's share of total stock in its category)

GROUP BY cannot produce that — it has already collapsed the rows by the time you would compute the share. **Window functions** keep every row and add the summary as a new column on each one. Same compute, no row loss.

The trick: instead of `GROUP BY`, you write `OVER (PARTITION BY column)`. The result is a per-row column showing the aggregate computed over the rows that share the same partition value.

## How It Works

### Side-by-side comparison

```sql
-- GROUP BY: collapses to one row per category
SELECT
  category,
  SUM(stock_qty) AS total_stock
FROM products
GROUP BY category;

-- Output:
-- shirt    | 450
-- pants    | 320
-- shoes    | 600
```

```sql
-- Window: keeps every row, adds category total to each
SELECT
  product_name,
  category,
  stock_qty,
  SUM(stock_qty) OVER (PARTITION BY category) AS category_total_stock
FROM products;

-- Output:
-- shirt-red-S    | shirt | 100 | 450
-- shirt-blue-M   | shirt | 200 | 450
-- shirt-green-L  | shirt | 150 | 450
-- pants-black-32 | pants | 120 | 320
-- ... etc
```

The window form lets you compute a row's share of its category in one query:

```sql
SELECT
  product_name,
  stock_qty,
  SUM(stock_qty) OVER (PARTITION BY category) AS category_total,
  stock_qty / SUM(stock_qty) OVER (PARTITION BY category) AS share_of_category
FROM products;
```

### Anatomy of the OVER clause

```sql
<aggregate>(<column>) OVER (
  PARTITION BY <grouping_column>     -- which rows belong to this row's window
  ORDER BY <sort_column>              -- order within the window (for ranking, running totals)
  ROWS BETWEEN ... AND ...            -- frame (for running totals over moving windows)
)
```

- `PARTITION BY` splits rows into groups (same idea as GROUP BY)
- `ORDER BY` is needed for ranking and running totals (not for simple per-partition aggregates)
- The frame clause is advanced — usually default suffices

### Common window function uses

```sql
-- 1. Partition aggregate: see the total alongside each row
SUM(stock_qty)   OVER (PARTITION BY category)

-- 2. Running total: cumulative within a partition, in order
SUM(amount)      OVER (PARTITION BY customer_id ORDER BY order_date)

-- 3. Ranking: position within a partition
ROW_NUMBER()     OVER (PARTITION BY category ORDER BY price DESC)
RANK()           OVER (PARTITION BY category ORDER BY price DESC)
DENSE_RANK()     OVER (PARTITION BY category ORDER BY price DESC)

-- 4. Lag / Lead: previous or next row's value
LAG(price, 1)    OVER (PARTITION BY product_id ORDER BY order_date)

-- 5. Percentile / percent rank
PERCENT_RANK()   OVER (PARTITION BY category ORDER BY price)
```

`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE` only exist as window functions — they have no GROUP BY equivalent.

### Window without PARTITION BY — whole table as one window

```sql
SELECT
  product_name,
  stock_qty,
  SUM(stock_qty) OVER () AS grand_total
FROM products;
```

Empty `OVER ()` means "the entire result is the window." Every row sees the same grand total.

### Multiple windows in one SELECT

```sql
SELECT
  order_id,
  customer_id,
  amount,
  SUM(amount)   OVER (PARTITION BY customer_id) AS customer_total,
  AVG(amount)   OVER (PARTITION BY customer_id) AS customer_avg,
  RANK()        OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rank_in_customer
FROM orders;
```

Each window is independent. Reading complex window SQL becomes easy once you internalize "everything inside OVER is the per-row window definition."

### Naming windows with WINDOW clause

```sql
SELECT
  customer_id,
  order_id,
  amount,
  SUM(amount) OVER w AS customer_total,
  AVG(amount) OVER w AS customer_avg
FROM orders
WINDOW w AS (PARTITION BY customer_id);
```

Avoids repeating the partition clause. Optional but improves readability when many windows share a definition.

## Key Parameters

- **PARTITION BY column(s)**: defines the row groups; NULL goes in its own partition
- **ORDER BY**: required for `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, and running totals
- **Frame clause** (`ROWS BETWEEN`, `RANGE BETWEEN`): defaults to the entire partition unless ORDER BY is present (then it's cumulative)
- **Performance**: window functions trigger a sort/partition shuffle; large partition columns can be expensive

## When To Use

- **Per-row context**: "show the row plus its share / rank / total"
- **Ranking within groups**: "top-3 products by sales per category"
- **Running totals / cumulative metrics**: "month-over-month cumulative revenue per customer"
- **Lead/lag analysis**: "compare each order to the previous order from the same customer"
- **Avoiding fan-out in joins**: see [[Window Functions Across Grain]]
- Anti-pattern: window function when GROUP BY suffices — wasteful (window keeps rows you do not need)
- Anti-pattern: huge PARTITION BY on a billion-row table without filtering — expensive shuffle

## Connections

- Related: [[Functions in SQL Overview]] (window functions are one of the four function families), [[Group By]] (the aggregate alternative), [[Window Functions Across Grain]] (advanced use), [[Sum Avg Min Max]] (the underlying aggregates)
- Builds on: [[Joins Fundamentals]] (windows often replace problematic joins)
- Compare with: pandas `.transform()` (preserves rows, similar concept), pandas `.rolling()` (frame-based windows)
- Used by: cohort analysis (see [[Measures of Central Tendency]]), funnel analysis, top-N queries, time-series analytics

## My Notes

- Mental hook: GROUP BY = "give me one row per group." Window = "give me every row, with a column showing the group summary."
- Practice: [Pencere (window) Fonksiyonları](https://nextgen.workintech.com.tr/project/202/5?pid=7606) — compute share-of-category for every row.
- BigQuery tip: when a window function and an aggregate would compute the same thing, prefer the aggregate — it's faster.
- Interview tip: be ready to write a top-3-per-category query with `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`. It's the classic window-function interview problem.
