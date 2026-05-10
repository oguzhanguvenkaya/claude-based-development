# /ingest — Source Ingestion Skill

## Usage
```
/ingest [domain] [source-path]
```
Example: `/ingest data-science raw/course-notes/week-5-ensemble-methods.md`

## Purpose
Read a raw source, extract key concepts, create/update wiki pages, and connect them with existing knowledge. This is the primary mechanism for growing the wiki.

## Steps

### 1. Read Source
- Read the file at the specified source path
- If no path given, list files in `[domain]/raw/` and ask user which to ingest

### 2. Discuss Takeaways
- Present 3-5 key takeaways from the source to the user
- Ask: "These are the main concepts I extracted. Should I proceed, or do you want to add/modify anything?"
- Wait for user confirmation before proceeding

### 3. Create New Pages
For each major concept that doesn't have an existing wiki page:
- Create a new page in `[domain]/pages/[category]/`
- Follow the wiki-page template exactly (frontmatter, one-line summary, all sections)
- Use lowercase-with-hyphens for filename
- Add the raw source to `sources` in frontmatter

### 4. CRITICAL — Revise Existing Pages
This is what makes the wiki compound. For every ingest:
- Identify 10-15 existing pages that relate to the new content
- For each related page:
  - Add new context or details learned from the source
  - Add `[[wikilinks]]` to newly created pages
  - Update the "Connections" section
  - Update the `updated` date in frontmatter
- If no existing pages exist yet (first ingest), skip this step

### 5. Update Index
- Open `[domain]/index.md`
- Add entries for new pages with one-line summaries
- Update summaries for revised pages if their scope changed
- Update `total_pages` count and `updated` date in frontmatter

### 6. Update Log
Append to `[domain]/log.md`:
```markdown
## [YYYY-MM-DD] ingest | Source Title
- Source: [[raw/path/to/source]]
- Pages created: [[Page 1]], [[Page 2]], ...
- Pages updated: [[Page 3]] (reason), [[Page 4]] (reason), ...
- Key takeaways: brief summary of what was learned
```

### 7. Report
Present a summary:
- Number of pages created
- Number of pages updated
- New connections made
- Suggest next steps (more sources to ingest, gaps to fill)

## Rules
- NEVER modify raw sources — they are immutable
- ALWAYS update the index and log — no silent changes
- ALWAYS add wikilinks — isolated pages are useless
- Prefer updating existing pages over creating duplicates
- Each page should be ~1000 words max — split if needed
