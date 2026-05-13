---
title: "Data Exploration and Cleaning Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/03-veri-kesfi-ve-temizlenmesi]]"
tags:
  - data-analysis
  - google-sheets
  - eda
  - data-cleaning
  - data-quality
---

# Data Exploration and Cleaning Sheets

> One-line summary: The first hands-on step after importing data — survey shape, spot anomalies, fix types, normalize text, deduplicate, and handle missing values — all using Sheets functions like TRIM, UPPER, COUNTA, and conditional formatting.

## Core Concept

Imported data is almost never analysis-ready. Mixed cases ("New York" vs "new york"), trailing spaces ("USA " vs "USA"), inconsistent date formats, duplicate rows, columns stored as text that should be numeric — every dataset arrives with at least a few of these problems. **Exploration** finds them; **cleaning** fixes them.

Skipping these steps is the single most common source of misleading analytical results. A pivot table that groups by city will show "New York" and "new york" as separate cities. A SUM column that includes "$1,200" as text will silently exclude it.

## How It Works

### Exploration techniques in Sheets

| Check | Sheets formula / action | What it tells you |
|-------|------------------------|-------------------|
| **Row count** | `=COUNTA(A:A)` | Total non-empty cells in column A |
| **Distinct values** | `=COUNTUNIQUE(A:A)` | Number of unique cities, products, etc. |
| **Missing values** | `=COUNTBLANK(A:A)` | NULL / empty cells per column |
| **Top values** | sort + scan, or `=COUNTIF(...)` | Most frequent categories |
| **Range** | `=MIN(B:B)`, `=MAX(B:B)` | Detect outliers and sentinel values |
| **Type sniff** | `=ISNUMBER(B1)`, `=ISTEXT(B1)` | Catches numbers stored as text |
| **Visual scan** | sort by column, browse top + bottom 20 | Catches obvious anomalies |

A 10-minute exploration pass catches 80% of issues before they corrupt downstream analysis.

### Common cleaning operations

```
=TRIM(A1)              — remove leading/trailing whitespace
=UPPER(A1)             — normalize to uppercase
=LOWER(A1)             — normalize to lowercase
=PROPER(A1)            — title case ("alice WANG" → "Alice Wang")
=SUBSTITUTE(A1, "$", "")  — strip currency symbols
=VALUE(A1)             — convert text-looking numbers to actual numbers
=IFERROR(A1/B1, 0)     — gracefully handle division errors
=CLEAN(A1)             — remove non-printable characters (line breaks, tabs)
=REGEXREPLACE(A1, "\s+", " ")  — collapse multiple spaces into single
```

These are the spreadsheet counterparts of [[String Cleaning Replace and Case]] in SQL.

### Handling missing values

| Strategy | When |
|----------|------|
| **Filter out blank rows** | When missingness is a small fraction (<5%) |
| **Fill with default** | When the missing value has a known sensible default ("Unknown" for category, 0 for count) |
| **Fill with mean/median** | For numeric columns where the average represents a reasonable guess |
| **Leave as blank** | When downstream analysis ignores blanks naturally (SUM, AVG do so) |

In Sheets, "blank" and "empty string" both behave like NULL in formulas but display differently. The `=ISBLANK(A1)` check returns TRUE only for truly empty cells, not for cells with empty strings — a subtle gotcha. See [[Null Handling SQL]] for the conceptual parallel.

### Deduplication

```
Data → Data cleanup → Remove duplicates
```

Pick the columns that define uniqueness — usually the primary identifier (customer_id, email). Sheets removes rows where all chosen columns match.

For more control, the `=UNIQUE(A:C)` formula returns the deduplicated set as a new range, leaving the original intact.

### Validation with conditional formatting

```
Format → Conditional formatting → Custom formula
```

Useful rules:
- Highlight cells where age < 0 (impossible)
- Highlight duplicate values (`=COUNTIF(A:A, A1) > 1`)
- Highlight blanks in required columns (`=ISBLANK(A1)`)
- Highlight outliers (`=ABS(A1 - AVERAGE(A:A)) > 3 * STDEV(A:A)`)

Color-coded validation makes anomalies pop visually — far faster than manually scanning columns.

### Detecting and fixing date format issues

Sheets often imports dates as text, especially in non-ISO formats:

```
=DATEVALUE(A1)         — converts "12/31/2024" or "31 Dec 2024" to a proper date serial
=TEXT(A1, "yyyy-mm-dd") — formats a date as ISO string
```

Always normalize dates to ISO (yyyy-mm-dd) early. Downstream pivot tables and charts treat them consistently.

### Splitting and combining columns

```
Data → Split text to columns        — splits one column into many by delimiter
=A1 & " " & B1                       — concatenates two columns
=SPLIT(A1, " ")                      — formula version of Split-to-Columns
```

The Sheets counterpart of [[String Concatenation Concat]].

## Key Parameters

- **Cleaning before analysis**: cleaning costs minutes; the bugs from unclean data cost hours
- **Reproducibility**: cleaning steps should be re-runnable — use formula columns instead of manual edits where possible
- **Documentation**: comment on cleaning decisions ("removed 47 test rows from 2025-Q4 dump")
- **Preserve raw**: keep the original imported sheet as a snapshot; do cleaning in a copy

## When To Use

- **Immediately after import**: the highest-ROI 10–30 minutes of any analysis
- **Before joining datasets**: case and whitespace mismatches cause 90% of low-match-rate complaints
- **Before computing aggregates**: bad rows or sentinel values (-1, 9999, "N/A") corrupt averages
- **When inheriting an analysis**: never trust the previous analyst's cleaning — re-explore
- Anti-pattern: cleaning manually (typing fixes) instead of using formulas — not reproducible
- Anti-pattern: skipping exploration "because the data looks fine at first glance" — first glance lies

## Connections

- Related: [[Data Analysis Workflow]] (steps 4 + 5), [[Importing Data to Sheets]] (previous step), [[Lookup Functions Sheets]] (enrichment after cleaning), [[Filter Query Unique Sheets]] (filtering relies on clean data)
- Builds on: spreadsheet formula fluency
- Compare with: [[String Cleaning Replace and Case]] (SQL counterpart), pandas `.dropna()`, `.fillna()`, `.str.strip()`
- Used by: every analysis; the foundation for everything in [[Pivot Tables Sheets]] and beyond

## My Notes

- The 10-minute exploration pass is the highest-ROI habit in spreadsheet analysis. Most "data is wrong" complaints trace to a skipped exploration.
- Practice: [Netflix Reklam Kampanya Analizi I](https://nextgen.workintech.com.tr/project/201/2?pid=7266) — explore the campaign data and document every cleaning decision before computing metrics.
- Useful pattern: dedicate one Sheet tab to "Cleaning log" — append a row each time you apply a fix. Future you will thank you.
- Interview tip: when asked about a tricky data problem, mention specific cleaning checks (case normalization, type conversion, duplicate detection) — shows hands-on awareness.
