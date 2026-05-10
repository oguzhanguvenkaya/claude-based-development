---
title: "Edge Case Thinking"
domain: fullstack-dev
category: 9-meta-skills
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - meta-skills
  - edge-cases
  - boundary-testing
  - reflex
---

# Edge Case Thinking

> One-line summary: Bug'ların yaşadığı yer sınır koşullarıdır. Bu sayfa edge case'lerin bir taksonomisini ve her input/state/interaction için sistematik boundary enumeration disiplinini tanımlar.

## Why It Matters (Senior Perspective)

Bugs happy path'te nadiren bulunur — happy path zaten test edilir. Bugs **sınırlarda** yaşar: bir koşulun bittiği, diğerinin başladığı yerlerde. Senior refleksi şudur:

> "Bu kodu yazarken nereden başlarım?" değil, "bu kodun limitleri neler, nerelerde kırılır?"

Junior "bu çalışıyor, test yazdım" der. Senior "bu şu 12 durumda çalışıyor, ama 13. — boş array ile — kırılıyor" der. Bu fark, edge case taksonomisini bilmekten geçer.

AI'ın edge case blind spot'u özellikle belirgin. AI happy path'i çok iyi yazar ama edge case'leri sık atlar. Bu yüzden AI-assisted kod manuel edge case enumeration'dan geçmelidir.

## Core Concept

Edge case thinking = **her değişken için uç ve boundary değerleri zihinde canlandırma disiplini**. Bir function, component veya feature tanımlanırken, sadece tipik değil, **sınırda olan** değerleri de düşünmek.

Üç temel soru:
1. **Neyin sınırı?** Her parametrenin kendi sınırı var
2. **Sınırda ne olur?** Off-by-one, overflow, underflow
3. **Sınırın ötesinde ne olur?** Invalid input, forbidden state

## The Edge Case Taxonomy

12 kategorili boundary taksonomisi. Her değişken için bu 12 kategoriden geçerli olanları kontrol et.

### 1. Empty
- Boş string `""`
- Boş array `[]`
- Boş object `{}`
- Boş set, map
- Whitespace-only string `"   "`
- **Klasik bug:** `array[0]` boş array'de undefined döner, sessiz hata

### 2. Null / Undefined
- `null` geçerli bir cevap mı?
- `undefined` beklenmeyen yerde?
- Nullable field zinciri: `user?.profile?.address?.city`
- **Klasik bug:** "Hiçbir zaman null olmaz" sanılan alan bir gün null olur

### 3. Zero
- Sayı 0 — divide by zero?
- 0 length list
- 0 items in cart
- 0 results in search
- **Klasik bug:** `if (value)` 0'ı false olarak alır, beklenmeyen davranış

### 4. Negative
- Negatif sayı beklenmeyen yerde
- Past date (rezervasyon geleceğe olmalı ama kullanıcı geçmişi seçer)
- Negative stock (refund sonrası)
- Scroll position < 0
- **Klasik bug:** `index = length - offset` negatif olabilir

### 5. Huge / Overflow
- 1 milyon kayıt listeleme (pagination yok)
- 10 GB file upload
- 50K karakterlik text (textarea'ya yapıştırılmış kitap)
- JavaScript `Number.MAX_SAFE_INTEGER` aşımı
- Memory limiti
- **Klasik bug:** `fetchAll()` scalar limiti olmadan DB'yi çökertir

### 6. Single
- Sadece 1 item — `items.length - 1` off-by-one?
- İlk sayfa, son sayfa — "previous" ve "next" butonları doğru mu?
- Array'de tek eleman — "ve" bağlacı yerine virgül hatası
- **Klasik bug:** "users" yerine "1 user" — grammar

### 7. Duplicate
- Aynı email ile iki hesap
- Aynı slug ile iki post
- Aynı file upload
- Aynı transaction id
- **Klasik bug:** Unique constraint olmayınca sessizce duplicate kayıt

### 8. Boundary (Off-by-One)
- İlk ve son eleman handle ediliyor mu?
- Pagination: page 1 mi, page 0 mı?
- Date range: endDate dahil mi, hariç mi?
- `length - 1` mi, `length` mi?
- **Klasik bug:** `for (let i = 0; i <= length; i++)` — length+1 iteration

### 9. Concurrency
- İki user aynı anda aynı satırı güncellerse?
- Double submit (kullanıcı 2 kez tıklar)
- Refresh mid-action
- Browser back button mid-flow
- **Klasik bug:** Optimistic lock yok, lost update

### 10. Network / Stale
- Cache'de stale veri
- Offline durumu
- Slow network (3s timeout)
- Request in flight during component unmount
- **Klasik bug:** setState after unmount warning

### 11. Permission / State
- Login olmadan erişim
- Bir permission'ı olan, diğeri olmayan kullanıcı
- Suspended, deactivated, deleted account
- Role değişti mid-session
- **Klasik bug:** IDOR — User A, User B'nin URL'sini tahmin eder ve erişir

### 12. Internationalization
- Unicode, emoji, RTL (Arabic, Hebrew)
- Turkish "İ" vs "i" (toLowerCase farklı çalışır)
- Date format (DD/MM/YYYY vs MM/DD/YYYY)
- Timezone — UTC vs local, DST transition
- Currency — decimal separator, digit grouping
- Collation — sort order locale'e göre değişir
- **Klasik bug:** `.toLowerCase()` Turkish I'yi bozar

## The Decision Framework

Her input/state için bu sırayla sor:

1. **Taxonomy pass:** 12 kategoriden hangisi uygulanabilir?
2. **Valid boundaries:** Geçerli min-max nedir? Geçerli enum set?
3. **Default behavior:** Sınırda ne dönmeli? Error mi, default mi, empty result mı?
4. **Failure strategy:** Invalid input'u reject mi, sanitize mi, log mu?
5. **User feedback:** Edge case hit olduğunda UX ne söylüyor?

## Patterns (Do This)

### 1. Boundary Value Analysis
Her numeric input için test et: min, min+1, normal, max-1, max, max+1. 6 değer, büyük coverage.

### 2. Equivalence Classes
Input alanını "aynı davranış" sınıflarına böl. Her sınıftan bir temsilci test et. Örnek: user yaşı için classes = negative, 0, child (1-12), teen (13-17), adult (18+), senior (65+), unrealistic (150+).

### 3. Explicit Null Handling
`null` ve `undefined`'ı görünür yap. TypeScript strict mode, optional chaining, nullish coalescing (`??`) kullan. "Should never be null" kodda geçerli bir ifade değil.

### 4. Use Types as Contracts
TypeScript'te `User | null` açıkça "null olabilir" der. Fonksiyon signature'ında `User` ise caller null geçemez. Edge case dökümantasyonu type system'de.

### 5. Enumerate, Don't Imagine
Edge case'leri hayal ederek değil, checklist'ten giderek bul. Hayal gücü unutur, checklist unutmaz.

### 6. Fuzz Testing Mindset
Random input ile test etme fikri — elle yapamasan bile zihinde yap. "Random bir string gelse ne olur? Random bir sayı? Random bir date?"

### 7. Empty States as Design Requirement
"Empty state" bir feature'ın parçası, eklenti değil. Design review'da her ekran için empty state gösterilmeli.

## Anti-Patterns (Don't Do This)

### "Won't Happen"
"Kullanıcı hiçbir zaman 0 ürünlü sepet görmeyecek" — evet görecek. İlk kez kaydolan kullanıcı. "Kullanıcı hiç negatif sayı girmez" — evet girer, copy-paste ile.

### Implicit Assumptions
`array[0]` ile başla, length kontrol etmeden — assumption: "array boş değil". Bu assumption kod içinde yazılmaz, ama bozulduğunda runtime'da patlayarak haber verir.

### Fixing Edge Cases Only After Bugs
"Bu bug raporu geldi, düzeltiriz" — her rapor için reactive fix. Senior refleksi: aynı bug pattern'ini diğer yerlerde de ara ve düzelt.

### Ignoring i18n Until Launch
"İlk önce İngilizce'ye çıkarız, sonra çeviririz" — Turkish I, RTL, Unicode problemleri baştan düşünülmezse büyük refactor olur.

### Relying on Happy Path Tests
Test yazarken sadece "should work" cases. Senior: "should handle empty list", "should reject negative count", "should deduplicate".

## Trade-offs

Her edge case'i handle etmek zaman alır. Ne kadar yeter?

| Kriter | Az Handle | Ortalama | Maksimum |
|--------|-----------|----------|----------|
| Kritiklik | Prototype, internal tool | Standard feature | Payment, auth, data integrity |
| Maliyet | Hızlı ama bug'lı | Makul | Yavaş ama sağlam |
| User impact | Az — iç kullanım | Orta | Yüksek — end user görür |
| Reversibility | Kolay düzeltme | Orta | Hard — data kayıpları |

**Pragma:** Her edge case'i handle etmek impossible ve unnecessary. Ama 12 kategoriyi **düşünmek** ve conscious karar almak gereklidir.

## Gotchas

- **Sessiz bug'lar:** Bir edge case yakalanmadan geçer, data corrupt olur, aylar sonra fark edilir
- **Empty initial state:** Yeni kaydolan kullanıcı her ekranda boş liste görür — empty state eksikse UX bozulur
- **Off-by-one camping:** En yaygın bug'lardan biri, özellikle pagination ve date range'de
- **Turkish I problemi:** `"İSTANBUL".toLowerCase()` İngilizce locale'de "i̇stanbul" (dot above i) üretir
- **Daylight savings:** `date + 24 hours` her zaman ertesi gün değildir
- **Assumption creep:** Başlangıçta "asla negatif olmaz" dersin, 6 ay sonra refund feature eklenir, assumption bozulur
- **Collection boundary confusion:** JavaScript `array.slice(0, 5)` 5 dahil değil, ama `Array.from({length: 5})` 5 uzunluk

## Connections

- Related: [[What Could Go Wrong]], [[AI-Assisted Engineering Discipline]]
- Leads to: [[Loading Empty Error States]], [[Form UX]], [[Validation Sanitization]]
- Used by: [[Testing Strategy]], [[Testability-Driven Design]]
- Informs: [[Concurrency Race Conditions]]

## Real Examples (From My Projects)

- **MarketPulse:** Scraped product list boş döndüğünde frontend "yükleniyor" mesajında sonsuza kadar kaldı. Empty category (kategori 1 kategoride) atlamıştı — hem backend hem frontend'te. Lesson: empty state backend kontratının ve frontend component'in **zorunlu** parçası → [[Loading Empty Error States]]
- **menzernaturkiye:** Ürün arama "İ" içeren terimler için case-insensitive çalışmıyordu. Klasik Turkish I problemi — `.toLowerCase()` tr locale olmadan yanlış çalışıyor. Lesson: i18n edge case'leri Turkish context'te başlangıçtan düşünülmeli → [[Accessibility]]
- **prompt_generator:** Kullanıcı 10K+ karakterlik prompt girdiğinde textarea'da lag oldu, form submit 30 saniye sürdü. "Huge input" edge case'i düşünülmemişti. Max length + debounce + pagination eklendi → [[Form UX]]

## My Notes

- Checklist kullanmak "yaratıcı düşünmeyi" kaybetmek değil — hayal gücünü boşa harcamamak. Checklist rutin şeyleri yakalar, yaratıcılığı asıl soruna odaklar
- Her bug report'unu "hangi edge case kategorisinde bu?" diye sorarak kategorize et. Zamanla pattern görürsün
- AI koduna edge case review yaparken 12 kategoriden hızlıca geç. Her biri 10 saniye, toplam 2 dakika — hayat kurtarır
- "İmkansız" dediğin edge case gerçekleşir. Mantık değil, olasılık. Yeterince kullanıcı → her edge case hit edilir
- Date/time/timezone edge case'leri her zaman daha fazla surprise verir, beklediğinden daha karmaşık. Library kullan (`date-fns`, `luxon`), elle hesaplamaya çalışma
