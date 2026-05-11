---
title: "Data Science Wiki — Log"
domain: data-science
updated: 2026-05-11
---

# Data Science Wiki — Log

## [2026-04-12] system | Wiki Initialized
- Domain wiki created with categories: statistics, machine-learning, math-foundations, sql-bigquery, python-data, projects
- Schema defined in CLAUDE.md
- Ready for first ingest

## [2026-04-12] ingest | Course Notes: Introduction to Descriptive Statistics
- Source: [[raw/course-notes/intro-to-descriptive-statistics]]
- Pages created: [[Descriptive Statistics]], [[Measures of Central Tendency]], [[Measures of Spread]]
- Pages updated: None (first ingest — no existing pages to revise)
- Key takeaways: Three pillars of descriptive stats (central tendency, spread, shape); mean vs median for skewness detection; IQR 1.5x rule for outlier detection; Bessel's correction for sample variance

## [2026-05-11] ingest | Sprint 2 / Lesson 1 — SQL'in Temelleri
- Source: `raw/course-notes/sprint 2/01-sql-temelleri/transcripts/` (17 transcripts, ~4,400 words)
- Pages created (14):
  - Foundation: [[Relational Data Model]], [[OLTP vs OLAP]], [[Entity Relationship Diagrams]], [[SQL Data Types and Casting]]
  - Reading: [[Select Statement]], [[Distinct and Deduplication]], [[Filtering Where]], [[Pattern Matching SQL]], [[In and Not In]], [[Column Aliasing and Ordering]]
  - Per-row logic: [[Conditional Expressions SQL]], [[Null Handling SQL]]
  - Writing: [[Create Update Delete]]
  - Umbrella: [[SQL Fundamentals Overview]]
- Pages revised (3):
  - [[Descriptive Statistics]] — added "Computed in SQL via" link
  - [[Measures of Central Tendency]] — added AVG/median SQL note
  - [[Measures of Spread]] — added STDDEV/VARIANCE/IQR SQL note
- Wikilinks added: ~40 new cross-references (mostly within sql-bigquery; 3 reverse links from statistics)
- Key takeaways:
  - SQL is declarative; engine handles execution. Order of evaluation differs from order of writing (FROM → WHERE → SELECT → ORDER BY)
  - Three-valued logic: NULL propagates through comparisons; use IS NULL, not = NULL
  - DISTINCT operates on the **combination** of all SELECT columns, not just one
  - SAFE_CAST replaces CAST when ingestion data may be malformed
  - BigQuery is OLAP; queries on it should not assume OLTP-style transactions
- Open questions:
  - JOIN concepts referenced multiple times but live in Lesson 3 (Sprint 2/3) — will create `joins.md` then
  - GROUP BY referenced multiple times; lives in Sprint 2/2 — will create on next ingest
- Next: Sprint 2 / Lesson 2 — SQL'de Hesaplanmış Veriler (aggregations, GROUP BY)

## [2026-05-11] ingest | Sprint 2 / Lesson 2 — SQL'de Hesaplanmış Veriler
- Source: `raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/` (11 transcripts, ~3,900 words)
- Pages created (10):
  - Aggregation: [[Count and Countif]], [[Sum Avg Min Max]], [[Safe Divide]]
  - Grouping: [[Group By]], [[Where vs Having]]
  - Scalar functions: [[Numeric Functions Round]], [[String Concatenation Concat]], [[String Cleaning Replace and Case]], [[Date Arithmetic Date Sub]]
  - Umbrella: [[SQL Computed Data Overview]]
- Pages revised (7):
  - Lesson 1 cross-links updated: [[Null Handling SQL]], [[Conditional Expressions SQL]], [[Select Statement]], [[Distinct and Deduplication]], [[Filtering Where]], [[SQL Fundamentals Overview]]
  - Statistics linked to specific SQL aggregates: [[Measures of Central Tendency]], [[Measures of Spread]]
- Wikilinks added: ~50 new cross-references; Lesson 1 ↔ Lesson 2 link density now substantial
- Key takeaways:
  - Aggregate functions collapse rows; scalar functions reshape values row by row. This mental model resolves most "GROUP BY error" confusion.
  - WHERE filters rows before grouping; HAVING filters groups after. Always filter earliest possible (WHERE first).
  - SAFE_DIVIDE is the dashboard-safe replacement for `/` — returns NULL instead of crashing on zero denominators.
  - String normalization (LOWER + TRIM + REPLACE) is the highest-ROI cleaning step for any customer-data join.
  - DATE_SUB / DATE_ADD / DATE_DIFF avoid implicit unit assumptions — always specify the unit (DAY, MONTH, YEAR).
- Open questions:
  - JOIN still referenced multiple times — will be created in Sprint 2 / Lesson 3
  - Window functions (`SUM(x) OVER (PARTITION BY y)`) deferred to Lesson 5
- Next: Sprint 2 / Lesson 3 — Tabloları Birleştirmek ve Test Etmek (JOINs and SQL testing)

## [2026-05-11] ingest | Sprint 2 / Lesson 3 — Tabloları Birleştirmek ve Test Etmek
- Source: `raw/course-notes/sprint 2/03-tablolari-birlestirmek-ve-test-etmek/transcripts/` (11 transcripts, ~3,900 words)
- Pages created (9):
  - Joins: [[Joins Fundamentals]] (merged 3 transcripts: intro + syntax + table aliasing), [[Join Types]], [[Multiple Joins]], [[Joins with Group By]], [[Join Pitfalls Grain and Fan Out]]
  - Testing: [[Testing Data Pipelines]] (motivation hub), [[Primary Key Test]], [[Column Test]], [[Value Preservation Test]]
- Pages revised (5):
  - [[Relational Data Model]] — linked to [[Joins Fundamentals]] and [[Primary Key Test]]
  - [[Entity Relationship Diagrams]] — linked to [[Joins Fundamentals]] and [[Multiple Joins]]
  - [[Group By]] — linked to [[Joins with Group By]] and [[Join Pitfalls Grain and Fan Out]]
  - [[Distinct and Deduplication]] — linked to [[Join Pitfalls Grain and Fan Out]]
  - [[SQL Computed Data Overview]] — added next-lesson pointer
- Wikilinks added: ~55 new cross-references (joins family is densely interconnected)
- Key takeaways:
  - JOIN type controls which unmatched rows survive — INNER drops, LEFT keeps left, FULL keeps both
  - Mismatched grain causes fan-out — aggregating after fan-out double-counts; pre-aggregate or use COUNT(DISTINCT)
  - Three test families catch different bugs: PK (uniqueness), column (per-column rules), value preservation (aggregates across joins). All three are needed.
  - The value preservation test catches what no other test does — silent corruption from wrong JOINs
  - In OLAP warehouses (BigQuery), PK constraints are NOT enforced; SQL tests are the only defense
- Open questions:
  - Subqueries / CTEs (WITH AS) — referenced multiple times; lives in Sprint 2/4
  - Window functions — referenced in joins-with-group-by and group-by; lives in Sprint 2/5
- Next: Sprint 2 / Lesson 4 — Subquery ve With As (CTEs and nested queries)

## [2026-05-11] ingest | Sprint 2 / Lesson 4 — Subquery ve With As
- Source: `raw/course-notes/sprint 2/04-subquery-ve-with-as/transcripts/` (6 transcripts, ~3,500 words)
- Pages created (6):
  - Query composition: [[Common Table Expressions Cte]], [[Nested Subqueries]], [[Join vs Subquery]], [[Union Operator]]
  - BigQuery-specific: [[Bigquery Insert with Cast Workflow]]
  - Code quality: [[Clean Sql Style Guide]]
- Pages revised (4):
  - [[Create Update Delete]] — linked to BigQuery INSERT workflow
  - [[Joins Fundamentals]] — linked to subquery alternatives + join-vs-subquery
  - [[In and Not In]] — linked to EXISTS via nested subqueries
  - [[SQL Data Types and Casting]] — linked to ingestion workflow as canonical use case
- Wikilinks added: ~35 new cross-references
- Key takeaways:
  - CTEs (WITH AS) turn deeply nested SQL into top-down narratives — refactor when a query exceeds ~15 lines
  - JOIN vs subquery: JOIN for "pulling multiple columns from another table"; EXISTS/IN-subquery for "filter by existence"; CTE for "multi-step pipelines"
  - `UNION ALL` should be the default — `UNION` silently deduplicates which is rarely what you want
  - `SAFE_CAST` + `REPLACE` is the canonical "parse messy strings to typed columns" pattern for BigQuery ingestion
  - Clean SQL style is the single highest-ROI habit for analytical work — naming, formatting, comments, lint enforcement
- Open questions:
  - Window functions and PARTITION BY — Sprint 2 / Lesson 5 (final SQL lesson)
- Next: Sprint 2 / Lesson 5 — Kullanıcı Tanımlı Fonksiyonlar ve Window Fonksiyonları

## [2026-05-11] ingest | Sprint 2 / Lesson 5 — Kullanıcı Tanımlı Fonksiyonlar ve Window Fonksiyonları
- Source: `raw/course-notes/sprint 2/05-fonksiyonlar-ve-window/transcripts/` (5 transcripts, ~2,300 words)
- Pages created (4):
  - Taxonomy hub: [[Functions in SQL Overview]]
  - UDFs: [[User Defined Functions Udf]]
  - Window functions: [[Window Functions Fundamentals]] (merged motivation + PARTITION BY/OVER), [[Window Functions Across Grain]]
- Pages revised (5):
  - [[Group By]] — concrete window function link instead of "future lesson"
  - [[Joins with Group By]] — linked to window functions and across-grain allocation
  - [[Join Pitfalls Grain and Fan Out]] — linked to across-grain window solution
  - [[Count and Countif]] — linked to window function COUNT variant
  - [[Distinct and Deduplication]] — linked to ROW_NUMBER() pattern
- Wikilinks added: ~30 new cross-references; "future lesson" placeholders resolved
- Key takeaways:
  - Four function families: scalar (row→row), aggregate (rows→row), window (rows→row with row preservation), UDF (your own definition)
  - Window functions = `<aggregate>(...) OVER (PARTITION BY ... ORDER BY ...)` — same partitioning as GROUP BY, but every row survives
  - Window functions are the elegant fix for grain-mismatch fan-out: allocate coarse totals proportionally across fine-grained rows without breaking the sum
  - UDFs (CREATE FUNCTION) package recurring logic — margin formulas, age buckets, classifications; persistent UDFs live in datasets, TEMP UDFs scope to current session
  - ROW_NUMBER, RANK, LAG, LEAD have NO GROUP BY equivalent — they only exist as window functions
- Sprint 2 milestone: **all 5 SQL lessons ingested** ✓ (54 wiki pages in sql-bigquery + statistics)
- Open questions:
  - Sprint 3 Lesson 1 (Advanced SQL: data warehouse cost, views, partitioning) — next iteration
  - Sprint 1 lessons (Google Sheets, KPI, Data Ecosystem) — pending
- Next: Sprint 3 / Lesson 1 — İleri Seviye SQL (Data warehousing, BigQuery cost model, partitioning) OR Sprint 1 / Lesson 1 (Google Sheets)

## [2026-05-12] ingest | Sprint 3 / Lesson 1 — İleri Seviye SQL (Data Warehousing)
- Source: `raw/course-notes/sprint 3/01-ileri-seviye-sql/transcripts/` (13 transcripts, ~6,500 words)
- Pages created (10):
  - Architecture: [[Data Pipeline Architecture]] (01, 02 merged), [[Data Platform Overview]]
  - Materialization: [[SQL Views in Pipelines]], [[Views vs Tables Tradeoffs]] (03, 05, 06 merged), [[Hybrid Table View Pipeline Pattern]]
  - Cost mechanics: [[Warehouse Storage vs Compute Cost]], [[Warehouse Pricing Models]], [[Bigquery Query Cost Model]] (11, 12 merged)
  - Vendors: [[Modern Warehouse Comparison]]
  - Optimization: [[Partitioning and Clustering]]
  - Umbrella: [[Data Warehouse Economics Overview]]
- Pages revised (5):
  - [[OLTP vs OLAP]] — linked to warehouse economics overview + data platform
  - [[SQL Computed Data Overview]] — added Sprint 3 next-pointer
  - [[Create Update Delete]] — linked to Views vs Tables Tradeoffs
  - [[Select Statement]] — linked to BigQuery query cost model (column pruning context)
  - [[Filtering Where]] — linked to Partitioning and Clustering
- Wikilinks added: ~70 new cross-references; Sprint 2 ↔ Sprint 3 link density now substantial
- Key takeaways:
  - **Storage is cheap, compute is expensive, materialization shifts cost between them** — the single mental model that governs all warehouse decisions
  - Bronze/silver/gold medallion architecture is the de facto pipeline standard; each layer has a contract with the next
  - View-only pipelines are simple but recompute on every read; table-only pipelines are fast but stale and storage-heavy; hybrid is the production norm
  - BigQuery prices by **bytes scanned**, primarily driven by **columns selected** (columnar storage) — column pruning + partitioning are 5+ orders of magnitude savings
  - Modern warehouses (BigQuery, Snowflake, Redshift, Databricks) decouple storage and compute — older designs (Redshift legacy) coupled them
  - Partitioning is binary: tables either have it (cheap queries) or don't (expensive queries) — middle ground rare
- Sprint 3 / Lesson 1 milestone: **all warehouse foundations covered** ✓ (10 of remaining 4 lessons cover Git + dbt, which are tooling layers built ON these foundations)
- Open questions:
  - Git/GitHub workflows — Sprint 3 / Lesson 2 (not yet held)
  - dbt models and orchestration — Sprint 3 / Lessons 3-4 (not yet held)
  - Sprint 1 lessons (Google Sheets, KPI, Data Ecosystem) — still pending
- Next: Sprint 1 / Lesson 1 — Google Sheets ile Analizin Temelleri (per user direction "c→a→b")
