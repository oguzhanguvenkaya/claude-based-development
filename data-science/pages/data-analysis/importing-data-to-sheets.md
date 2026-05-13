---
title: "Importing Data to Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/02-google-sheetse-import-etmek]]"
tags:
  - data-analysis
  - google-sheets
  - data-import
  - csv
  - importrange
---

# Importing Data to Sheets

> One-line summary: Two paths to get data into Google Sheets — manual CSV import (with Split-Text-to-Columns for cleanup) and IMPORTRANGE for live links to other sheets — each suited to different freshness and source needs.

## Core Concept

Every analysis starts by getting the data into the tool. In Sheets, this is the entry point of the [[Data Analysis Workflow]]. The choice of import method matters more than it seems: a manual one-time copy serves a snapshot analysis well, but breaks the moment the source data updates. A live link via IMPORTRANGE stays fresh but introduces dependency risk if the source moves or permissions change.

Knowing both methods and when each applies is a low-glamour but consequential skill.

## How It Works

### Manual CSV import

```
File → Import → Upload (drag the CSV)
   or
File → Open → select CSV → Sheets converts on the fly
```

When the CSV has all values jammed into one column (common with non-standard delimiters):

```
Data → Split text to columns → choose delimiter (comma, semicolon, tab, custom)
```

The delimiter dropdown auto-detects in most cases. Manually pick when auto-detection fails (semicolon-separated European exports, for example).

After import:
- Check column types — Sheets may treat numeric columns as text if they contain symbols (`$`, `%`, `,`)
- Trim whitespace — `=TRIM(A1)` strips leading/trailing spaces
- Convert numbers — `=VALUE(A1)` parses a text-looking number into actual numeric

### Manual import — when to use

- One-time analysis of a static export
- Source data that does not update frequently
- When the source is a third party with no API (vendor reports, partner exports)
- When you need to inspect data before incorporating it into a recurring workflow

### IMPORTRANGE — live link to another sheet

```
=IMPORTRANGE("https://docs.google.com/spreadsheets/d/SOURCE_FILE_ID/edit", "Sheet1!A:F")
```

First argument: URL or ID of the source spreadsheet. Second: sheet name + range to pull.

The first time you call IMPORTRANGE pointing to a new source, Sheets prompts you to grant permission. After that, the data live-links: edits in the source propagate to the importing sheet within seconds.

```
=IMPORTRANGE(source_url, sheet_range)
```

Use cases:
- Sales team maintains a master file; analysts pull live copies for reports
- Daily auto-refresh from a Google Forms response sheet
- Pulling reference tables (countries, products, regions) from a central catalog

### IMPORTRANGE limitations

- Both spreadsheets must be in Google Sheets (cannot import from Excel without first opening it as a Sheets file)
- Permission required from the source's owner
- Slower than local data; large IMPORTRANGEs can lag the spreadsheet
- Limited to ~50,000 cells imported per single formula

### Other import functions

| Function | Source | Use case |
|----------|--------|----------|
| `IMPORTRANGE` | Another Google Sheet | Live linked tables |
| `IMPORTDATA` | CSV / TSV URL | Public CSVs from the web |
| `IMPORTHTML` | HTML page | Tables or lists from a webpage |
| `IMPORTFEED` | RSS / Atom feed | News / blog feeds |
| `IMPORTXML` | XML / HTML with XPath | Structured web data |

`IMPORTDATA` is the most useful after IMPORTRANGE — it lets you pull public CSV exports (government data, sports statistics, exchange rates) directly into Sheets.

### Beyond Sheets: when to go bigger

Google Sheets hits practical limits around 100,000–500,000 rows. Past that, performance degrades and formulas slow. The next step:

1. Push the data to BigQuery (free import, ~unlimited scale)
2. Query with SQL ([[Select Statement]], [[Filtering Where]])
3. Use Looker, Tableau, or Sheets + Connected Sheets to visualize

Connected Sheets is a specific feature: it lets a Sheet query a BigQuery table directly, keeping the Sheets interface familiar while delegating the heavy lifting to BigQuery.

## Key Parameters

- **Source format**: CSV, TSV, Excel, ODS, Google Sheets, Parquet (via BigQuery)
- **Delimiter**: comma is universal but European exports often use semicolon; tab for TSV; pipe `|` for some legacy systems
- **Encoding**: UTF-8 is standard; rare files use UTF-16 or Latin-1 and may need re-export with UTF-8
- **IMPORTRANGE refresh**: near real-time but not instant; large imports may take seconds to update
- **Sheet size limits**: 10 million cells per Sheet, ~50k rows of formulas before performance issues

## When To Use

- **Manual CSV**: one-time analysis, snapshot data, vendor exports
- **IMPORTRANGE**: linked sheets within Google ecosystem, live updates needed
- **IMPORTDATA**: public CSVs from the web
- **Connected Sheets / BigQuery**: data beyond 100k rows or needing daily refresh
- Anti-pattern: stitching IMPORTRANGE chains across 5+ sheets — slow, fragile, hard to debug
- Anti-pattern: importing 500,000 rows into Sheets when the analysis would fit better in BigQuery

## Connections

- Related: [[Data Analysis Workflow]] (Step 1 / 2: getting the data), [[Data Exploration and Cleaning Sheets]] (next step), [[Google Sheets Analytics Overview]]
- Builds on: spreadsheet basics
- Compare with: SQL ingestion ([[Bigquery Insert with Cast Workflow]]) — same conceptual step at a different scale
- Used by: every Sheets-based analysis; precedes every other workflow step

## My Notes

- Defensive habit: after every import, run a quick `=COUNTA(A:A)` and check the count matches the source. Surprising number of imports lose rows to encoding or delimiter issues.
- Practice: [Netflix Reklam Kampanya Analizi I](https://nextgen.workintech.com.tr/project/201/2?pid=7266) — practice importing campaign data and verifying row counts.
- IMPORTRANGE permission prompts can be frustrating; document which sheets need which permissions in your team wiki.
- Interview tip: when discussing Sheets-vs-warehouse decisions, mention the 100k-row practical limit and Connected Sheets as the bridge — shows you know the scaling story.
