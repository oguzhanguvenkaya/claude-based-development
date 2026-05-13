---
title: "Data Visualization Sheets"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/11-veriyi-gorsellestirme]]"
tags:
  - data-analysis
  - google-sheets
  - visualization
  - charts
  - slicers
---

# Data Visualization Sheets

> One-line summary: Charts and slicers turn cleaned, summarized data into communicable insights — Sheets supports the full chart toolkit (line, bar, pie, combo, scatter) plus interactive slicers that filter dashboards without rebuilding pivots.

## Core Concept

After cleaning, pivoting, and filtering, the analysis still has to **communicate**. Numbers in cells answer the analyst's question. Charts answer the stakeholder's question. The same data presented in a table vs a line chart often gets different reactions, even though the numbers are identical — visual encoding is part of the analysis, not an afterthought.

Sheets supports the standard chart types and a few interactive features (slicers) that make a single chart serve multiple drill-down scenarios.

## How It Works

### Chart types and when each fits

| Chart | Best for |
|-------|----------|
| **Line chart** | Trends over time (revenue per month, daily active users) |
| **Column / Bar chart** | Comparing categories (revenue per region, count per status) |
| **Pie / Donut** | Parts of a whole (channel share of acquisition) — use sparingly |
| **Combo chart** | Two metrics at different scales (revenue line + AOV bar) |
| **Scatter plot** | Relationship between two numeric variables (price vs units sold) |
| **Histogram** | Distribution of a single variable (order amount buckets) |
| **Geo / Map** | Data with location (sales per state, per country) |
| **Sparkline (in-cell)** | Trend indicators inside table cells — `=SPARKLINE(B2:F2)` |

The rule: **pick the chart that matches the question.** "How did X change over time?" → line. "Which X is bigger?" → bar. "What share of total?" → pie (or stacked bar for >5 categories).

### Creating a chart

```
Insert → Chart → select data range → Sheets auto-suggests type
```

The chart editor pane lets you:
- Switch chart type
- Configure axes (titles, scale, gridlines)
- Add a chart title and legend
- Customize colors per series
- Add trend lines (linear / polynomial / moving average)
- Add error bars and annotations

Most defaults are reasonable. Spending 5 minutes refining a chart is usually worth it before sharing.

### Charts built on pivot tables

The canonical workflow:

```
Raw data        → Pivot table       → Chart from pivot
(10,000 rows)     (50 rows summary)   (visual report)
```

Insert a chart **from inside** a pivot table (Insert → Chart while the pivot is selected) and the chart auto-binds to the pivot. As you change the pivot configuration, the chart updates. Powerful for interactive exploration.

### Slicers — interactive filters for charts

```
Data → Add a slicer → choose source range → choose filter column
```

A slicer is a UI control attached to the sheet that lets a viewer click to filter the underlying pivot / chart without changing the source.

Use case: a dashboard with one chart showing monthly revenue. Add a slicer on "country" — clicking countries in the slicer instantly filters the chart to those countries.

```
Slicer: country (multi-select)        Chart: Revenue per month
[ ] All                                     ┌─────────────┐
[x] US                                      │   /\        │
[x] UK                                      │  /  \      /│
[ ] DE                                      │ /    \____/ │
[ ] FR                                      └─────────────┘
```

Slicers turn static charts into interactive dashboards. The viewer drives exploration; the analyst doesn't have to rebuild for each segment.

### Annotations and storytelling

Charts gain power from annotation:

- Title that states the takeaway, not the description ("Q1 revenue beat target by 12%" beats "Revenue per Quarter")
- Highlight color on the segment that matters
- A short text label calling out the inflection point
- Trend line or target line to provide context

Stakeholders read titles first. A good title summarizes the chart in one sentence; the chart confirms.

### Sharing charts

| Method | When |
|--------|------|
| **Publish chart to web** | Embedded in a doc or Confluence page |
| **Image export** (PNG, PDF, SVG) | Slide decks, emails |
| **Share the Sheet** with view access | Interactive use, viewers can click slicers |
| **Embed in Google Slides** | Auto-updates when the Sheet changes |

For executive reports, image exports go in slides; for ongoing dashboards, share-the-sheet with slicers serves better.

### Limitations

- Sheets charts work well up to a few thousand source rows; performance degrades beyond
- No native dashboard layout (multiple charts on one page work but are not auto-aligned like a BI tool)
- Animations and interactive features are basic compared to Tableau / Looker
- Chart styling is limited; for design-heavy reports, export to a slide / design tool

For dashboards beyond Sheets' capacity, consider Looker Studio (formerly Data Studio) — free, integrates with Sheets and BigQuery, far better dashboard layout.

## Key Parameters

- **Source range**: prefer pinned cell ranges (`$A$1:$D$100`) to keep charts stable; use named ranges for clarity
- **Refresh cadence**: charts auto-update on source change; live BigQuery sources update on each open via Connected Sheets
- **Chart types in slicers**: slicers work with most chart types; pie charts and geo maps work less smoothly
- **Mobile**: charts render but slicers are limited on mobile; design for desktop

## When To Use

- **Step 7 of every analysis**: communicating the result (see [[Data Analysis Workflow]])
- **Executive reporting**: image exports in slide decks
- **Ongoing team dashboards**: share-the-sheet with slicers for interactive use
- **Quick sanity checks**: a chart often reveals data issues a table hides
- Anti-pattern: chart-first analysis — pick the question and pivot before choosing a chart
- Anti-pattern: pie chart with 12 slices — use a bar chart for comparing >5 categories

## Connections

- Related: [[Pivot Tables Sheets]] (charts usually built from pivots), [[Filter Query Unique Sheets]] (filter the data before charting), [[Data Analysis Workflow]] (step 7: visualize)
- Builds on: [[Data Exploration and Cleaning Sheets]] (clean data charts cleanly)
- Compare with: Looker Studio (Google's BI tool — more dashboard-oriented), Tableau / Power BI (enterprise BI), matplotlib / plotly (code-driven)
- Used by: every business review, every weekly stakeholder report

## My Notes

- A useful test: show your chart to someone who has not seen the analysis. If they can answer "what does this chart say?" in 5 seconds, the visual works. If they need explanation, the chart isn't doing its job.
- Practice: build a one-chart Sheets dashboard with a slicer for [Netflix Reklam Kampanya Analizi III](https://nextgen.workintech.com.tr/project/201/2?pid=7268). Share with a non-analyst and see what they conclude.
- Title rule: state the takeaway in the title, not the data description. "Q1 churn dropped 30%" beats "Churn rate by quarter".
- Interview tip: when discussing visualization, mention specific chart-type-to-question mapping (trend → line, comparison → bar, composition → stacked bar / pie). Many candidates pick chart types randomly.
