# /query — Wiki Query Skill

## Usage
```
/query [domain] [question]
/query [question]          — searches across all domains
```
Example: `/query data-science When should I use Random Forest vs XGBoost?`

## Purpose
Search the wiki for relevant information, synthesize an answer with citations, and optionally save high-quality answers as new wiki pages.

## Steps

### 1. Find Relevant Pages
- Read `[domain]/index.md` to identify relevant pages by their one-line summaries
- If cross-domain query (no domain specified), read `master-index.md` first, then relevant domain indexes
- Select the most relevant pages (typically 3-8)

### 2. Read Pages
- Read the full content of selected wiki pages
- Note any gaps — is the wiki missing information needed to answer?

### 3. Synthesize Answer
- Combine information from multiple pages into a coherent answer
- Cite sources using `[[wikilinks]]` inline: "According to [[Random Forest]], the key advantage is..."
- If the wiki lacks sufficient information, say so explicitly — don't hallucinate

### 4. Offer to Save
If the synthesized answer adds value beyond what individual pages contain:
- Ask: "This answer synthesizes multiple topics. Want me to save it as a new wiki page?"
- If yes, create a new page following the wiki-page template
- Add it to the index

### 5. Log the Query
Append to `[domain]/log.md`:
```markdown
## [YYYY-MM-DD] query | "The question asked"
- Pages consulted: [[Page 1]], [[Page 2]], ...
- Answer quality: High/Medium/Low
- Saved as: [[New Page Title]] (if saved)
- Gaps found: description of missing information (if any)
```

## Rules
- ALWAYS cite which wiki pages you're drawing from
- NEVER make up information not in the wiki — state gaps explicitly
- If a gap is found, suggest it as a topic for future ingest
