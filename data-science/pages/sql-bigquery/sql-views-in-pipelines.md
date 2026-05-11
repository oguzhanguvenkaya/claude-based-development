---
title: "SQL Views in Pipelines"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/04-gorunumler-view-ve-veri-hatlari]]"
tags:
  - sql
  - views
  - materialized-view
  - pipeline
  - bigquery
---

# SQL Views in Pipelines

> One-line summary: A view is a saved SELECT statement that behaves like a table when queried — used to expose reusable query logic to many consumers without duplicating SQL or paying repeated storage cost.

## Core Concept

Imagine a recipe card. The recipe is the SQL logic. Anyone with the card can produce the dish (the result set) every time, fresh, without having to know the steps. A **view** is exactly that: a saved SQL recipe, stored in the database, that any query can call as if it were a table.

Views unlock two things: **reuse** (write the cleaning/joining logic once, every dashboard calls the view) and **freshness** (the view always reflects the underlying tables — no staleness window). The tradeoff is **recompute cost**: every query against the view re-runs the underlying SQL.

## How It Works

### Creating a view

```sql
CREATE OR REPLACE VIEW analytics.active_customers AS
SELECT
  c.customer_id,
  c.name,
  c.email,
  COUNT(o.id) AS lifetime_orders,
  SUM(o.amount) AS lifetime_revenue
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE c.status = 'active'
GROUP BY c.customer_id, c.name, c.email;
```

Now any query can hit the view:

```sql
SELECT * FROM analytics.active_customers WHERE lifetime_revenue > 1000;
```

The engine substitutes the view definition under the hood: this is essentially `SELECT * FROM (CREATE VIEW body) WHERE ...`. Same plan, no storage of the result.

### Three flavors of view

| Type | Behavior | Storage | Freshness |
|------|----------|---------|-----------|
| **Standard view** | Re-runs SQL on every query | None (just the definition) | Always live |
| **Materialized view** | SQL precomputed, result cached | Stores result | Refreshed automatically or on-demand |
| **Table (CTAS)** | Full result persisted | Stores result | Stale until you recompute |

Materialized views are the "best of both" — fast like tables, fresh like views — but they have engine restrictions on what SQL is allowed.

### Chaining views — a pipeline in SQL

```sql
CREATE VIEW silver.clean_orders AS
SELECT order_id, SAFE_CAST(amount AS NUMERIC) AS amount, ...
FROM bronze.raw_orders
WHERE order_id IS NOT NULL;

CREATE VIEW silver.orders_with_customer AS
SELECT o.*, c.segment
FROM silver.clean_orders o
JOIN silver.dim_customers c ON o.customer_id = c.id;

CREATE VIEW gold.daily_revenue AS
SELECT DATE(order_date) AS day, segment, SUM(amount) AS revenue
FROM silver.orders_with_customer
GROUP BY day, segment;
```

When `gold.daily_revenue` is queried, the engine executes the entire chain: bronze → silver clean → silver enriched → gold aggregated. The result is always fresh; nothing is stored except the final query's output.

This is a **view-only pipeline**. It is simple to build and always live, but heavy queries can recompute the same intermediate logic many times. See [[Views vs Tables Tradeoffs]] for when to switch some steps to materialized tables.

### Materialized view example (BigQuery)

```sql
CREATE MATERIALIZED VIEW analytics.daily_revenue_mv AS
SELECT DATE(order_date) AS day, SUM(amount) AS revenue
FROM orders
GROUP BY day;
```

BigQuery automatically refreshes this when the base table changes, within seconds in most cases. Queries hit the precomputed result, paying only the lookup cost.

Restrictions in BigQuery materialized views:
- Only `SUM`, `COUNT`, `MIN`, `MAX`, `AVG`, `COUNT(DISTINCT)` allowed as aggregates
- No `ORDER BY`, no window functions, no self-joins
- Single base table or simple inner joins

If your view exceeds these, you cannot materialize it — use a scheduled query to refresh a regular table instead.

### When the SQL is more complex than allowed

```sql
-- Cannot be a materialized view (uses window functions)
-- So we use a scheduled INSERT INTO instead

INSERT INTO gold.daily_revenue_with_share
SELECT
  DATE(order_date) AS day,
  category,
  SUM(amount) AS revenue,
  SUM(amount) / SUM(SUM(amount)) OVER (PARTITION BY DATE(order_date)) AS share
FROM orders
GROUP BY day, category;
```

This combination — scheduled INSERT to maintain a table — is the manual version of what materialized views do automatically. See [[Bigquery Insert with Cast Workflow]].

## Key Parameters

- **`CREATE VIEW` vs `CREATE OR REPLACE VIEW`**: OR REPLACE updates without dropping
- **`MATERIALIZED VIEW`**: stores result, refreshed automatically; engine-restricted
- **`AUTHORIZED VIEW`** (BigQuery): a view that can query datasets the caller cannot access directly — useful for fine-grained data sharing
- **Permissions**: granting SELECT on a view does NOT grant access to the underlying tables; views are a permission boundary
- **Schema changes**: if an underlying table changes columns, dependent views may break — keep dependencies documented

## When To Use

- **Reusable cleaning / joining logic**: define once, every dashboard query benefits
- **Permission isolation**: expose only specific columns / rows to a downstream team via a view
- **Live freshness without ETL**: when the underlying table updates continuously and consumers need to see the latest
- **Chained pipelines for prototypes**: rapidly build a view-only stack to validate the logic, then materialize the expensive parts
- Anti-pattern: deeply chained views (10+ levels) — performance dies; either flatten or materialize intermediate layers
- Anti-pattern: using a view when consumers need point-in-time stability (e.g., financial reports) — they want a table snapshot, not a live view

## Connections

- Related: [[Data Pipeline Architecture]] (views are one tool in pipelines), [[Views vs Tables Tradeoffs]] (the storage/freshness/cost decision), [[Hybrid Table View Pipeline Pattern]] (mixing both), [[Create Update Delete]] (CTAS is the table counterpart)
- Builds on: [[Select Statement]], [[Joins Fundamentals]] — a view is just a saved SELECT
- Compare with: materialized views (precomputed), temp tables (session-scoped), CTEs (query-scoped)
- Used by: every modern data warehouse stack; dbt's "view" materialization is exactly this

## My Notes

- A useful default: build silver and gold layers as views first. Materialize only after you have measured slowness or cost. Easier to materialize than to un-materialize.
- Practice: rebuild a multi-CTE query as a chain of views in `analytics.*` and observe how queries against the final view perform.
- BigQuery tip: hover over a view in the Console — the right pane shows the SQL definition. Document the view's purpose in a comment at the top.
- Interview tip: when discussing pipeline architecture, distinguish "view (recompute each time)" from "table (precomputed, possibly stale)" from "materialized view (cached, auto-refresh)." Many candidates conflate them.
