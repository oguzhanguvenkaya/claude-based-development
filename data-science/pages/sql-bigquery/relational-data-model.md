---
title: "Relational Data Model"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/02-tablolar-anahtarlar]]"
tags:
  - sql
  - relational-model
  - primary-key
  - foreign-key
  - schema
---

# Relational Data Model

> One-line summary: A database structure where data is stored in tables of rows and columns, with strict type rules and explicit relationships enforced by primary and foreign keys.

## Core Concept

The relational model organizes data into **tables** (also called relations). Each table represents one type of entity — customers, orders, products — and stores instances of that entity as rows. Unlike spreadsheets, relational tables enforce structural discipline: every column has a fixed data type, and every row must have a unique identifier. This discipline is what enables databases to scale to millions of rows while staying fast and consistent.

Relationships between tables are not implicit (as in a spreadsheet) but explicit, declared via **keys**. This lets the database engine optimize queries, enforce referential integrity, and prevent orphaned records.

## How It Works

A table has three core building blocks:

| Element | Description | Example |
|---------|-------------|---------|
| **Row** (record) | One instance of an entity | A single customer |
| **Column** (field) | One attribute of the entity, with a fixed type | `email VARCHAR`, `signup_date DATE` |
| **Cell** | The intersection of a row and column | `"alice@example.com"` |

Rules of the model:
- One value per cell (no lists, no nested objects in classical SQL)
- All values in a column share the same data type ([[SQL Data Types and Casting]])
- Row order is **not** guaranteed unless you explicitly request it with [[Column Aliasing and Ordering]]

### Primary Key (PK)

A column (or combination of columns) that **uniquely identifies each row**. Common examples: `customer_id`, `order_number`. A PK cannot be NULL and cannot repeat. It is the identity card of the row.

### Foreign Key (FK)

A column that **references the PK of another table**, creating a relationship. Example: an `orders` table has a `customer_id` FK pointing to `customers.customer_id`. This links each order to the customer who placed it.

```sql
-- Conceptual: customers table
customer_id (PK) | name      | city
1                | Alice     | New York
2                | Bob       | Boston

-- orders table — customer_id is a FK
order_id (PK) | customer_id (FK) | amount
101           | 1                | 250.00
102           | 1                | 49.99
103           | 2                | 120.00
```

## Key Parameters

- **NOT NULL** constraint: a column that must always have a value (used for PKs and any required field)
- **UNIQUE** constraint: enforces that values do not repeat, even if not a PK
- **Composite PK**: a primary key built from multiple columns when no single column is unique (common in junction tables)
- **Referential integrity**: the database refuses inserts/updates that would create an FK pointing to a non-existent PK

## When To Use

- **Always** for transactional data with clear entities and relationships (customers ↔ orders ↔ products)
- When you need data consistency guarantees (banking, inventory, billing)
- When multiple users/applications read and write the same data and you cannot afford spreadsheet-style corruption
- **Anti-pattern**: Don't use a relational model for purely hierarchical or graph-shaped data where every query traverses many relationships — graph databases (Neo4j) fit better

## Connections

- Related: [[Entity Relationship Diagrams]] (visual notation for the model), [[OLTP vs OLAP]] (when relational shines)
- Builds on: Set theory (rows are sets, no duplicates), basic typing
- Compare with: Spreadsheets (no key enforcement), document stores (nested data)
- Used by: [[Select Statement]], [[Joins Fundamentals]] (FK ↔ PK relationships drive JOIN), [[Create Update Delete]]
- Validated by: [[Primary Key Test]] (the test that proves PK uniqueness in production)

## My Notes

- A spreadsheet works until it doesn't — the moment you need to join multiple sheets reliably, you need a relational model
- Practice: [CRM Kampanya Verisi ile Temel SQL İşlemleri](https://nextgen.workintech.com.tr/project/202/1?pid=7523) — exercises basic table reading
- Interview gotcha: "Can a table have no primary key?" Technically yes, but it is almost always a design smell. Without a PK, you cannot reliably identify or update a specific row.
- Foreign keys are not automatically created — you have to define them. Tools like dbt often omit them and rely on tests instead.
