---
title: "Failure Modes"
domain: fullstack-dev
category: 4-backend-reliability-security
type: concept
level: foundation
created: 2026-04-13
updated: 2026-04-13
sources: []
tags:
  - reliability
  - failure
  - resilience
  - decision-making
---

# Failure Modes

> One-line summary: Bir sistemin nasıl bozulabileceğinin sistematik kataloğu. Happy path'in dışında yaşayan tüm "ne olursa"ları yazılım tasarımının baştan parçası yapmak.

## Why It Matters (Senior Perspective)

Bir sistemin "çalışması" demek **iyi günde çalışması** değil, **kötü günde kontrollü bozulması** demektir. Senior refleksi: bir component tasarlarken "bu nasıl bozulacak?" sorusunu "bu nasıl çalışacak?" kadar öne koyar.

Junior kod yazarken "database'e bağlanır, sorgu çalıştırır, sonuç döner" der. Senior aynı yerde 5 failure mode listeler: connection pool exhausted, query timeout, partial result, network blip, DB restart. Her birinin handling'i açık strateji ile belirlenir.

> AI kodu happy path bias'ı ile doludur. Failure mode düşüncesi tam olarak AI'ın zayıf olduğu yerdir — bu senin sisteme en fazla değer katacağın alan.

## Core Concept

Her external dependency (DB, API, cache, file system, 3rd party) bir failure surface'ı getirir. Failure modes bu surface'ın taxonomisidir:

1. **Unavailable** — Erişilemez (bağlanamazsın)
2. **Slow** — Erişilebilir ama yavaş (timeout)
3. **Degraded** — Çalışır ama yanlış / eksik (partial response)
4. **Intermittent** — Bazen çalışır, bazen çalışmaz (flaky)
5. **Overloaded** — Kapasitesini aştı (rate limit, 503)
6. **Corrupted** — Veri yanlış geliyor (schema değişti, encoding bozuk)

Her failure mode için **nasıl tespit** ve **nasıl tepki** stratejisi gerekir.

## The Decision Framework

Bir dependency kullanırken sor:

1. **Criticality:** Bu dependency olmazsa sistem ne kadar çalışır? (Blocker / degraded / tolerable)
2. **Detection:** Bozulduğunu nasıl anlayacağım? (Timeout? Error code? Silent bad data?)
3. **Response:** Bozulduğunda ne yapacağım? (Fail, retry, fallback, circuit break, cache)
4. **Blast radius:** Bu dependency çökerse kaç kullanıcı / feature etkilenir?
5. **Recovery:** Normal'e dönüşü nasıl bileceğim?

## Patterns (Do This)

### 1. Timeouts Everywhere
Default "sonsuza kadar bekle" hiçbir zaman doğru değil. Her dış çağrıda explicit timeout. 30 saniyede cevap gelmediyse büyük ihtimalle hiç gelmeyecek.

### 2. Circuit Breaker
Bir dependency ardarda fail ediyorsa, kısa süre **denemeyi bile bırak**. Yarım saat sonra tekrar dene. Bu hem senin sistemini, hem onların sistemini korur (cascade failure önleme).

### 3. Graceful Degradation
Bir feature çökünce tüm app çökmesin. "Recommendations" servis düştü → recommendation bölümü boş göster, ana ürün sayfası çalışsın.

### 4. Fallback Values
Cache hit alamadıysa → default value. 3rd party analytics down → boş array. Hard fail değil, soft fail.

### 5. Bulkhead Isolation
Bir dependency için ayrı connection pool, ayrı thread pool. Biri tükendiğinde diğerleri etkilenmez. Titanic'in bölmeli gövdesi mantığı.

### 6. Idempotent Operations
Retry yapılabilir kod → idempotent olmalı. Aynı operation iki kez çalıştırılırsa yan etki olmasın.

### 7. Explicit Error Types
`throw new Error("failed")` değil, `throw new PaymentTimeoutError(...)`. Caller hangi failure olduğunu bilsin.

## Anti-Patterns (Don't Do This)

### Silent Swallow
```ts
try { await fetchUser(); } catch { /* nothing */ }
```
Hata yok sayılır, data null olur, downstream'de null reference exception. Görünür yap, handle et.

### Infinite Retry
Hiç bekleme yok, exponential backoff yok, max attempts yok → server'ı DDoS ediyorsun kendi isteklerinle.

### No Timeout
Default timeout yoksa, yavaş bir dependency tüm thread/connection pool'u doldurur ve her şey donar.

### Retry Without Idempotency
Payment processing'de "network timeout oldu, tekrar denedim" → kullanıcı iki kez ücretlendirildi.

### Happy Path Testing Only
Test suite'de sadece "başarılı case" — ne oldu failures? Failures test edilmiyorsa code path'i dead.

### Generic Error Handling
`catch (e)` → log → rethrow. Her hata aynı muamele, hiçbir recovery mantığı yok.

## Trade-offs — Ne Kadar Resilience?

| Context | Resilience Seviyesi | Maliyet |
|---------|-------------------|---------|
| Critical path (checkout) | Maksimum — redundancy, fallback | Yüksek dev effort |
| Read-heavy list pages | Yüksek — cache, degraded mode | Orta |
| Analytics, logs | Orta — best effort | Düşük |
| Internal dashboard | Düşük — "oops" OK | Minimal |
| Prototype | Yok | Yok |

**Uyarı:** Over-engineering resilience kendi complexity'sini getirir. Circuit breaker, retry logic, fallback layer — hepsi bug kaynağı olabilir. Context'e göre seç.

## The 6 Failure Modes in Detail

### 1. Unavailable
- **Sinyal:** Connection refused, DNS failure, 503
- **Tepki:** Circuit break + fallback veya kullanıcıya anlamlı mesaj
- **Örnek:** DB down → maintenance page göster

### 2. Slow (Timeout)
- **Sinyal:** Request timeout, gecikmeli response
- **Tepki:** Timeout set, retry with backoff, fallback to cache
- **Örnek:** API 10 saniye yerine 30 saniye sürdü

### 3. Degraded (Partial/Wrong)
- **Sinyal:** Schema mismatch, missing fields, 200 ama garbage
- **Tepki:** Schema validation, graceful parsing, log and alert
- **Örnek:** 3rd party API field rename yaptı

### 4. Intermittent (Flaky)
- **Sinyal:** %10 failure rate
- **Tepki:** Retry (idempotent ops için), error budget tracking
- **Örnek:** Packet loss olan network üzerinde API calls

### 5. Overloaded (Rate Limit)
- **Sinyal:** 429 Too Many Requests, explicit rate limit headers
- **Tepki:** Backoff, queue, request coalescing
- **Örnek:** Scraping rate limit aşıldı

### 6. Corrupted (Bad Data)
- **Sinyal:** Validation failure, unexpected types, decode errors
- **Tepki:** Reject input, log for investigation, don't propagate
- **Örnek:** User upload'ında malformed JSON

## Gotchas

- **Cascade failures:** Bir dependency çökünce onun bağlı olduğu 5 servis de çöker → domino
- **Thundering herd:** Circuit breaker kapandığında aynı anda 1000 request geri dener → 2. DDoS
- **Silent degradation:** Her şey biraz yavaş, hata yok, monitoring yokluğunda fark edemezsin
- **Retry storm:** Retry logic'i her katmanda var → tek user request 16 gerçek request oluyor
- **Fallback to stale:** Cache fallback yapıyorsun ama cache 2 gün eski → kullanıcı yanlış veri görüyor
- **Hidden dependencies:** Gizli transitive dependency — küçük bir auth servis çökünce her şey dursa bile beklemezsin

## Connections

- Related: [[What Could Go Wrong]], [[Edge Case Thinking]], [[Retries Timeouts Idempotency]]
- Leads to: [[Graceful Degradation]], [[Structured Logging]], [[Root Cause Analysis]]
- Used by: [[Adding a New Feature]] (failure mode enumeration step)
- Contrast with: Fire-and-forget code (no error handling)

## Real Examples (From My Projects)

- **MarketPulse:** Scraping pipeline'da 3rd party API rate limit'e takıldı. İlk reaction: retry loop — ama idempotent olmayan cache write'ları duplicate kayıtlara yol açtı. Fix: rate limiter + idempotency key + dead letter queue.
- **menzernaturkiye:** Product API'si 2 saniye'den sonra yanıt vermiyordu, tüm sayfa hang oluyordu (no timeout). 8s timeout + skeleton UI → UX dramatically improved.
- **prompt_generator:** OpenAI API intermittent 500 dönüyordu (~%3). Initial code hiç retry yapmıyordu → kullanıcılar "bozuk" zannetti. Exponential backoff + user-facing "retrying..." mesajı eklendi.

## My Notes
- Buraya kendi gözlemlerini ekle
