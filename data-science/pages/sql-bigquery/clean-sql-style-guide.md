---
title: "Clean Sql Style Guide"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/06-temiz-kodun-onemi]]"
tags:
  - sql
  - code-style
  - readability
  - conventions
  - code-review
---

# Clean Sql Style Guide

> One-line summary: Conventions for naming, formatting, indentation, and commenting that make SQL queries readable by humans, reviewable by teammates, and debuggable months later — the same code-quality discipline software engineering uses, applied to SQL.

## Core Concept

SQL is read more often than it is written. A query that takes five minutes to write and lives in production for two years will be opened by future-you (or a teammate) dozens of times. Every minute spent on readability now saves an hour later.

There is no single official SQL style guide, but the conventions below are widely adopted across modern data teams using BigQuery, Snowflake, and dbt. They are taste-based but defensible, and a team converging on one style is more valuable than the exact choices.

## How It Works

### Naming

```sql
-- BAD
SELECT * FROM tbl1 t WHERE t.fld1 > 100;

-- GOOD
SELECT * FROM orders WHERE amount > 100;
```

Rules:
- **Tables, columns, aliases**: `snake_case`, lowercase, descriptive
- **No abbreviations** unless universally understood (`url`, `id`, `pk` are fine; `qty` over `quantity` is borderline; `usrcnt` is bad)
- **Plural for tables that hold many** (`customers`, `orders`), **singular for one-row config tables** (`schema_metadata`)
- **No reserved keywords** as column names (`order`, `select`, `from`, `date` — quote them if you must, but rename if possible)

### Indentation and line breaks

```sql
-- BAD: one long line
SELECT c.name, COUNT(o.id) AS order_count FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE c.signup_date >= '2025-01-01' GROUP BY c.name HAVING COUNT(o.id) > 5 ORDER BY order_count DESC;

-- GOOD: one clause per line, indented arguments
SELECT
  c.name,
  COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o
  ON c.id = o.customer_id
WHERE c.signup_date >= '2025-01-01'
GROUP BY c.name
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;
```

One clause keyword (SELECT, FROM, WHERE, GROUP BY) starts a new line. Long argument lists get one item per line. The shape of the query mirrors its structure.

### Keyword case

Two camps: UPPERCASE (traditional, scannable) or lowercase (modern, less noise). Pick one and stay consistent within a project — `sqlfluff` enforces either.

### Commenting

```sql
-- HIGH-VALUE: explains WHY
-- Excludes test accounts (created during QA, identified by email domain)
SELECT *
FROM customers
WHERE email NOT LIKE '%@test.example.com';

-- LOW-VALUE: explains WHAT (obvious from the code)
-- Get all customers
SELECT * FROM customers;
```

Comment the **why**, not the **what**. The code already tells you what it does; the comment should explain the business rule, the workaround, or the deliberate choice.

Use comments to:
- Document non-obvious filters ("excludes test data")
- Explain magic numbers ("90-day churn window per finance team")
- Mark TODOs and known limitations
- Link to ticket numbers or design docs

### Naming aliases

Single-letter aliases (`c`, `o`) work for 2–3 table queries; switch to 3–4 letter aliases (`cust`, `ord`) for larger joins. Avoid `x`/`y`/`z` entirely — they encode nothing.

### CTEs over deep nesting

```sql
-- BAD: deep nesting
SELECT *
FROM (SELECT *, (SELECT MAX(date) FROM events e WHERE e.user_id = u.id) AS last_seen
      FROM users u) sub
WHERE last_seen > CURRENT_DATE() - 30;

-- GOOD: CTE pipeline
WITH last_seen AS (
  SELECT u.id, MAX(e.date) AS last_event
  FROM users  u
  LEFT JOIN events e ON e.user_id = u.id
  GROUP BY u.id
)
SELECT *
FROM last_seen
WHERE last_event > DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);
```

See [[Common Table Expressions Cte]]. Past 2 nesting levels, refactor.

### Avoid SELECT *

```sql
-- BAD in production
SELECT * FROM orders;

-- GOOD
SELECT order_id, customer_id, amount, status FROM orders;
```

`SELECT *` breaks when the schema changes and bills for columns you do not use. See [[Select Statement]].

### Linting

Run automated checks:
- **`sqlfluff`** — the de facto SQL linter, dbt-aware
- **`sql-formatter`** — auto-formats SQL files
- **`prettier-sql`** — VS Code extension for live formatting

Lint config lives in your repo and runs on every PR. Style debates become "what does the linter say?" instead of arguments.

## Key Parameters

- **Consistency > perfection**: any consistent style beats a mix of styles
- **Code review**: PRs that change SQL should go through review; "did you read this in 30 seconds?" is a useful question
- **Tooling enforcement**: pre-commit hooks running `sqlfluff` catch deviations automatically
- **Team conventions**: write them down in a `STYLE.md`; new joiners need a single page to reference

## When To Use

- **Always**: even one-off exploratory queries benefit from light formatting
- **Especially**: production pipelines, dbt models, anything that lives beyond a few hours
- **Code review**: catching style drift is one of the cheapest review tasks
- Anti-pattern: arguing style without tooling — pick a linter and let it decide
- Anti-pattern: writing in a personal style that the team has not agreed to — creates merge conflicts and bus-factor

## Connections

- Related: [[Common Table Expressions Cte]] (the single biggest readability lever), [[Select Statement]] (avoiding SELECT *), [[Joins Fundamentals]] (alias conventions)
- Builds on: software engineering code quality principles applied to SQL
- Compare with: PEP 8 for Python, gofmt for Go, prettier for JavaScript — same idea, different language
- Used by: every mature data team; dbt's culture is built around clean SQL practices

## My Notes

- Style ROI compounds: a clean style that a team adopts saves 10–20% of every analyst's reading time, every week, for the life of the codebase.
- Practice: run `sqlfluff lint your_query.sql` on one of your recent queries — fix the warnings and watch your style mature.
- BigQuery tip: in the Console, Cmd/Ctrl + Shift + F auto-formats the current query. Use it every time before saving.
- Interview tip: bring up `sqlfluff` or a linter when discussing code quality in data interviews — many candidates do not, so it differentiates.
