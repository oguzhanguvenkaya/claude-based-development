---
title: "Data Science Wiki — Index"
domain: data-science
updated: 2026-05-11
total_pages: 46
---

# Data Science Wiki — Index

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

## Python Data Tools
<!-- Pages about pandas, numpy, scikit-learn, visualization -->

## Projects
<!-- Kaggle guides, EDA checklists, project templates -->
