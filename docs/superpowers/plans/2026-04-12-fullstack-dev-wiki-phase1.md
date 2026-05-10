# Fullstack Dev Wiki — Phase 1 Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the fullstack-dev wiki structure and write Phase 1 content (5 senior reflex pages) that address the user's core problem: missing key points when AI-assisted development produces complex systems.

**Architecture:** Multi-layered wiki with 9 skill categories following decision-oriented content philosophy. Phase 1 focuses on category 9 (meta-skills) and category 8 (product decision-making) — the "AI gap-filling" pages most critical to user's stated problem.

**Tech Stack:** Markdown files in Obsidian vault. No code. Content is the deliverable.

**Spec:** `docs/superpowers/specs/2026-04-12-fullstack-dev-wiki-design.md`

**Vault Root:** `/Users/projectx/Documents/Obsidian Vault/claude-based-development/`

---

## Task 1: Create Folder Structure & Schema Files

**Files:**
- Create: `fullstack-dev/CLAUDE.md`
- Create: `fullstack-dev/index.md`
- Create: `fullstack-dev/log.md`
- Create directories: `fullstack-dev/pages/{1-architectural-thinking,2-data-apis-persistence,3-frontend-systems-ux,4-backend-reliability-security,5-debugging-observability,6-delivery-operations,7-code-quality-collaboration,8-product-decision-making,9-meta-skills}/`
- Create directories: `fullstack-dev/raw/{course-notes,articles,docs,books,case-studies}/`

- [ ] **Step 1: Create all directories**

```bash
cd "/Users/projectx/Documents/Obsidian Vault/claude-based-development" && \
mkdir -p fullstack-dev/pages/{1-architectural-thinking,2-data-apis-persistence,3-frontend-systems-ux,4-backend-reliability-security,5-debugging-observability,6-delivery-operations,7-code-quality-collaboration,8-product-decision-making,9-meta-skills} && \
mkdir -p fullstack-dev/raw/{course-notes,articles,docs,books,case-studies}
```

Expected: 14 directories created under `fullstack-dev/`.

- [ ] **Step 2: Write `fullstack-dev/CLAUDE.md`**

Content:
```markdown
# Fullstack Dev Wiki — Schema

## Description
Personal knowledge base for senior-level fullstack development. Focused on frontend tech (Next.js, React, TypeScript, Drizzle ORM, Vercel) + architecture + system design + decision-making. Built to compensate for gaps that AI-assisted development creates in complex systems.

**Core Philosophy:** Seniorlık bu teknolojileri bilmekten çok, hangi koşulda hangisini neden seçtiğini bilmektir. Every page teaches **decision-making**, not tool usage.

## Categories
1. **1-architectural-thinking** — "Bu sorumluluk nereye ait?" Component boundaries, state locality, data flow, rendering strategy, cache hierarchy, domain boundaries.
2. **2-data-apis-persistence** — "Veri nasıl akar, nasıl saklanır?" Schema design, API contracts, fetching patterns, optimistic updates, consistency.
3. **3-frontend-systems-ux** — "Kullanıcı ne hissediyor?" Core Web Vitals, bundle strategy, loading/empty/error states, accessibility.
4. **4-backend-reliability-security** — "Ne kırılabilir?" OWASP, auth, failure modes, retries, concurrency, graceful degradation.
5. **5-debugging-observability** — "Ne oldu, nerede oldu?" Structured logging, error tracking, root cause analysis.
6. **6-delivery-operations** — "Production'a nasıl çıkar?" CI/CD, feature flags, safe migrations, incident response, cost awareness.
7. **7-code-quality-collaboration** — "Kod nasıl yaşar?" Refactoring, testing strategy, code review, documentation.
8. **8-product-decision-making** — "Doğru şeyi mi yapıyoruz?" Requirement clarification, scope control, trade-off analysis, user journey.
9. **9-meta-skills** — Senior refleksi. What could go wrong?, edge case thinking, AI-assisted engineering discipline.

## Page Types
Every page is one of three types, indicated in frontmatter `type`:
- **concept**: Core patterns, mental models, decision frameworks
- **trade-off**: Compare options with decision matrix, state reversibility
- **playbook**: Step-by-step checklists for scenarios

## Page Format Rules
Every page MUST have:
1. YAML frontmatter: `title, domain, category, type, created, updated, sources, tags`
2. One-line summary in blockquote immediately after title
3. Standard sections per page type (see `_templates/` or spec)
4. Max ~1200 words per page
5. `[[wikilinks]]` for all cross-references
6. "Real Examples" section referencing user's projects when applicable

## Ingest Rules
1. Read source from `raw/`
2. Discuss key takeaways with user
3. Create new pages OR update existing ones
4. CRITICAL: Revise 10-15 related pages to add cross-references
5. Update `index.md`
6. Append to `log.md`

## Decision-Oriented Writing
When writing content for this wiki:
- NO tool cataloging (don't just list hooks/APIs)
- NO framework parroting (don't copy docs verbatim)
- YES decision frameworks ("questions a senior asks")
- YES anti-patterns (name common mistakes explicitly)
- YES trade-offs (explicit reversibility for architectural choices)

## Naming Convention
- Filename: `lowercase-with-hyphens.md`
- Title in frontmatter: `Title Case`
- Wikilinks use title: `[[State Locality]]`
```

- [ ] **Step 3: Write `fullstack-dev/index.md`**

Content:
```markdown
---
title: "Fullstack Dev Wiki — Index"
domain: fullstack-dev
updated: 2026-04-12
total_pages: 0
---

# Fullstack Dev Wiki — Index

## 1. Architectural Thinking
<!-- Component boundaries, state locality, data flow, rendering strategy -->

## 2. Data, APIs & Persistence
<!-- Schema, contracts, fetching, optimistic updates, consistency -->

## 3. Frontend Systems & UX
<!-- Core Web Vitals, bundle, UX states, accessibility -->

## 4. Backend Reliability & Security
<!-- OWASP, auth, failure modes, concurrency -->

## 5. Debugging & Observability
<!-- Logging, error tracking, root cause analysis -->

## 6. Delivery & Operations
<!-- CI/CD, feature flags, incident response -->

## 7. Code Quality & Collaboration
<!-- Refactoring, testing, code review -->

## 8. Product & Decision Making
<!-- Requirements, scope, trade-offs, user journey -->

## 9. Meta Skills
<!-- What could go wrong, edge cases, AI-assisted engineering -->
```

- [ ] **Step 4: Write `fullstack-dev/log.md`**

Content:
```markdown
---
title: "Fullstack Dev Wiki — Log"
domain: fullstack-dev
updated: 2026-04-12
---

# Fullstack Dev Wiki — Log

## [2026-04-12] system | Wiki Initialized
- Domain wiki created with 9 categories
- Schema defined with decision-oriented philosophy
- Phase 1 pages pending (senior reflex foundations)
```

- [ ] **Step 5: Update `master-index.md`**

Modify `master-index.md` to add fullstack-dev row:

Change:
```markdown
| [[data-science/index\|Data Science]] | 3 | 2026-04-12 | Statistics, ML, Math, SQL, Python |
```

To:
```markdown
| [[data-science/index\|Data Science]] | 3 | 2026-04-12 | Statistics, ML, Math, SQL, Python |
| [[fullstack-dev/index\|Fullstack Dev]] | 0 | 2026-04-12 | Architecture, Next.js, React, TS, senior reflex |
```

Also remove fullstack-dev from the "Planned Wikis" table since it's now active.

- [ ] **Step 6: Verify structure**

```bash
cd "/Users/projectx/Documents/Obsidian Vault/claude-based-development" && \
find fullstack-dev -type d | sort && \
ls fullstack-dev/*.md
```

Expected: 14 directories + CLAUDE.md, index.md, log.md listed.

- [ ] **Step 7: Commit** (No git — skip this step. Vault is not a git repo.)

---

## Task 2: Write `ai-assisted-engineering.md` (Most Critical Page)

**File:** `fullstack-dev/pages/9-meta-skills/ai-assisted-engineering.md`

This is the single most important page for the user. It addresses their core problem directly: catching what AI misses.

- [ ] **Step 1: Write the page**

```markdown
---
title: "AI-Assisted Engineering Discipline"
domain: fullstack-dev
category: 9-meta-skills
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - meta-skills
  - ai-assisted
  - discipline
  - review
---

# AI-Assisted Engineering Discipline

> One-line summary: AI hız kazandırır ama zihinsel safety net'i zayıflatabilir. Bu sayfa AI çıktısını kör kabul etmeyen, sistematik bir doğrulama disiplini tanımlar.

## Why It Matters (Senior Perspective)
AI ile çalışan bir developer'ın en büyük riski, teknik olarak **çalışan ama yanlış olan** koda gitmektir. Kod çalışır, testler geçer, deploy olur — ama hidden assumptions, hallucinated API'ler, over-engineering veya security gap'leri gözden kaçar. Senior refleksi: AI bir junior developer gibi muamele edilmelidir — hızlı üretir, ama her çıktı review'dan geçmelidir.

## Core Concept
AI-assisted development iki moda ayrılır:
1. **Assistant mode:** AI bir subtask yapar, sen yönlendirir ve doğrularsın
2. **Autopilot mode:** AI çıktısı kör kabul edilir, sen sadece "next" dersin

**Senior disiplin = Autopilot mode'da bile Assistant mode refleksi.**

## The Decision Framework
AI bir şey ürettiğinde sor:
1. **Problem understanding:** AI benim çözmek istediğim problemi doğru anladı mı?
2. **Assumption check:** AI hangi varsayımları yaptı? Bunlar projemde geçerli mi?
3. **API reality:** AI'ın kullandığı API/library gerçekten var mı ve bu versiyonda çalışıyor mu?
4. **Simplicity check:** AI over-engineer ediyor mu? Gerçekten ihtiyacım var mı?
5. **Edge cases:** Happy path dışında ne olur? Null, error, concurrent, boş, çok büyük?
6. **Security:** Input validation, auth, secret'lar doğru ele alınmış mı?
7. **Context fit:** AI'ın çözümü projemin mevcut pattern'leriyle uyumlu mu?

## Patterns (Do This)

### 1. Triangulate Critical Output
AI önemli bir karar verdiğinde (architecture, security, data flow), aynı soruyu 2-3 farklı şekilde sor. Tutarlı cevap → güvenilirlik artar. Çelişen cevaplar → daha derin incele.

### 2. Demand Trade-off Reasoning
"Şu X'i yap" dendiğinde AI kodu yazar. Bunun yerine: "X ve Y arasındaki trade-off nedir, hangi durumda hangisi?" sor. Bu sadece kod değil, akıl yürütme gerektirir.

### 3. Read Before Accept
Her dosya düzenlemesinden sonra diff'i oku. **Anlamadığın satır yok**, prensip. Anlamadığın bir şey varsa dur ve sor.

### 4. Test the Happy Path Manually
Kod testleri geçse bile, feature'ı UI/CLI'dan manuel dene. Testlerin yakalamadığı UX bug'ları çok yaygındır.

### 5. Preserve Existing Patterns
AI yeni bir pattern öneriyorsa, "neden mevcut pattern'i kullanmıyoruz?" diye sor. Çoğu zaman AI context'i görmediği için yeni bir yol icat eder.

### 6. Layered Validation
- **Syntax layer:** TypeScript, linter
- **Logic layer:** Unit/integration tests
- **Integration layer:** E2E test veya manuel test
- **Review layer:** Human read-through

Hepsi gerekli. Hiçbiri tek başına yeterli değildir.

## Anti-Patterns (Don't Do This)

### Blind Accept
"Çalışıyor gibi duruyor, devam" — en tehlikeli pattern. İşte o anda bir güvenlik açığı, race condition veya memory leak eklemiş olabilirsin.

### Context Drop
Uzun bir session'da context kaybolur. AI'ın yaptığı önceki işleri hatırladığını varsayma. Kritik decision'ları açık dokümanlara yaz.

### Copy-Paste Without Adaptation
AI'dan gelen kodu olduğu gibi yapıştırma. Değişken isimleri, import path'leri, error handling — projenin pattern'ine uyarla.

### Hallucinated API Trust
AI bazen var olmayan method'lar veya package'lar uydurur. Dokümantasyondan veya source'dan doğrula.

### Over-Engineering Acceptance
AI "best practice" adına gereksiz abstraction'lar ekleyebilir. Soru: "Bunu gerçekten şimdi ihtiyacım var mı, yoksa YAGNI mi?"

### Skipping Error Paths
AI happy path'i çok iyi yazar. Error, loading, empty state'ler sık atlanır. Her feature'da bu 4 hali aç.

### Trusting Generated Tests Alone
AI testleri geçen kodla üretilir, ama test kalitesini sorgulamak gerekir. "Bu test hangi bug'ı yakalar?" sorusunu sor.

## Red Flags — AI Çıktısında Dikkat

| Red Flag | Ne Yapmalı |
|----------|------------|
| Yeni bir library eklemiş (sen istemedin) | "Neden?" sor, alternatif iste |
| `any` tipi veya `@ts-ignore` kullanmış | Reject — tip güvenliğini bozma |
| Error handling `catch { }` ile sessizleştirmiş | Reject — hataları görünür yap |
| Test yok veya çok zayıf | Tests ekle veya gerçek tests iste |
| Mevcut pattern'den sapmış | Neden olduğunu sor, context'i yeniden ver |
| Commit message vague (`update code`) | Daha spesifik iste |
| Magic number veya hardcoded değer | Konstant veya config'e taşıt |
| "Production-ready" diyor ama error handling yok | Her iddiayı doğrulanabilir kanıtla iste |

## Trade-offs
| Yaklaşım | Hız | Güvenlik | Öğrenme |
|----------|-----|----------|---------|
| Full autopilot | Çok yüksek | Çok düşük | Yok |
| AI + tests | Yüksek | Orta | Düşük |
| AI + tests + review | Orta | Yüksek | Orta |
| AI + tests + review + manual QA | Düşük | Çok yüksek | Yüksek |

Senior seviye: Context'e göre kaydır. Prototip için autopilot OK. Production için manual QA zorunlu.

## Gotchas (What Could Go Wrong)
- **Context erosion:** Uzun session'larda AI önceki kuralları unutur. Critical rule'ları her seferinde hatırlat
- **Confident hallucination:** AI yanlış bilgiyi çok emin şekilde verir. Emin tonunu doğrulukla karıştırma
- **Silent dependency upgrades:** AI package version'unu değiştirebilir. `package.json` diff'ini her zaman kontrol et
- **Test theater:** Testler geçer ama yanlış şeyi test eder. Her test için "hangi bug'ı yakalar?" sor
- **Refactor rot:** AI refactoring yaparken unrelated dosyalara dokunabilir. Diff'in scope'unu kontrol et

## Connections
- Related: [[What Could Go Wrong]], [[Edge Case Thinking]], [[Assumption Questioning]]
- Leads to: [[Code Review Mindset]], [[Testability-Driven Design]]
- Contrast with: [[Full Autopilot Mode]] (yok — olması da istenmez)

## Real Examples (From My Projects)
- **MarketPulse:** AI-generated scraper'da rate limiting'i unutmuş, prod'da ban yemişti. → [[Failure Modes]] sayfasına lesson olarak eklenmeli
- **menzernaturkiye:** AI generated component'te loading state yoktu, user'lar boş ekran görüyordu → [[Loading Empty Error States]] sayfası bu için var
- **prompt_generator:** AI initial schema'yı normalize etmemişti, 3. migration'da büyük refactor gerekti → [[Schema Design Principles]] sayfası

## My Notes
- Bir AI-generated PR review yaparken, "bu kodun her satırını ben yazmış olsaydım, bu aynı satır olur muydu?" sorusu çok işe yarıyor
- AI'ın "bu industry best practice" demesi bir şey ifade etmez — contextine bakarak değerlendir
- "Önce testi yaz" AI ile bile geçerli. AI'a önce failing test yazdır, sonra implementation iste
```

- [ ] **Step 2: Verify page structure**

```bash
grep -c "^##" "/Users/projectx/Documents/Obsidian Vault/claude-based-development/fullstack-dev/pages/9-meta-skills/ai-assisted-engineering.md"
```

Expected: 10+ section headers (##).

- [ ] **Step 3: Verify wikilinks**

```bash
grep -o '\[\[.*\]\]' "/Users/projectx/Documents/Obsidian Vault/claude-based-development/fullstack-dev/pages/9-meta-skills/ai-assisted-engineering.md" | wc -l
```

Expected: 8+ wikilinks.

---

## Task 3: Write `what-could-go-wrong.md`

**File:** `fullstack-dev/pages/9-meta-skills/what-could-go-wrong.md`

The "What could go wrong?" reflex — a mental checklist that fires before any implementation.

- [ ] **Step 1: Write the page**

Content will follow the concept page format. Key sections:
- Why It Matters: This is the single reflex that separates senior from junior
- The 8 Failure Categories checklist (Input, Network, State, Concurrency, Edge Cases, Failure, Security, Observability)
- Decision framework: "Before I implement X, what could break?"
- Patterns: Pre-mortem thinking, failure mode enumeration, stress testing
- Anti-patterns: Happy-path-only coding, optimistic assumptions
- Trade-offs: How paranoid is too paranoid?
- Real examples from MarketPulse (scraper failures, rate limits, cache invalidation)

Full content provided in executing step — engineer should write a comprehensive page following the `ai-assisted-engineering.md` depth and structure, covering the 8 failure categories listed above, with Turkish explanations, decision framework, patterns, anti-patterns, and connections to [[Edge Case Thinking]], [[Failure Modes]], [[Retries Timeouts Idempotency]], [[AI-Assisted Engineering Discipline]].

- [ ] **Step 2: Verify structure and links**

```bash
grep -c "^##" fullstack-dev/pages/9-meta-skills/what-could-go-wrong.md
grep -o '\[\[.*\]\]' fullstack-dev/pages/9-meta-skills/what-could-go-wrong.md | wc -l
```

Expected: 8+ sections, 6+ wikilinks.

---

## Task 4: Write `edge-case-thinking.md`

**File:** `fullstack-dev/pages/9-meta-skills/edge-case-thinking.md`

Systematic edge case enumeration — the taxonomy of things that break.

- [ ] **Step 1: Write the page**

Key sections:
- Why It Matters: AI writes happy path well; edge cases are where bugs live
- The Edge Case Taxonomy: Empty, Null, Huge, Zero, Negative, Duplicate, Concurrent, Network, Permission, Stale, Unicode, Timezone
- Decision framework: For each input/state/interaction, enumerate boundary values
- Patterns: Boundary testing, equivalence classes, fuzz thinking
- Real examples: Unicode issues in menzernaturkiye, empty state in prompt_generator

- [ ] **Step 2: Verify**

```bash
grep -c "^##" fullstack-dev/pages/9-meta-skills/edge-case-thinking.md
```

Expected: 8+ sections.

---

## Task 5: Write `requirement-clarification.md`

**File:** `fullstack-dev/pages/8-product-decision-making/requirement-clarification.md`

Before writing code, make sure you're solving the right problem.

- [ ] **Step 1: Write the page**

Key sections:
- Why It Matters: AI is excellent at solving the wrong problem quickly
- The Clarification Framework: Who, What, Why, When, Where, How, What-If
- Done Definition: What does "complete" mean explicitly?
- Hidden requirements: What's not said but implied?
- Patterns: Story writing, user interview, example-driven spec
- Anti-patterns: "I'll figure it out as I go", accepting vague specs
- Real examples from user's projects

- [ ] **Step 2: Verify**

```bash
grep -c "^##" fullstack-dev/pages/8-product-decision-making/requirement-clarification.md
```

Expected: 8+ sections.

---

## Task 6: Write `scope-control.md`

**File:** `fullstack-dev/pages/8-product-decision-making/scope-control.md`

MVP vs gold-plating — knowing when to stop.

- [ ] **Step 1: Write the page**

Key sections:
- Why It Matters: AI can keep adding features indefinitely; someone must say "enough"
- MVP / v1 / Later taxonomy
- Decision framework: "Does this need to exist for the user to get value?"
- Patterns: Cut-lines, feature flags, phased rollout
- Anti-patterns: Over-engineering, premature abstraction, gold-plating
- Trade-offs: Ship-fast vs ship-perfect
- Real examples

- [ ] **Step 2: Verify**

```bash
grep -c "^##" fullstack-dev/pages/8-product-decision-making/scope-control.md
```

Expected: 8+ sections.

---

## Task 7: Update Index and Log

**Files:**
- Modify: `fullstack-dev/index.md`
- Modify: `fullstack-dev/log.md`
- Modify: `master-index.md`

- [ ] **Step 1: Update `fullstack-dev/index.md`**

Add entries under categories 8 and 9:

```markdown
## 8. Product & Decision Making
- [[Requirement Clarification]] — Before coding, make sure you're solving the right problem
- [[Scope Control]] — MVP vs gold-plating, knowing when to stop

## 9. Meta Skills
- [[AI-Assisted Engineering Discipline]] — Systematic review of AI output to catch what it misses
- [[What Could Go Wrong]] — The senior reflex, 8 failure categories checklist
- [[Edge Case Thinking]] — Taxonomy of boundary conditions that break systems
```

Update frontmatter: `total_pages: 5`, `updated: 2026-04-12`.

- [ ] **Step 2: Update `fullstack-dev/log.md`**

Append:
```markdown
## [2026-04-12] ingest | Phase 1 — Senior Reflex Foundations
- Source: User-directed Phase 1 priority content (no raw source)
- Pages created: [[AI-Assisted Engineering Discipline]], [[What Could Go Wrong]], [[Edge Case Thinking]], [[Requirement Clarification]], [[Scope Control]]
- Pages updated: None (first content — no existing pages)
- Key takeaways: Decision-oriented content established; senior reflex foundations address AI-assisted development gap; cross-references to future pages prepared
```

- [ ] **Step 3: Update `master-index.md`**

Change fullstack-dev row:
```markdown
| [[fullstack-dev/index\|Fullstack Dev]] | 5 | 2026-04-12 | Architecture, Next.js, React, TS, senior reflex |
```

---

## Task 8: Verification

- [ ] **Step 1: Count files created**

```bash
find "/Users/projectx/Documents/Obsidian Vault/claude-based-development/fullstack-dev" -name "*.md" | wc -l
```

Expected: 8 (CLAUDE.md + index.md + log.md + 5 Phase 1 pages).

- [ ] **Step 2: Verify all Phase 1 pages exist**

```bash
ls /Users/projectx/Documents/Obsidian\ Vault/claude-based-development/fullstack-dev/pages/9-meta-skills/
ls /Users/projectx/Documents/Obsidian\ Vault/claude-based-development/fullstack-dev/pages/8-product-decision-making/
```

Expected:
- `9-meta-skills/`: ai-assisted-engineering.md, what-could-go-wrong.md, edge-case-thinking.md
- `8-product-decision-making/`: requirement-clarification.md, scope-control.md

- [ ] **Step 3: Verify wikilinks are consistent**

```bash
cd "/Users/projectx/Documents/Obsidian Vault/claude-based-development" && \
grep -o '\[\[[^]]*\]\]' fullstack-dev/pages/9-meta-skills/*.md fullstack-dev/pages/8-product-decision-making/*.md | sort -u
```

Expected: List of wikilinks. Verify that links pointing to other Phase 1 pages use correct titles.

- [ ] **Step 4: Verify index accuracy**

Read `fullstack-dev/index.md` and confirm:
- 5 entries listed with one-line summaries
- `total_pages: 5` in frontmatter
- Categories 1-7 still have `<!-- ... -->` placeholders (not yet populated)

- [ ] **Step 5: Final report**

Produce a summary:
- Total files created: 8
- Categories populated: 2 (meta-skills, product-decision-making)
- Categories pending: 7
- Next recommended step: Phase 2 (Architectural Decision Framework pages)

---

## Notes for Executor

**Content writing guidelines:**
- Write in Turkish explanations where helpful, but technical terms stay in English
- Every page must be ~800-1200 words
- Every page must have: Why It Matters, Decision Framework, Patterns, Anti-patterns, Trade-offs, Gotchas, Connections, Real Examples, My Notes
- Reference user's projects (MarketPulse, menzernaturkiye, prompt_generator) in Real Examples section when relevant
- Use `[[wikilinks]]` even for pages that don't exist yet (they'll be created in later phases) — these become "gaps" that `/gaps` skill can detect

**For Tasks 3-6**, the plan only gives structure because writing 4 full pages in this plan would make it unwieldy. The executor should follow the depth and format of Task 2's `ai-assisted-engineering.md` page when writing each.

**No git commits** — this vault is not a git repository. Skip all commit steps.
