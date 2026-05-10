---
title: "Component Boundaries"
domain: fullstack-dev
category: 1-architectural-thinking
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - architecture
  - components
  - separation-of-concerns
  - decision-making
---

# Component Boundaries

> One-line summary: Component ne kadar büyük, ne kadar küçük olmalı? Doğru boundary seçimi kod okunabilirliği, test edilebilirliği ve değiştirilebilirliğin temelidir.

## Why It Matters (Senior Perspective)

Component boundary kararı component'in **sorumluluğunu** tanımlar. Yanlış boundary → prop explosion, çoklu sorumluluk, test zor, değişiklik maliyeti yüksek. Doğru boundary → single responsibility, test kolay, yeniden kullanılabilir.

Junior "tek component'e hepsini yazarım" veya "her şeyi mikro component'e ayırırım" uçlarına gider. Senior dengeyi bulur: **bir component'in yaptığı iş, bir cümlede açıklanabilmelidir.**

> "Çok büyük" ve "çok küçük" arasındaki orta yol, context'e göre değişir. Kural ezberi değil, refleks.

## Core Concept

Component boundary iki soruyla çizilir:
1. **Sorumluluk:** Bu component neyi temsil ediyor / yapıyor?
2. **Değişim ekseni:** Bu component'i değiştirmek için ne kadar sebep var?

Tek sorumluluk, tek değişim ekseni → iyi boundary. Birden fazla → split adayı.

## The Decision Framework

Bir component için sor:

1. **Single responsibility?** Bir cümlede özetlenebilir mi? "User profile gösterir" ✓, "User profile gösterir, edit form, upload avatar, settings de" ✗
2. **Prop count?** 7+ props genelde kötü koku. Bazı props "group" halinde ise destructure et veya ayır.
3. **File length?** 300+ satır genelde fazla — split adayı. 50 satırın altı çoğu zaman under-engineered.
4. **Re-use?** Bu parça başka yerde de kullanılacak mı? Kullanılmayacaksa component olma zorunluluğu yok.
5. **Test story:** Bu component'i nasıl test ederim? Test zor ise boundary yanlış olabilir.
6. **Change frequency:** Hangi parçalar birlikte değişir? Birlikte değişen → birlikte kalsın. Ayrı değişen → ayrılsın.

## Patterns (Do This)

### 1. Single Responsibility per Component
Her component tek iş yapar. `<UserCard>` user bilgisi gösterir, edit form ayrı bir component (`<UserEditForm>`).

### 2. Composition Over Configuration
```tsx
// ❌ Configuration
<Card title="..." body="..." actions={[...]} footer="..." />

// ✓ Composition
<Card>
  <Card.Title>...</Card.Title>
  <Card.Body>...</Card.Body>
</Card>
```

### 3. Container / Presentation Split (When Useful)
Data fetching ve state logic bir component'te, UI rendering başka. Her zaman değil, sadece complex durumlarda.

### 4. Extract When There's Reuse or Complexity
JSX tekrarlanıyor veya bir parça kendi başına anlamlı bir birim → extract et. Sadece "uzun görünüyor" diye extract etme.

### 5. Colocation
Birlikte değişen dosyalar birlikte yaşar. `UserCard.tsx`, `UserCard.test.tsx`, `UserCard.module.css` aynı folder'da.

### 6. Feature Folders, Not Tech Folders
```
❌ /components/, /hooks/, /utils/
✓ /features/user/components/, /features/user/hooks/, /features/user/api/
```

### 7. Leaf Components Should Be Simple
Tree'nin altındaki presentational component'ler minimal logic içermeli — sadece props alıp render.

## Anti-Patterns (Don't Do This)

### God Component
500+ satır, 15+ prop, iç içe 6 state, 10 useEffect. Test imkansız, değiştirmesi korkutucu.

### Prop Drilling Through Layers
Component'ler sadece prop'u aktarıyor, kullanmıyor. 5+ katman prop drill → component boundary yanlış yerde.

### Premature Extraction
Henüz 2. kullanımı yok, ama "belki lazım olur" deyip generic component yapmak. YAGNI ihlali.

### Extraction for Length
Component uzun diye middle'dan keserek sub-component çıkarmak. Sorumluluk değil, satır sayısı odaklı split → worse architecture.

### Tech-Grouped Folders
`/components/`, `/hooks/`, `/utils/` → feature değişirken 5 farklı folder'da değişiklik. Feature folders daha iyi.

### Business Logic in Components
Component'in içinde fetching, transformation, validation, business rules. Component sadece "ne render" olmalı. Logic custom hook'lara veya services'e.

## Trade-offs

| Yaklaşım | Basitlik | Reusability | Change Cost | Test Kolaylığı |
|----------|----------|-------------|-------------|----------------|
| 1 big component | Çok yüksek | Yok | Çok yüksek | Çok zor |
| A few medium components | Yüksek | Orta | Orta | İyi |
| Many small components | Orta | Yüksek | Düşük | Çok iyi |
| Micro-components everywhere | Düşük | Teorik yüksek | Yüksek (indirection) | Orta |

**Sweet spot:** "Birkaç orta" genelde doğru başlangıç. Gereksinim arttıkça "çok küçük"e kaydır, başta oraya gitme.

## Stack-Specific: React + Next.js

- **Server Components:** Data fetching burada, props olarak client'a geçer
- **Client Components (`"use client"`):** Interactive parts — minimize scope
- **Client/Server boundary:** Mantıklı kırılma noktası — leaf client components
- **Composition:** `<Layout>{children}</Layout>` pattern RSC ile çok güçlü
- **`React.memo` component boundary seviyesinde yarar sağlar, içerde useMemo ile her şeyi sarmak yarar getirmez

## Gotchas

- **Over-abstraction:** "Generic" component yaparken edge case'lere direnemez, sonunda if/else dolu
- **Extraction fatigue:** Her küçük JSX parçası component oluyor → tree çok derin, debug zor
- **Props explosion creep:** Başta 3 prop, zamanla 15 — boundary re-evaluation gerekli
- **Hook-as-component misuse:** Business logic'i custom hook yerine component'e koyma
- **Circular deps:** A component'i B'ye import eder, B A'ya → refactor gerekli

## Connections

- Related: [[State Locality]], [[Data Flow]], [[Changeability Maintainability]]
- Leads to: [[Domain Boundaries]], [[Testability-Driven Design]]
- Used by: [[Adding a New Feature]] (component design step)
- Contrast with: Template engines (Pug, Handlebars) where boundaries are file-based

## Real Examples (From My Projects)

- **menzernaturkiye:** `<ProductCard>` başta tek component'ti (image, info, actions, quick view modal — hepsi). 200 satır ve testi zor. `<ProductCardImage>`, `<ProductCardInfo>`, `<ProductQuickView>` ayrılınca her biri tek iş yapıyor oldu, test kolay.
- **MarketPulse:** Dashboard'da filters, chart, table, stats — hepsi `<Dashboard>` içindeydi. 600 satır. Feature folder'a taşındı, her biri ayrı component.
- **prompt_generator:** Editor'u başta mikro-component'lere ayırdım (20+ component). Over-engineered. Orta büyüklüğe geri çekildi, 8 component kaldı. "Her şey component" ezberinden kurtulma dersi.

## My Notes
- Buraya kendi gözlemlerini ekle
