---
title: "Join Types"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/04-join-turleri]]"
tags:
  - sql
  - join
  - inner-join
  - left-join
  - right-join
  - full-outer-join
---

# Join Types

> One-line summary: INNER, LEFT, RIGHT, and FULL OUTER joins differ in which unmatched rows survive — INNER keeps only matches, LEFT keeps all left-side rows, RIGHT keeps all right-side rows, FULL keeps everything.

## Core Concept

Once you know how to write `A JOIN B ON A.x = B.y` ([[Joins Fundamentals]]), the next question is: **what happens to rows that have no match?** That is exactly what the join type controls.

Picking the right join type is the difference between "show me orders **with** customer info" (INNER) and "show me **all** orders, even those whose customer record was deleted" (LEFT). Pick the wrong type and your analysis silently drops or duplicates rows.

## How It Works

Imagine two tables:

```
customers           orders
─────────────       ─────────────
1  Alice            101 → cust 1
2  Bob              102 → cust 1
3  Carol            103 → cust 2
                    104 → cust 999  (orphaned: customer 999 does not exist)
```

### INNER JOIN — only matches

```sql
SELECT c.name, o.id
FROM customers c
INNER JOIN orders o ON c.id = o.cust_id;
```

Result: 3 rows. Alice's 2 orders + Bob's 1 order. Carol drops (no order). Order 104 drops (no customer).

INNER is the default — `JOIN` alone means INNER JOIN. Use when you only care about matched data.

### LEFT JOIN (LEFT OUTER JOIN) — keep all left rows

```sql
SELECT c.name, o.id
FROM customers c
LEFT JOIN orders o ON c.id = o.cust_id;
```

Result: 4 rows. Alice (2 orders), Bob (1 order), **Carol with NULL order** (kept even though she has no orders). Order 104 still drops (it is on the right side).

The "left" table is the one before `JOIN`; the "right" is after. LEFT JOIN keeps every left row, filling right-side columns with NULL when there is no match.

### RIGHT JOIN (RIGHT OUTER JOIN) — keep all right rows

```sql
SELECT c.name, o.id
FROM customers c
RIGHT JOIN orders o ON c.id = o.cust_id;
```

Result: 4 rows. Alice (2 orders), Bob (1 order), Carol drops, **order 104 with NULL customer** (kept).

RIGHT JOIN is mathematically equivalent to swapping the table order and using LEFT JOIN — and that is what most teams do. RIGHT JOIN is rarely seen in production code.

### FULL OUTER JOIN — keep all rows from both sides

```sql
SELECT c.name, o.id
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.cust_id;
```

Result: 5 rows. Everyone: Alice (2 orders), Bob (1 order), Carol with NULL, order 104 with NULL.

Use when you want a union of both sides, even when matches are missing.

### Visual summary

| Type | Left unmatched | Right unmatched | Use case |
|------|:--------------:|:---------------:|----------|
| INNER | dropped | dropped | "Both sides exist" |
| LEFT  | kept (NULL right) | dropped | "Keep all customers; show orders if any" |
| RIGHT | dropped | kept (NULL left) | (rare; use swapped LEFT) |
| FULL OUTER | kept | kept | "Show everything from both" |

### Anti-join: finding "with no match"

```sql
-- Customers with NO orders
SELECT c.*
FROM customers c
LEFT JOIN orders o ON c.id = o.cust_id
WHERE o.id IS NULL;
```

LEFT JOIN + WHERE right_table.key IS NULL is the canonical pattern for "find the missing." See [[Null Handling SQL]].

## Key Parameters

- **OUTER keyword is optional**: `LEFT JOIN` ≡ `LEFT OUTER JOIN`; same for RIGHT and FULL
- **NULL in join keys**: still dropped by INNER, kept on the outer side by LEFT/RIGHT/FULL — surprising at first
- **Performance**: INNER is usually fastest; FULL OUTER is slowest because both sides must be fully scanned
- **Engine support**: every modern SQL engine supports all four; some legacy MySQL versions lacked FULL OUTER

## When To Use

- **INNER**: "show me matched records" — most analytical queries
- **LEFT**: "show me all my customers and their orders, even if no orders yet" — preserving the driving entity
- **FULL OUTER**: rare; "audit which IDs appear in only one of these two sources"
- **RIGHT**: almost never; swap the tables and use LEFT
- Anti-pattern: LEFT JOIN when INNER would do — keeps unwanted NULL rows that pollute aggregates
- Anti-pattern: INNER JOIN when LEFT is needed — silently drops customers, undercounting metrics

## Connections

- Related: [[Joins Fundamentals]], [[Multiple Joins]] (mixing INNER and LEFT), [[Join Pitfalls Grain and Fan Out]] (wrong join type causes row explosions or drops), [[Null Handling SQL]] (outer joins introduce NULLs you must handle)
- Builds on: set theory — INNER = intersection; LEFT/RIGHT = inclusion; FULL = union
- Compare with: set operators `UNION`, `INTERSECT`, `EXCEPT` — alternatives when columns are identical on both sides
- Used by: every multi-table query; the choice of type is the most consequential design decision

## My Notes

- Mnemonic: "LEFT keeps the left." The direction in the keyword is the side that survives.
- Practice: [Greenweez Finans - JOIN](https://nextgen.workintech.com.tr/project/202/3?pid=7599) — switch the join type and watch row counts change.
- A row-count sanity check: after every JOIN, run `SELECT COUNT(*)` and compare to the expected base table count. INNER ≤ base; LEFT ≥ base only if matches multiply (fan-out — see [[Join Pitfalls Grain and Fan Out]]).
- Interview tip: when asked "what's the difference between INNER and LEFT JOIN?", answer with row-count behavior plus a concrete example, not just definitions.
