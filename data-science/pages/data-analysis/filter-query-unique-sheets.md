---
title: "Filter Query Unique Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/06-veriyi-filter-ile-filtrelemek]]"
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/07-veriyi-query-ile-filtrelemek]]"
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/08-veriyi-unique-ile-filtrelemek]]"
tags:
  - data-analysis
  - google-sheets
  - filter
  - query
  - unique
---

# Filter Query Unique Sheets

> One-line summary: Three Google Sheets functions that subset data — FILTER for simple row selection by condition, QUERY for SQL-like multi-clause queries, UNIQUE for deduplication — together they cover almost every "show me only the rows I care about" question.

## Core Concept

Imported data sets are bigger than the question. A 100,000-row CRM dump contains 200 customers from Paris in 2024 — the ones the marketing lead actually asked about. **Filtering** narrows the data; **deduplication** removes noise; **querying** lets you combine filtering with sorting and aggregation in one expression.

These three functions are the spreadsheet equivalents of [[Filtering Where]] (FILTER), full SQL via syntax (QUERY), and [[Distinct and Deduplication]] (UNIQUE).

## How It Works

### FILTER — conditional row selection

```sheets
=FILTER(range, condition1, [condition2], ...)
```

```sheets
-- Customers from Paris
=FILTER(A2:E1000, B2:B1000 = "Paris")

-- Customers from Paris with revenue > $1000
=FILTER(A2:E1000, B2:B1000 = "Paris", D2:D1000 > 1000)

-- Customers from any city in a list
=FILTER(A2:E1000, REGEXMATCH(B2:B1000, "^(Paris|London|Berlin)$"))
```

FILTER returns the matching rows as a live range. Edit the source, the filter result updates instantly. No buttons, no menu — just a formula.

### QUERY — SQL-like power in one formula

```sheets
=QUERY(range, "sql_string", [headers])
```

```sheets
-- 2024 Paris customers, first 100 rows
=QUERY(Customers!A:F, "SELECT * WHERE B = 'Paris' AND YEAR(D) = 2024 LIMIT 100")

-- Total revenue per city, sorted descending
=QUERY(Customers!A:F, "SELECT B, SUM(E) WHERE D >= date '2024-01-01' GROUP BY B ORDER BY SUM(E) DESC")

-- Specific columns with calculated total
=QUERY(Customers!A:F, "SELECT A, B, E, E * 1.18 LABEL E * 1.18 'with_tax'")
```

QUERY's syntax is a subset of SQL (the Google Visualization API query language, very close to SQL). Supports:
- `SELECT col1, col2, calculated_expr`
- `WHERE` with AND / OR
- `GROUP BY` with `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`
- `ORDER BY ... ASC / DESC`
- `LIMIT n`
- `LABEL` to rename headers
- `FORMAT` for date / number formatting

Column references use **letters** (A, B, C) not column names. This is the awkward part; comment your QUERY formulas to explain which letter means what.

### UNIQUE — deduplication

```sheets
=UNIQUE(range)
```

```sheets
-- Distinct list of cities
=UNIQUE(B2:B1000)

-- Distinct (city, country) pairs
=UNIQUE(B2:C1000)

-- Distinct + sorted
=SORT(UNIQUE(B2:B1000))
```

UNIQUE returns the deduplicated set as a new range. Same input row appearing 50 times → one row out.

The Sheets equivalent of SQL [[Distinct and Deduplication]]. Like SQL DISTINCT, UNIQUE on multiple columns considers the **combination** unique, not each column independently.

### Combining them — common patterns

**Filter then dedupe:**
```sheets
=UNIQUE(FILTER(B2:B1000, C2:C1000 = "active"))
-- Distinct list of cities among active customers
```

**Query as a one-liner replacement for FILTER + UNIQUE + SUM:**
```sheets
=QUERY(A:E, "SELECT B, COUNT(A) WHERE C = 'active' GROUP BY B")
-- Active customer count per city
```

QUERY can replace most multi-formula chains with a single expression. Tradeoff: QUERY's SQL syntax requires learning; FILTER and UNIQUE are pure spreadsheet logic.

### When to use which

| Task | Best tool |
|------|-----------|
| Simple row selection by one or two conditions | FILTER |
| Distinct list of values | UNIQUE |
| Multi-clause analysis (filter + sort + group + limit) | QUERY |
| Selecting specific columns from a wide source | QUERY |
| Live-linked filtered subset | FILTER (live updates with source) |
| Need SQL fluency in Sheets | QUERY |

### Limitations

- **FILTER**: only returns rows; cannot reshape columns
- **QUERY**: subset of SQL — no JOINs, no subqueries, no window functions; for those, use BigQuery
- **UNIQUE**: scales poorly past 50k rows; consider Pivot Table or SQL
- **All three**: results are read-only formula outputs; editing requires changing the source

### From Sheets to SQL — concept mapping

| Sheets | SQL counterpart |
|--------|-----------------|
| `FILTER(range, cond)` | `SELECT * FROM table WHERE cond` |
| `UNIQUE(col)` | `SELECT DISTINCT col FROM table` |
| `QUERY(range, "SELECT ... WHERE ...")` | nearly full SQL — see [[Select Statement]], [[Filtering Where]], [[Group By]] |

Mastering Sheets QUERY makes the transition to BigQuery feel like learning dialect differences, not a whole new language.

## Key Parameters

- **Live evaluation**: all three functions recompute when source data changes — heavy formulas can slow the sheet
- **Column references**: QUERY uses letters; FILTER and UNIQUE use range syntax — pick consistent style per sheet
- **Whitespace**: invisible trailing spaces will break equality checks; combine with `TRIM` from [[Data Exploration and Cleaning Sheets]]
- **Headers**: pass `1` as third arg of QUERY to declare the first row as headers (recommended)

## When To Use

- **Quick analytical drill-downs**: "show me X under condition Y" — FILTER
- **Reference / picklist generation**: distinct values for dropdowns or downstream lookups — UNIQUE
- **One-shot complex analyses**: GROUP BY equivalent without leaving Sheets — QUERY
- Anti-pattern: chaining 5 levels of FILTER + UNIQUE + SORT when one QUERY would suffice
- Anti-pattern: QUERY on 100,000 rows for repeated dashboard updates — move to BigQuery

## Connections

- Related: [[Lookup Functions Sheets]] (enrichment), [[Pivot Tables Sheets]] (alternative for grouping), [[Data Exploration and Cleaning Sheets]] (clean before filter)
- Builds on: spreadsheet formula fluency, basic boolean logic
- Compare with: [[Filtering Where]] (WHERE), [[Distinct and Deduplication]] (DISTINCT), [[Group By]] (QUERY's GROUP BY clause) — SQL counterparts
- Used by: every Sheets-based ad-hoc analysis

## My Notes

- FILTER + UNIQUE are the bread and butter of Sheets analysis. QUERY is the secret weapon — once you know it, half of your Sheets formulas become one-liners.
- Practice: [Netflix Reklam Kampanya Analizi I](https://nextgen.workintech.com.tr/project/201/2?pid=7266) — extract campaign-specific customer lists with FILTER, find distinct channels with UNIQUE, build a per-channel summary with QUERY.
- QUERY's column-letter referencing is its biggest weakness — document every QUERY formula with a comment naming the columns by what they represent.
- Interview tip: explaining the FILTER / QUERY / UNIQUE / Pivot decision tree signals that you treat Sheets as a serious analysis tool, not just data entry.
