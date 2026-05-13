---
title: "Data Science Wiki — Index"
domain: data-science
updated: 2026-05-11
total_pages: 82
---

# Data Science Wiki — Index

## Data Analysis

### Sprint 1 Wrap-Up Umbrella
- [[Sprint 1 Data Analytics Fundamentals Overview]] — Complete map of all 25 Sprint 1 pages across the 4 lessons

### Google Sheets Fundamentals (Sprint 1 / Lesson 1)
- [[Google Sheets Analytics Overview]] — Umbrella + Sheets ↔ SQL concept bridge
- [[Data Analysis Workflow]] — The 7-step methodology (ask → identify → choose type → explore → clean → summarize → visualize)
- [[Importing Data to Sheets]] — CSV import, IMPORTRANGE for live links
- [[Data Exploration and Cleaning Sheets]] — EDA + cleaning techniques (TRIM, UPPER, deduplication)
- [[Lookup Functions Sheets]] — XLOOKUP, VLOOKUP, INDEX-MATCH compared
- [[Pivot Tables Sheets]] — The spreadsheet equivalent of GROUP BY
- [[Filter Query Unique Sheets]] — FILTER, QUERY (SQL-in-Sheets), UNIQUE
- [[Data Visualization Sheets]] — Charts, slicers, dashboards

### Workflow Deep Dive + KPI Fundamentals (Sprint 1 / Lesson 2)
- [[Seven Step Framework in Practice]] — All 7 steps walked through narratively (GreenFit case)
- [[KPI Fundamentals]] — What is a KPI, KPI vs metric, vanity metrics, lead vs lag indicators
- [[Finance KPIs]] — Gross margin, net margin, profitability fundamentals
- [[Inventory KPIs]] — Stockout rate, days of supply, carrying cost trade-off
- [[Quality KPIs]] — Return rate, returns by reason, financial impact of returns

### Advanced KPI Strategy + Customer Analytics (Sprint 1 / Lesson 3)
- [[KPI by Business Model]] — B2C vs B2B, transactional vs subscription, maturity stage
- [[KPI by Team and Function]] — Per-team KPI design and the North Star dashboard pattern
- [[Vanity Metrics Anti Patterns]] — Avoiding metrics that flatter but don't drive action; Goodhart's Law
- [[Customer Acquisition and Expansion Funnels]] — Acquisition channels, CAC, retention, LTV, NRR
- [[Customer Segmentation Rfm]] — Recency/Frequency/Monetary scoring with named segments
- [[Cohort Analysis]] — Time-based grouping to reveal trends that averages hide

### Data Ecosystem, Roles, and Real-World Cases (Sprint 1 / Lesson 4)
- [[Data Professional Role and Collaboration]] — The translator/bridge role + 4-step business↔data collaboration framework
- [[Data Lifecycle]] — Six stages: collect → store → clean → transform → analyze → feedback
- [[Data Team Roles and Responsibilities]] — Engineer / Analytics Engineer / Analyst / BA / Scientist / ML Engineer (construction crew metaphor)
- [[Data Team Maturity Evolution]] — Early → Growth → Mature: how teams scale with company size
- [[Real World Data Analytics Case Studies]] — Museum, Nestlé, Vodafone, US grocery chain

## Statistics
- [[Descriptive Statistics]] — Methods for summarizing datasets using central tendency, spread, and shape
- [[Measures of Central Tendency]] — Mean, median, and mode with outlier sensitivity comparison
- [[Measures of Spread]] — Variance, standard deviation, range, and IQR for quantifying dispersion

## Machine Learning
<!-- Pages about supervised, unsupervised, ensemble, and deep learning -->

## Math Foundations
<!-- Pages about linear algebra, calculus, optimization, probability -->

## SQL & BigQuery

### Foundation
- [[SQL Fundamentals Overview]] — Umbrella: map of all foundational SQL concepts in one entry-point page
- [[Relational Data Model]] — Tables, rows, columns, primary keys, foreign keys
- [[OLTP vs OLAP]] — Operational vs analytical databases, the two worlds an analyst inhabits
- [[Entity Relationship Diagrams]] — Visual notation for documenting and designing schemas
- [[SQL Data Types and Casting]] — Types as contracts; CAST/SAFE_CAST for conversions

### Reading Data
- [[Select Statement]] — The verb of every query; choose columns and tables
- [[Distinct and Deduplication]] — Collapse duplicate rows with DISTINCT
- [[Filtering Where]] — WHERE with AND/OR/NOT/BETWEEN for row-level filtering
- [[Pattern Matching SQL]] — LIKE and REGEXP for fuzzy text search
- [[In and Not In]] — Set membership; replaces long OR chains
- [[Column Aliasing and Ordering]] — AS for renaming, ORDER BY for sorting

### Per-Row Logic
- [[Conditional Expressions SQL]] — CASE WHEN and IF for derived columns and bucket labels
- [[Null Handling SQL]] — Three-valued logic, IS NULL, COALESCE, SAFE_CAST

### Writing Data
- [[Create Update Delete]] — DDL (CREATE/ALTER/DROP) and DML (INSERT/UPDATE/DELETE)

### Aggregation and Scalar Functions
- [[SQL Computed Data Overview]] — Umbrella for aggregation + scalar function families
- [[Count and Countif]] — COUNT variants and conditional row counting
- [[Sum Avg Min Max]] — The four canonical numeric aggregates
- [[Safe Divide]] — SAFE_DIVIDE to avoid divide-by-zero errors
- [[Group By]] — Bucket rows so aggregates compute per category
- [[Where vs Having]] — Pre-aggregation vs post-aggregation filtering
- [[Numeric Functions Round]] — ROUND, CEIL, FLOOR, TRUNC, ABS for number formatting
- [[String Concatenation Concat]] — CONCAT for building composite strings
- [[String Cleaning Replace and Case]] — REPLACE, LOWER, UPPER, INITCAP for text normalization
- [[Date Arithmetic Date Sub]] — DATE_SUB / DATE_ADD / DATE_DIFF for time-window logic

### Joins
- [[Joins Fundamentals]] — JOIN, ON clause, table aliasing
- [[Join Types]] — INNER, LEFT, RIGHT, FULL OUTER and when to use each
- [[Multiple Joins]] — Chaining 3+ tables (star-schema queries)
- [[Joins with Group By]] — Aggregating after a JOIN; avoiding common GROUP BY errors
- [[Join Pitfalls Grain and Fan Out]] — Mismatched grain, fan-out, and silent row drops

### Data Quality Testing
- [[Testing Data Pipelines]] — Why test data; the three test families (hub)
- [[Primary Key Test]] — Verifying uniqueness of the PK
- [[Column Test]] — NULL checks, range checks, accepted values
- [[Value Preservation Test]] — Confirming aggregates survive JOINs and transforms

### Query Composition & Style
- [[Common Table Expressions Cte]] — WITH AS for named multi-step queries
- [[Nested Subqueries]] — Subqueries in WHERE / FROM / SELECT
- [[Join vs Subquery]] — Choosing between JOIN, IN-subquery, EXISTS, and CTEs
- [[Union Operator]] — UNION and UNION ALL for vertical row stacking
- [[Bigquery Insert with Cast Workflow]] — INSERT INTO + SAFE_CAST ingestion pattern
- [[Clean Sql Style Guide]] — Naming, indentation, comments, linting

### Functions and Window Functions
- [[Functions in SQL Overview]] — Four function families (scalar, aggregate, window, UDF) — taxonomy hub
- [[User Defined Functions Udf]] — CREATE FUNCTION (persistent and TEMP)
- [[Window Functions Fundamentals]] — PARTITION BY, OVER, ranking, running totals
- [[Window Functions Across Grain]] — Allocating coarse totals across fine-grained rows

### Data Warehouse Architecture & Economics (Sprint 3 / Lesson 1)
- [[Data Warehouse Economics Overview]] — Umbrella: architecture + cost map
- [[Data Platform Overview]] — Five-layer modern data stack (sources → ingestion → storage → transform → consumption)
- [[Data Pipeline Architecture]] — Bronze/Silver/Gold medallion + transformation stages
- [[SQL Views in Pipelines]] — Views as reusable SQL recipes; materialized views
- [[Views vs Tables Tradeoffs]] — Storage vs compute decision per pipeline step
- [[Hybrid Table View Pipeline Pattern]] — Canonical production mix
- [[Warehouse Storage vs Compute Cost]] — The two-meter cost model
- [[Warehouse Pricing Models]] — On-demand vs flat-rate reservations
- [[Modern Warehouse Comparison]] — BigQuery / Snowflake / Redshift / Databricks
- [[Bigquery Query Cost Model]] — What BigQuery charges + columnar storage implications
- [[Partitioning and Clustering]] — The biggest scan-cost reducer

## Python Data Tools
<!-- Pages about pandas, numpy, scikit-learn, visualization -->

## Projects
<!-- Kaggle guides, EDA checklists, project templates -->
