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

AI ile çalışan bir developer'ın en büyük riski, teknik olarak **çalışan ama yanlış olan** koda gitmektir. Kod derlenir, testler geçer, deploy olur — ama hidden assumptions, hallucinated API'ler, over-engineering veya security gap'leri gözden kaçar. Junior'lar "çalışıyor, tamam" der. Senior refleksi farklıdır:

> **AI bir junior developer gibi muamele edilmelidir** — hızlı üretir, iyi görünen kod yazar, ama her çıktı review'dan geçmelidir. AI'ın hız avantajı, ancak senin review disiplinini kaybetmediğin sürece değerlidir.

## Core Concept

AI-assisted development iki moda ayrılır:
1. **Assistant mode:** AI bir subtask yapar, sen yönlendirir ve doğrularsın
2. **Autopilot mode:** AI çıktısı kör kabul edilir, sen sadece "next" dersin

**Senior disiplin = Autopilot mode'da bile Assistant mode refleksi.**

AI, problemin %80'ini hızlı çözer. Kalan %20 — edge cases, integration points, hidden assumptions — senin senior bakış açınla kapatılmalıdır. Bu %20 çoğu zaman production'da en çok acı veren kısımdır.

## The Decision Framework

AI bir şey ürettiğinde sırayla sor:

1. **Problem understanding:** AI benim çözmek istediğim problemi **doğru** anladı mı? Yoksa kendi yorumuyla farklı bir problemi mi çözüyor?
2. **Assumption check:** AI hangi varsayımları yaptı? Bu varsayımlar **benim** context'imde geçerli mi?
3. **API reality:** AI'ın kullandığı API / library / method gerçekten var mı ve **bu versiyonda** çalışıyor mu?
4. **Simplicity check:** AI over-engineer ediyor mu? Bu abstraction'a **gerçekten şimdi** ihtiyacım var mı?
5. **Edge cases:** Happy path dışında ne olur? Null, empty, error, concurrent, huge, zero, negative?
6. **Security:** Input validation, auth, secret'lar, CORS doğru ele alınmış mı?
7. **Context fit:** AI'ın çözümü projemin **mevcut pattern**'leriyle uyumlu mu, yoksa yeni bir pattern mı icat etti?
8. **Observability:** Bu kod bozulursa nasıl fark edeceğim? Logging, error tracking var mı?

## Patterns (Do This)

### 1. Triangulate Critical Output
AI önemli bir karar verdiğinde (architecture, security, data flow), aynı soruyu 2-3 farklı şekilde sor. Tutarlı cevap → güvenilirlik artar. Çelişen cevaplar → daha derin incele, belki AI hallucinate ediyor.

### 2. Demand Trade-off Reasoning
"Şu X'i yap" dediğinde AI sana kodu verir. Bunun yerine: "X ve Y arasındaki trade-off nedir, hangi durumda hangisi?" sor. Bu sadece kod değil, **akıl yürütme** gerektirir ve AI'ın gerçekten düşünüp düşünmediğini ortaya çıkarır.

### 3. Read Before Accept
Her dosya düzenlemesinden sonra diff'i oku. **Prensip: anlamadığın satır yok**. Anlamadığın bir şey varsa dur, sor, araştır. "Kısmen anladım" yeterli değil.

### 4. Test the Happy Path Manually
Kod testleri geçse bile, feature'ı UI/CLI'dan manuel dene. Testlerin yakalamadığı UX bug'ları, hydration sorunları, yanlış data formatları çok yaygındır.

### 5. Preserve Existing Patterns
AI yeni bir pattern öneriyorsa, "neden mevcut pattern'i kullanmıyoruz?" diye sor. Çoğu zaman AI projenin context'ini tam görmediği için yeni bir yol icat eder. Bu code base tutarsızlığına yol açar.

### 6. Layered Validation
Tek katman yeterli değil. Her kritik değişiklikte 4 katman:
- **Syntax layer:** TypeScript compiler, ESLint
- **Logic layer:** Unit/integration tests
- **Integration layer:** E2E test veya manuel senaryo
- **Review layer:** Human read-through — sen

### 7. Make AI Justify, Not Just Produce
"Bu kodu yaz" yerine "bu kodu yaz ve neden böyle yazdığını açıkla" de. Justification sürecinde AI kendi gap'lerini fark edebilir veya sen gerekçede yanlışlık görebilirsin.

## Anti-Patterns (Don't Do This)

### Blind Accept
"Çalışıyor gibi duruyor, devam" — en tehlikeli pattern. İşte o anda bir güvenlik açığı, race condition veya memory leak eklemiş olabilirsin. Çalışmak ≠ doğru olmak.

### Context Drop
Uzun bir session'da context kaybolur. AI'ın yaptığı önceki işleri hatırladığını varsayma. Kritik decision'ları açık dokümanlara (wiki, CLAUDE.md) yaz — AI'ın memory'sine güvenme.

### Copy-Paste Without Adaptation
AI'dan gelen kodu olduğu gibi yapıştırma. Değişken isimleri, import path'leri, error handling, logging formatı — projenin pattern'ine **mutlaka** uyarla.

### Hallucinated API Trust
AI bazen var olmayan method'lar veya package'lar uydurur. Özellikle az bilinen library'lerde bu riskli. Dokümantasyondan veya `node_modules/` source'dan doğrula.

### Over-Engineering Acceptance
AI "best practice" adına gereksiz abstraction'lar ekleyebilir — factory pattern, dependency injection container, generic wrapper'lar. Soru: "Bunu **şimdi** gerçekten ihtiyacım var mı, yoksa YAGNI mi?"

### Skipping Error Paths
AI happy path'i çok iyi yazar. Error, loading, empty state'ler sık atlanır. Her feature'da bu 4 hali açıkça açmaya zorla.

### Trusting Generated Tests Alone
AI testleri koda göre üretir, ama test kalitesini sorgulamak gerekir. Sor: "Bu test **hangi bug'ı** yakalar? Kaldırırsak ne olur?" Tautology test'ler (sadece koda eşit assertion'lar) sık çıkar.

## Red Flags — AI Çıktısında Dikkat Edilecekler

| Red Flag | Ne Yapmalı |
|----------|------------|
| Yeni bir library eklemiş (sen istemedin) | "Neden?" sor, mevcut araçlarla alternatif iste |
| `any` tipi veya `@ts-ignore` kullanmış | Reject — tip güvenliğini bozma, neden gerektiğini sor |
| Error handling `catch { }` ile sessizleştirmiş | Reject — hataları görünür yap veya açıkça decide et |
| Test yok veya çok zayıf | Gerçek, behavior-focused testler iste |
| Mevcut pattern'den sapmış | Neden olduğunu sor, context'i yeniden ver |
| Commit message vague (`update code`) | Daha spesifik iste — hangi feature, hangi fix |
| Magic number veya hardcoded değer | Konstant veya config'e taşıt |
| "Production-ready" diyor ama error handling yok | Her iddiayı doğrulanabilir kanıtla iste |
| Refactoring sırasında unrelated dosyalar değişmiş | Scope'u daralt, sadece task ile ilgili kısmı iste |
| Env variable hardcode edilmiş | `process.env` üzerinden, validation ile iste |

## Trade-offs

| Yaklaşım | Hız | Güvenlik | Öğrenme | Uygun Yer |
|----------|-----|----------|---------|-----------|
| Full autopilot | Çok yüksek | Çok düşük | Yok | Throwaway prototype, spike |
| AI + tests | Yüksek | Orta | Düşük | MVP, internal tooling |
| AI + tests + review | Orta | Yüksek | Orta | Standard production code |
| AI + tests + review + manual QA | Düşük | Çok yüksek | Yüksek | Payment, auth, critical path |

**Senior seviye:** Context'e göre kaydır. Prototip için autopilot OK. Production'a çıkan kod için en az "AI + tests + review". Payment veya auth dokunuyorsan manual QA zorunlu.

## Gotchas (What Could Go Wrong)

- **Context erosion:** Uzun session'larda AI önceki kuralları unutur. Critical rule'ları her seferinde hatırlat veya project CLAUDE.md'ye yaz
- **Confident hallucination:** AI yanlış bilgiyi çok emin şekilde verir. **Emin tonunu doğrulukla karıştırma** — güven seviyesi ile doğruluk orantılı değil
- **Silent dependency upgrades:** AI package version'unu değiştirebilir. `package.json` ve lock file diff'ini **her zaman** kontrol et
- **Test theater:** Testler geçer ama yanlış şeyi test eder. Her yeni test için "hangi bug'ı yakalar?" sor
- **Refactor rot:** AI refactoring yaparken unrelated dosyalara dokunabilir. Diff'in scope'unu kontrol et — "bir method'u rename et" → 30 dosya değişmiş → durak
- **Hidden state mutation:** AI sometimes mutates objects/arrays in place. Immutable pattern'den sapıldıysa dur
- **Forgotten cleanup:** Event listener, interval, subscription, connection — AI bunları kurar ama cleanup'ını unutabilir

## Connections

- Related: [[What Could Go Wrong]], [[Edge Case Thinking]], [[Assumption Questioning]]
- Leads to: [[Code Review Mindset]], [[Testability-Driven Design]]
- Used by: [[Adding a New Feature]] playbook, [[Debugging Playbook]]
- Contrast with: Full manual coding (slower but higher assumption awareness)

## Real Examples (From My Projects)

- **MarketPulse:** AI-generated scraper'da rate limiting'i ve retry backoff'u unutmuş, prod'da IP ban yemişti. Root cause: AI happy path yazdı, failure mode düşünmedi. → [[Failure Modes]] ve [[Retries Timeouts Idempotency]] sayfalarına lesson olarak eklenmeli
- **menzernaturkiye:** AI generated ProductCard component'inde loading state yoktu, kullanıcılar API cevap dönene kadar boş ekran görüyordu. Root cause: AI'a "card component yap" denmiş, 4 hal (loading/empty/error/success) istenmemiş. → [[Loading Empty Error States]] sayfası bu incident için var
- **prompt_generator:** AI initial Drizzle schema'yı normalize etmemiş, tüm metadata JSON column'da tutmuş. 3. migration'da büyük refactor gerekti çünkü query performance'ı düştü. Root cause: AI "quick start" moduna kaçtı, uzun vadeli evolution düşünmedi. → [[Schema Design Principles]] ve [[Changeability Maintainability]] sayfaları

## My Notes

- "Bu kodun her satırını ben yazmış olsaydım, bu aynı satır olur muydu?" sorusu çok işe yarıyor. Cevap "hayır" ise → incele
- AI'ın "bu industry best practice" demesi bir şey ifade etmez. Context'ine bakarak değerlendir — best practice ≠ your case
- "Önce testi yaz" AI ile bile geçerli. AI'a önce failing test yazdır, sonra implementation iste — bu happy-path bias'ını azaltır
- AI'ın hallucinate ettiği en yaygın yerler: 1) Az kullanılan library'lerin method isimleri, 2) Framework version'ları arası API değişiklikleri, 3) Type definition'lar
- Her AI session sonunda kendi kendine "bugün kod yazdım ama ne öğrendim?" sor. Eğer cevap "hiçbir şey" ise → autopilot'taydın, dikkat et
