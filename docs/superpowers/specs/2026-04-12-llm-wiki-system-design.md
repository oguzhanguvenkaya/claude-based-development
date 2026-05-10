# Personal Knowledge Wiki System (PKWS) — Design Spec

**Date:** 2026-04-12
**Status:** Draft
**Domain:** Multi-domain personal knowledge management
**Pilot:** Data Science wiki

---

## Context

### Problem
The user works across 8+ domains (fullstack dev, data science, AI/ML, cloud, marketing, 3D design, backend, system design) with active projects in each. Knowledge is scattered across GitHub repos, course materials, browser bookmarks, and memory. This fragmentation causes:
- Loss of control over what is known vs. what needs learning
- Inability to leverage cross-domain connections
- Claude Code sessions starting from zero context each time
- No structured learning path or progress tracking

### Solution
Build a **multi-domain LLM Wiki system** inside a single Obsidian vault, based on Andrej Karpathy's LLM Wiki pattern. Each domain gets its own wiki with dedicated schema, index, and content. Claude Code maintains the wiki through structured ingest/query/lint workflows. The system compounds knowledge over time — every source ingested makes future interactions richer and more contextual.

### Inspirations
- **Karpathy's LLM Wiki gist** — 3-layer architecture (raw sources, wiki, schema), ingest/query/lint workflows
- **KJ's AI Second Brain** — Two-layer strategy/project system, Claudian plugin, setup skills
- **Internet Vin (Greg Isenberg podcast)** — Custom thinking commands (/ghost, /challenge, /emerge, /ideas, /connect, /trace), strict human/AI separation, vault-as-context philosophy

---

## Architecture

### Vault Structure

```
claude-based-development/                # Obsidian Vault root
├── CLAUDE.md                            # Global master schema
├── master-index.md                      # Catalog of all domain wikis
├── log.md                               # Global ingest/query/lint log
│
├── _meta/                               # Strategy layer (minimal)
│   ├── goals.md                         # Learning goals & roadmap
│   └── profile.md                       # Skills inventory & competency map
│
├── _templates/                          # Obsidian templates (Templater)
│   ├── wiki-page.md                     # Standard wiki page template
│   ├── raw-source.md                    # Raw source metadata template
│   └── daily-note.md                    # Daily note template
│
├── _skills/                             # Claude Code custom commands
│   ├── ingest.md                        # Source → wiki pages workflow
│   ├── query.md                         # Wiki Q&A workflow
│   ├── lint.md                          # Consistency check workflow
│   ├── ideas.md                         # Cross-domain idea generation
│   ├── challenge.md                     # Belief pressure-testing
│   ├── connect.md                       # Cross-domain bridging
│   ├── gaps.md                          # Knowledge gap detection
│   ├── profile-update.md               # Update skills inventory
│   └── roadmap.md                       # Learning roadmap generation
│
├── data-science/                        # PILOT WIKI
│   ├── CLAUDE.md                        # Domain-specific schema & rules
│   ├── index.md                         # Domain page catalog
│   ├── log.md                           # Domain activity log
│   ├── raw/                             # Unprocessed sources
│   │   ├── course-notes/                # From active data science course
│   │   ├── papers/                      # Academic papers
│   │   └── web-clips/                   # Obsidian Web Clipper output
│   └── pages/                           # Wiki articles
│       ├── statistics/
│       ├── machine-learning/
│       ├── math-foundations/
│       ├── sql-bigquery/
│       ├── python-data/
│       └── projects/
│
├── fullstack-dev/                       # Future wikis (same structure)
├── backend-api/
├── ai-ml/
├── cloud/
├── marketing/
├── 3d-design/
└── system-design/
```

### Three-Layer Model (per Karpathy)

1. **Raw Sources Layer** (`raw/`): Immutable collection of articles, papers, course notes, PDFs. The LLM reads but never modifies these.
2. **Wiki Layer** (`pages/`): LLM-generated and LLM-maintained markdown files. Summaries, concept pages, entity pages, cross-referenced documentation.
3. **Schema Layer** (`CLAUDE.md`): Configuration that defines wiki structure, conventions, and workflows. One global + one per domain.

---

## Wiki Page Format

Every wiki page follows this structure:

```markdown
---
title: "Page Title"
domain: data-science
category: machine-learning
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[raw/source-file-name]]"
tags:
  - tag1
  - tag2
---

# Page Title

> One-line summary: Concise description of what this page covers.

## Core Concept
[Main explanation — clear, practical, in your own words]

## How It Works
[Technical details, algorithms, processes]

## Key Parameters / Components
[Important variables, settings, configurations]

## When To Use
[Use cases, advantages, disadvantages, decision criteria]

## Connections
- Related: [[Related Page 1]], [[Related Page 2]]
- Builds on: [[Prerequisite Concept]]
- Compare with: [[Alternative Approach]]

## My Notes
[Personal observations, course insights, practical experience]
```

### Page Rules
- One-line summary at the top (helps LLM decide relevance without reading full page)
- Max ~1000 words per page (focused, not catch-all)
- Use `[[wikilinks]]` for all cross-references
- Cite sources via frontmatter `sources` field
- Consistent tagging with domain vocabulary
- English content (technical terms stay natural)

---

## Index Format

### Master Index (`master-index.md`)

```markdown
# Master Wiki Index

Last updated: YYYY-MM-DD

## Active Wikis

| Wiki | Pages | Last Updated | Focus |
|------|-------|-------------|-------|
| [[data-science/index]] | N | YYYY-MM-DD | Statistics, ML, SQL, Python |
| [[fullstack-dev/index]] | - | - | Not started |
| [[ai-ml/index]] | - | - | Not started |
```

### Domain Index (`data-science/index.md`)

```markdown
# Data Science Wiki — Index

Last updated: YYYY-MM-DD
Total pages: N

## Statistics
- [[Descriptive Statistics]] — Mean, median, mode, variance, std dev
- [[Probability Distributions]] — Normal, binomial, Poisson, exponential

## Machine Learning
- [[Random Forest]] — Ensemble method using bootstrap + decision trees
- [[Linear Regression]] — Baseline supervised learning model
```

One-line summaries per entry. Organized by category. Updated on every ingest.

---

## Log Format

```markdown
# Data Science Wiki — Log

## [2026-04-12] ingest | Week 5 Course Notes: Ensemble Methods
- Source: [[raw/course-notes/week-5-ensemble-methods]]
- Pages created: [[Random Forest]], [[Bagging]]
- Pages updated: [[Decision Trees]] (added ensemble context), [[index]]
- Key takeaways: Random forests reduce overfitting through feature randomization

## [2026-04-12] query | "When should I use Random Forest vs XGBoost?"
- Pages consulted: [[Random Forest]], [[Gradient Boosting]], [[XGBoost]]
- Answer quality: High — saved as [[RF vs XGBoost Comparison]]
```

Append-only. Chronological. Parseable by Unix tools.

---

## Workflows

### 1. Ingest Workflow

**Trigger:** User adds a source to `raw/` and runs `/ingest`

```
User adds source to raw/ → /ingest command
  → Claude reads the source
  → Discusses key takeaways with user
  → Creates new wiki pages for new concepts
  → CRITICAL: Revises 10-15 existing related pages
    (add new context, update cross-references, note connections)
    This is the compounding mechanism — every ingest enriches the whole wiki
  → Adds [[wikilinks]] to connect new and updated pages
  → Updates domain index.md with new/changed entries
  → Appends entry to domain log.md (pages created + pages updated)
  → Reports summary of all changes
```

### 2. Query Workflow

**Trigger:** User asks a question via `/query`

```
User asks question → /query command
  → Search index.md for relevant pages
  → (Future: qmd MCP for semantic search)
  → Read relevant wiki pages
  → Synthesize answer with [[page]] citations
  → If answer is high quality → offer to save as new wiki page
  → Append query to log.md
```

### 3. Lint Workflow

**Trigger:** User runs `/lint` periodically (e.g., weekly)

```
/lint command
  → Scan all pages for:
    - Contradictions between pages
    - Orphan pages (no incoming wikilinks)
    - Missing cross-references
    - Stale information (old update dates)
    - Pages missing one-line summaries
    - Index entries without matching pages
  → Report findings
  → Offer to fix automatically or flag for user review
```

---

## Custom Commands (Skills)

All commands live as markdown files in `_skills/`.

### Core Wiki Commands

| Command | Purpose | Scope |
|---------|---------|-------|
| `/ingest [domain] [source]` | Process raw source into wiki pages | Single domain |
| `/query [domain] [question]` | Search wiki and synthesize answer | Single or cross-domain |
| `/lint [domain]` | Check wiki consistency and health | Single domain |

### Thinking & Learning Commands

| Command | Purpose | Inspired By |
|---------|---------|-------------|
| `/ideas` | Deep cross-domain scan to generate actionable ideas | Vin's /ideas |
| `/challenge [topic]` | Pressure-test a wiki page's claims with counter-evidence | Vin's /challenge |
| `/connect [domain1] [domain2]` | Find bridges between two domains | Vin's /connect |
| `/gaps [domain]` | Detect knowledge gaps — topics without pages | Original |
| `/roadmap [domain]` | Generate or update a learning roadmap | Original |
| `/profile-update` | Update skills inventory based on recent activity | KJ's weekly-update |

---

## Domain Schema (CLAUDE.md per domain)

Each domain wiki has its own CLAUDE.md defining:

1. **Domain description** — what this wiki covers
2. **Category structure** — how pages are organized into subcategories
3. **Page format rules** — frontmatter fields, section structure
4. **Ingest rules** — how to process raw sources
5. **Quality standards** — max page length, summary requirement, linking rules
6. **Vocabulary** — consistent terminology for tags and categories

Example for data-science:

```markdown
# Data Science Wiki — Schema

## Description
Personal knowledge base covering statistics, machine learning, 
math foundations, SQL/BigQuery, and Python data tools.
Built to support active coursework, Kaggle competitions, and 
company data projects.

## Categories
- statistics: Descriptive, inferential, Bayesian
- machine-learning: Supervised, unsupervised, ensemble, deep learning
- math-foundations: Linear algebra, calculus, optimization, probability
- sql-bigquery: SQL patterns, BigQuery-specific, data warehousing
- python-data: pandas, numpy, scikit-learn, visualization
- projects: Kaggle, EDA checklists, project templates

## Ingest Rules
1. Read the source from raw/
2. Identify key concepts — each major concept gets its own page
3. Check existing pages — update rather than duplicate
4. Add [[wikilinks]] connecting new content to existing pages
5. Update index.md
6. Log the ingest

## Quality Standards
- Every page starts with a one-line summary in blockquote
- Max ~1000 words per page
- Use [[wikilinks]] for all cross-references
- Cite sources in frontmatter
- Include "When To Use" and "Connections" sections
```

---

## Search Strategy

### Phase 1: Direct File Reading (Now)
- Claude Code reads `index.md` to find relevant pages
- Reads full pages for detailed answers
- Works well up to ~200-300 pages

### Phase 2: qmd MCP Server (Later)
- Install qmd as MCP server when wiki exceeds ~300 pages
- Provides BM25 + vector hybrid search
- Claude Code queries qmd → gets ranked results → reads top pages
- Config in `.claude/settings.json`:
  ```json
  {
    "mcpServers": {
      "qmd": {
        "command": "npx",
        "args": ["qmd", "--vault", "./"]
      }
    }
  }
  ```

---

## Obsidian Plugins

| Plugin            | Purpose                                     | Priority |
| ----------------- | ------------------------------------------- | -------- |
| Dataview          | Query wiki pages by frontmatter metadata    | High     |
| Templater         | Wiki page, raw source, daily note templates | High     |
| Web Clipper       | Save web articles to raw/ as markdown       | High     |
| Local Images Plus | Download linked images to local vault       | Medium   |


---

## Pilot Plan: Data Science Wiki

### Phase 1: Setup
1. Create folder structure (`data-science/`, `_meta/`, `_templates/`, `_skills/`)
2. Write global CLAUDE.md (master schema)
3. Write data-science CLAUDE.md (domain schema)
4. Create template files
5. Create index.md and log.md stubs
6. Install Obsidian plugins (Dataview, Templater, Web Clipper)

### Phase 2: First Ingest
1. Add first course notes to `raw/course-notes/`
2. Run `/ingest` to create first wiki pages
3. Verify: pages created, index updated, log written, wikilinks work

### Phase 3: Grow Organically
- Add sources as you learn: course notes, papers, web clips
- Use `/query` to test knowledge retrieval
- Run `/lint` weekly to maintain quality
- Use `/gaps` to find what to learn next
- Use `/roadmap` to plan learning path

### Phase 4: Expand to Other Domains
- Once data-science wiki is working well, create next domain wiki
- Reuse same structure, templates, and skills
- Test cross-domain commands (`/ideas`, `/connect`)

---

## Verification Plan

1. **Structure test:** All folders, files, and templates exist and follow conventions
2. **Ingest test:** Add a course note → run /ingest → verify wiki page created with correct format, index updated, log written
3. **Query test:** Ask a question → verify answer references correct wiki pages
4. **Cross-reference test:** Ingest second source → verify wikilinks created to existing pages
5. **Obsidian test:** Open vault in Obsidian → verify graph view shows connections, templates work, plugins functional
6. **Lint test:** Run /lint → verify it catches intentionally broken page (missing summary, orphan)
7. **Index test:** Verify index.md accurately lists all pages with summaries

---

## Future Expansion

| Domain | When | Notes |
|--------|------|-------|
| fullstack-dev | After pilot stabilizes | 3+ active repos, daily work |
| ai-ml | When starting LLM fine-tuning | Claude Code, prompt engineering |
| system-design | Cross-domain | Architecture skills, tech stack decisions |
| backend-api | With fullstack-dev | Python, FastAPI, PostgreSQL |
| cloud | As needed | GCP, AWS — only relevant services |
| marketing | As needed | Meta/Google Ads, analytics |
| 3d-design | As needed | Blender, Fusion 360 |
