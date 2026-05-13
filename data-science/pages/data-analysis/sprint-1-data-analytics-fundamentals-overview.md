---
title: "Sprint 1 Data Analytics Fundamentals Overview"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/01-google-sheets-ile-analizin-temelleri/transcripts/01-veri-analizinin-asamalari]]"
tags:
  - data-analysis
  - overview
  - umbrella
  - sprint-1
  - curriculum
---

# Sprint 1 Data Analytics Fundamentals Overview

> One-line summary: A complete map of Sprint 1 (Data Analysis Fundamentals) — the spreadsheet toolkit, the seven-step analytical methodology, KPI design (fundamentals + advanced strategy), customer analytics (acquisition + segmentation + cohort), and the data ecosystem (roles, lifecycle, real-world cases) — covering 25 wiki pages from 45 lecture videos in one entry-point document.

## Core Concept

Sprint 1 ("Veri Analizinin Temelleri" — Data Analysis Fundamentals) is the conceptual and practical foundation of the entire data analytics curriculum. It teaches **how to think** about data problems before Sprint 2 teaches **how to query** them with SQL. The four lessons build on each other:

```
Lesson 1: Sheets toolkit + analytical workflow (Google Sheets ile Analizin Temelleri)
   │
   ▼
Lesson 2: KPI design from first principles (KPI'ın Temelleri)
   │
   ▼
Lesson 3: KPI strategy + customer analytics (İleri Seviye KPI'lar)
   │
   ▼
Lesson 4: Data ecosystem, roles, real-world cases (Data Analiz Ekosistemi)
```

By the end of Sprint 1, the analyst has:
- A toolkit (Sheets / SQL-ready mental models)
- A methodology (7-step framework + iteration)
- A KPI design vocabulary (department-specific + business-model-aware)
- A customer lens (acquisition → retention → segmentation)
- An ecosystem view (roles, lifecycle, cross-functional collaboration)

This document is the **entry point** to all 25 wiki pages produced from this Sprint.

## How It Works — The Concept Map

### Lesson 1: Google Sheets ile Analizin Temelleri

The toolkit and workflow:

- [[Data Analysis Workflow]] — The 7-step methodology (ask → identify → choose type → explore → clean → summarize → visualize)
- [[Importing Data to Sheets]] — CSV, IMPORTRANGE, IMPORTDATA
- [[Data Exploration and Cleaning Sheets]] — EDA + cleaning techniques (TRIM, UPPER, deduplication)
- [[Lookup Functions Sheets]] — VLOOKUP, XLOOKUP, INDEX-MATCH compared
- [[Pivot Tables Sheets]] — Aggregation via drag-and-drop
- [[Filter Query Unique Sheets]] — FILTER, QUERY (SQL-in-Sheets), UNIQUE
- [[Data Visualization Sheets]] — Charts, slicers, dashboards
- [[Google Sheets Analytics Overview]] — Lesson 1 hub with the **Sheets ↔ SQL bridge table**

### Lesson 2: KPI'ın Temelleri — workflow deep dive + KPI core

The methodology applied and KPIs introduced:

- [[Seven Step Framework in Practice]] — All 7 steps walked through with the GreenFit case study + iteration principle
- [[KPI Fundamentals]] — What is a KPI, KPI vs metric, vanity test
- [[Finance KPIs]] — Gross margin, net margin
- [[Inventory KPIs]] — Stockout rate, carrying cost trade-off
- [[Quality KPIs]] — Return rate, returns by reason

### Lesson 3: İleri Seviye KPI'lar — strategy + customer analytics

KPI strategy and the customer lens:

- [[KPI by Business Model]] — B2C/B2B/subscription/maturity layers
- [[KPI by Team and Function]] — Per-team KPI design, North Star pattern
- [[Vanity Metrics Anti Patterns]] — Goodhart's Law, what to avoid
- [[Customer Acquisition and Expansion Funnels]] — CAC, LTV, NRR, the two-funnel view
- [[Customer Segmentation Rfm]] — Recency × Frequency × Monetary scoring
- [[Cohort Analysis]] — "The diagonal is the story"

### Lesson 4: Data Analiz Ekosistemi — roles + lifecycle + cases

The data team's role in the organization:

- [[Data Professional Role and Collaboration]] — The translator/bridge role + 4-step collaboration framework
- [[Data Lifecycle]] — Collect → Store → Clean → Transform → Analyze → Feedback
- [[Data Team Roles and Responsibilities]] — Engineer / Analytics Engineer / Analyst / BA / Scientist / ML Engineer
- [[Data Team Maturity Evolution]] — Early → Growth → Mature team patterns
- [[Real World Data Analytics Case Studies]] — Museum, Nestlé, Vodafone, grocery chain

## How They Fit Together

The most important insight from Sprint 1: every concept reinforces every other one.

**A worked example — building a customer churn analysis:**

1. **Question** ([[Seven Step Framework in Practice]] step 1): "Why is our subscription churn rising in Q1?"
2. **Stakeholder mapping** ([[Data Professional Role and Collaboration]]): customer success, marketing, finance all care; align on the definition of "churn"
3. **Data needs** ([[Data Lifecycle]] stages 1-2): pull from billing, product usage, support tickets
4. **Clean** ([[Data Exploration and Cleaning Sheets]] / [[Data Lifecycle]] stage 3): normalize dates, handle NULLs
5. **Cohort analysis** ([[Cohort Analysis]]): is churn rising across cohorts, or only recent ones?
6. **Segmentation** ([[Customer Segmentation Rfm]]): is one segment driving the churn?
7. **KPI framing** ([[KPI Fundamentals]], [[KPI by Business Model]]): NRR is the right KPI for this subscription business
8. **Visualization** ([[Data Visualization Sheets]] / [[Pivot Tables Sheets]]): chart cohort retention with the inflection point highlighted
9. **Iteration**: the finding raises a new question — drill into the segment
10. **Feedback** ([[Data Lifecycle]] stage 6): push the at-risk customer list to Customer Success tooling

A single analysis touches ~10 of the 25 Sprint 1 pages. They are not independent topics — they are facets of one integrated practice.

## Bridge to Sprint 2 (SQL)

Sprint 1 lives in Google Sheets. Sprint 2 ports the same concepts to SQL on BigQuery:

| Sprint 1 (Sheets) | Sprint 2 (SQL) |
|-------------------|----------------|
| [[Pivot Tables Sheets]] | [[Group By]] + [[Sum Avg Min Max]] |
| [[Lookup Functions Sheets]] | [[Joins Fundamentals]] + [[Join Types]] |
| [[Filter Query Unique Sheets]] | [[Filtering Where]] + [[Distinct and Deduplication]] |
| [[Data Exploration and Cleaning Sheets]] | [[String Cleaning Replace and Case]] + [[Null Handling SQL]] + [[SQL Data Types and Casting]] |
| Cohort / RFM in Sheets | [[Cohort Analysis]] + [[Window Functions Fundamentals]] + [[Customer Segmentation Rfm]] |
| [[Importing Data to Sheets]] | [[Bigquery Insert with Cast Workflow]] |

The full bridge table lives in [[Google Sheets Analytics Overview]].

After Sprint 2 (SQL fundamentals), Sprint 3 covers production data warehouse work — see [[Data Warehouse Economics Overview]].

## Key Parameters

- **Sprint 1 page count**: 25 wiki pages from 45 lecture videos
- **Reading time**: ~3-4 hours to read all 25 pages thoroughly
- **Skill level after Sprint 1**: ready to start SQL in Sprint 2; ready to design KPIs and dashboards in Sheets
- **Audience**: junior data analyst onboarding, business stakeholders, anyone learning data analytics

## When To Use

- **As an analyst's onboarding path**: read this overview first, then drill into specific pages
- **For interview preparation**: use as a checklist of foundational topics
- **For team training**: assign specific pages to specific topics
- **For self-assessment**: which Sprint 1 topics am I weak on?
- Anti-pattern: skipping the foundations to "get to ML / advanced SQL" — the bridge thinking (analyst as translator) is harder to learn after the technical skills

## Connections

- Builds on: nothing (this is the entry point to the analytics curriculum)
- **Next:** Sprint 2 SQL fundamentals — start with [[SQL Fundamentals Overview]]; the SQL counterpart of this overview
- **Beyond:** Sprint 3 data warehouse work — [[Data Warehouse Economics Overview]]
- Related: [[Descriptive Statistics]], [[Measures of Central Tendency]], [[Measures of Spread]] (the math foundations)
- Compare with: bootcamp programs at other providers (DataCamp, General Assembly, Springboard); this curriculum is more concept-focused, less tool-focused than most

## My Notes

- Sprint 1's depth on the **soft skills** (stakeholder management, KPI design strategy, role taxonomy) is unusual for a bootcamp — most bootcamps over-index on tools. This curriculum balances both.
- The four lessons of Sprint 1 mirror real career growth: tool fluency (L1) → methodology (L2) → strategic thinking (L3) → organizational awareness (L4).
- Practice projects across Sprint 1:
  - Lesson 1: [Netflix Reklam Kampanya Analizi I-III](https://nextgen.workintech.com.tr/project/201/2?pid=7266) (Sheets toolkit)
  - Lesson 2: [Amazon Books Tedarik Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7269), [Amazon Books Kalite Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7281) (KPI design)
  - Lesson 3: (covered by Lesson 4 projects)
  - Lesson 4: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283), [Amazon Books NPS Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7292) (ecosystem + cases)
- Returning to this overview after each Sprint 2 / Sprint 3 ingest reinforces the conceptual hierarchy — Sprint 1 is the foundation everything else builds on.
