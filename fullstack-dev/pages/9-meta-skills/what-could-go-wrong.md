---
title: "What Could Go Wrong"
domain: fullstack-dev
category: 9-meta-skills
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - meta-skills
  - failure-thinking
  - pre-mortem
  - reflex
---

# What Could Go Wrong

> One-line summary: Her implementation öncesi devreye girmesi gereken senior refleksi — "bu kod production'da nasıl patlar?" sorusunu sistematik olarak sorma ve 8 failure kategorisi üzerinden geçme.

## Why It Matters (Senior Perspective)

Junior ve senior arasındaki en net fark şurada görünür: junior "kodum çalışıyor" der, senior "kodum **nasıl bozulabilir?**" diye sorar. Bu refleks AI-assisted development'ta daha da kritik çünkü AI'ın happy path bias'ı senin failure mode farkındalığını köreltir.

Pre-mortem düşünme — "bu proje başarısız oldu, neden?" sorusunu **başlamadan önce** sorma — senior engineering'in temel taşıdır. Failure mode brainstorming yapmayan biri sürekli production'da sürpriz yer.

> Senin bahsettiğin "kompleks sistemde key point'leri kaçırıyorum" problemi, tam olarak failure mode düşünmeyi atlamanın bir semptomudur.

## Core Concept

Yazılan her satır kod, gelecekte bir sorunun kaynağı olabilir. "What could go wrong?" refleksi her implementation kararından önce devreye girer ve şunu sorar:

1. **Bu kod hangi koşullarda yanlış çalışır?**
2. **Bu kod bozulursa nasıl fark ederim?**
3. **Bozulduğunda ne kadar zarar verir?**
4. **Önlemesi mi kolay, düzeltmesi mi?**

Bu dört soru bir pre-mortem mini-framework'tür. Saniyeler sürer, saatler kazandırır.

## The 8 Failure Categories

Senior bir developer, her implementation öncesi bu 8 kategoride zihinsel kontrol yapar. Bu bir checklist'tir — hızlıca üstünden geçilir, ama hiçbiri atlanmaz.

### 1. Input Failures
- **Empty input:** Boş string, empty array, empty object — handle ediliyor mu?
- **Null/undefined:** Nullable değer sessizce kabul mu ediliyor yoksa explicit mi?
- **Wrong type:** Number bekleniyor, string gelirse? TypeScript runtime korumaz
- **Out of range:** Max length, min value, pagination limit aşılırsa?
- **Malformed:** Invalid JSON, malformed URL, corrupt base64 — parse hatası nasıl?
- **Unicode/encoding:** Emoji, Arabic, RTL, çoklu byte karakter
- **Injection:** SQL, XSS, command injection — sanitization var mı?

### 2. Network Failures
- **Timeout:** Request 30 saniye cevap vermezse?
- **Connection refused:** API endpoint çalışmıyorsa?
- **Partial response:** Stream yarıda kesilirse?
- **Wrong response shape:** API bir değişiklik yaptı ve response farklı geldi?
- **Rate limit:** 429 aldığında ne olur?
- **DNS failure:** Çözümleme başarısızsa?
- **TLS/SSL error:** Certificate expired, hostname mismatch?

### 3. State Failures
- **Stale data:** Cache'de eski veri varsa, kullanıcı günceli bekliyorsa?
- **Race condition:** İki istek aynı anda aynı kaynağı değiştirirse?
- **Duplicate submit:** Kullanıcı butona iki kez tıklarsa?
- **Browser back/forward:** State bozuk mu kalır?
- **Refresh mid-action:** Form yarısında refresh?
- **Multi-tab:** Aynı app farklı tab'larda açıksa?
- **Optimistic update failure:** UI güncellendi ama server red ederse?

### 4. Concurrency Failures
- **Thundering herd:** Cache expire olduğunda 1000 request aynı anda DB'ye giderse?
- **Write conflict:** İki user aynı record'u düzenlerse?
- **Deadlock:** Circular lock oluşursa?
- **Lost update:** Read → modify → write sırasında araya başka yazma girerse?
- **Broken invariant:** Bir transaction yarım kalırsa?
- **Ordering assumption:** Async operation'lar sırayla tamamlanacak varsayımı

### 5. Edge Cases
- **Zero:** 0 length, 0 count, 0 price — divide by zero?
- **Negative:** Negative number beklenmeyen yerde?
- **Huge:** 1 milyon kayıt, 10 GB file, 50K karakter?
- **Single:** Sadece 1 item — array length, pagination logic?
- **Duplicate:** Aynı email, aynı slug iki kez?
- **Boundary:** İlk ve son item (off-by-one?)
- **Timezone:** UTC vs local, DST transition, midnight
- **Leap year, leap second, Feb 29**

### 6. Failure Handling
- **3rd party down:** Payment gateway çalışmıyorsa?
- **DB unavailable:** Connection pool tükenirse?
- **Disk full:** Upload sırasında disk dolarsa?
- **Out of memory:** Process OOM alırsa?
- **Graceful degradation:** Bir feature çökerse tüm app çökmesin
- **Retry vs fail-fast:** Hangisi daha doğru bu case için?
- **Idempotency:** Retry yapınca duplicate oluşmasın

### 7. Security
- **Auth bypass:** Unauthenticated user endpoint'e erişebiliyor mu?
- **Authz broken:** User A, User B'nin verisini görebiliyor mu (IDOR)?
- **CSRF:** State-changing request protected mi?
- **XSS:** User input sanitize edilmeden render ediliyor mu?
- **SQL injection:** Parameterized query kullanılıyor mu?
- **Secret leak:** Env var client'a geçiyor mu? Log'da secret var mı?
- **Dependency vuln:** Package'larda bilinen CVE var mı?

### 8. Observability Gaps
- **Silent failure:** Bir şey bozulursa log'a düşüyor mu?
- **No alerting:** Bozulmayı nasıl fark edeceğim — user mi şikayet etsin?
- **Missing context:** Log'da hangi user, hangi request, hangi state?
- **Unreachable state:** Kod buraya nasıl geldi — stack trace var mı?
- **Untestable:** Bu kodu nasıl test edeceğim, reproducible mi?

## The Decision Framework

Her implementation öncesi sor:

1. **Scope:** Bu değişiklik neyi etkiler? Sadece 1 dosya mı, yoksa 5 sistem mi?
2. **Failure blast radius:** Bu kod bozulursa kaç kullanıcı, ne kadar veri etkilenir?
3. **Reversibility:** Yanlış giderse geri dönebilir miyim? Database migration reversible mi?
4. **Detection:** Bozulursa 5 dakika içinde mi fark ederim, 5 gün sonra mı?
5. **Recovery:** Düzelmek kaç dakika sürer?

Düşük blast radius + hızlı detection + hızlı recovery = güvenli. Yüksek blast radius + gecikmeli detection + zor recovery = durak, daha dikkatli ol.

## Patterns (Do This)

### 1. Pre-Mortem Ritual
Her önemli değişiklik öncesi 2 dakika: "Bu prod'a çıktı, 1 hafta sonra incident oldu. Neden?" Kendi kendine 3-5 senaryo türet.

### 2. Failure Mode Enumeration
Yeni bir component yazıyorsan, 8 kategoride çabuk geçiş yap. Her birinde "geçerli mi?" sor. Çoğu geçerli değildir, ama olan 1-2 tanesi kritik.

### 3. "What If" Diyalogları
Kendi kodunla sohbet et:
- "Bu fetch timeout olursa?" → retry logic
- "Response şekli değişirse?" → schema validation
- "Kullanıcı butona 5 kez basarsa?" → debounce veya disable

### 4. Chaos Mindset (Mental)
Netflix Chaos Monkey gerçek değilse bile, zihninde çalıştır: "DB yavaşladı, ne olur? Redis düştü, ne olur?"

### 5. Exit Criteria Before Implementation
"Bu feature ne zaman done?" sorusuna **implementation'dan önce** cevap yaz. Failure mode'lar handle edilmedeyse done değildir.

## Anti-Patterns (Don't Do This)

### Happy-Path Syndrome
"Kullanıcı doğru şekilde kullanırsa çalışır" — hayır, kullanıcılar her şeyi yanlış kullanır. Browser back yaparlar, refresh atarlar, iki tab açarlar.

### Optimistic Assumption Stacking
"API hızlı cevap verir" + "DB down olmaz" + "Cache güncel olur" — bu üç optimistic assumption'ın çarpımı %90 \* %99 \* %95 = %84 reliability. Senior %84'e razı olmaz.

### "Handle Later" Debt
"Şimdilik try/catch atıp loglayalım, sonra düzeltiriz" — sonra gelmez. Handling stratejisi implementasyonun parçası, sonraki iterasyonun konusu değil.

### "It Should Work" Reasoning
"Test edildi, çalışmalı" değil — "test edildi, ve şu 3 senaryoda davranışını doğruladım". Emin olmakla doğrulamak farklı şeyler.

### Dependency Trust
"Stripe hep çalışır" — hayır. Outage olur. Incident response planın var mı?

## Trade-offs — Paranoia Dengesi

Ne kadar paranoia gerekli? Context'e göre değişir:

| Context | Paranoia Seviyesi | Neden |
|---------|------------------|-------|
| Payment, auth, data integrity | Maksimum | Yanlış giderse çok pahalı (para, güven, legal) |
| Core business logic | Yüksek | Bozulursa kullanıcı etkilenir |
| Nice-to-have features | Orta | Fail ederse tolere edilebilir |
| Internal admin tools | Düşük | Sınırlı etki, trusted users |
| Prototypes, spikes | Çok düşük | Throwaway kod |

**Uyarı:** Yanlış tarafta hata yapmak asimetriktir. Low-paranoia + high-stakes = felaket. High-paranoia + low-stakes = zaman kaybı. Pahasını düşün.

## Gotchas

- **Rare combinations:** Failure'lar tek başlarına değil, kombinasyon halinde gelir. "DB yavaş + cache miss + kullanıcı refresh" → thundering herd
- **Silent degradation:** Her şey yavaşlıyor ama hata yok. Monitoring olmadan fark etmezsin
- **Regional outages:** AWS us-east-1 çökünce tüm app'in çöker mi? Multi-region stratejisi var mı?
- **Dependency cascades:** Bir servis düşünce hangi bağımlı servisler etkilenir?
- **Time-based bugs:** Gün dönümünde, ay sonunda, yıl sonunda çalışan bugs
- **Human errors as failures:** Yanlış env var, yanlış deploy command, typo in SQL — bunlar da failure mode

## Connections

- Related: [[Edge Case Thinking]], [[AI-Assisted Engineering Discipline]], [[Failure Modes]]
- Leads to: [[Retries Timeouts Idempotency]], [[Graceful Degradation]], [[Concurrency Race Conditions]]
- Used by: [[Adding a New Feature]] (pre-development checklist), [[Code Review Mindset]]
- Contrast with: Optimistic coding (ships fast, incidents often)

## Real Examples (From My Projects)

- **MarketPulse:** Scraper 3rd party API'nin rate limit'ini handle etmeden prod'a çıktı. "What could go wrong?" yapılmış olsaydı "rate limit" Network Failures kategorisinde ilk anlarda yakalanırdı. Şimdi retry + backoff + circuit breaker patterns zorunlu → [[Retries Timeouts Idempotency]]
- **menzernaturkiye:** Product listing'de `products.map()` vardı, ama API boş array dönebiliyordu. Edge Cases kategorisinde "zero items" eksikti. Empty state UI yok → boş ekran → kullanıcı "site bozuk" zannetti → [[Loading Empty Error States]]
- **prompt_generator:** User input sanitize edilmeden markdown render ediliyordu. Security kategorisinde XSS riski. Reviewer yakaladı, ama sen implementation sırasında "what could go wrong?" sorsaydın kendin de yakalayabilirdin → [[OWASP Top 10]]

## My Notes

- Pre-mortem 2 dakika sürer ama failure mode'ları yakalamak için 2 saat gerekir. Asimetrik avantaj
- En değerli failure mode'lar hiç düşünmediklerindir — bu yüzden checklist kullan, kendi yaratıcılığına güvenme
- "Bu failure mode production'da oldu mu?" diye kendi log'larına bak. Tarih tekerrür ediyor — aynı kategori sürekli
- AI kod ürettikten sonra **manuel olarak** failure mode pass yap. AI çoğu zaman happy path bias'ıyla çalışır
- En sinsi failure'lar silent olanlardır — hata yok ama davranış yanlış. Logging ve alerting bu yüzden failure handling'in bir parçası, eklentisi değil
