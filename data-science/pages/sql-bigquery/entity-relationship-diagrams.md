---
title: "Entity Relationship Diagrams"
domain: data-science
category: sql-bigquery
created: 2026-05-11
updated: 2026-05-11
sources:
  - "[[raw/course-notes/sprint 2/01-sql-temelleri/transcripts/04-entity-iliski-diyagramlari-erd]]"
tags:
  - sql
  - erd
  - data-modeling
  - schema-design
---

# Entity Relationship Diagrams

> One-line summary: A visual notation for describing the entities in a database and the relationships between them, used to design and document schemas before writing SQL.

## Core Concept

An **Entity Relationship Diagram (ERD)** is the blueprint of a relational schema. Each box represents an entity (a table), each line represents a relationship between entities, and annotations on the lines describe **cardinality** — how many rows in one table can connect to rows in another.

A useful mental model: the database is a city, each table is a building, each row is a person inside, the primary key is their ID card, and foreign keys are the streets that connect buildings. The ERD is the city map.

## How It Works

### Components

| Element | Notation | Meaning |
|---------|----------|---------|
| **Entity** | Rectangle | A table (Customer, Order, Product) |
| **Attribute** | Listed inside the box | A column (often with type and key marker) |
| **Primary key** | Underlined or marked `PK` | The unique identifier |
| **Foreign key** | Marked `FK` | Reference to another table |
| **Relationship** | Line connecting two entities | "Customer places Order" |
| **Cardinality** | Crow's foot, `1`, `N` | How many rows can relate to how many |

### Cardinality types

- **One-to-One (1:1)** — one row in A relates to exactly one row in B. Rare; usually a sign that the two tables should be merged.
- **One-to-Many (1:N)** — one row in A relates to many in B. The most common pattern. One Customer has many Orders.
- **Many-to-Many (N:N)** — rows in both tables relate to many on the other side. Implemented with a **junction table** (e.g., `students` ↔ `enrollments` ↔ `courses`).

### Example ERD (text rendering)

```
┌──────────────┐         ┌──────────────┐
│   CUSTOMER   │         │    ORDER     │
├──────────────┤  1   N  ├──────────────┤
│ customer_id PK├────────│ order_id PK  │
│ name          │         │ customer_id FK│
│ city          │         │ amount       │
│ signup_date   │         │ order_date   │
└──────────────┘         └──────────────┘
```

Reading this: one customer can place many orders, but each order belongs to exactly one customer.

## Key Parameters

- **Logical vs physical ERD**: logical describes business entities (no DB-specific types); physical adds DB types, indexes, partitions
- **Conceptual model**: even higher level — just entities and verbs, no attributes
- **Notation styles**: Chen (academic), Crow's Foot (industry standard), UML class diagrams

## When To Use

- **Schema design**: before writing CREATE TABLE statements, sketch the ERD to catch missing relationships
- **Onboarding**: a good ERD is the fastest way for a new analyst or engineer to understand a database
- **Refactoring**: when changing schemas, the ERD shows downstream impact
- **Querying**: when you don't know how two tables connect, look at the ERD to find the join path
- **Anti-pattern**: trying to fit everything into one diagram. Large schemas (50+ tables) need ERDs split by domain (orders, inventory, marketing).

## Connections

- Related: [[Relational Data Model]] (ERD is the visual layer on top of it)
- Builds on: Set theory and graph thinking
- Compare with: Data flow diagrams (process focus) vs ERDs (state focus)
- Used by: Schema design, [[Joins Fundamentals]] and [[Multiple Joins]] (joins follow the FK paths drawn in the ERD)

## My Notes

- Tools: dbdiagram.io, Lucidchart, DrawSQL, ERAlchemy. For BigQuery, the Console has a schema browser but no native ERD view.
- A well-drawn ERD will reveal modeling bugs before they hit production. Spend the 30 minutes.
- Practice: when working on [Carrefour CRM İstekleri](https://nextgen.workintech.com.tr/project/202/1?pid=7556), draft an ERD of the tables involved before writing JOINs.
- Interview tip: be ready to walk through an ERD verbally — "Customer has many Orders, each Order has many Line Items..." This builds trust faster than SQL trivia.
