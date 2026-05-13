---
title: "Lookup Functions Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/04-lookup-fonksiyonlari]]"
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/09-lookup-kullanarak-veri-temizleme]]"
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/10-index-match-ile-analiz]]"
tags:
  - data-analysis
  - google-sheets
  - vlookup
  - xlookup
  - index-match
---

# Lookup Functions Sheets

> One-line summary: VLOOKUP, XLOOKUP, and INDEX-MATCH let Google Sheets cells fetch values from another table by matching a key — the spreadsheet equivalent of a SQL JOIN — with XLOOKUP being the modern, most flexible option and INDEX-MATCH the legacy workaround for VLOOKUP's limitations.

## Core Concept

Spreadsheet data often lives in multiple sheets: a customer list, a campaign list, a product catalog. To answer "which campaign did this customer come from?", you must **look up** the campaign ID in the customer's row in the campaign table — the spreadsheet equivalent of joining two tables on a key.

Sheets provides three flavors of lookup, each from a different era of spreadsheet evolution:

- **VLOOKUP** (Vertical Lookup, 1985 / Excel original): the classic, with rigid constraints
- **INDEX-MATCH** (mid-90s): the expert workaround that bypasses VLOOKUP's limits
- **XLOOKUP** (2019 / modernized): the modern unified replacement; the right default

Knowing all three matters because legacy sheets are full of VLOOKUP, and INDEX-MATCH still appears in many companies' templates.

## How It Works

### VLOOKUP — the classic

```
=VLOOKUP(search_key, range, column_index, [is_sorted])
```

- `search_key`: the value to find (a customer ID)
- `range`: the lookup table (must include the key column on its **leftmost** side)
- `column_index`: which column number (1-based) to return from the matched row
- `is_sorted`: FALSE for exact match (always use FALSE for analysis)

```sheets
=VLOOKUP(A2, Campaigns!A:D, 4, FALSE)
```

This looks for the value in `A2` in the leftmost column of `Campaigns!A:D` and returns the value from the 4th column.

### VLOOKUP limitations (and why it's not the default anymore)

| Limit | Problem |
|-------|---------|
| **Key must be leftmost column** | If the key is in column C of the source, you can't VLOOKUP — must restructure |
| **Column number is hard-coded** | Insert a column in the source, your formula returns wrong data |
| **No leftward lookup** | Cannot return a column to the left of the key |
| **No multi-criteria match** | One key column only; multi-key matches require concatenation hacks |
| **Returns first match only** | No control over which match wins when duplicates exist |

These limits drove generations of analysts to INDEX-MATCH and now XLOOKUP.

### XLOOKUP — the modern default

```
=XLOOKUP(search_key, lookup_range, return_range, [if_not_found], [match_mode], [search_mode])
```

```sheets
=XLOOKUP(A2, Campaigns!A:A, Campaigns!D:D, "no campaign")
```

What XLOOKUP fixes:
- **Lookup_range and return_range are independent**: key can be anywhere, return column can be anywhere
- **Bidirectional**: search left or right of the key
- **Custom not-found value**: "no campaign" instead of `#N/A`
- **Match modes**: exact, exact-or-next-smaller, wildcard, etc.
- **Search modes**: first match, last match, binary search

XLOOKUP is the right default in 2026. Use it unless the sheet inherits VLOOKUP / INDEX-MATCH and consistency demands matching the existing style.

### INDEX-MATCH — the bridge

Before XLOOKUP, expert analysts used `INDEX` + `MATCH` to dodge VLOOKUP's limits:

```sheets
=INDEX(Campaigns!D:D, MATCH(A2, Campaigns!A:A, 0))
```

- `MATCH(A2, Campaigns!A:A, 0)` finds the row number where `A2` appears in column A (0 = exact match)
- `INDEX(Campaigns!D:D, row_number)` returns the value from column D at that row

INDEX-MATCH is essentially "look up the row, then read the column" — two separate operations composed. The flexibility comes from the separation.

Why it still appears: old sheets, Excel versions before 2019 that lacked XLOOKUP, analysts trained pre-XLOOKUP.

### Side-by-side: same task, three ways

Goal: find the acquisition channel for customer ID 12345.

```sheets
-- VLOOKUP: requires id in leftmost column
=VLOOKUP(12345, Customers!A:E, 5, FALSE)

-- INDEX-MATCH: works regardless of column order
=INDEX(Customers!E:E, MATCH(12345, Customers!A:A, 0))

-- XLOOKUP: cleanest
=XLOOKUP(12345, Customers!A:A, Customers!E:E)
```

All three return the same answer. XLOOKUP is the most readable.

### Data enrichment via lookups

The typical use case: enrich a row with related data.

```sheets
Customer | Email          | City        | Region (looked up)
---------|----------------|-------------|--------------------
Alice    | alice@x.com    | New York    | =XLOOKUP(C2, Regions!A:A, Regions!B:B)
Bob      | bob@x.com      | Boston      | =XLOOKUP(C3, Regions!A:A, Regions!B:B)
```

The Region column is computed from the City via a lookup against a Regions table. This is the [[Joins Fundamentals]] concept applied to spreadsheets.

### Handling missing matches

```sheets
=XLOOKUP(A2, Source!A:A, Source!B:B, "Unknown")
=IFERROR(VLOOKUP(A2, Source!A:E, 5, FALSE), "Unknown")
```

XLOOKUP has built-in not-found handling. VLOOKUP requires wrapping with IFERROR. Always provide a fallback — silent `#N/A` errors are the spreadsheet equivalent of unhandled NULL.

## Key Parameters

- **Exact match (FALSE / 0)**: always use this for analytical lookups — fuzzy match (TRUE) is for sorted ranges and rarely what you want
- **Volatility**: lookup formulas recompute when their sheet changes; sheets with thousands of XLOOKUPs slow down — consider Pivot Tables or Connected Sheets for large data
- **Reference style**: use absolute references (`$A$2:$E$1000`) when copying down a formula column to keep the lookup range fixed
- **Column index reliance**: VLOOKUP breaks when columns are inserted in the source; INDEX-MATCH and XLOOKUP do not

## When To Use

- **Enriching one sheet with data from another** — adding region from a city lookup, product details from a SKU
- **Reconciling two datasets** — matching IDs across systems
- **Building dashboards that compose data from multiple sources**
- Anti-pattern: VLOOKUP in new sheets — XLOOKUP is strictly better; the only reason to use VLOOKUP is matching an existing convention
- Anti-pattern: lookup formulas in a sheet with > 50,000 rows — performance dies; move to Pivot or BigQuery

## Connections

- Related: [[Filter Query Unique Sheets]] (filtering after enrichment), [[Pivot Tables Sheets]] (summarizing enriched data), [[Data Analysis Workflow]]
- Builds on: [[Importing Data to Sheets]], [[Data Exploration and Cleaning Sheets]]
- Compare with: [[Joins Fundamentals]] — XLOOKUP ≈ LEFT JOIN with one-to-one keys; the spreadsheet analog
- Used by: virtually every multi-sheet analysis

## My Notes

- Personal default: XLOOKUP for new work; only fall back to VLOOKUP or INDEX-MATCH to match existing convention.
- Practice: [Netflix Reklam Kampanya Analizi II](https://nextgen.workintech.com.tr/project/201/2?pid=7267) — enrich customer data with campaign info using all three lookup variants; compare readability.
- Useful debugging tip: when a lookup returns `#N/A`, copy-paste both keys into a `=EXACT(A1, B1)` formula. Reveals invisible whitespace or case differences.
- Interview tip: when discussing lookups, mention XLOOKUP first and INDEX-MATCH as fallback — shows you know the modern toolkit.
