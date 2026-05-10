---
title: "Domain Boundaries"
domain: fullstack-dev
category: 1-architectural-thinking
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - architecture
  - domain-driven-design
  - modularity
  - decision-making
---

# Domain Boundaries

> One-line summary: "Bu iş kuralı nereye ait?" sorusunun sistematik cevabı. Feature'lar arası sınırları doğru çizmek uzun vadeli maintainability'nin temelidir.

## Why It Matters (Senior Perspective)

Component boundaries bir sayfadaki parçaları, **domain boundaries** ise tüm sistemdeki feature'ları ayırır. Yanlış domain boundary = feature'lar birbirine karışır, bir yerde yapılan değişiklik beklenmedik yerleri etkiler, test'ler coupled olur.

Senior refleksi: her iş kuralı için "bu **kimin sorumluluğu?**" diye sorma. Payment, notification, user management — her biri kendi dünyası olmalı, komşuları hakkında minimal bilgiyle yaşamalı.

> Domain-Driven Design (DDD) karmaşık konseptlerle dolu ama tek bir prensibi senin için yeterli: **aynı dile konuşanlar birlikte yaşasın, farklı dile konuşanlar explicit interface ile konuşsun.**

## Core Concept

Bir "domain" bir iş alanıdır — kullanıcı yönetimi, ödeme, katalog, sepet, bildirim, analytics. Her domain'in:

1. **Kendi verisi** (schema, tablolar)
2. **Kendi kuralları** (business logic)
3. **Kendi dili** (terminology — "user" e-commerce'te "customer", CRM'de "account")
4. **Kendi arayüzü** (diğer domain'lere açılan contract)

Domain boundary doğru çizilirse, bir domain'de yapılan değişiklik diğerlerini etkilemez. Yanlış çizilirse, her değişiklik ripple effect yaratır.

## The Decision Framework

Yeni bir iş kuralı geldiğinde sor:

1. **Ubiquitous language:** Bu kuralın konuştuğu dil hangi domain'inkiyle aynı? Oraya ait.
2. **Data ownership:** Bu kural hangi data'yı okuyup yazıyor? Data'nın sahibi domain'e ait.
3. **Change frequency:** Bu kural diğer hangi kurallarla birlikte değişir? Beraber değişenler aynı domain'de.
4. **Cross-domain dependency:** Bu kural başka bir domain'i değiştiriyor mu? → Event veya explicit API ile konuşsun, direkt DB değil.
5. **Team boundary:** Farklı takımlar / farklı insanlar farklı domain'lere bakıyorsa, boundary doğrudur.

## Patterns (Do This)

### 1. Feature-Based Folder Structure
```
src/
├── features/
│   ├── auth/
│   ├── catalog/
│   ├── cart/
│   ├── checkout/
│   ├── payment/
│   └── notifications/
└── shared/
    ├── ui/
    ├── utils/
    └── types/
```

Her feature kendi `components/`, `hooks/`, `api/`, `types/` içerir.

### 2. Explicit Public API per Feature
Her feature'ın `index.ts`'inde sadece dışa açık şeyler export edilir. Internal helper'lar dışa çıkmaz.

```ts
// features/auth/index.ts
export { useAuth } from './hooks/useAuth';
export { LoginForm } from './components/LoginForm';
// Internal utils, helpers NOT exported
```

### 3. Cross-Feature Communication via Events/Actions
Bir feature diğerini değiştirecek → direkt DB yazmak yerine event fırlatıp diğer feature'ın listen etmesini sağlasın. Loose coupling.

### 4. Shared Language Consistency
Tek domain içinde terminology tutarlı. "User" mi "customer" mı — karıştırma, seç ve uygula.

### 5. Anti-Corruption Layer
Dış sisteme (3rd party API, legacy service) adapter yaz. Dış sistemin şekli senin domain'ine sızmasın.

```ts
// features/payment/adapters/stripeAdapter.ts
export function toPaymentResult(stripeResponse: Stripe.PaymentIntent): PaymentResult {
  // Translate stripe shape → your domain shape
}
```

### 6. Bounded Context per Domain
Aynı kelime iki domain'de farklı anlama gelir — her domain kendi "User" type'ına sahip olabilir. Payment context'teki User ≠ Auth context'teki User.

## Anti-Patterns (Don't Do This)

### God Module
`/utils/`, `/helpers/`, `/shared/` içine her şey karışır. 1000 satırlık `utils.ts` — hiçbir domain'e ait değil, her şeye ait, test zor.

### Cross-Domain Direct DB Access
Payment feature'ı User tablosuna direkt yazıyor. User schema değişince payment kırılır.

### Shared Types Everywhere
`User` type'ı her feature'ın her yerinde import ediliyor. User'ın bir field'ı değişince 50 dosya etkilenir.

### Leaky Abstractions
Stripe Response şekli tüm app'in içinde geziyor. Stripe'dan vazgeçmek imkansız.

### Feature Folder with Tech Mixing
```
❌
/components/UserCard.tsx
/components/ProductCard.tsx
/hooks/useUser.ts
/hooks/useProduct.ts

✓
/features/user/components/UserCard.tsx
/features/user/hooks/useUser.ts
/features/product/components/ProductCard.tsx
/features/product/hooks/useProduct.ts
```

### Domain Service Megaclass
`UserService` 50 method'lu sınıf — auth, profile, settings, billing, notifications hepsi orada. Split et.

## Trade-offs

| Yaklaşım | Coupling | Flexibility | Onboarding | Consistency |
|----------|----------|-------------|------------|-------------|
| Single module (monolith file) | Tight | Düşük | Kolay | Çok yüksek |
| Tech-based folders | Orta | Orta | Orta | Orta |
| Feature-based folders | Loose | Yüksek | Orta | Yüksek (per domain) |
| Microservices | Çok loose | Çok yüksek | Zor | Düşük (koordinasyon) |

**Monolith → feature folders** çoğu app için sweet spot. Microservices'e sıçramak çoğu zaman gereksiz.

## When to Split, When to Merge

**Split signal (domain çok büyük):**
- Folder 20+ dosya
- Sub-responsibility'ler ayrılabiliyor
- Farklı takım bakıyor
- Release cadence farklı

**Merge signal (domain çok küçük):**
- 2-3 dosyalık "feature"
- Sadece 1 yerden çağrılıyor
- Standalone anlamı yok
- Coupling zaten yüksek

## Gotchas

- **Feature sprawl:** Her küçük şey "feature" → yüzlerce folder, hiçbiri substantial değil
- **Shared hell:** `/shared/` folder'ı çöp sepeti oluyor → per-domain discipline gerekli
- **Cross-cutting concerns:** Logging, auth, analytics gibi yatay endişeler feature'a zorla girmez — middleware veya hook katmanı
- **Domain drift:** Başta iyi boundary, zamanla bulanıklaşır. Periyodik refactor gerekli
- **Monorepo confusion:** Feature folder'lar paket mi, folder mı? Tek repo için folder yeterli; multi-repo için paket
- **Over-modularization:** Her şey bir "module" olmak zorunda değil. Pragmatik kal

## Connections

- Related: [[Component Boundaries]], [[Changeability Maintainability]], [[Schema Design Principles]]
- Leads to: [[Error Design]], [[API Contracts]]
- Used by: [[Requirement Clarification]] (hangi domain'e ait?)
- Contrast with: Flat structure, tech-layer folders

## Real Examples (From My Projects)

- **MarketPulse:** Başta `/utils/`, `/models/`, `/services/` klasik tech folder'lar. Feature eklemek her yerde değişiklik gerektiriyordu. Feature-based'e geçiş (6 ay sonra) büyük refactor oldu. Lesson: başta feature folders başla.
- **menzernaturkiye:** Catalog, cart, checkout, user, blog — her biri feature folder. Ancak user type'ı her yerde shared olarak kullanıldı, sonra "auth user" vs "customer" ayrımı gerektiği zaman sancılı oldu.
- **prompt_generator:** "Save prompt" logic'i 3 ayrı yerde vardı (editor, list, share). Domain'de tek yerde toplandı (`features/prompt/services/savePrompt.ts`), diğerleri buradan çağırıyor.

## My Notes
- Buraya kendi gözlemlerini ekle
