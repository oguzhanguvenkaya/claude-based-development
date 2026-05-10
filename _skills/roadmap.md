# /roadmap — Learning Roadmap Generation

## Usage
```
/roadmap [domain]
/roadmap [domain] [specific-goal]
```
Example: `/roadmap data-science "prepare for first Kaggle competition"`

## Purpose
Generate or update a structured learning roadmap for a domain based on current wiki coverage, knowledge gaps, and stated goals.

## Steps

### 1. Assess Current State
- Read `[domain]/index.md` for existing knowledge
- Run a quick `/gaps` analysis
- Read `_meta/goals.md` for priorities
- Read `_meta/profile.md` for current skill level

### 2. Define the Path
- Identify prerequisite chains (what must come before what)
- Group topics into phases (foundation → intermediate → advanced)
- Estimate learning priority based on goals

### 3. Generate Roadmap
```
## Learning Roadmap — [Domain] — [date]

### Current Level
[Assessment based on wiki coverage and profile]

### Goal
[From goals.md or user-specified]

### Phase 1: Foundation (Priority: Now)
- [ ] [Topic 1] — Status: [[existing page]] or "not covered"
- [ ] [Topic 2] — Status: ...
- Suggested sources: [types of materials to find]

### Phase 2: Intermediate (Priority: Next)
- [ ] [Topic 3] — Requires: [[Topic 1]]
- [ ] [Topic 4] — Requires: [[Topic 2]]

### Phase 3: Advanced (Priority: Later)
- [ ] [Topic 5] — Requires: [[Topic 3]], [[Topic 4]]

### Quick Wins
- [Topics you can cover quickly with existing knowledge]
```

### 4. Save & Track
- Save roadmap as a wiki page in `[domain]/pages/projects/`
- Link to relevant existing pages
- Update `_meta/goals.md` with roadmap reference
