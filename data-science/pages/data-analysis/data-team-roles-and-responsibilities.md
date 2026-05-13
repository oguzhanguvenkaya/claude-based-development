---
title: "Data Team Roles and Responsibilities"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/04-data-analiz-ekosistemi/transcripts/07-veri-rolleri-i]]"
  - "[[raw/course-notes/sprint 1/04-data-analiz-ekosistemi/transcripts/08-veri-rolleri-ii]]"
  - "[[raw/course-notes/sprint 1/04-data-analiz-ekosistemi/transcripts/09-veri-rolleri-iii]]"
tags:
  - data-analysis
  - data-team
  - roles
  - careers
  - org-design
---

# Data Team Roles and Responsibilities

> One-line summary: A modern data team is like a construction crew — engineers build the foundation, analytics engineers transform raw materials, data analysts decorate the result for business use, business analysts maintain alignment with business needs, and data scientists / ML engineers handle the specialized predictive work; each role has a clear focus, and effective teams pair them deliberately.

## Core Concept

The titles "data analyst," "data engineer," "data scientist," "business analyst," and "analytics engineer" overlap in vocabulary but differ sharply in day-to-day responsibility. New analysts often confuse them; hiring managers often misuse them. This page is the canonical role taxonomy.

The construction metaphor is useful: a modern data team builds an "analytical home." Different people specialize in different parts of the construction. Pairing them well — with clear ownership boundaries — is what makes a data team productive.

## How It Works

### The construction crew metaphor

```
DATA ENGINEER          → Foundation + plumbing + electricity
ANALYTICS ENGINEER     → Framing + drywall (raw materials → usable rooms)
DATA ANALYST           → Decorator (makes rooms livable for business users)
BUSINESS ANALYST       → Gardener (keeps the home connected to its surroundings)
DATA SCIENTIST         → Architect of predictive features (smart home AI)
```

Each role builds on the others. A house without foundation collapses. A house without decorators is uninhabitable. A garden without a gardener overgrows.

### Data Engineer — the foundation builder

**Focus:** infrastructure and reliability.

**Responsibilities:**
- Build and maintain data ingestion pipelines (Fivetran, Airbyte, custom)
- Manage the warehouse / lakehouse infrastructure
- Implement security, access control, and data governance
- Ensure pipelines run reliably (monitoring, alerting, SLAs)
- Optimize cost and performance at the infrastructure level

**Tools:** Python, SQL, Airflow / Dagster, Kafka, Terraform, cloud platforms (AWS / GCP / Azure).

**Example output:** A daily ingestion pipeline that pulls 50 SaaS sources into BigQuery at 02:00 UTC, with automated retries and failure alerts.

### Analytics Engineer — the framer

**Focus:** transforming raw data into reliable analytical models.

**Responsibilities:**
- Build dbt models that transform bronze → silver → gold
- Define and maintain the canonical KPI definitions (the "metrics layer")
- Write tests on data quality and model correctness
- Document data lineage and semantic meaning
- Bridge between data engineers and analysts

**Tools:** SQL, dbt, Python, Git, BI tools.

**Example output:** A dbt project with ~50 models powering the company's KPI dashboard, with automated tests that catch regressions before they reach production.

This role emerged around 2018 and is now the fastest-growing data role. It fills the gap between pure infrastructure work and pure analysis.

### Data Analyst — the decorator

**Focus:** turning data into insights that business teams can use.

**Responsibilities:**
- Build dashboards (Looker, Tableau, Metabase)
- Design KPIs (see [[KPI Fundamentals]], [[KPI by Team and Function]])
- Run ad-hoc analyses for specific business questions
- Communicate findings to non-technical stakeholders
- Apply the [[Seven Step Framework in Practice]] daily

**Tools:** SQL, BI tool, Sheets / Excel, sometimes Python.

**Example output:** A Power BI dashboard showing churn trends by segment with a clear narrative of why churn moved this quarter.

> "Data analyst is the decorator: after the structure is built, the analyst makes the home livable for the business. Focus: analyst and action. Tasks: dashboards, KPIs, communication. Idea: turn data into stories that drive decisions."

### Business Analyst — the gardener

**Focus:** keeping the analytics aligned with business needs.

**Responsibilities:**
- Gather requirements from business stakeholders
- Maintain reporting against established processes
- Validate that metrics match the way the business actually operates
- Translate domain knowledge into analytical requirements
- Lighter SQL, heavier domain expertise

**Tools:** SQL (basic), BI tools, lots of stakeholder time, often industry-specific software (Salesforce, SAP, etc.).

**Example output:** Confirming that the "customer churn" metric in the data team's dashboard aligns with how Sales tracks it in Salesforce — and proposing reconciliation when it doesn't.

> "Business analyst is the gardener: the garden makes the home feel alive. The BA keeps analytics connected to the business world. Focus: business context. Tasks: gather requirements, maintain reports, ensure metric alignment with business needs."

### Data Scientist — the predictive architect

**Focus:** statistical models, ML, predictive analytics.

**Responsibilities:**
- Build predictive / classification / clustering models
- Run experiments (A/B tests, causal inference)
- Apply advanced statistics (regression, time-series, Bayesian methods)
- Often, deploy models to production via MLOps practices
- Lighter on dashboards, heavier on Python / R

**Tools:** Python (pandas, scikit-learn, PyTorch), R, SQL, Jupyter, MLOps tools (MLflow, Weights & Biases).

**Example output:** A churn-prediction model that scores each customer weekly with churn risk, fed back via [[Data Lifecycle]] stage 6 to Customer Success tooling.

### ML Engineer — the production ops

**Focus:** taking data science models from notebook to production.

**Responsibilities:**
- Deploy models behind APIs or batch inference
- Monitor model performance over time (drift detection)
- Optimize inference cost and latency
- Build feature stores and ML platforms

**Tools:** Python, Docker, Kubernetes, MLflow, cloud ML services.

Closer to software engineering than to analytics. Many companies pair an ML Engineer with each Data Scientist.

### Role overlap and team size

Teams often hire fewer specialized roles and have one person wear multiple hats:

| Team size | Typical role mix |
|-----------|------------------|
| 1–2 person team | "Data Analyst" doing all five jobs |
| 3–5 | + Data Engineer + Analytics Engineer |
| 5–15 | + dedicated Data Scientist, Business Analysts |
| 15+ | Specialized teams per role + ML Engineers, Data PM |

The compression flows upward: junior generalist → multi-hat senior → specialist as team grows.

### When to hire which

| Symptom | Hire |
|---------|------|
| "Our data pipelines keep breaking" | Data Engineer |
| "Every dashboard contradicts another" | Analytics Engineer |
| "We can't see what's happening week-to-week" | Data Analyst |
| "Marketing and Sales disagree on the same metric" | Business Analyst |
| "We want to predict customer churn / build a recommender" | Data Scientist |
| "Our model works in a notebook but not in production" | ML Engineer |

### Career paths

Common trajectories:

- **Analyst → Senior Analyst → Analytics Engineer → Data Lead → Director**
- **Data Scientist → Senior DS → ML Engineer → ML Platform Lead**
- **Business Analyst → Product Analyst → Product Manager (data-leaning)**
- **Data Engineer → Senior DE → Data Platform Lead → CTO-track**

The roles are not silos — moves between them are common, especially in mid-career.

## Key Parameters

- **Role clarity per hire**: write the exact responsibilities before posting; mismatched expectations cause turnover
- **Pairing**: a Data Analyst + Analytics Engineer pairing produces 3× the output of either alone
- **Hiring sequence**: typical first 5 hires — Analyst, Engineer, Analytics Engineer, Analyst, Scientist
- **Reporting structure**: data team often best reports to a Chief Data Officer or COO, not buried under engineering or finance

## When To Use

- **Org design discussions**: clarify role boundaries before hiring
- **Team scaling decisions**: identify which role is the bottleneck
- **Career planning**: choose the lane that fits your strengths
- **Job description writing**: use the construction metaphor to communicate the role
- Anti-pattern: hiring a "Data Scientist" when the actual need is dashboard work — frustrates both sides
- Anti-pattern: one person doing all five roles long-term — burnout, quality suffers

## Connections

- Related: [[Data Professional Role and Collaboration]] (the bridge function across all roles), [[Data Team Maturity Evolution]] (how the mix scales), [[Data Platform Overview]] (the tech that each role works on), [[Data Lifecycle]] (which role owns which stage)
- Builds on: organizational behavior fundamentals
- Compare with: software engineering team composition (frontend, backend, DevOps, SRE) — similar specialization pattern
- Used by: every CDO building their team; every analyst planning a career

## My Notes

- Analytics Engineer is the newest of these roles and the highest-leverage hire for most mid-stage data teams. Many companies still under-hire it.
- Practice: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283) — for a fictional 8-person data team supporting a 200-person company, write the role allocation and justify each.
- Interview tip: when discussing your current role, use the construction metaphor — clarifies what you actually do without title confusion.
- The boundary between "Analytics Engineer" and "Data Analyst" is fluid; in some companies they are the same person; in others they are deliberately split. Both terms are correct for the same person if the work matches.
