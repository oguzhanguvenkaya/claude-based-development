---
title: "Scope Control"
domain: fullstack-dev
category: 8-product-decision-making
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - product-thinking
  - scope
  - mvp
  - yagni
  - decision-making
---

# Scope Control

> One-line summary: Feature'ın neyi içereceği kadar neyi içermeyeceğini de bilme disiplini. AI ile hızlı eklemek kolay olduğu için, "ne zaman duracağım" artık daha kritik bir beceri.

## Why It Matters (Senior Perspective)

AI ile çalışırken scope kontrolü daha önemli, daha az değil. Nedeni basit: AI her öneriyi "evet, yapayım" diye karşılar. Bir feature eklerken 3 "nice to have" daha önerir. Bunlar birer birer küçük görünür, ama kümülatif olarak projeyi **MVP'den mega-feature'a** dönüştürür.

Junior "daha fazla daha iyi" der. Senior **"yeterli ne zaman yeterli"** diye sorar. Senior refleksi:

> "Bu eklenirse kaç gün kazandıracak? Eklenmezse kaç gün kaybettirecek?" — cevabı bilmiyorsan, eklemesen de olur.

Senin bahsettiğin "kontrol kaybetmek" duygusunun önemli bir kısmı scope control eksikliğinden gelir. Multi-domain bir builder olarak her projede "şunu da ekleyeyim" refleksine kapılırsan, hiçbiri bitmez.

## Core Concept

Scope control üç soruyla yapılır:
1. **Now** (Şimdi): Bu release için zorunlu olan ne?
2. **Next** (Sonraki): Bir sonraki iterasyona bırakılabilecek ne?
3. **Never** (Hiçbir zaman): Hiç yapmamamız gereken ne?

Çoğu developer "now" ve "next"i konuşur. Senior ekstra olarak **"never"** kategorisini de açıkça tanımlar. "Never" olmadan, her şey eninde sonunda "now" olur.

## MVP / v1 / v2 / Later — Taksonomi

Her feature list'i 4 kategoriye ayrılmalı:

### MVP (Minimum Viable)
- Bu olmadan feature anlamsız
- Core value proposition için zorunlu
- En basit "working version"
- Çoğu kullanıcının çoğu zamanda kullanacağı şey

### v1 (Launch Ready)
- Production'a çıkabilmek için gerekli (error states, monitoring, basic mobile)
- MVP + "production baseline"
- "Shippable" için minimum

### v2 (Nice to Have, Soon)
- Kullanıcı memnuniyetini artıracak ama launch için zorunlu olmayan
- Real kullanıcı feedback'inden sonra önceliklendirilecek
- Backlog'da kayıtlı, dondurulmuş değil

### Later (Maybe / Never)
- Teorik olarak güzel ama unclear value
- Sonraki yıl veya asla
- Dondurulmuş, feature creep'i engellemek için açıkça "later" etiketli

## The Decision Framework — "Does This Belong in MVP?"

Bir feature MVP'ye ait mi? Bu soruları sor:

1. **Value test:** Bu olmadan kullanıcı temel ihtiyacını karşılayabiliyor mu?
   - Evet → v2 veya sonraya
   - Hayır → MVP'de olabilir
2. **Frequency test:** Bunu kullanıcıların kaçı, ne sıklıkta kullanacak?
   - Herkes, her gün → MVP
   - Azınlık, nadiren → sonraya
3. **Reversibility test:** Launch sonrası eklemek kolay mı?
   - Evet → sonraya, şimdi yapma
   - Hayır (schema değiştirmeli vb.) → baştan düşün
4. **Cost test:** Bu ne kadar zaman/karmaşıklık ekliyor?
   - Düşük → belki MVP'de
   - Yüksek → v2+
5. **Risk test:** Bu olmadan launch edersek ne risk doğar?
   - User confusion, data loss, security → MVP
   - Memnuniyetsizlik, "güzel olurdu" → v2

Bu 5 sorudan 3'ü "v2" diyorsa, büyük olasılıkla MVP'ye ait değil.

## Patterns (Do This)

### 1. Explicit Cut Lines
Her feature planlaması: "MVP line" çiz. Çizginin altındaki her şey v2+. Bu line kod yazmadan önce çizilmeli, yazarken değil.

### 2. One Feature At a Time
Paralel feature eklemek yerine tek feature'ı tam bitir, sonra diğerine geç. "Bir şeyi 100% bitirmek" diğer 10 şeyi %10 etmekten daha değerli.

### 3. Feature Flags for Uncertain Features
Emin değilsen, feature flag arkasına al. Production'da olsun ama kapalı — "later" kategorisine geçici yerleşim.

### 4. Non-Goals List
Her proje için "yapmayacağız" listesi yaz. Örnek:
- "Bu MVP'de sadece email/password auth var, OAuth yok"
- "Bu v1'de offline support yok"
- "Bu release'te çoklu dil yok"

Bu liste ileride birisi "ama bunu ekliyebilir miyiz?" dediğinde başvuru noktası olur.

### 5. Time-Boxed Experiments
Yeni bir feature idea'sı? "Bu fikri 2 saat araştır, sonra karar ver" de. Time box olmadan araştırma saatlere yayılır, commit olursun.

### 6. "Would I Trade a Day For This?"
Yeni bir feature önerildiğinde kendine sor: "Bunun için 1 günlük çalışmamı verir miyim?" Cevap "hayır" ise ekleme. Bu soru opportunity cost'u görünür yapar.

### 7. Cut From The End, Not From Features
Zaman daralıyorsa "bir feature eksik" yapma. "Her feature %80 done" olmak çok daha kötü. Bazı feature'ları tamamen çıkar, kalanları tam bitir.

## Anti-Patterns (Don't Do This)

### Feature Creep
"Madem bunu yapıyoruz, şunu da ekleyelim" — her "şunu da" gün ekler. MVP'den launch arası süreyi 2-3 katına çıkarır.

### Gold Plating
"Bu kod çalışıyor ama daha güzel yazabilirim" — çalışan kodu refactor etmek yerine yeni feature'a geç. Refactor'ı gerçekten gerektiğinde yap.

### Premature Abstraction
"Bu kodu reusable yapayım, belki başka yerde de lazım olur" — **Şu an** gerekli değilse abstraction yapma. YAGNI (You Ain't Gonna Need It). İkinci kullanım geldiğinde refactor et.

### Infinite Polishing
"Launch etmeden önce biraz daha improve edeyim" — polish sonsuz bir süreçtir. "Ship ve feedback al, sonra improve et" döngüsü daha hızlı ve doğru evrilir.

### Feature Parity Obsession
"Rakipler X'i yapıyor, biz de yapmalıyız" — ama **sen** X'e ihtiyaç duyuyor musun? Pattern-matching ile değil, problem-solving ile karar ver.

### "It's Just a Small Change"
Hiçbir değişiklik "just a small change" değildir. Her ekleme test surface'ını, maintenance burden'ını, bug olasılığını artırır. Küçük görünen şey birikir.

### AI-Driven Expansion
AI'a "bu feature'ı yap" dersin, AI "bu arada X, Y, Z'yi de ekledim, best practice" der. Red flag — review et, gereksiz olanları çıkar. AI optimization for comprehensiveness yapar, sen optimization for focus yapmalısın.

## Trade-offs — Scope Genişliği

| Yaklaşım | Launch Süresi | Kullanıcı Değeri | Risk | Uygun Durum |
|----------|--------------|------------------|------|-------------|
| Tight MVP | Hızlı | Temel | Düşük | Yeni ürün, unclear fit |
| Rich v1 | Orta | Orta | Orta | Rekabet alanı, olgun ürün |
| Feature-complete launch | Yavaş | Yüksek | Yüksek | Enterprise, B2B |
| Continuous shipping | N/A | Artan | Düşük/Orta | Olgun ekip, CI/CD kurulu |

**Senin profilin:** Multi-project builder olarak **tight MVP → continuous shipping** en iyi. Her projede tight MVP ile launch et, sonra feedback-driven büyüt. Bu scope control'u daha da kritik yapar.

## The "Enough" Signal

Feature ne zaman "yeterli"? İşte sinyaller:

- Happy path çalışıyor
- Error states handled
- Empty state var
- Loading state var
- Mobile responsive
- Critical tests pass
- Performance kabul edilebilir

Bu listeyi karşıladığın an **dur**. Daha fazlası v2'nin işi. "Bir şey daha" dürtüsüne direnç göster.

## Gotchas

- **Invisible scope creep:** Tek tek küçük eklemeler her biri haklı gibi görünür, toplamda projeyi büyütür
- **Sunk cost fallacy:** "Bu kadar yatırım yaptım, bitireyim" — yanlış yolda isen, erken bırakmak doğrudur. Sunk cost'u dikkate alma
- **Perfectionism disguised as quality:** "Kaliteli iş yapıyorum" bazen "perfection'a takıldım" demektir. Kalite ≠ perfection
- **Premature optimization:** "Performans için şu da lazım" — ölçmeden optimize etme
- **AI feature avalanche:** AI her requestte eklentiler önerir. "Sadece istediğimi yap, başka bir şey ekleme" diye açıkça söyle
- **Stakeholder ambition creep:** "Bir de şunu..." ikinci kez duyulduğunda "bu v2'ye" diye document et
- **Launch delay spiral:** Her hafta "bir hafta daha" deniyorsa, launch asla olmaz. Sabit launch date koy, scope'u date'e sığdır

## Connections

- Related: [[Requirement Clarification]], [[MVP Thinking]], [[Prioritization]]
- Leads to: [[Trade-off Analysis]], [[Risk Assessment]]
- Used by: [[Adding a New Feature]] (scope phase), [[Refactoring Strategy]]
- Contrast with: Big-bang releases (yüksek risk, düşük feedback)

## Real Examples (From My Projects)

- **MarketPulse:** İlk versiyonda "price monitoring" MVP yeterliydi ama ben "alerting, reporting, user management, dashboard customization" ekledim. 3 ay gecikti. Sonradan fark ettim ki kullanıcılar sadece price notification istiyordu, gerisi noise. MVP = just notification → [[Requirement Clarification]]
- **menzernaturkiye:** Product listing yeterliyken "blog section, video library, testimonials carousel" ekledim. Test edilmemiş feature'lar, hiçbiri kullanılmadı. Cut line çizmemiştim → [[MVP Thinking]]
- **prompt_generator:** Folder system + sharing + export + tags + version history hepsi v1'de planlandı. Teslim baskısı altında hiçbiri kalitesiz çıktı. Doğru karar: sadece "save and retrieve" MVP, diğerleri v2. Gold plating anti-pattern klasiği → [[Scope Control]] (bu sayfa)

## My Notes

- "Bunu eklemek isteyen ben miyim, kullanıcı mı?" sorusu feature creep'i açığa çıkarır
- Her iterasyon sonunda "scope'tan neler çıkardık?" retro sorusu scope discipline kaslarını güçlendirir
- AI'a iş verirken scope'u explicit söyle: "Sadece X yap, Y ve Z'yi ekleme" — AI default olarak ekler
- "YAGNI" ve "MVP" kelimelerini conversation'ında sık kullan — kendine hatırlatır
- Launch etmeden bir release daha refine etmek genelde verimsizdir. Launch → feedback → iterate daha hızlı öğrenme sağlar
- "Later" listesini geçici değil, kalıcı dondurulmuş bir yer gibi düşün — çoğu "later" aslında hiçbir zaman yapılmamalıdır
- Her feature için "non-goals" yazmak göründüğünden daha güçlü bir disiplindir — seni explicit hale zorlar
