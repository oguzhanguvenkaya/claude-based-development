---
title: "Data Flow"
domain: fullstack-dev
category: 1-architectural-thinking
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - architecture
  - data-flow
  - state-management
  - decision-making
---

# Data Flow

> One-line summary: Veri sistemde nasıl hareket eder — yukarıdan aşağıya, aşağıdan yukarıya, yatay geçişler. Doğru data flow pattern'i öngörülebilir ve debug edilebilir sistemin temelidir.

## Why It Matters (Senior Perspective)

"Data flow" konusunda yanlış karar, bug'ların en çok saklandığı yerdir. State doğru yerde olsa bile, **nasıl akıyor** yanlışsa race condition, stale data, impossible state bug'ları doğar.

Senior refleksi: "bu veri oraya nasıl gidiyor?" sorusunun cevabını **kod okumadan** söyleyebilmek. Eğer söyleyemiyorsan, data flow net değil demektir — ve bu bir bug mıknatısıdır.

> React'in "tek yönlü data flow" felsefesi de boşuna değildir. Multi-directional flow debug imkansızlığına götürür.

## Core Concept

Data flow 4 temel pattern'e ayrılır:

1. **Top-down (props):** Parent → Child, synchronous, predictable
2. **Bottom-up (callbacks/events):** Child → Parent, event-driven
3. **Horizontal (sibling):** Common ancestor üzerinden, lift state
4. **Out-of-band (context/store/URL):** Ağaç yerine direkt erişim

Her pattern'in kendi use case'i vardır. Karışıklık, bunları ayırt etmeden hepsini aynı anda kullanmaktan doğar.

## The Decision Framework

Bir data'nın akışı için sor:

1. **Source:** Bu data nereden geliyor? (Server, user input, derived?)
2. **Destination:** Nereye gidecek? (Bir component, birkaç, hepsi?)
3. **Direction:** Yukarıdan aşağı mı, aşağıdan yukarı mı, yatay mı?
4. **Timing:** Sync mi, async mi? Event-driven mi?
5. **Frequency:** Bir kez mi, continuous mu, periyodik mi?
6. **Reversibility:** Değişiklik geri alınabilir mi? (Optimistic update?)

## Patterns (Do This)

### 1. Props Down, Events Up
Parent data verir, child event bildirir. Child parent'ı direkt değiştirmez, event fırlatır ve parent karar verir. Bu React'in default pattern'i ve iyi bir başlangıç.

### 2. Lift State to Common Ancestor
İki sibling aynı data'yı paylaşıyorsa, en yakın ortak parent'a lift et. God store'a koyma.

### 3. Unidirectional Flow
Mutation → store → view döngüsü. View, store'u direkt değiştirmez, action/mutation gönderir. Flux, Redux, Zustand hepsi bu paradigmada.

### 4. Server State via Query Library
Server data için React Query veya SWR kullan. Bu cache'i, refetch'i, invalidation'ı ele alır. Sen sadece "ne zaman stale" tanımlarsın.

### 5. Mutations Through Actions
Mutation'ları bir "action"a kapsülle: `updateUser(id, changes)`. Bu action server'a yazar + local cache'i günceller. İki yerde değil, tek action.

### 6. Derived Data via Computation
Derived data ayrı state değildir. Selector, computed property, useMemo — her neyse hesapla, saklama.

### 7. Event-Driven Cross-Tree Communication
Component tree'de uzak iki node iletişmeli ise: event emitter veya URL state kullan, prop drilling yapma.

## Anti-Patterns (Don't Do This)

### Prop Drilling
5+ katman props geçirme. Lift state veya context kullan. Prop drilling "kodun hasta olduğunun" belirtisi.

### Two-Way Binding Mess
Child parent'ı doğrudan değiştirir, parent child'ı doğrudan günceller. Angular'ın eski sorunu. Circular dependency ve debug cehennemi.

### Spagetti Event Chains
"A trigger B, B trigger C, C trigger A" — sonsuz döngü veya impossible state. Her event'in nereye gideceği belirsizse mimari bozuk.

### Silent Mutation
`items.push(newItem)` — immutable pattern'i bozar. React re-render etmeyebilir, time-travel debugging çalışmaz. Her zaman `setItems([...items, newItem])`.

### Manual Cache Sync
Server data'yı `useState` + `useEffect` ile manuel cache yapmak. React Query gibi araçlar bunu çözer.

### Direct DOM Manipulation
`document.getElementById('foo').innerHTML = ...` React context'inde. React state, DOM = state projection. State değiştir, DOM kendini update etsin.

## Trade-offs

| Pattern | Komplekslik | Debug Kolaylığı | Scalability |
|---------|------------|-----------------|-------------|
| Props down | Düşük | Çok iyi | Orta (deep trees sorunlu) |
| Callbacks up | Düşük | İyi | Orta |
| Context | Orta | Orta | İyi |
| Global store | Orta | Orta | Çok iyi |
| React Query | Orta | İyi | Çok iyi (server data için) |
| Event bus | Yüksek | Düşük (implicit) | Yüksek |

## Stack-Specific: Next.js App Router + React 19

- **Server Components:** Data server'da fetch edilir, props olarak client'a geçer
- **Server Actions:** Form submissions, mutations — `use server` ile tanımlı, client'tan çağrılır
- **Suspense boundaries:** Async data akışını UI'ya bağlar
- **`use()` hook:** Promise'leri direkt component'te consume etme
- **Parallel data fetching:** Promise.all veya Suspense + server component ile

## Gotchas

- **Stale closure in useEffect:** Dependency array güncel tutulmazsa eski state görünür
- **Render thrashing:** State update render tetikler, render state update tetikler → infinite loop
- **Async race conditions:** Aynı data için iki fetch, ikincisi birinci'den önce gelir, yanlış sonuç
- **Optimistic update rollback:** UI güncellenir ama server reddeder → "rollback" nasıl?
- **Cross-component sync:** İki component aynı data'yı farklı yerden alıyor → divergence
- **SSR + client hydration:** Initial data server'dan, sonra client fetch'leyince diverge edebilir

## Connections

- Related: [[State Locality]], [[Component Boundaries]], [[Fetching Patterns]]
- Leads to: [[Optimistic Updates]], [[Consistency Rollback]]
- Used by: [[Form UX]], [[Adding a New Feature]]
- Contrast with: Mutable global state

## Real Examples (From My Projects)

- **MarketPulse:** Initial olarak prop drilling ile 5 katman geçiyordu (price list → filters → card → cell → action). 3. ayda context API'ye geçiş, sonra React Query'ye. Her refactor gereksizdi, baştan doğru karar ile yapılabilirdi.
- **menzernaturkiye:** Cart state için iki kaynak vardı — localStorage + server. Sync bug'ları sürekli çıkıyordu. Single source of truth (server) + React Query ile çözüldü.
- **prompt_generator:** Form state'i Zustand'daydı, her keystroke'ta global re-render. `react-hook-form`'a taşınınca 10x performance.

## My Notes
- Buraya kendi gözlemlerini ekle
