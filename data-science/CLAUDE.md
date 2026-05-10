# Data Science Wiki — Schema

## Description
Personal knowledge base covering statistics, machine learning, math foundations, SQL/BigQuery, and Python data tools. Built to support active coursework, Kaggle competitions, and company data projects.

## Categories
- **statistics**: Descriptive, inferential, Bayesian statistics
- **machine-learning**: Supervised, unsupervised, ensemble, deep learning
- **math-foundations**: Linear algebra, calculus, optimization, probability
- **sql-bigquery**: SQL patterns, BigQuery-specific, data warehousing
- **python-data**: pandas, numpy, scikit-learn, visualization
- **projects**: Kaggle, EDA checklists, project templates

## Page Format
Every wiki page in this domain MUST follow the template in `_templates/wiki-page.md`:
1. YAML frontmatter with `domain: data-science` and appropriate `category`
2. One-line summary in blockquote
3. Standard sections: Core Concept, How It Works, Key Parameters, When To Use, Connections, My Notes
4. Max ~1000 words
5. `[[wikilinks]]` for cross-references within and across domains

## Ingest Rules
1. Read the source from `raw/`
2. Identify key concepts — each major concept gets its own page in `pages/{category}/`
3. Check existing pages — UPDATE rather than duplicate
4. CRITICAL: After creating new pages, revise 10-15 existing related pages to add context and cross-references. This is what makes the wiki compound.
5. Add `[[wikilinks]]` connecting new content to existing pages
6. Update `index.md` with new/changed entries
7. Append to `log.md`

## Quality Standards
- Every page starts with a one-line summary in blockquote
- Max ~1000 words per page (split if longer)
- Use `[[wikilinks]]` for ALL cross-references
- Cite sources in frontmatter `sources` field
- Include "When To Use" and "Connections" sections always
- Tag consistently using category vocabulary above

## Naming Convention
- Filename: lowercase-with-hyphens.md (e.g., `random-forest.md`)
- Title in frontmatter: Title Case (e.g., "Random Forest")
- Wikilinks use title: `[[Random Forest]]`
