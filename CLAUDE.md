# Personal Knowledge Wiki System — Master Schema

## System Overview
This Obsidian vault is a multi-domain LLM Wiki system based on Andrej Karpathy's LLM Wiki pattern. Claude Code maintains structured wiki pages through ingest/query/lint workflows. Knowledge compounds over time — every source ingested enriches the entire wiki.

## Architecture
- **Raw sources** (`raw/`): Immutable. Read but never modify.
- **Wiki pages** (`pages/`): LLM-generated and LLM-maintained markdown files.
- **Schema** (`CLAUDE.md`): This file + domain-specific CLAUDE.md files.

## Vault Structure
```
├── CLAUDE.md              ← You are here (global rules)
├── master-index.md        ← Catalog of all domain wikis
├── log.md                 ← Global activity log
├── _meta/                 ← Strategy layer (goals, profile)
├── _templates/            ← Obsidian page templates
├── _skills/               ← Claude Code custom commands
├── data-science/          ← Domain wiki (has its own CLAUDE.md)
└── [future domains]/      ← fullstack-dev, ai-ml, cloud, etc.
```

## Global Rules

### Language
- Wiki content: English
- Communication with user: Turkish (unless user switches)

### Wiki Page Format
Every wiki page MUST have:
1. YAML frontmatter (title, domain, category, created, updated, sources, tags)
2. One-line summary in blockquote immediately after the title
3. Sections: Core Concept, How It Works, Key Parameters, When To Use, Connections, My Notes
4. Max ~1000 words per page
5. `[[wikilinks]]` for all cross-references
6. Sources cited in frontmatter

### Index Format
- Each domain has an `index.md` listing every page with a one-line summary
- `master-index.md` lists all domain wikis with page counts and status
- Update index on every ingest

### Log Format
- Append-only, chronological
- Format: `## [YYYY-MM-DD] type | Title`
- Types: ingest, query, lint
- Include: pages created, pages updated, key takeaways

## Workflows

### /ingest [domain] [source-path]
1. Read the raw source
2. Discuss key takeaways with user
3. Create new wiki pages for new concepts
4. CRITICAL: Revise 10-15 existing related pages (add context, update cross-references)
5. Add [[wikilinks]] connecting new and updated pages
6. Update domain index.md
7. Append to domain log.md
8. Report all changes

### /query [domain] [question]
1. Read domain index.md to find relevant pages
2. Read relevant wiki pages
3. Synthesize answer with [[page]] citations
4. If high quality → offer to save as new wiki page
5. Append to log.md

### /lint [domain]
1. Scan all pages for: contradictions, orphans, missing cross-refs, stale info, missing summaries
2. Check index accuracy
3. Report findings
4. Offer to fix or flag for review

## Custom Commands
Skills are defined in `_skills/` as markdown files. Run them by referencing the skill name.

## Domain Wikis
Each domain wiki has its own `CLAUDE.md` with domain-specific rules. When working in a domain, read its CLAUDE.md first.
