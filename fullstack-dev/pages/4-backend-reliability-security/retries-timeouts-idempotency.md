---
title: "Retries Timeouts Idempotency"
domain: fullstack-dev
category: 4-backend-reliability-security
type: concept
level: pattern
created: 2026-04-13
updated: 2026-04-13
sources: []
tags:
  - reliability
  - retry
  - timeout
  - idempotency
  - resilience
---

# Retries, Timeouts & Idempotency

> One-line summary: Network tabanlı operation'ların "bozulma hakkı" vardır. Bu 3 kavram — retry, timeout, idempotency — bu bozulmayı kontrollü hale getiren triple'dir.

## Why It Matters (Senior Perspective)

Network hiç zaman %100 güvenilir değildir. "Network transparently works" assumption'ı production'da her zaman kırılır. Bu 3 kavramı doğru uygulamak, çökmeyen sistemin minimum gereksinimidir.

Junior "retry ekledim, sorun çözüldü" der. Senior sorar: "retry idempotent mi? Exponential backoff var mı? Max attempts ne? Retry budget'ını kim koruyor? Retry edilen transaction yan etki bıraktı mı?"

> AI kodu genelde "simple retry" ekler — ama idempotency'yi atlarsa retry kendi başına bir bug kaynağıdır.

## Core Concept — The Triple

Bu 3 kavram **birlikte** çalışır, ayrı ayrı değil:

1. **Timeout**: "Bu kadar bekleyeceğim, daha fazla değil"
2. **Retry**: "Başarısızsa tekrar deneyeceğim — ama akıllıca"
3. **Idempotency**: "Aynı işlem iki kez çalışsa aynı sonucu verecek"

Sadece retry + no timeout = sonsuz hang. Retry + timeout + no idempotency = duplicate side effects. Üçü birlikte = reliable resilient system.

## Timeouts

### The Rule
**Her dış çağrıda explicit timeout.** Default timeout (sonsuz veya OS default) kabul edilemez.

### How to Pick
- **Fast local API:** 1-3 saniye
- **Database query:** 5-10 saniye (long query'ler farklı pool)
- **External API:** 10-30 saniye
- **File upload:** Proportional to size
- **Background job:** 5-10 dakika

### Cascading Timeouts
Üst seviye timeout > alt seviye toplamı olmalı. Eğer API endpoint 30s timeout, içinde 5 DB query 10s timeout'luysa → kazandığın tek şey 50 saniye hang.

**Doğru:** Üst timeout = 30s, iç operation'lar < 30s toplamı.

## Retries

### When to Retry
- **Idempotent operation** (GET, PUT with same body, DELETE)
- **Transient failure** (network blip, 503, timeout)
- **External dependency** (uzak API)

### When NOT to Retry
- **Non-idempotent** (POST that creates resources without idempotency key)
- **Permanent failure** (400 bad request, 401 unauthorized, 404 not found)
- **Validation errors** (invalid input)

### Exponential Backoff
```
Attempt 1: fail → wait 1s
Attempt 2: fail → wait 2s
Attempt 3: fail → wait 4s
Attempt 4: fail → wait 8s
Attempt 5: give up
```

Jitter ekle: `wait = base * 2^attempt + random(0, base)`. Bu thundering herd'i önler.

### Retry Budget
Total retry sayısını sınırla — sonsuza kadar retry yapma. 3-5 attempt yeterli.

## Idempotency

### The Rule
**Retry edilebilir her operation idempotent olmalı.** İki kez çalışırsa aynı sonucu vermeli.

### Idempotent by Nature
- GET requests
- PUT (full update)
- DELETE
- Pure computations

### Needs Idempotency Key
- POST (create)
- Payment
- Email send
- Notification

### Idempotency Key Pattern
Client unique key gönderir (UUID), server bu key ile aynı operation'u aynı sonucu üretir.

```ts
// Client
const idempotencyKey = uuidv4();
await fetch('/api/payment', {
  headers: { 'Idempotency-Key': idempotencyKey },
  body: JSON.stringify({ amount: 100 })
});

// Server
if (await wasProcessed(idempotencyKey)) {
  return previousResult;
}
// process, then store
```

### Database-Level Idempotency
`INSERT ... ON CONFLICT DO NOTHING` veya unique constraint + catch.

## Patterns (Do This)

### 1. Retry with Exponential Backoff + Jitter
Base library kullan (`axios-retry`, `p-retry`). Elle yazma, bug yapma.

### 2. Circuit Breaker + Retry
Retry mantığının ötesi. Ardarda fail ederse dur, daha sonra dene.

### 3. Idempotency Keys for Mutations
Her POST için client-side unique key. Server bu key'i geçici olarak hatırlar (Redis, DB).

### 4. Hierarchical Timeouts
Üst → alt operation'lar cascading timeout. `client request 30s → server work 25s → db query 5s`.

### 5. Fail Fast on Non-Retryable
400 response → retry etme, hemen fail. Validation error'ları retry cehennemi.

### 6. Distinguish Errors
Retryable vs non-retryable ayrı exception types. Generic `Error` değil.

## Anti-Patterns (Don't Do This)

### Retry Non-Idempotent POST
Payment request timeout oldu → retry et → kullanıcı iki kez ücretlendirildi. Idempotency key YOKKEN retry **bug**'dır.

### Constant Delay Retry
`setTimeout(..., 1000)` 5 kez. Exponential backoff değil, thundering herd'e aday.

### No Jitter
100 client aynı anda fail olur, aynı exponential backoff ile aynı anda retry → 2. DDoS. Jitter zorunlu.

### Infinite Retry Loop
Max attempts yok. Server'ı DDoS ediyorsun.

### Retry on Validation Error
Kullanıcı yanlış input girdi → 400. Sen retry yapıyorsun → kullanıcı "dönüyor" görüyor, aynı 400 tekrar geliyor.

### Default Timeout (None)
Fetch timeout vermediysen, browser'a göre değişir — bazen 5 dakika, bazen sonsuz. Bilmemek = kontrolsüzlük.

## Trade-offs

| Strateji | Reliability | Latency | Complexity |
|----------|------------|---------|------------|
| No retry | Düşük | Düşük | Düşük |
| Simple retry | Orta | Orta | Düşük |
| Retry + backoff | Yüksek | Yüksek (worst case) | Orta |
| Retry + circuit breaker | Çok yüksek | Kontrollü | Orta |
| Retry + idempotency key | Çok yüksek | Kontrollü | Yüksek |

**Sweet spot:** Production serv için retry + backoff + idempotency. Prototype için no retry OK.

## Gotchas

- **Duplicate side effects:** Non-idempotent + retry = iki kez email, iki kez payment
- **Retry storm:** Her katmanda retry var → 1 request 32 request oluyor (2^5)
- **Client vs server retry:** Client'ta retry var, load balancer'da retry var, ingress'te retry var → 3x çarpım
- **Idempotency key expiration:** Key 24 saat sonra expire oldu, gerçek retry 25 saatte geldi → duplicate
- **Timeout < network latency:** Slow network'te timeout'a takılıp retry → asla başarılı olamaz
- **Blocking retry:** Synchronous retry UI thread'i bloklar → app donar

## Connections

- Related: [[Failure Modes]], [[Graceful Degradation]], [[What Could Go Wrong]]
- Leads to: [[Concurrency Race Conditions]], [[Structured Logging]]
- Used by: [[Adding a New Feature]] (reliability checklist)
- Contrast with: Fire-and-forget (no error handling)

## Real Examples (From My Projects)

- **MarketPulse:** Scraper retry loop'u idempotent değildi → her retry yeni row ekledi → 1000 ürün yerine 7000 kayıt oluştu. Fix: unique constraint on `(source, product_id)` + UPSERT.
- **menzernaturkiye:** Stripe webhook'u retry ediyordu, order status iki kez güncelleniyordu. Idempotency key (webhook event id) ile çözüldü.
- **prompt_generator:** OpenAI API timeout'u 5 saniyeydi ama API bazen 15s sürüyordu → her request fail. Timeout 30s'e çıkarıldı + exponential backoff retry eklendi.

## My Notes
- Buraya kendi gözlemlerini ekle
