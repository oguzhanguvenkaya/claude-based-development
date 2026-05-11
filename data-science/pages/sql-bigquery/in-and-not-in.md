---
title: "In and Not In"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/10-in-ve-not-in-kullanimi]]"
tags:
  - sql
  - in-operator
  - set-membership
  - filtering
---

# In and Not In

> One-line summary: The IN operator tests whether a column's value belongs to a given list (or subquery result), replacing long OR chains with a cleaner set-membership check.

## Core Concept

When you have a column and a finite set of acceptable values, you can write the filter with OR:

```sql
WHERE city = 'New York' OR city = 'Boston' OR city = 'Chicago'
```

This works but reads poorly and breaks the moment the list grows. `IN` is the cleaner form:

```sql
WHERE city IN ('New York', 'Boston', 'Chicago')
```

Same result, far easier to scan and modify. `NOT IN` does the opposite — excludes any value in the list.

## How It Works

### Basic IN with a literal list

```sql
SELECT * FROM customers
WHERE city IN ('New York', 'Boston', 'Chicago');
```

### NOT IN

```sql
-- Exclude specific cities
SELECT * FROM customers
WHERE city NOT IN ('Detroit', 'Cleveland');
```

### IN with a subquery

```sql
-- Customers who have placed at least one order
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);
```

The subquery returns a set of `customer_id` values; the outer query keeps rows whose ID appears in that set. This is one of the most useful patterns in SQL.

### IN with numbers, dates, mixed types

```sql
WHERE order_status IN ('paid', 'shipped', 'delivered')
WHERE rating IN (4, 5)
WHERE event_date IN (DATE '2025-01-01', DATE '2025-07-04', DATE '2025-12-25')
```

## Key Parameters

- **List length**: most engines handle lists of thousands of values without issue, but very large lists (10k+) start to slow queries
- **Type matching**: the values in the list must match the column's data type — comparing strings to integers produces unexpected results in some engines
- **NULL trap**: `NOT IN` returns NULL (and excludes the row) if the list contains a NULL — almost never what you want. Use `NOT EXISTS` or pre-filter NULLs out of the list.
- **Subquery vs join**: `IN (subquery)` is often equivalent to a semi-join; the optimizer may rewrite it. Performance depends on engine and indexes.

### NULL in NOT IN — the classic gotcha

```sql
-- If 'allowed_cities' contains a NULL:
WHERE city NOT IN ('New York', NULL, 'Boston')
-- This returns ZERO rows. Always.
```

Reason: `city != NULL` is NULL (three-valued logic), and the engine treats NULL as "exclude." See [[Null Handling SQL]].

## When To Use

- **Replace OR chains** of more than 2 equalities — cleaner, easier to maintain
- **Filter by an external list** — e.g., "show me sales from these 50 stores"
- **Subquery membership** — "customers who appear in this other table"
- Anti-pattern: hard-coding business-critical lists inline. Maintain them as a small lookup table and `IN (SELECT id FROM allowed_list)`.
- Anti-pattern: using NOT IN with a subquery that might return NULL — use NOT EXISTS instead

```sql
-- Safer than NOT IN when nulls are possible
SELECT * FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM blocked_customers b WHERE b.customer_id = c.customer_id
);
```

## Connections

- Related: [[Filtering Where]] (IN is a comparison operator inside WHERE), [[Pattern Matching SQL]] (LIKE for shapes, IN for finite lists)
- Builds on: set theory — IN is set membership (`x ∈ S`)
- Compare with: `EXISTS` / `NOT EXISTS` — see [[Nested Subqueries]] (returns true if subquery has any rows; safer for NULL handling)
- Used by: every filter that targets a finite list of values; see [[Join vs Subquery]] for picking IN vs JOIN

## My Notes

- The `NOT IN` + NULL trap has caused more silent SQL bugs than I can count. When in doubt, use `NOT EXISTS`.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), filter campaigns to a known target list of cities or segments using IN.
- BigQuery tip: `IN UNNEST(@array)` is the pattern for parameterized queries — lets you pass an array from a script instead of hard-coding values.
- Interview tip: be ready to explain why `NOT IN` with NULL returns no rows — it tests both your SQL skill and your understanding of three-valued logic.
