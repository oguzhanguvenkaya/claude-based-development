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
3. Standard sections per page type
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
