---
title: "Where vs Having"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/06-where-ve-having-ile-filtreleme]]"
tags:
  - sql
  - where
  - having
  - filtering
  - execution-order
---

# Where vs Having

> One-line summary: WHERE filters individual rows before grouping; HAVING filters aggregated groups after grouping. Choosing the right clause depends on whether the predicate references a row-level column or an aggregate value.

## Core Concept

Both clauses filter — they keep some rows and drop others. The difference is **when** they run in the query pipeline and **what they can reference**.

WHERE filters rows fed into GROUP BY. HAVING filters the groups GROUP BY produces. That single ordering rule explains every behavioral difference between them and every "why did I get this error" moment.

## How It Works

### Execution pipeline (recap)

```
1. FROM        → read raw rows
2. WHERE       → keep matching rows  ← BEFORE GROUP BY
3. GROUP BY    → bucket remaining rows
4. HAVING      → keep matching groups ← AFTER GROUP BY
5. SELECT      → project aggregates
6. ORDER BY    → sort
```

### Example: WHERE before GROUP BY

```sql
-- "How many orders did each customer place in January?"
SELECT
  customer_id,
  COUNT(*) AS orders_in_january
FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31'  -- filters individual rows
GROUP BY customer_id;
```

`WHERE` narrows the input to January rows. Every customer with a January order shows up, even if they have only 1.

### Example: HAVING after GROUP BY

```sql
-- "Which customers spent over $1000 total?"
SELECT
  customer_id,
  SUM(amount) AS lifetime_spend
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;   -- filters aggregated groups
```

`HAVING` filters on `SUM(amount)`, which only exists after grouping. You cannot put `SUM(amount) > 1000` in WHERE — at WHERE time, SUM has not been computed yet.

### Both together — the common idiom

```sql
-- "Of orders from active customers, which products had more than 10 sales last month?"
SELECT
  product_id,
  COUNT(*) AS sales_count
FROM orders
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)  -- row filter
  AND customer_status = 'active'                                -- row filter
GROUP BY product_id
HAVING COUNT(*) > 10;                                           -- group filter
```

Read this as: "first reduce to last-month rows from active customers, then group by product, then keep groups whose count is over 10."

### Why not just use HAVING for everything?

You technically could — HAVING is allowed to reference grouping columns too. But it is wasteful: WHERE filters before grouping (cheap), HAVING filters after (expensive). Always filter as early as possible.

```sql
-- Wasteful — runs the aggregate on every row, then drops the group
SELECT customer_id, COUNT(*) FROM orders
GROUP BY customer_id
HAVING customer_id = 42;

-- Correct — drops everything but customer 42 before aggregating
SELECT customer_id, COUNT(*) FROM orders
WHERE customer_id = 42
GROUP BY customer_id;
```

## Key Parameters

- **WHERE references**: only raw columns and computed expressions; cannot reference aggregates or SELECT aliases
- **HAVING references**: grouping columns AND aggregates; can use SELECT aliases in some engines
- **Performance**: WHERE almost always cheaper than HAVING for equivalent filters
- **Cost in BigQuery**: WHERE on a partitioned/clustered column prunes scanned data; HAVING does not

## When To Use

- **WHERE**: filtering by raw row attributes — date ranges, status flags, IDs, categories
- **HAVING**: filtering by aggregate results — total over X, average above Y, count below Z
- **Combine**: WHERE to narrow input, HAVING to refine output
- Anti-pattern: putting row-level filters in HAVING — works but slower
- Anti-pattern: trying to reference an aggregate in WHERE — error; rewrite as a subquery or move to HAVING

## Connections

- Related: [[Filtering Where]] (deep dive on WHERE syntax), [[Group By]] (HAVING only makes sense with GROUP BY), [[Sum Avg Min Max]] (typical HAVING predicates)
- Builds on: query execution order, [[Conditional Expressions SQL]]
- Compare with: subqueries / CTEs — "filter the aggregated result" can also be done in an outer query (`WHERE` of a subquery)
- Used by: every analytical query that filters on aggregated metrics

## My Notes

- Mnemonic: **"WHERE = where in the table"** (which rows), **"HAVING = having which property"** (which groups).
- Practice: [Circle Stok/Ürün Takipleri - 2](https://nextgen.workintech.com.tr/project/202/2?pid=7595) — "show products with stock below threshold" (WHERE) vs "show products whose average stock is below threshold" (HAVING).
- Interview question: "Why does `WHERE COUNT(*) > 10` error?" Answer: aggregates do not exist at WHERE time — execution order.
- Sometimes a CTE is cleaner: compute the aggregate in one CTE, filter in the outer query — see future lessons on CTEs.
