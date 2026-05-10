# Fullstack Dev Wiki — Design Spec

**Date:** 2026-04-12
**Status:** Draft
**Domain:** fullstack-dev
**Parent System:** Personal Knowledge Wiki System (PKWS)
**Related Spec:** `2026-04-12-llm-wiki-system-design.md`

---

## Context

### Problem
The user is an AI-assisted fullstack developer who can build complex web applications (Next.js, React, TypeScript, Drizzle ORM, Vercel) but experiences a specific senior-level gap: **complex systems have blind spots that AI-generated code misses**. The user needs to operate at a senior fullstack developer level to:

1. **Debug complex systems** — trace issues through layers, find root causes
2. **Add features correctly** — catch edge cases, failure modes, and non-happy-path behavior
3. **Make architectural decisions** — decide state locality, data flow, rendering strategy, boundaries
4. **Question AI output** — catch hallucinated APIs, over-engineering, hidden assumptions

The core philosophy guiding this wiki:
> "Seniorlık bu teknolojileri bilmekten çok: hangi koşulda hangisini neden seçtiğini bilmek."

Every page teaches **decision-making**, not tool usage.

### Solution
A multi-layered wiki organized around **9 senior-level skill categories**, with each page following a "patterns + checklists + trade-offs" format. The wiki compounds knowledge from courses, articles, docs, and — most valuably — real case studies from the user's own projects (MarketPulse, menzernaturkiye, prompt_generator).

### Scope Boundaries
- **IN scope:** Frontend tech (Next.js, React, TS, Drizzle, Vercel), fullstack architecture, system design, decision-making, senior refleksi
- **OUT of scope:** Python/FastAPI backend deep-dives (belongs to separate `backend-api` wiki)
- **Cross-reference:** Architecture patterns that apply to both frontend and backend will link from/to the backend-api wiki once it exists

---

## Architecture

### Wiki Structure

```
fullstack-dev/
├── CLAUDE.md                              # Domain schema
├── index.md                               # Master catalog
├── log.md                                 # Activity log
├── raw/                                   # Sources
│   ├── course-notes/
│   ├── articles/
│   ├── docs/                              # Framework/library docs
│   ├── books/                             # Book excerpts
│   └── case-studies/                      # Real project lessons
│
└── pages/
    ├── 1-architectural-thinking/
    ├── 2-data-apis-persistence/
    ├── 3-frontend-systems-ux/
    ├── 4-backend-reliability-security/
    ├── 5-debugging-observability/
    ├── 6-delivery-operations/
    ├── 7-code-quality-collaboration/
    ├── 8-product-decision-making/
    └── 9-meta-skills/
```

### The 9 Categories

#### 1. Architectural Thinking — "Bu sorumluluk nereye ait?"
Component boundaries, separation of concerns, state locality, data flow, rendering strategy, cache hierarchy, domain boundaries, changeability & maintainability.

#### 2. Data, APIs & Persistence — "Veri nasıl akar, nasıl saklanır?"
Schema design, relations/indexing/migrations, API contracts, error design, versioning, fetching patterns, pagination/filtering/sorting, optimistic updates, consistency & rollback.

#### 3. Frontend Systems & UX — "Kullanıcı ne hissediyor?"
Core Web Vitals, bundle strategy, hydration cost, render performance, loading/empty/error states, form UX, perceived performance, accessibility, responsive/mobile behavior.

#### 4. Backend Reliability & Security — "Ne kırılabilir?"
OWASP Top 10, auth architecture, validation/sanitization, secret management, CORS/CSP/headers, failure modes, retries/timeouts/idempotency, concurrency/race conditions, graceful degradation.

#### 5. Debugging & Observability — "Ne oldu, nerede oldu?"
Structured logging, error tracking, performance profiling, network debugging, reproduction strategy, root cause analysis.

#### 6. Delivery & Operations — "Production'a nasıl çıkar?"
CI/CD workflows, environment separation, feature flags, safe migrations, monitoring/alerting, incident response, rollback/release strategy, cost awareness.

#### 7. Code Quality & Collaboration — "Kod nasıl yaşar?"
Refactoring strategy, testing strategy, testability-driven design, code review mindset, git workflow, documentation.

#### 8. Product & Decision Making — "Doğru şeyi mi yapıyoruz?"
Requirement clarification, scope control, MVP thinking, trade-off analysis, prioritization, risk assessment, user journey awareness, DX/UX/speed trade-offs.

#### 9. Meta Skills — Senior refleksi
What could go wrong?, edge case thinking, assumption questioning, technical debt awareness, systems thinking, AI-assisted engineering discipline.

---

## Page Formats

Every page serves one of three types, chosen by the content:

### Type 1: Concept / Pattern Page

```markdown
---
title: "State Locality"
domain: fullstack-dev
category: 1-architectural-thinking
type: concept
level: foundation | pattern | stack-specific
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [[raw/...]]
tags: [state-management, architecture]
---

# State Locality

> One-line summary: ...

## Why It Matters (Senior Perspective)
Junior vs senior view of this topic.

## Core Concept
Fundamental idea.

## The Decision Framework
The questions a senior asks when making this decision.

## Patterns (Do This)
Validated approaches.

## Anti-Patterns (Don't Do This)
Common mistakes.

## Trade-offs
Comparison matrix across options.

## Stack-Specific: Next.js / React / TS / Drizzle
How this concept applies in our stack.

## Gotchas (What Could Go Wrong)
Hidden landmines.

## Connections
- Related: [[...]]
- Leads to: [[...]]
- Contrast with: [[...]]

## Real Examples (From My Projects)
Concrete applications in MarketPulse, menzernaturkiye, etc.

## My Notes
Personal observations, incidents, lessons learned.
```

### Type 2: Trade-off Page

```markdown
---
title: "CSR vs SSR vs SSG vs RSC"
domain: fullstack-dev
category: 1-architectural-thinking
type: trade-off
---

# CSR vs SSR vs SSG vs RSC

> One-line summary: ...

## The Question
What decision this page helps make.

## Decision Matrix
| Option | Dimension 1 | Dimension 2 | Use Case |
|--------|-------------|-------------|----------|
| ... | ... | ... | ... |

## Reversibility
Which choices are reversible vs one-way doors.

## When to Choose What
Decision tree.

## Real Examples
From user's projects.

## Connections
```

### Type 3: Playbook Page

```markdown
---
title: "Adding a New Feature"
domain: fullstack-dev
category: 8-product-decision-making
type: playbook
---

# Playbook: Adding a New Feature

> Step-by-step process.

## Pre-Development Checklist
- [ ] Requirement clarification
- [ ] ...

## Design Phase Checklist
- [ ] ...

## Implementation Phase Checklist
- [ ] ...

## Pre-Ship Verification
- [ ] ...

## Post-Ship
- [ ] ...

## Common Mistakes
List of things that go wrong.

## Connections
```

---

## Philosophy: Decision-Oriented Content

Every page must answer "how to decide", not just "how to use". This means:

- **NO tool cataloging**: Don't just list `useMemo`, `useCallback`, `React.memo`. Explain *when* each applies, *why*, and *what breaks* without them.
- **NO framework parroting**: Don't copy Next.js docs. Explain the *underlying model* (rendering strategies, cache hierarchies) so the knowledge transfers.
- **YES decision frameworks**: Every concept page has a "Decision Framework" section with the questions a senior asks.
- **YES anti-patterns**: Every concept page names common mistakes explicitly.
- **YES reversibility**: Trade-off pages explicitly state which decisions are reversible vs one-way doors.

---

## Ingest Source Strategy

### Source Categories
1. **Official docs** (`raw/docs/`) — Next.js, React, Drizzle, TypeScript, MDN
2. **Expert articles** (`raw/articles/`) — Dan Abramov, Kent C. Dodds, Josh Comeau, Vercel blog, Tanner Linsley
3. **Case studies** (`raw/case-studies/`) — Real incidents and decisions from user's projects (highest value source)
4. **Course notes** (`raw/course-notes/`) — Any fullstack courses taken or watched
5. **Books** (`raw/books/`) — Designing Data-Intensive Applications, DDD Distilled, Refactoring, Accelerate

### Case Study Template
```markdown
# Case Study: [Project] [Issue]

## What Happened
## Root Cause
## Fix
## Lessons Learned → [[Wiki Page to Update]]
```

Case studies are the highest-value ingest source because they encode real-world learning specific to the user's context.

---

## Pilot Plan — Phased Growth

### Phase 1: Senior Reflex Foundations (Week 1)
The "AI gap-filling" pages — most critical to user's stated problem:
1. `9-meta-skills/ai-assisted-engineering.md` ⭐ Highest priority — user-specific
2. `9-meta-skills/what-could-go-wrong.md`
3. `9-meta-skills/edge-case-thinking.md`
4. `8-product-decision-making/requirement-clarification.md`
5. `8-product-decision-making/scope-control.md`

### Phase 2: Architectural Decision Framework (Week 2)
Core system design pages:
6. `1-architectural-thinking/state-locality.md`
7. `1-architectural-thinking/data-flow.md`
8. `1-architectural-thinking/rendering-strategy.md`
9. `1-architectural-thinking/component-boundaries.md`
10. `1-architectural-thinking/domain-boundaries.md`

### Phase 3: Defensive Engineering (Week 3)
"Don't miss the key points" pages:
11. `4-backend-reliability-security/failure-modes.md`
12. `4-backend-reliability-security/retries-timeouts-idempotency.md`
13. `3-frontend-systems-ux/loading-empty-error-states.md`
14. `5-debugging-observability/structured-logging.md`
15. `5-debugging-observability/root-cause-analysis.md`

### Phase 4: Playbooks (Week 4)
16. `8-product-decision-making/adding-new-feature.md` (playbook)
17. `5-debugging-observability/debugging-playbook.md`
18. `4-backend-reliability-security/security-review.md` (playbook)

### Phase 5+: Organic Growth
Remaining ~50 pages grow organically through:
- Course ingests
- Article ingests
- Case studies from real project work
- Gap-filling triggered by `/gaps` skill
- Query results that reveal missing topics

---

## Success Metrics

How we know this wiki is working:

1. **The "Key Point" Test**: When starting a new feature, the user can open `adding-new-feature.md` playbook and catch at least 2-3 concerns they would have otherwise missed.

2. **The Debug Time Test**: When encountering a bug, the user can open `debugging-playbook.md` and follow a systematic process instead of random exploration.

3. **The AI Review Test**: When AI generates code, the user can cross-reference `ai-assisted-engineering.md` checklist and catch common AI mistakes.

4. **The Decision Confidence Test**: When facing a "which approach" question, the user can find a trade-off page with a decision matrix instead of guessing.

5. **The Wiki Growth Test**: After 4 weeks of Phase 1-4 content, the wiki has 15-18 high-quality pages with 50+ cross-references.

---

## Verification Plan

1. **Structure test:** Folders `1-architectural-thinking/` through `9-meta-skills/` exist with `raw/` subdirectories
2. **Schema test:** `CLAUDE.md` contains the 9 categories and decision-oriented philosophy
3. **First ingest test:** Create first page (`ai-assisted-engineering.md`) following concept page format
4. **Cross-reference test:** Second page correctly links to the first via `[[wikilinks]]`
5. **Case study test:** One real case study from MarketPulse ingested and linked to relevant wiki pages
6. **Index accuracy test:** `index.md` lists all created pages with one-line summaries
7. **Pilot page coverage:** After Phase 1, all 5 pages exist and are interlinked
