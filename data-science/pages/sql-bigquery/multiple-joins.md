---
title: "Multiple Joins"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/05-coklu-join-islemleri]]"
tags:
  - sql
  - join
  - multi-table
  - star-schema
---

# Multiple Joins

> One-line summary: Chaining several JOIN clauses combines three or more tables into a single result, reading them left-to-right and applying each ON condition against the accumulated working set.

## Core Concept

Real analytical questions almost never live in one table. "Show each purchase with the buyer's name and the product's category" pulls from three: purchases, buyers, products. SQL handles this by **chaining JOINs**: after the first JOIN produces a virtual two-table result, the next JOIN attaches a third table to it, and so on.

The mental model is a Lego assembly. You start with the central table (often a fact table — purchases, events, transactions) and snap on dimensional tables one at a time using their keys.

## How It Works

### Two joins, three tables

```sql
SELECT
  pu.id          AS purchase_id,
  b.name         AS buyer_name,
  pr.name        AS product_name,
  pu.quantity,
  pr.price
FROM purchases AS pu
JOIN buyers   AS b  ON pu.buyer_id   = b.id
JOIN products AS pr ON pu.product_id = pr.id;
```

Read top to bottom:
1. Start with `purchases` (aliased `pu`)
2. Attach `buyers` where the buyer_id matches
3. Attach `products` where the product_id matches

Result: one row per purchase, enriched with buyer and product details.

### Mixed join types

```sql
SELECT
  c.name,
  o.id           AS order_id,
  s.tracking_no
FROM customers AS c
LEFT JOIN orders   AS o ON c.id  = o.customer_id  -- keep customers with no orders
LEFT JOIN shipments AS s ON o.id = s.order_id;    -- keep orders with no shipment yet
```

Mixing INNER and LEFT is common. The driving entity (the one you must keep all rows of) leads with LEFT JOIN; lookups that always exist can use INNER. Be deliberate: a single misplaced INNER in a long chain can silently drop rows.

### Order matters (sometimes)

```sql
-- These two are equivalent — INNER JOINs are commutative
FROM a JOIN b ON a.x = b.x JOIN c ON b.y = c.y
FROM a JOIN c ON c.y = a.y_via_b JOIN b ON a.x = b.x

-- These are NOT equivalent — LEFT/RIGHT joins are NOT commutative
FROM a LEFT JOIN b ON ...    -- keeps all of a
FROM b LEFT JOIN a ON ...    -- keeps all of b
```

For INNER chains, reordering does not change the result (only the query plan). For outer joins, order is semantically meaningful.

### Star-schema flavor

```sql
SELECT
  d_date.year,
  d_date.month,
  d_product.category,
  d_store.region,
  SUM(f_sales.amount) AS revenue
FROM fact_sales         AS f_sales
JOIN dim_date           AS d_date    ON f_sales.date_id    = d_date.id
JOIN dim_product        AS d_product ON f_sales.product_id = d_product.id
JOIN dim_store          AS d_store   ON f_sales.store_id   = d_store.id
GROUP BY 1, 2, 3, 4;
```

The fact table is the center; dimensions hang off it. This is the canonical pattern in data warehouses ([[OLTP vs OLAP]]).

### Reading the chain visually

```
purchases ──join──> buyers
    │
    └──join──> products
```

Either order produces the same final width, but query planners may pick different physical plans.

## Key Parameters

- **Aliases mandatory**: with 3+ tables, unaliased queries become unreadable
- **ON conditions per JOIN**: each new JOIN has its own ON; do not put them all at the end
- **Self-joins**: a table joined to itself (`employees e1 JOIN employees e2 ON e1.manager_id = e2.id`) — aliases are required to distinguish the two roles
- **Join order optimization**: modern engines reorder INNER joins automatically; humans usually do not need to tune it

## When To Use

- Fact-table queries: combine sales/events with their dimensions (date, product, customer, store)
- Multi-level hierarchies: orders → order_items → products
- Self-joins for hierarchies in one table (employees → manager → manager's manager)
- Anti-pattern: 8+ JOINs in one query — usually a sign that an intermediate table or CTE should materialize a sub-result
- Anti-pattern: missing ON clause for one of the joins — produces a CROSS JOIN explosion

## Connections

- Related: [[Joins Fundamentals]], [[Join Types]] (mixing inner and outer in chains), [[Join Pitfalls Grain and Fan Out]] (multi-joins are where fan-out lurks), [[Joins with Group By]] (aggregating after multiple joins)
- Builds on: [[Entity Relationship Diagrams]] (the diagram shows the join path), [[Relational Data Model]]
- Compare with: denormalized wide tables (no joins needed, but storage cost and update anomalies); document databases (nested data, no joins)
- Used by: every BI dashboard query, every star-schema warehouse, every reporting layer

## My Notes

- Defensive habit: after each new JOIN, re-run `COUNT(*)` mentally — does the row count make sense? A 2x explosion after the third JOIN is the classic fan-out symptom.
- Practice: [Greenweez Finans - JOIN](https://nextgen.workintech.com.tr/project/202/3?pid=7599) — combine 3 finance tables and validate row counts at each step.
- BigQuery tip: large multi-joins (5+ tables, large fact tables) benefit from materializing intermediate CTEs or temp tables — keeps the planner from getting stuck.
- Interview tip: when given a multi-table question, sketch the ERD on paper first — it makes the JOIN order obvious.
