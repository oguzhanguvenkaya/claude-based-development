---
title: "Fullstack Dev Wiki — Index"
domain: fullstack-dev
updated: 2026-04-13
total_pages: 15
---

# Fullstack Dev Wiki — Index

## 1. Architectural Thinking
- [[State Locality]] — State nerede yaşamalı: local/URL/server/shared karar framework'ü
- [[Data Flow]] — Veri sistemde nasıl akar: top-down, bottom-up, horizontal, out-of-band patterns
- [[Rendering Strategy]] — CSR/SSR/SSG/ISR/RSC karar matrisi ve reversibility
- [[Component Boundaries]] — Component ne kadar büyük/küçük olmalı, single responsibility
- [[Domain Boundaries]] — Feature-based organization, ubiquitous language, anti-corruption layer

## 2. Data, APIs & Persistence
<!-- Schema, contracts, fetching, optimistic updates, consistency -->

## 3. Frontend Systems & UX
- [[Loading Empty Error States]] — 4 state mode (loading/empty/error/success) her data-driven ekran için

## 4. Backend Reliability & Security
- [[Failure Modes]] — 6 failure kategorisi (unavailable/slow/degraded/intermittent/overloaded/corrupted)
- [[Retries Timeouts Idempotency]] — Reliable network ops için 3'lü: timeout + backoff + idempotency key

## 5. Debugging & Observability
- [[Structured Logging]] — JSON logs, correlation ID, levels, event naming convention
- [[Root Cause Analysis]] — 5 Whys, reproduce-first debugging, fishbone diagram

## 6. Delivery & Operations
<!-- CI/CD, feature flags, incident response -->

## 7. Code Quality & Collaboration
<!-- Refactoring, testing, code review -->

## 8. Product & Decision Making
- [[Requirement Clarification]] — Before coding, make sure you're solving the right problem using the 7W framework
- [[Scope Control]] — MVP/v1/v2/later taxonomy, knowing when to stop adding and start shipping

## 9. Meta Skills
- [[AI-Assisted Engineering Discipline]] — Systematic review of AI output to catch hallucinations, over-engineering, and missing edge cases
- [[What Could Go Wrong]] — The senior reflex, 8 failure categories checklist applied before any implementation
- [[Edge Case Thinking]] — Taxonomy of boundary conditions (empty, null, zero, huge, duplicate, concurrent, i18n) that break systems
