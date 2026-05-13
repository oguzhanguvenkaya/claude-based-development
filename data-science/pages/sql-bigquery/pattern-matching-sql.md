---
title: "Pattern Matching SQL"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/09-desen-eslestirme-pattern-matching]]"
tags:
  - sql
  - like
  - pattern-matching
  - regex
  - string-search
---

# Pattern Matching SQL

> One-line summary: The LIKE operator filters string columns using wildcard patterns (% for any sequence, _ for any single character), enabling fuzzy text search without writing dozens of OR clauses.

## Core Concept

When you want "all customers whose name starts with C" or "all emails on the gmail domain," exact equality (`=`) is the wrong tool. **Pattern matching** lets you describe the shape of the string you are looking for, and the database finds every row whose value fits that shape.

`LIKE` is the basic operator. For more complex patterns, modern SQL engines (including BigQuery) support full regular expressions via `REGEXP_CONTAINS` and friends.

## How It Works

### LIKE with two wildcards

| Wildcard | Meaning |
|----------|---------|
| `%` | Zero or more characters (any length) |
| `_` | Exactly one character |

```sql
-- Names starting with C
SELECT * FROM customers WHERE first_name LIKE 'C%';
-- Matches: Clara, Chris, Charlotte

-- Names ending with 'son'
SELECT * FROM customers WHERE last_name LIKE '%son';
-- Matches: Anderson, Johnson, Wilson

-- Names containing 'ann' anywhere
SELECT * FROM customers WHERE first_name LIKE '%ann%';
-- Matches: Joanna, Anna, Hannah, Annabelle

-- Names of exactly 5 letters
SELECT * FROM customers WHERE first_name LIKE '_____';
-- Matches: Clara, Henry, James (NOT Alex or Charlotte)

-- Names starting with 'J' and exactly 4 letters long
SELECT * FROM customers WHERE first_name LIKE 'J___';
-- Matches: John, Jake, Jane
```

### Case sensitivity

Standard SQL is case-sensitive on string comparisons in most engines (BigQuery is case-sensitive). To match case-insensitively:

```sql
-- BigQuery / PostgreSQL approach
SELECT * FROM customers WHERE LOWER(first_name) LIKE 'c%';

-- Some engines support ILIKE
SELECT * FROM customers WHERE first_name ILIKE 'c%';  -- PostgreSQL
```

### NOT LIKE

```sql
SELECT * FROM emails WHERE address NOT LIKE '%@spam.com';
```

### Escaping wildcards

If your search target contains a literal `%` or `_`, escape it:

```sql
WHERE comment LIKE '50\%%' ESCAPE '\';  -- finds "50%..."
```

### Regular expressions (BigQuery)

For complex patterns, REGEXP is far more powerful:

```sql
-- All phone numbers in the format XXX-XXX-XXXX
SELECT * FROM customers
WHERE REGEXP_CONTAINS(phone, r'^\d{3}-\d{3}-\d{4}$');

-- Email validation (simplified)
WHERE REGEXP_CONTAINS(email, r'^[^@]+@[^@]+\.[^@]+$');
```

## Key Parameters

- **`%` is greedy**: matches as much as possible
- **`_` is exact-one**: useful for fixed-width fields like ISO country codes (`_ _`)
- **Anchors**: LIKE patterns are implicitly anchored to the whole string; `LIKE 'C'` matches only the single character C, not strings starting with C
- **Performance**: leading-wildcard patterns (`LIKE '%abc'`) cannot use a standard index and trigger a full scan — costly on large tables
- **REGEXP power**: anchors (`^`, `$`), character classes (`[a-z]`), quantifiers (`+`, `*`, `?`, `{n,m}`), alternation (`|`)

## When To Use

- **LIKE**: simple prefix/suffix/contains searches in queries written by humans
- **REGEXP**: data validation, parsing semi-structured text, extracting substrings
- **Search bars**: implementing a "type to filter" feature in a small dataset
- Anti-pattern: `LIKE '%name%'` on a 100M-row table — use a full-text search index (BigQuery Search Index, Postgres tsvector) instead
- Anti-pattern: trying to parse complex hierarchical data (JSON, XML) with REGEXP — use the proper JSON/XML functions

## Connections

- Related: [[Filtering Where]] (LIKE is a comparison operator inside WHERE), [[In and Not In]] (use IN for finite lists, LIKE for shapes)
- Builds on: string operations, basic regex theory
- Compare with: full-text search engines (Elasticsearch, BigQuery Search) — built for `%text%` patterns at scale
- Used by: data cleaning, email/phone normalization

## My Notes

- The single most common LIKE bug: forgetting that `_` is a wildcard and getting unexpected matches on underscored column names like `user_name`.
- Practice: in [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), use LIKE to filter customers by name prefix or city pattern.
- BigQuery tip: `STARTS_WITH(col, 'C')` is sometimes faster and clearer than `col LIKE 'C%'`.
- Interview tip: know when to switch from LIKE to REGEXP — when the pattern has alternation, character classes, or repetitions.
