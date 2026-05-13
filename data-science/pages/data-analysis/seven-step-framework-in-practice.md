---
title: "Seven Step Framework in Practice"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/01-adim-1-sorular-sor]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/02-adim-2-veri-ihtiyaclarini-belirle]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/03-adim-3-analiz-turunu-sec]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/04-adim-4-veriyi-kesfet]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/05-adim-5-verileri-temizle]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/06-adim-6-icgorulerini-ozetle]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/07-adim-7-sonuclari-gorsellestir]]"
  - "[[raw/course-notes/sprint 1/02-kpi-temelleri/transcripts/08-sonuc-ve-yinelemenin-onemi]]"
tags:
  - data-analysis
  - workflow
  - methodology
  - kpi
  - case-study
---

# Seven Step Framework in Practice

> One-line summary: A walkthrough of the seven-step data analysis framework using a fictional retail company (GreenFit) — showing the concrete activity, common pitfalls, and 80/20 effort distribution at every step, plus why the cycle is iterative not linear.

## Core Concept

[[Data Analysis Workflow]] introduces the seven-step methodology at a glance. This page goes deeper: each step gets concrete activities, anti-patterns, and how it threads into the next. The case study follows Emma, a data analyst at GreenFit (a sportswear retailer), as she answers "why did our profit margins drop on April 5th?"

The hidden lesson: **iteration**. New analysts treat the seven steps as a linear chain; experienced analysts treat them as a loop where step 4 often sends you back to step 2.

## How It Works

### Step 1 — Ask the right questions

The question quality determines everything downstream. A good question is:
- **Specific**: "Why did the profit margin drop on April 5th?" not "Tell me about profit"
- **Answerable**: must map to data we actually have or could plausibly collect
- **Actionable**: knowing the answer should enable a decision

> A good analyst starts not from the data, but from clear and curious questions.

Bad question: "Show me everything you can about our finance." Good question: "Among the 12% of orders flagged as 'returned,' is there a pattern by region or product category?"

### Step 2 — Identify the data you need

Beginners try to collect every possible column. This is wrong: ~80% of company data is unused noise. Sharp scoping at this stage saves weeks of confusion.

For Emma's April 5th question, she scopes to three sources:
- Orders table (revenue, costs per order)
- Shipping costs
- Marketing spend by campaign

She **does not** pull customer demographics, product images, or warehouse temperature logs — none of them feed the question.

### Step 3 — Choose the analysis type

| Type | When |
|------|------|
| **Ad-hoc** | One-time investigation ("why did X happen on April 5?") |
| **Regular reporting** | Continuous dashboard ("daily profit margin by region") |

The choice changes implementation:
- Ad-hoc → quick Sheets analysis, manual cleanup, throwaway code
- Regular → invest in clean pipelines, automation, tests, documentation

Emma's question is ad-hoc — a one-off investigation. She does not build a dashboard for it.

### Step 4 — Explore the data ("trust but verify")

Open the data and look at it. Emma notices marketing spend spiked 4× on April 5 — her first hypothesis: a campaign overspent. But she does not stop there. Exploration must be **broad** (check every relevant column) before narrowing to one cause.

Tools in this step: distribution checks, sort by extreme values, scan for NULLs, sanity-check totals against a known reference. See [[Data Exploration and Cleaning Sheets]].

Common pitfall: jumping to step 6 (summary) before completing exploration — leads to confident but wrong conclusions.

### Step 5 — Clean the data

**Garbage in, garbage out.** Per Harvard Business Review, ~50% of newly created business records contain errors. If Emma's "April 5 anomaly" comes from a data entry bug (a duplicated row, a misplaced decimal), her analysis is meaningless.

Cleaning activities:
- Fix types (text-stored numbers, malformed dates)
- Handle NULLs ([[Null Handling SQL]])
- Deduplicate
- Normalize case and whitespace ([[Data Exploration and Cleaning Sheets]], [[String Cleaning Replace and Case]])
- Flag outliers for human review

In Emma's case: she discovers two duplicate orders inflating Apr 5 revenue. Cleaning them changes the picture.

### Step 6 — Summarize insights

Now compute the answer. Pivot tables ([[Pivot Tables Sheets]]), GROUP BY queries ([[Group By]]), or aggregates ([[Sum Avg Min Max]]) — whichever fits the data scale.

For Emma: gross margin per day, segmented by region. She finds the April 5 drop is concentrated in two regions where shipping costs spiked due to a freight carrier change.

The output of step 6 is one or more **business-readable numbers** with confidence intervals or sensitivity analysis if needed.

### Step 7 — Visualize and present

A table buried in an email gets ignored. A clear chart with a one-line takeaway title gets action. HBR research: stakeholders are **2× more likely to act** when results come with a visual summary instead of just numbers.

Emma's deliverable: a one-slide chart showing daily margin over the last month, with April 5 highlighted in red and an annotation explaining the freight cost change. See [[Data Visualization Sheets]].

### Iteration — the hidden eighth principle

Beginners think:
```
Step 1 → 2 → 3 → 4 → 5 → 6 → 7 → done
```

Reality:
```
Step 1 → 2 → 3 → 4 → "wait, I need different data" → 2 → 4 → 5 → 6
       → "the summary surfaces a new question" → 1 → ... → 7
```

MIT Sloan research: iterative analytical approaches lead to **better decisions** than linear pursuit of the original question. Each pass through the cycle teaches you what you should have asked the first time.

Plan for at least 2 passes. Budget time accordingly.

## Key Parameters

- **Step 1 quality** is the highest-leverage investment — 20% of the time, 80% of the value
- **Iteration count**: budget for 2–3 passes; first-pass results are rarely production-ready
- **Time allocation rule of thumb**: 30% questions/scoping/exploration, 40% cleaning, 20% summarizing, 10% visualization. New analysts spend too much on visualization, too little on cleaning.
- **Documentation**: log the question, the data sources, the cleaning decisions, the assumptions — future-you will need them

## When To Use

- **Every analysis task** — even quick 30-minute reviews benefit from the framework
- **Onboarding** — teach the framework before any specific tool
- **Stakeholder management** — when an analyst is overwhelmed, the framework gives a defensible structure ("I'm currently on step 4 of the analysis")
- **Post-mortem on failed analyses** — which step was rushed? Usually 1 (question) or 4 (exploration)
- Anti-pattern: jumping to visualization without exploration — leads to pretty but misleading charts
- Anti-pattern: treating the framework as a checkbox exercise — the discipline matters more than the boxes

## Connections

- Related: [[Data Analysis Workflow]] (the high-level summary), [[KPI Fundamentals]] (the framework's typical output is KPIs), [[Data Exploration and Cleaning Sheets]] (steps 4 + 5 in Sheets), [[Pivot Tables Sheets]] (step 6), [[Data Visualization Sheets]] (step 7)
- Builds on: spreadsheet basics or SQL fluency (see [[Google Sheets Analytics Overview]] for the toolkit mapping)
- Compare with: CRISP-DM (the older industry-standard methodology, slightly more elaborate at 6 steps), dbt project structure (encodes a similar workflow in code)
- Used by: every analytical role; the foundation of [[KPI Fundamentals]] in Lesson 2 and beyond

## My Notes

- The GreenFit case in this lesson is fictional but realistic. When studying, mentally substitute your own company's data and walk through the same seven steps.
- Practice: [Amazon Books Tedarik Raporu](https://nextgen.workintech.com.tr/project/201/3?pid=7269) — apply all seven steps end-to-end on a real-ish dataset.
- The iteration principle is the most important takeaway. If you only remember one thing: **the analytical process is a loop, not a line.**
- Interview tip: when describing a past analysis, narrate it in the seven-step structure. Interviewers love the clear narrative shape.
