---
title: "Data Analysis Workflow"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/01-veri-analizinin-asamalari]]"
tags:
  - data-analysis
  - workflow
  - methodology
  - process
---

# Data Analysis Workflow

> One-line summary: A step-by-step methodology that turns raw data into business decisions — ask questions, identify the data, choose the analysis type, explore, clean, summarize, visualize — followed in roughly the same shape by every analytics team from Google to a two-person startup.

## Core Concept

Data analysis is only powerful when it follows a repeatable, structured process. The same raw data can produce useful insight or misleading noise depending on the discipline of the analyst working it. Modern technology companies — Google, Apple, Microsoft, Amazon — train new analysts on the same fundamental workflow because consistency makes results trustworthy and reproducible.

The metaphor: crude oil is useless until it goes through distillation, cracking, and refinement. Raw data is identical. Without structured processing, it stays messy and misleading. With the right stages, it becomes business intelligence.

## How It Works

### The seven steps

```
1. Ask questions          → What are we trying to learn? (motivation)
2. Identify data needs    → What data do we need to answer it? (scoping)
3. Choose analysis type   → Descriptive? Diagnostic? Predictive? Prescriptive?
4. Explore the data       → What does it look like? Distribution, gaps, outliers
5. Clean the data         → Fix types, handle NULLs, deduplicate, normalize
6. Summarize insights     → Pivot, aggregate, segment — find the patterns
7. Visualize and present  → Communicate clearly to non-analyst stakeholders
```

This is the framework that everything in Sprint 1 onward builds on. Each step has its own toolkit.

### Step-by-step in practice

**1. Ask questions.** "Why did revenue drop last quarter?" or "Which customer segment is most profitable?" Without a clear question, analysis drifts into expensive exploration without an actionable conclusion.

**2. Identify data needs.** Which tables, sources, time ranges, columns does the question require? At this stage you might discover that needed data does not exist, which itself is useful information.

**3. Choose analysis type.**
- **Descriptive** (what happened?): KPIs, dashboards, summaries
- **Diagnostic** (why did it happen?): cohort analysis, segmentation, drill-down
- **Predictive** (what will happen?): forecasting, modeling
- **Prescriptive** (what should we do?): optimization, simulation, recommendations

Most analyst work is descriptive and diagnostic. Predictive is ML territory.

**4. Explore the data.** Open the dataset, check shape, types, sample rows, NULL rates, distributions. The single most underrated step — analysts who skip this miss obvious data quality issues that wreck downstream conclusions.

**5. Clean the data.** Fix anything found in exploration. Convert types ([[SQL Data Types and Casting]] in SQL, equivalents in [[Data Exploration and Cleaning Sheets]] for Sheets). Handle missing values. Deduplicate.

**6. Summarize insights.** This is where aggregation, pivoting, and grouping happen — [[Pivot Tables Sheets]] in Sheets or [[Group By]] in SQL. The output is one or more business-readable numbers.

**7. Visualize and present.** Charts, dashboards, slide decks. The work is wasted if the audience cannot understand the result.

### Iteration is the secret

The workflow looks linear but is iterative. Step 4 (exploration) usually surfaces questions the original Step 1 missed. Step 7 (presentation) often triggers new questions that send you back to Step 2. Senior analysts treat the cycle as a loop, not a line.

### Mapping to tooling

| Step | Google Sheets | SQL (BigQuery) | Python (pandas) |
|------|---------------|----------------|-----------------|
| 1. Ask | conversation | conversation | conversation |
| 2. Identify | catalog browsing | INFORMATION_SCHEMA | inspect data sources |
| 3. Choose type | (mental) | (mental) | (mental) |
| 4. Explore | `=COUNTA`, sorting, filtering | `SELECT COUNT(*), ...` | `.head()`, `.describe()` |
| 5. Clean | TRIM, UPPER, REPLACE, manual fix | CAST, REGEXP_REPLACE, COALESCE | `.astype()`, `.fillna()` |
| 6. Summarize | Pivot tables, FILTER, QUERY | GROUP BY, aggregates, window functions | `.groupby().agg()` |
| 7. Visualize | Charts, slicers | export → BI tool | matplotlib, plotly |

Each tool has its sweet spot. Sheets for small data and quick prototypes; SQL for warehouses; Python for ML and complex transformations.

### Why Google Sheets first

The Sprint 1 / Lesson 1 curriculum starts in Google Sheets for three reasons:
- **Low friction**: no installation, no SQL, no Python — just open a browser
- **Universal familiarity**: most knowledge workers can already navigate a spreadsheet
- **The concepts transfer**: pivot tables become GROUP BY, lookups become JOINs, FILTER becomes WHERE

Once the workflow is fluent in Sheets, scaling up to SQL and Python is a matter of changing tools, not changing thinking.

## Key Parameters

- **Question quality**: "Why is revenue down?" beats "Tell me about the data." Specificity drives focused analysis.
- **Data freshness vs cost**: live queries are fresh but expensive; cached / dashboarded data is cheap but stale (see [[Views vs Tables Tradeoffs]])
- **Iteration count**: budget for 2–3 cycles per real analysis; pure first-pass results are rarely production-ready
- **Stakeholder communication**: build in time for presentation and revision — Step 7 is not a postscript

## When To Use

- **Every analysis task**, from a 30-minute Sheets review to a multi-month modeling project
- **Onboarding new analysts**: teach the framework before any specific tool
- **Reviewing past work**: which step was skipped? Usually exploration (4) or cleaning (5)
- **Cross-functional projects**: shared framework eliminates "what is this analysis about?" questions
- Anti-pattern: jumping straight to charts (step 7) without exploration (step 4) — leads to misleading visuals
- Anti-pattern: spending all time in cleaning (step 5) — diminishing returns; ship when the data is good enough

## Connections

- Related: [[Google Sheets Analytics Overview]] (lesson umbrella), [[Data Exploration and Cleaning Sheets]], [[Pivot Tables Sheets]], [[Data Visualization Sheets]]
- Builds on: spreadsheet basics and statistical literacy
- Compare with: dbt project structure (encodes a similar workflow in code), CRISP-DM (the older industry-standard methodology, slightly more elaborate)
- Used by: every analytical role; the foundation for KPI work in later Sprint 1 lessons

## My Notes

- The 7-step framework is taught deeply in Sprint 1 / Lesson 2 with explicit per-step videos and a fictional company case (GreenFit). See [[Seven Step Framework in Practice]] for the deep dive with all 7 steps walked through narratively, plus the iteration principle.
- Output of the framework is typically a KPI — see [[KPI Fundamentals]] and the department-specific examples ([[Finance KPIs]], [[Inventory KPIs]], [[Quality KPIs]]).
- Practice: [Netflix Reklam Kampanya Analizi I](https://nextgen.workintech.com.tr/project/201/2?pid=7266) — applies the full workflow to a campaign-analysis scenario.
- Personal habit: write down the question (step 1) before opening any tool. Stops the "exploration that goes nowhere" trap.
- Interview tip: when asked "walk me through how you would analyze X", lead with the 7-step framework explicitly. Most candidates skip directly to tools and lose narrative coherence.
