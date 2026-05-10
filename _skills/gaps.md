# /gaps — Knowledge Gap Detection

## Usage
```
/gaps [domain]
```
Example: `/gaps data-science`

## Purpose
Detect knowledge gaps in a domain wiki — topics that should exist but don't, areas with thin coverage, and missing connections.

## Steps

### 1. Analyze Current Coverage
- Read `[domain]/index.md` for all existing pages
- Read `[domain]/CLAUDE.md` for defined categories
- Check which categories have few or no pages

### 2. Identify Gaps
Compare against:
- **Category completeness**: Are all schema categories represented?
- **Prerequisite chains**: Are foundation topics covered before advanced ones?
- **Dead-end references**: Pages that link to `[[topics]]` that don't exist yet
- **Goals alignment**: Check `_meta/goals.md` — are priority topics covered?
- **Standard curriculum**: For learning domains, what topics would a standard course cover?

### 3. Present Gap Analysis
```
## Gap Analysis — [Domain] — [date]

### Missing Foundation Topics (Priority: High)
- [Topic]: Required by [[Page 1]], [[Page 2]] but no page exists
- [Topic]: Part of [category] but not covered

### Thin Coverage Areas (Priority: Medium)
- [Category]: Only N pages, expected ~N for adequate coverage

### Broken References (Priority: High)
- [[Non-existent Page]] referenced by [[Page 1]], [[Page 2]]

### Goal Alignment Gaps
- Goal: [from goals.md] — Missing pages: [topics needed]

### Suggested Ingest Sources
- [Type of source] about [topic] would fill gaps in [area]
```

### 4. Offer Next Steps
- "Want me to create stub pages for the high-priority gaps?"
- "Want me to generate a `/roadmap` based on these gaps?"
