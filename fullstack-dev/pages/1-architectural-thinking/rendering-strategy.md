---
title: "Rendering Strategy"
domain: fullstack-dev
category: 1-architectural-thinking
type: trade-off
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - architecture
  - rendering
  - performance
  - seo
  - decision-making
---

# Rendering Strategy

> One-line summary: CSR, SSR, SSG, ISR, RSC — 5 farklı rendering stratejisi, 5 farklı trade-off profili. Her sayfa için doğru stratejiyi seçmek SEO, performance, freshness ve complexity arasında denge kurmaktır.

## Why It Matters (Senior Perspective)

Rendering strategy, bir sayfanın tüm karakterini belirler: ne kadar hızlı yüklenir, SEO'da nasıl görünür, kullanıcı etkileşimi ne kadar hızlı hissedilir, server cost'u ne kadar olur. Yanlış seçim geri dönmesi en zor kararlardan biridir — bazen tüm data fetching yeniden yazılır.

Senior refleksi: "bu sayfa hangi soruları çözüyor?" → SEO? Freshness? Interactivity? Cost? — cevaba göre strateji seçimi.

> "Next.js kullanıyorum, App Router var, hepsi RSC" — bu bir karar değildir, bir kaçıştır. Her sayfa için açık düşün.

## The Question
Hangi sayfa için hangi rendering stratejisi? Bu karar:
- SEO gerekli mi?
- Content ne kadar dinamik?
- Interactivity ne kadar kritik?
- Cost bütçesi nedir?

## Core Concept — 5 Strateji

### CSR (Client-Side Rendering)
Browser boş HTML alır, JavaScript indirir, React render eder, sonra data fetch eder. Traditional SPA yaklaşımı.

### SSR (Server-Side Rendering)
Server her request için HTML üretir. Data fetch server'da olur, rendered HTML gelir. Client'ta sonra "hydrate" olur (interaktif hale gelir).

### SSG (Static Site Generation)
Build time'da HTML üretilir. Her request aynı HTML'i alır, CDN'den servis edilir. Super hızlı, ama stale.

### ISR (Incremental Static Regeneration)
SSG + background refresh. Build time'da üretilir ama belirli aralıklarla (veya trigger ile) yeniden üretilir. Next.js'e özgü kavram.

### RSC (React Server Components)
Next.js App Router'ın default modu. Components server'da render edilir, HTML + serialized data client'a gider. Client hydration cost'u düşer, bundle size küçülür.

## Decision Matrix

| Strateji | SEO | First Byte | Interactivity | Freshness | Cost | Complexity |
|----------|-----|-----------|---------------|-----------|------|-----------|
| CSR | Zayıf | Çok hızlı (boş HTML) | Yavaş (JS bekle) | Her zaman fresh | Düşük | Düşük |
| SSR | İyi | Orta (server time) | Orta (hydrate cost) | Fresh | Yüksek (server) | Orta |
| SSG | Mükemmel | Çok hızlı (CDN) | Yavaş (hydrate) | Stale (build'de) | Çok düşük | Düşük |
| ISR | Mükemmel | Çok hızlı (CDN) | Yavaş (hydrate) | Eventual fresh | Düşük | Orta |
| RSC | Mükemmel | Hızlı | Hızlı (az JS) | Fresh | Orta | Yüksek |

## When to Choose What

### CSR için ideal
- Dashboard, admin panel, internal tool
- SEO gereksiz (auth required, private content)
- Heavy interactivity (canvas, real-time, drag-drop)
- Data her kullanıcı için farklı, cache imkansız

### SSR için ideal
- Personalized content (logged-in user data)
- SEO gerekli + fresh data şart
- Kritik initial render ama CDN cache yeterli değil
- Örnek: E-commerce product detail (price, stock changes)

### SSG için ideal
- Marketing pages, landing, blog
- Content nadiren değişir
- Max speed + zero runtime cost
- Örnek: docs, portfolio, news (at publish time)

### ISR için ideal
- SSG istiyorsun ama biraz freshness da gerekli
- Büyük e-commerce (ürün sayfaları, periyodik güncelleme)
- Content update tahmin edilebilir aralıkta
- Örnek: Hepsiburada product page — her 60 saniyede revalidate

### RSC için ideal
- Modern full-stack Next.js app
- Large dataset, client'a göndermek istemiyorsun
- SEO + fresh data + düşük JS bundle
- Örnek: Modern dashboard, content management

## Reversibility

| Geçiş | Zorluk | Not |
|-------|--------|-----|
| SSG ↔ ISR | Kolay | Sadece `revalidate` ekle/çıkar |
| SSG → SSR | Orta | `getStaticProps` → `getServerSideProps` |
| CSR → SSR | Zor | Data fetching, auth, hydration yeniden |
| SSR → RSC | Zor | Component mimari değişir, client/server boundary |
| RSC → CSR | Zor | `"use client"` ekle, data fetch strategy değişir |

**Genel prensip:** Düşük-effort'tan yüksek-effort'a doğru seç. Reversible kararlar al.

## Patterns (Do This)

### 1. Mix Per Route
Tüm app tek strateji değil. Landing SSG, dashboard RSC, admin CSR — her sayfa kendi cevabı.

### 2. Start with RSC in Next.js App Router
Bilmediğin bir durum için default RSC. Sadece gerekli yerlerde `"use client"` ekle.

### 3. ISR as Smart Default for Public Pages
Static-ish content için ISR genellikle SSG + SSR'ın en iyi kombinasyonu.

### 4. Avoid Premature CSR Escape
"Bu karmaşık, CSR yapayım" demeden önce server component ile yapılıp yapılamayacağını düşün.

### 5. Progressive Enhancement
Server'dan meaningful HTML → JS yüklenmeden de iş görsün → sonra interactive olsun.

## Anti-Patterns (Don't Do This)

### One-Size-Fits-All
Tüm app için tek strateji seçmek. Her sayfa ayrı değerlendirme hak eder.

### Over-Engineering with RSC
Basit CSR app için RSC'ye zorla geçmek. Gereksiz complexity.

### SEO for Auth-Protected Pages
Dashboard SEO'luyor — boşa efor. Auth required sayfalar index edilemez zaten.

### Stale Data in Dynamic Contexts
Fiyat ve stock sürekli değişirken SSG — kullanıcı yanlış fiyat görür.

### Hydration Cost Blindness
"SSR kullanıyorum çünkü hızlı" — hydration büyük JS bundle ile toplam "interactive olma" zamanı CSR'dan yavaş olabilir

## Stack-Specific: Next.js App Router

```tsx
// RSC (default)
async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}

// SSG behavior
export const dynamic = 'force-static';

// ISR
export const revalidate = 60; // 60 saniyede bir yeniden üret

// SSR
export const dynamic = 'force-dynamic';

// Client component (CSR-like for that part)
'use client';
function InteractiveWidget() { ... }
```

## Gotchas

- **Hydration mismatch:** Server'da rendered HTML ≠ client'ta rendered HTML → warning + re-render
- **ISR stale window:** Revalidate trigger ile gerçek update arası bir istek eski veriyi alır
- **SSG at build time:** Dynamic routes için `generateStaticParams` eksik → build hatası
- **RSC cookie/headers:** Server component'te cookies okunur ama dinamik hale gelir (cache'lenmez)
- **Server actions timeout:** Long-running mutation'lar serverless limitini aşar
- **Client bundle bloat:** `"use client"` koyulunca o subtree client bundle'a eklenir

## Connections

- Related: [[State Locality]], [[Data Flow]], [[Core Web Vitals]]
- Leads to: [[Hydration Cost]], [[Cache Hierarchy]]
- Used by: [[Adding a New Feature]] (rendering decision step)
- Contrast with: Static HTML generation from other tools (Astro, Hugo)

## Real Examples (From My Projects)

- **menzernaturkiye:** Product listing başta CSR'dı (React Query ile fetch). SEO yoktu, Google index edemiyordu. SSR'a çekildi → SEO düzeldi ama server cost arttı. En sonunda ISR (her 5 dk) → ideal denge.
- **MarketPulse:** Dashboard başta SSR denedi, ama data her kullanıcı için çok farklı ve heavy interactivity vardı. CSR'a geri döndü — doğru karar.
- **prompt_generator:** Landing page SSG, app RSC, editor client component. Her sayfa için ayrı karar verildi.

## My Notes
- Buraya kendi gözlemlerini ekle
