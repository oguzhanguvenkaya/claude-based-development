# /lint — Wiki Health Check Skill

## Usage
```
/lint [domain]
/lint all        — lint all domains
```
Example: `/lint data-science`

## Purpose
Periodic health check to maintain wiki quality. Finds contradictions, orphans, missing links, stale content, and index mismatches.

## Steps

### 1. Scan All Pages
Read every page in `[domain]/pages/` and check for:

**Structural Issues:**
- Missing one-line summary (blockquote after title)
- Missing or incomplete frontmatter (title, domain, category, created, updated, sources, tags)
- Missing standard sections (Core Concept, Connections, etc.)
- Pages exceeding ~1000 words

**Linking Issues:**
- Orphan pages — no incoming `[[wikilinks]]` from other pages
- Dead links — `[[wikilinks]]` pointing to non-existent pages
- Missing cross-references — pages on related topics that don't link to each other

**Content Issues:**
- Contradictions between pages (conflicting claims)
- Stale information — pages with `updated` date older than 60 days
- Duplicate content across pages

### 2. Check Index Accuracy
- Compare `index.md` entries against actual pages in `pages/`
- Find: pages not in index, index entries without matching pages
- Check one-line summaries still match page content

### 3. Report Findings
Present findings organized by severity:
```
## Lint Report — [domain] — [date]

### Critical (fix now)
- [list contradictions, dead links]

### Warning (fix soon)
- [list orphans, stale pages, missing sections]

### Info (nice to fix)
- [list word count issues, minor formatting]

### Stats
- Total pages: N
- Healthy pages: N
- Issues found: N
```

### 4. Offer Fixes
- Ask: "Want me to auto-fix the structural issues (missing sections, index updates)?"
- Content issues (contradictions, stale info) always require user review
- Apply fixes if approved, then re-run a quick check

### 5. Log the Lint
Append to `[domain]/log.md`:
```markdown
## [YYYY-MM-DD] lint | Health Check
- Pages scanned: N
- Issues found: N critical, N warning, N info
- Auto-fixed: N issues
- Requires review: [list]
```
