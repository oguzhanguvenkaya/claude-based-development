---
title: "Pivot Tables Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/05-pivot-tablo]]"
tags:
  - data-analysis
  - google-sheets
  - pivot-table
  - aggregation
  - summarization
---

# Pivot Tables Sheets

> One-line summary: A pivot table collapses thousands of rows into a configurable summary grid — drag a column into rows, another into columns, an aggregate into values, and Sheets computes the cross-tab interactively, no formulas required.

## Core Concept

For raw data, "what is the total revenue per region per month?" is a heavy SUMIF + UNIQUE + manual layout exercise. **Pivot tables** make this trivial: drag fields into row / column / value zones, and Sheets builds the cross-tabulated summary automatically. It's the highest-leverage feature in any spreadsheet tool.

Pivot tables are the spreadsheet analog of SQL `GROUP BY`. Once you understand them in Sheets, [[Group By]] becomes intuitive: same operation, code-driven syntax instead of drag-and-drop.

## How It Works

### Creating a pivot table

```
Insert → Pivot table → choose data range → New sheet
```

A new sheet appears with the pivot editor in the right pane. Four configurable zones:

| Zone | What goes here | Example |
|------|----------------|---------|
| **Rows** | Columns whose values become row labels | Region, Product Category |
| **Columns** | Columns whose values become column headers | Month, Channel |
| **Values** | Numeric columns aggregated for each cell | Revenue (SUM), Orders (COUNT) |
| **Filters** | Columns used to restrict the source rows | Status = "active" |

Drag the relevant columns from the panel into each zone. The grid updates live.

### A concrete example

Raw data:
```
order_id | region | month    | revenue
---------|--------|----------|--------
1001     | North  | 2026-01  | 1500
1002     | South  | 2026-01  | 900
1003     | North  | 2026-02  | 2100
1004     | East   | 2026-02  | 750
... (10,000 more rows)
```

Configure pivot:
- Rows: region
- Columns: month
- Values: SUM of revenue

Result:
```
            | 2026-01 | 2026-02 | 2026-03 | Total
North       | 18,500  | 21,000  | 23,400  | 62,900
South       | 9,200   | 11,400  | 12,000  | 32,600
East        | 7,500   | 8,100   | 9,300   | 24,900
West        | 12,000  | 13,200  | 14,500  | 39,700
Grand Total | 47,200  | 53,700  | 59,200  | 160,100
```

What previously took 30 minutes of SUMIF formulas takes 30 seconds.

### Aggregation functions in Values

| Aggregate | When |
|-----------|------|
| **SUM** | Totals (revenue, units, hours) |
| **COUNT** | How many rows per group |
| **COUNTA** | Non-empty rows (counting customer_ids when some are blank) |
| **AVERAGE** | Mean per group |
| **MIN / MAX** | Smallest / largest in group (first sale, biggest deal) |
| **MEDIAN** | Robust central value |
| **COUNTUNIQUE** | Distinct count per group |
| **STDEV / VAR** | Spread per group |
| **Custom formula** | Bring your own aggregation logic |

Each Value field has its own aggregation; you can have multiple Values stacked (Sum of revenue AND Count of orders in the same pivot).

### Calculated fields

```
Pivot editor → Values → Add → Calculated field
=SUM(revenue) / COUNT(order_id)    -- average order value
```

Calculated fields let you compute ratios and derived metrics within the pivot itself — average order value, conversion rate, share of total. Avoids re-doing math outside.

### Filter zone

Drag a column to Filters to restrict the source rows feeding the pivot:

- Filter status = "paid" → exclude refunds, cancellations
- Filter date >= 2026-01-01 → current-year only
- Filter country IN (US, UK, DE) → top markets only

The filter is applied **before** aggregation. The shown rows / columns / values reflect only the filtered subset.

### Drill-down

Double-clicking a value cell in the pivot creates a new sheet showing the **source rows** that contributed to that cell. Excellent for sanity-checking unexpected numbers.

### Pivots in chained workflows

```
Raw data sheet           (10,000+ rows)
       │
       ▼  PIVOT
Per-month-per-region summary    (a few hundred cells)
       │
       ▼  CHART
Visualization              ([[Data Visualization Sheets]])
```

The pivot reduces volume; the chart communicates. Each step takes the previous step's output as its source.

### Pivot table vs PIVOT in SQL

There is no standalone `PIVOT` keyword in standard SQL — the equivalent is `GROUP BY` with conditional aggregates:

```sql
SELECT
  region,
  SUM(CASE WHEN month = '2026-01' THEN revenue ELSE 0 END) AS jan,
  SUM(CASE WHEN month = '2026-02' THEN revenue ELSE 0 END) AS feb,
  SUM(CASE WHEN month = '2026-03' THEN revenue ELSE 0 END) AS mar,
  SUM(revenue) AS total
FROM orders
GROUP BY region;
```

The Sheets pivot UI generates this kind of query automatically. See [[Group By]] and [[Conditional Expressions SQL]].

### Limitations

- **Performance**: Sheets pivot on > 50k rows lags noticeably
- **Real-time refresh**: pivot recomputes when source data changes — heavy pivots can slow the whole sheet
- **No row-level interactivity**: cannot edit values in pivot cells directly; modify the source instead

For larger data, move to BigQuery + Connected Sheets, or build the equivalent with SQL.

## Key Parameters

- **Source range**: pin to specific range (`A1:F10000`) or whole columns (`A:F`); whole-column source auto-includes new rows
- **Refresh**: pivot recomputes automatically on source change
- **Sort order**: rows / columns sort alphabetically by default; configure in pivot editor for desired order (e.g., months chronological)
- **Subtotals + Grand totals**: toggle in editor; on by default
- **Show as % of**: change Value display to "% of row" / "% of column" / "% of grand total" — instant share calculations

## When To Use

- **Any "summary per category" question** — the canonical pivot use case
- **Cross-tab reports** — rows × columns matrix
- **Quick exploration** — drag columns around to see the data from multiple angles
- **Prototyping a SQL query** — sketch the result in Sheets first, then write the matching GROUP BY
- Anti-pattern: building one pivot per metric when calculated fields would unify them
- Anti-pattern: large source data (> 100k rows) — performance suffers; use SQL or Connected Sheets

## Connections

- Related: [[Filter Query Unique Sheets]] (often used together — filter, then pivot), [[Lookup Functions Sheets]] (enrich before pivoting), [[Data Visualization Sheets]] (chart the pivot), [[Data Analysis Workflow]] (step 6: summarize)
- Builds on: [[Data Exploration and Cleaning Sheets]] (pivots assume clean data)
- Compare with: [[Group By]] (SQL counterpart), pandas `.pivot_table()`, Excel pivot tables (essentially identical)
- Used by: every operational dashboard, every weekly business review prepared in Sheets

## My Notes

- Pivot tables are the single most underused feature in many teams. Analysts who master them deliver answers in minutes rather than hours.
- Practice: [Netflix Reklam Kampanya Analizi III](https://nextgen.workintech.com.tr/project/201/2?pid=7268) — build a campaign performance pivot with calculated fields for CPA and ROAS.
- A useful pattern: build the pivot first, then convert the layout to a SQL `GROUP BY` query — solidifies the conceptual link between the two skills.
- Interview tip: when asked how you'd quickly summarize 50,000 rows, "Pivot table in Sheets" or "GROUP BY in SQL" are both correct — explain when each fits.
