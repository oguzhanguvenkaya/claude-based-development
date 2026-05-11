---
title: "String Cleaning Replace and Case"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/09-sutunlardaki-metinleri-degistirme]]"
  - "[[raw/course-notes/sprint 2/02-sql-hesaplanmis-veriler/transcripts/10-buyuk-kucuk-harf-bicimi]]"
tags:
  - sql
  - string-cleaning
  - replace
  - upper
  - lower
  - initcap
  - normalization
---

# String Cleaning Replace and Case

> One-line summary: REPLACE substitutes substrings; LOWER, UPPER, and INITCAP normalize letter case — together they are the standard toolkit for cleaning inconsistent text before joins and analysis.

## Core Concept

Real-world string data is messy. "New York", "new york", "NEW YORK", and "new  york" all refer to the same city but compare as different values. Inconsistent text breaks joins, breaks GROUP BY, and produces misleading aggregates.

Two complementary tools fix this: **REPLACE** edits the content of strings, and **case functions** (LOWER, UPPER, INITCAP) enforce a single capitalization style. Apply them once during ingestion or in a CTE, and downstream analytics gets a clean canonical form.

## How It Works

### REPLACE — substitute substrings

```sql
SELECT REPLACE('Hello, World!', 'World', 'SQL') AS greeting;
-- "Hello, SQL!"
```

`REPLACE(source, target, replacement)` substitutes every occurrence of `target` with `replacement`.

```sql
-- Strip a prefix
SELECT REPLACE(sku_code, 'PROD-', '') AS sku_short FROM products;

-- Standardize separators
SELECT REPLACE(phone, '.', '-') AS phone_normalized FROM customers;

-- Remove characters
SELECT REPLACE(REPLACE(price_text, '$', ''), ',', '') AS price_str FROM raw_data;
-- "$1,234.56" → "1234.56"  (now ready for CAST)
```

Nested REPLACE is the common idiom for stripping multiple characters. For complex patterns, switch to [[Pattern Matching SQL]] with `REGEXP_REPLACE`.

### LOWER / UPPER

```sql
SELECT
  LOWER(email)       AS email_normalized,    -- "alice@example.com"
  UPPER(country_code) AS country_normalized  -- "US"
FROM customers;
```

`LOWER` and `UPPER` are usually paired with comparisons or joins:

```sql
-- Case-insensitive join
SELECT *
FROM purchases p
JOIN crm_leads c ON LOWER(p.email) = LOWER(c.email);
```

### INITCAP — title case

```sql
SELECT INITCAP('alice WANG-smith') AS display_name;
-- "Alice Wang-Smith"
```

Capitalizes the first letter of each word. Useful for display fields where users entered names in mixed cases. INITCAP is in BigQuery and PostgreSQL; some engines lack it.

### Combining for canonical form

```sql
SELECT
  TRIM(LOWER(REPLACE(REPLACE(email, ' ', ''), '\t', ''))) AS email_clean
FROM raw_leads;
```

Strip whitespace and tabs, lowercase. Resulting strings join reliably with any other clean source.

### Real-world: cleaning a join key

```sql
-- Before cleaning — only some rows match
SELECT COUNT(*) FROM purchases p
JOIN crm_leads c ON p.email = c.email;
-- Returns 10,000 (out of 50,000 purchases)

-- After cleaning — most rows match
SELECT COUNT(*) FROM purchases p
JOIN crm_leads c ON LOWER(TRIM(p.email)) = LOWER(TRIM(c.email));
-- Returns 45,000
```

The 35,000-row jump came entirely from case and whitespace differences.

## Key Parameters

- **REPLACE is case-sensitive**: `REPLACE('Apple', 'apple', 'X')` returns `Apple` unchanged
- **REPLACE replaces all occurrences** in the string, not just the first
- **TRIM**: a related function that strips leading/trailing whitespace; often paired with these
- **NULL behavior**: input NULL → output NULL
- **REGEXP_REPLACE**: pattern-based REPLACE for complex transformations
- **Performance**: applying these in WHERE / JOIN disables index use; precompute in a CTE or as a materialized column for large tables

## When To Use

- Normalizing email, phone, country code, SKU before joining or grouping
- Removing currency symbols and separators before CAST to NUMERIC
- Building canonical display names (INITCAP)
- Pre-processing user-typed search input ("nyc" → match "NYC", "New York City")
- Anti-pattern: cleaning the same column repeatedly in every query — clean once in a staging layer
- Anti-pattern: REPLACE for pattern-based edits — use REGEXP_REPLACE for anything that needs wildcards

## Connections

- Related: [[String Concatenation Concat]] (clean each part, then assemble), [[Pattern Matching SQL]] (REGEXP for more complex string ops), [[Null Handling SQL]] (cleaning often deals with empty strings vs NULL), [[Distinct and Deduplication]] (case-normalized values dedupe correctly)
- Builds on: string fundamentals
- Compare with: `TRIM`, `LPAD`, `RPAD`, `SUBSTR`, `REGEXP_REPLACE` — the rest of the string toolkit
- Used by: every analysis that joins or groups by text columns, every customer-data deduplication pipeline

## My Notes

- Email canonicalization is the highest-ROI cleaning step in customer analytics — most "missing" customer matches come from case or whitespace.
- Practice: [Circle Teslimat Takibi](https://nextgen.workintech.com.tr/project/202/2?pid=7596) — clean address strings before grouping by city.
- BigQuery tip: `NORMALIZE(text, NFKC)` handles unicode normalization (e.g., curly quotes vs straight, accented characters) — sometimes needed for international data.
- Interview tip: when asked about a low join-match rate, "are you normalizing case and trimming whitespace?" is almost always the right first question.
