---
title: "Structured Logging"
domain: fullstack-dev
category: 5-debugging-observability
type: concept
level: foundation
created: 2026-04-13
updated: 2026-04-13
sources: []
tags:
  - observability
  - logging
  - debugging
  - production
---

# Structured Logging

> One-line summary: Log'lar string değil, parse edilebilir data olmalı. Structured logging (JSON) + context + level + correlation ID = production debug'ın temelleri.

## Why It Matters (Senior Perspective)

`console.log("it worked")` development'ta OK. Production'da **işe yaramaz**. Bir problem çıktığında, milyonlarca request içinden seninkini bulamazsın. Hangi user, hangi timestamp, hangi request ID, hangi state — bunlar olmadan debug impossible.

Senior refleksi: "Production'da bu kod bozuldu — log'dan ne öğrenebilirim?" sorusu **kod yazarken** sorulmalı. Log ekleme retroactive olarak incident sırasında eklenirse, o incident zaten kaybedildi.

> AI'ın ürettiği kodda logging genelde minimal veya yanlış. Bu senin compensate etmen gereken bir başka alan.

## Core Concept

Structured logging = logs as **data**, not as **text**.

```ts
// ❌ Unstructured
console.log(`User ${userId} failed to login at ${new Date()}: ${error.message}`);

// ✓ Structured
logger.warn('login_failed', {
  userId,
  timestamp: new Date().toISOString(),
  error: error.message,
  errorCode: error.code,
  requestId,
  userAgent,
});
```

Structured log'lar query edilebilir, aggregate edilebilir, alert tanımlanabilir. Unstructured log'lar sadece insan gözüyle taranabilir — ki production scale'de imkansızdır.

## The 5 Components of a Good Log

### 1. Level
- `debug` — Development only, çok verbose
- `info` — Normal events (request received, user logged in)
- `warn` — Unusual but not broken (retry happened, fallback used)
- `error` — Something broke (exception, failed operation)
- `fatal` — App-level failure (can't start, critical dep down)

### 2. Message (Event Name)
"login_failed" gibi **stable event name**. String interpolation içermez. Query'lenebilir.

### 3. Structured Fields
- `userId`, `orgId`, `requestId`
- `duration`, `statusCode`, `errorCode`
- `source`, `feature`, `action`

### 4. Context (Correlation)
- **Request ID**: Bir kullanıcı request'inin tüm log'larını birbirine bağla
- **Trace ID**: Distributed system'de request path'ı
- **User ID / Session ID**: Kullanıcı bazında filtre

### 5. Timestamp
ISO 8601, UTC, millisecond precision. Client-side log'larsa timezone tutma.

## The Decision Framework

Bir yer log'lamaya değer mi? Sor:

1. **Debug value:** Bu log bir incident'ta işe yarar mı?
2. **Cost:** Ne kadar volume yaratır? (High-traffic endpoint'te her line log'lamak $$)
3. **Sensitive data:** Password, token, PII log'da yok, değil mi?
4. **Action:** Log gözlemcisi bunu gördüğünde ne yapacak?
5. **Uniqueness:** Bu event benzersiz mi, yoksa gürültü mü?

## Patterns (Do This)

### 1. Structured Format (JSON)
Pino, Winston (structured), Bunyan — modern logger kullan. `console.log` production için değil.

### 2. Correlation ID
Her request'e unique ID (middleware ile), aşağıya propagate et. Tüm downstream log'lar bu ID'yi içerir.

```ts
// Middleware
req.id = crypto.randomUUID();
logger.info('request_start', { requestId: req.id, path: req.path });
```

### 3. Context Enrichment
Base logger'a sabit context ekle (service name, version, env):
```ts
const log = logger.child({ service: 'api', version: '1.2.3', env: 'prod' });
```

### 4. Event Naming Convention
- `<subject>_<action>`: `user_logged_in`, `payment_failed`, `cache_missed`
- Tutarlı vocabulary — query'leme kolaylaşır

### 5. Log Critical Paths
- All requests (path, method, duration, status)
- Auth events (login, logout, failure)
- Mutations (create, update, delete)
- External API calls (service, duration, outcome)
- Errors (always)

### 6. Sampling for High-Volume
Her request log'lamak pahalı olabilir — %1 sampling ile pattern'i yakala. Error'lar %100 log'lanmalı.

### 7. Redaction
Sensitive field'ları otomatik kes (password, token, credit card, email opsiyonel):
```ts
logger.info('user_created', redact({ email, password, name }, ['password']));
```

## Anti-Patterns (Don't Do This)

### console.log Production
"Development'ta kullanıyorum, prod'a da kaldı" — unstructured, query edilemez, slow.

### String Interpolation in Message
`"User " + userId + " failed"` → her userId için farklı message string → aggregation zor.

### Logging Secrets
Password, API key, auth token, session id, credit card — hiç log'lanmamalı. PII için de dikkat.

### Too Much Detail
Her satır log → $$ ve noise. Critical path'i log'la, helper function internal'larını log'lama.

### Vague Messages
"something happened", "error", "failed" — context yok, debug imkansız.

### No Correlation ID
Multiple log line'ı bir request'e bağlayamazsın → parallel request'ler karışır.

### Logging at Wrong Level
Her şey `info` veya her şey `error` → level kaybını → alert tanımlanamaz.

## Log Levels in Practice

| Level | Örnek | Prod'da Yer |
|-------|-------|-------------|
| debug | "entering function foo" | Disabled |
| info | "request received", "user logged in" | Enabled, sampled |
| warn | "retry attempted", "fallback used" | Enabled, alerted on spike |
| error | "payment failed", "db query error" | Enabled, alerted |
| fatal | "cannot connect to db" | Enabled, paged |

## Trade-offs

| Approach | Debugability | Cost | Performance |
|----------|-------------|------|-------------|
| No logging | Sıfır | Sıfır | Çok iyi |
| Minimal logging | Düşük | Düşük | İyi |
| Structured, critical only | Yüksek | Orta | İyi |
| Structured, everything | Çok yüksek | Yüksek | Orta |
| + tracing + metrics | Maksimum | Yüksek | Orta |

**Sweet spot:** Structured logging + sampling critical paths + %100 error logs. Enterprise'da tracing ekle.

## Gotchas

- **Log volume explosion:** `logger.info` in a loop → millions of log lines → $$$
- **Sensitive leakage:** Request body'i log'larken içinde password var → security incident
- **Async context loss:** Node.js'te async context'i takip için AsyncLocalStorage gerekli
- **Timezone confusion:** Server UTC, log UI local → log search yanıltıcı
- **Level misuse:** Her şey `error` → alert fatigue → gerçek hatalar görünmez
- **Message mutations:** Interpolated strings → event aggregation imkansız

## Connections

- Related: [[Failure Modes]], [[Root Cause Analysis]], [[What Could Go Wrong]]
- Leads to: [[Monitoring Alerting]], [[Error Tracking]], [[Incident Response]]
- Used by: [[Debugging Playbook]], [[Adding a New Feature]] (observability checklist)
- Contrast with: `console.log` debugging

## Real Examples (From My Projects)

- **MarketPulse:** Production'da random scraping failures vardı. Log'lar `console.log('error')` seviyesindeydi. Request ID + scraper name + target URL + error code structured log'a geçince, 15 dakikada root cause bulundu (belirli bir vendor ID formatı parse edemiyordu).
- **menzernaturkiye:** Order processing'de "bazen 2 kez gönderiliyor" bildirildi. Correlation ID olmadığı için 100+ log satırı arasında hangisinin aynı order'a ait olduğunu bulamadık. Correlation ID eklendi, hemen anlaşıldı (retry loop).
- **prompt_generator:** User login failures'ı `warn` ile log'landı, `error` değil. Alert trigger olmadı, kullanıcılar 2 gün login olamadı. Level fix + alert threshold eklendi.

## My Notes
- Buraya kendi gözlemlerini ekle
