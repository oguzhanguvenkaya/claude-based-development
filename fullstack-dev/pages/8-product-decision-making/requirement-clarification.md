---
title: "Requirement Clarification"
domain: fullstack-dev
category: 8-product-decision-making
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - product-thinking
  - requirements
  - scope
  - decision-making
---

# Requirement Clarification

> One-line summary: Kod yazmadan önce gerçek problemin ne olduğunu anlama disiplini. AI hızlı yanlış çözüm üretmekte usta olduğu için, doğru soruyu sormak artık daha kritik.

## Why It Matters (Senior Perspective)

Senior ile junior arasındaki en sessiz fark burada görünür: junior **yazılan requirement**'i uygular, senior **altındaki gerçek ihtiyacı** anlamadan hareket etmez.

AI-assisted development bu sorunu iki kat büyütür: AI da requirement'i "olduğu gibi" alır ve çok hızlı yanlış yöne gider. Saatler sonra ortaya çıkar ki yanlış problemi çözmüşsün, çünkü "ne istendi?" sorusu atlandı.

> "Teknik olarak çalışan ama yanlış çözüme giden kod" — bu tam olarak AI çağında en yaygın senior gap'tir.

Gerçek senior refleksi: **"Önce soruyu netleştir, sonra koda geç"**. Bu çok sıkıcı gelebilir ama bir feature'ı 3 kez yeniden yazmaktan daha hızlıdır.

## Core Concept

Her "requirement" aslında bir iceberg'dir:
- **Görünür kısım:** Yazılan veya söylenen istek ("bir login sayfası istiyorum")
- **Gizli kısım:** Altındaki gerçek ihtiyaç, kısıtlar, başarı kriterleri, bağlam

Requirement clarification = gizli kısmı yüzeye çıkarma sanatı. Bu yapılmazsa AI (veya junior developer) "görünür kısma" göre hızlıca çözer — ve gizli kısımlarla çakışınca feature yeniden yazılır.

## The Clarification Framework — 7W

Her requirement'i 7 soruyla netleştir:

### 1. Who (Kim?)
- Bu feature'ı kim kullanacak?
- Authenticated mi, anonymous mu?
- Admin mi, regular user mı, external partner mı?
- Teknik kullanıcı mı, sıfır deneyim mi?
- **Klasik hata:** "User" deyip geçmek — hangi user?

### 2. What (Ne?)
- Kullanıcı bu feature'dan ne bekliyor?
- Output nedir? (liste, sayı, notification, PDF?)
- Input nedir? (form, file, URL, none?)
- "İstediği" ile "ihtiyacı" aynı mı? (Çoğu zaman değil)
- **Klasik hata:** Asıl problemi değil, kullanıcının **çözüm önerisini** yapmak

### 3. Why (Neden?)
- Bu feature'ın iş değeri nedir?
- Hangi problemi çözüyor?
- Bu feature olmadan kullanıcı ne yapıyor şu an?
- Yoksa ne kaybederiz?
- **Klasik hata:** "Why"i bilmeden "what"i yapmak — sonra değişir

### 4. When (Ne zaman?)
- Kullanıcı bu feature'ı hangi durumda kullanır?
- Günde bir mi, dakikada bir mi?
- Peak yükler var mı?
- Deadline var mı?
- **Klasik hata:** Usage frequency'yi bilmemek → yanlış performance assumption

### 5. Where (Nerede?)
- Mobile mı, desktop mı, ikisi de?
- Hangi ekrandan ulaşılacak?
- Offline çalışmalı mı?
- Hangi browser/device support?
- **Klasik hata:** "Web app" deyip mobile sorumluluğunu atlamak

### 6. How Much (Ne kadar?)
- Kaç kullanıcı etkilenecek?
- Kaç veri satırı işlenecek?
- Rate limit, quota var mı?
- Max input size?
- **Klasik hata:** Scale'i düşünmeden pattern seçmek (10 user pattern vs 10M user pattern)

### 7. What If (Ya...?)
- Failure mode'lar ne? (Bak: [[What Could Go Wrong]])
- Edge case'ler ne? (Bak: [[Edge Case Thinking]])
- Kötüye kullanım nasıl olabilir?
- 6 ay sonra değişir mi?
- **Klasik hata:** Happy path üstüne feature inşa etmek

## Done Definition — "Bitti" Ne Demek?

Requirement'ın en çok atlanan kısmı **bitiş kriteri**. "Done" tanımlanmadan başlanırsa "bitmiş gibi görünen ama eksik" kod çıkar.

Senior done tanımı şunları içerir:

```
[ ] Happy path works end-to-end
[ ] Error states handled (network, validation, auth)
[ ] Empty state designed
[ ] Loading state designed  
[ ] Accessibility baseline (keyboard, semantic HTML)
[ ] Mobile responsive
[ ] Tests cover critical path
[ ] Documentation updated (if user-facing)
[ ] Monitoring/logging in place
[ ] Rollback plan (if production-critical)
```

Bu liste feature'a göre daralır veya genişler — ama liste **açıkça yazılır**, implementation öncesi.

## Hidden Requirements — Söylenmeyen Ama Varsayılan

Bazı şeyler söylenmez ama beklenir. Bunları yakalamak senior refleksidir.

**Örnek:** "Ürün listesi göster"
- Söylenmemiş ama beklenen: pagination, search, sort, filter, loading state, empty state, error state, mobile responsive, accessible
- AI sadece "map and render" yapar — diğerleri eksik

Hidden requirement'ları yakalamak için sor:
1. "Bu feature mevcut benzer feature'lara göre ne olmalı?" (Pattern consistency)
2. "Bu production'a çıksın dendiğinde neyi beklenir?" (Production baseline)
3. "Başka bir dev bu feature'ı devralsa ne bulmayı bekler?" (Completeness)

## The Decision Framework

Requirement geldiğinde, kod yazmadan önce 5 dakika şu framework'ten geç:

1. **Problem netliği:** Problemin 1-cümle özetini yazabiliyor muyum?
2. **Kullanıcı flow'u:** Kullanıcı adım adım ne yapacak?
3. **Başarı kriterleri:** Bu feature ne zaman "çalışıyor" sayılır?
4. **Non-goals:** Bu feature ne olmayacak? (Scope control için kritik)
5. **Acceptance scenarios:** Hangi concrete senaryolar başarılı = "done"?

**Eğer 5 dakikada bu 5 soruya cevap yazamıyorsan, requirement net değil.** Clarify et.

## Patterns (Do This)

### 1. Restate Before Building
Requirement geldiğinde, kendi kelimelerinle yeniden ifade et ve onaylat. "Anladığım kadarıyla X istiyorsun çünkü Y. Doğru mu?" Bu sadece 30 saniye alır ve büyük yanlış anlamaları ortaya çıkarır.

### 2. Example-Driven Spec
"Şunu yap" yerine "şöyle bir input, şöyle bir output" şeklinde somut örnekler iste. Concrete examples abstract description'dan her zaman daha iyi iletişim kurar.

### 3. User Story Format
"As a [user type], I want to [action], so that [benefit]" — bu format who, what, why'ı aynı cümlede zorlar.

### 4. Pre-Mortem Spec
"Bu feature prod'a çıktı, 2 hafta sonra kullanıcılar şikayet etti. Neden?" Bu senaryoyu zihnen çalıştır → eksik requirement'ları yüzeye çıkarır.

### 5. Ask "Why" Three Times
İlk cevap genelde yüzeyseldir. "Neden?" 3 kez üst üste sorulursa gerçek ihtiyaç ortaya çıkar.

**Örnek:**
- "Export to CSV istiyorum" — Neden?
- "Excel'de analiz yapmak için" — Neden Excel?
- "Manager'a raporlamak için" — Neden her seferinde?
- **Gerçek ihtiyaç:** Otomatik rapor, manager'a email'lenen. CSV export bunun bir çözüm önerisiydi, asıl problem değildi.

### 6. Non-Functional Requirements
"Nasıl çalışmalı"nın yanında "ne kadar hızlı, ne kadar güvenli, ne kadar available" sorularını da sor. Performance, security, availability — bunlar default "iyi" değil, explicit olmalı.

## Anti-Patterns (Don't Do This)

### "I'll Figure It Out As I Go"
"Başlarım, sonra anlarım" — bu junior moda. Başlarsan AI tarafından "bir çözüm" üretilir ve sonra bu çözümden kurtulmak zor olur (sunk cost fallacy).

### Accepting Vague Specs
"Kullanıcı yönetimi istiyorum" → bu bir requirement değil, bir kategori. Bu kadar bulanık spec'e "tamam" deme.

### Solution-First Thinking
Müşteri/PM "solution" söyler ("CSV export yap"). Sen problem'e in. Çözüm onların önerisi, requirement onların **ihtiyacı**.

### Assumption Cascades
"Herhalde şöyle olmalı..." yerine sor. Assumption ne kadar çok birikirse, yanlış yöne gitme olasılığı o kadar artar.

### Skipping Non-Functional
"Hızlı olsun, güvenli olsun" — default iyi değildir. "Ne kadar hızlı? P50 mi, P99 mu? 500ms mi, 2s mi?" — explicit iste.

### AI Direct-to-Code
Requirement'i direkt AI'a verip kod istemek. AI da senin gibi requirement'i yüzeysel okur ve hemen çözüme geçer. Araya clarification katmanı koy.

## Trade-offs — Ne Kadar Soru?

| Context | Clarification Depth | Neden |
|---------|---------------------|-------|
| Quick prototype / spike | Minimal | Throwaway, fast feedback loop |
| Internal tool | Orta | Kullanıcı sınırlı, iteration hızlı |
| User-facing feature | Yüksek | Yanlış yön pahalı |
| Payment, auth, critical | Maksimum | Hata çok pahalı, regulatory risk |
| Legacy system extension | Yüksek | Mevcut assumptions bilinmeli |

**Uyarı:** Over-clarification ile under-clarification arasında denge var. Her detayı sormak paralyze eder, hiçbir şey sormamak yanlış yöne götürür. Doğru denge: **önemli olanı sor, önemsizini varsay ve doğrulat**.

## Gotchas

- **Implicit context assumptions:** "Authentication yap" — hangi method (session, JWT)? Hangi provider (oauth, email)? Assume etme, sor
- **Changing requirements:** İlk soruda A dedi, implementation'ın yarısında "aslında B" dedi. Bu requirement creep'tir — document et, push back
- **"Should" vs "Must":** Bazı requirement'lar "güzel olur", bazıları "zorunlu". Farkı netleştirmeden hepsini must gibi implement etme
- **Hidden stakeholders:** Spec'i söyleyen tek kişi olsa da etki başkalarına geçer. "Bu feature'dan kim etkilenir?" sor
- **Assumption drift:** 2 ay önce netleşen requirement bugün hala geçerli mi? Uzun projelerde re-clarify et
- **Happy path language:** "When user clicks submit..." → "What if they don't? What if they click twice? What if network fails?" — language happy path odaklıysa, alarm
- **AI doesn't ask:** AI çoğu zaman clarify etmez, hemen çözer. Bu bir bug — sen compensate etmelisin

## Connections

- Related: [[Scope Control]], [[MVP Thinking]], [[What Could Go Wrong]]
- Leads to: [[User Journey Awareness]], [[Trade-off Analysis]], [[Adding a New Feature]] playbook
- Used by: [[Adding a New Feature]], [[Refactoring Strategy]]
- Contrast with: Solution-first development (hızlı ama yanlış yöne gider)

## Real Examples (From My Projects)

- **MarketPulse:** "Trendyol ve Hepsiburada'dan fiyat çek" denmişti. Clarify etmedim, doğrudan scraper yazdım. Sonra "aslında sadece değişenleri bildirmeliyiz" dendi — tüm architecture'ı değiştirdim (polling yerine change detection + notification). Doğru ilk soru: "Bu feature'dan kullanıcı ne bekliyor — tüm data mı, değişiklik mi?" → [[Failure Modes]], [[Changeability Maintainability]]
- **menzernaturkiye:** "Ürün sayfası" — söylenmemişti ama beklenen: mobile responsive, SEO, lazy image loading, accessibility, breadcrumb. Implicit requirement'ları başta yakalasaydım 3 sprint sonra refactor gerekmezdi → [[Core Web Vitals]], [[Accessibility]]
- **prompt_generator:** "User'lar kendi prompt'larını kaydedebilsin" denmişti. Sor: "paylaşabilsin mi, folder'layabilsin mi, export edebilsin mi?" — sormadım, tek kullanıcı/flat liste yaptım. 2 ay sonra feature request: "sharing lazım" — schema redesign → [[Schema Design Principles]]

## My Notes

- Clarification soruları "soru çok soruyor" gibi görünebilir ama bu yatırım, maliyet değil
- AI ile çalışırken ilk prompt **requirement clarification moduna çevir**: "Önce bu requirement'i netleştirelim, kod yazmayalım. Hangi soruları sormalıyım?"
- Yazılı requirement nadiren tam. Sözlü kısmı yakala, onu yaz ve onayla
- "Bu feature neden bugün?" sorusu urgency ile importance'ı ayırır — zaman önceliklendirmesini düzeltir
- Her feature başlangıcında 1 sayfa "mini spec" yaz: problem, kullanıcı, done tanımı, non-goals, 3 acceptance scenario. 30 dakika yatırım, saatlerce koruma
- Bir requirement 3 kere sorulduğunda hala netsizse, requirement yanlış biçimlenmiş demektir. Problem'e geri dön, solution'a değil
