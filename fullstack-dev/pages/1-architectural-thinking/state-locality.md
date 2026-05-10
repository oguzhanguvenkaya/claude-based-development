---
title: "State Locality"
domain: fullstack-dev
category: 1-architectural-thinking
type: concept
level: foundation
created: 2026-04-12
updated: 2026-04-12
sources: []
tags:
  - architecture
  - state-management
  - data-flow
  - decision-making
---

# State Locality

> One-line summary: State nerede yaşamalı sorusuna sistematik bir yaklaşım — client, server, URL veya cache hangi state'i tutmalı ve neden?

## Why It Matters (Senior Perspective)

State management'ta en yaygın junior hata "her şeyi global store'da tutmak"tır. Bu basit görünür ama re-render cehennemi, stale data, refresh'te kayıplar, debugging zorluğu gibi problemleri beraber getirir.

Senior refleksi: **her state parçası için "bu kim tarafından biliniyor olmalı?"** diye sorar. State'in yanlış yerde yaşaması, sistemin ilerleyen aşamalarında en çok refactor gerektiren karar tiplerinden biridir — ve çoğu zaman baştan doğru konumlandırılırsa problem hiç doğmaz.

> State locality, component'leri yeniden yazmadan önce verilmesi gereken karardır. AI genelde "en basit" yere koyar (useState), ama "en basit" ≠ "en doğru".

## Core Concept

State 4 temel yere yaşayabilir, her birinin farklı bir karakteri vardır:

1. **Local state** (Component içi) — Ephemeral, tek component'in işi
2. **URL state** (Query params, route) — Shareable, bookmarkable, refresh-safe
3. **Server state** (DB veya uzak servis) — Source of truth, persistent
4. **Shared client state** (Context, global store) — Multiple component'in gördüğü, app-wide

Doğru state locality = her data parçasını **kimin okuyacağına** göre en dar scope'ta tutmak.

## The Decision Framework

Bir state parçası için soru zinciri:

1. **Kim okuyor?** Sadece 1 component → local. Birkaç yakın component → lift up. Yaygın → shared veya server.
2. **Source of truth nerede?** Server'daysa → client sadece **cache** tutar, duplicate etmez.
3. **Persist olmalı mı?** Refresh'te kaybolmasın istiyorsan → URL, localStorage, veya server
4. **Shareable URL gerekli mi?** Link paylaşılabilir olmalı mı → URL state
5. **Değişim sıklığı?** Her keystroke'ta değişiyor → mümkünse local (re-render scope dar). Nadiren → context OK.
6. **Derive edilebilir mi?** Başka state'ten hesaplanabiliyorsa **saklama**, hesapla.

## Patterns (Do This)

### 1. Local First, Lift When Proven Necessary
`useState` ile başla. İkinci component'in ihtiyacı olduğunda **en yakın ortak ancestor'a** lift et. Global değil, necessary.

### 2. URL for Shareable State
Filter, sort, pagination, active tab, modal open — bunlar URL state olmalı. Kullanıcı refresh atınca kaybolmasın, link paylaşabilsin, back button çalışsın.

### 3. Server State with React Query (or Next.js fetch cache)
Server'dan gelen veri bir **cache** olmalı, bir copy değil. React Query, SWR veya RSC fetch cache kullan. `useState` ile server data tutma.

### 4. Context for Rarely-Changing App-Wide Config
Theme, locale, auth user, feature flags — bunlar context için uygun. Her keystroke'ta değişen şeyler context'e **konmaz**.

### 5. Derived State via useMemo or Selectors
`filteredItems = items.filter(...)` gibi şeyler ayrı state değildir, derived computation. `useMemo` veya selector ile hesapla.

### 6. Form State Separately
Form state'i global store'da tutmak klasik anti-pattern. `react-hook-form`, `formik`, veya sadece local `useState` kullan.

## Anti-Patterns (Don't Do This)

### Global Everything
Her şeyi Redux/Zustand'a koymak — re-render cehennemi, test zor, debug zor, navigation sonrası stale.

### Server Data Duplication
`useEffect` ile fetch → `useState`'e koy → sonra manuel "refresh" button. Bu React Query gibi araçların çözdüğü bir problem. Cache ≠ duplicate state.

### State for Derivable Values
```ts
// ❌ Anti-pattern
const [items, setItems] = useState([]);
const [filteredItems, setFilteredItems] = useState([]); // Derived!

// ✓ Pattern
const [items, setItems] = useState([]);
const filteredItems = useMemo(() => items.filter(...), [items]);
```

### Modal State in Store
`isModalOpen` global store'da — bu sadece component ihtiyacı, lift etme gereksiz.

### URL State as Local State
Active tab'ı `useState` ile tutup refresh'te kaybetmek. URL state olmalıydı.

### Context for Hot State
Context'teki her değişiklik tüm consumer'ları re-render eder. Hızlı değişen şeyler (keystroke, mouse pos) context'e uygun değildir.

## Trade-offs

| Yaklaşım | Basitlik | Performance | Persistence | Shareability |
|----------|----------|-------------|-------------|--------------|
| `useState` | Çok yüksek | Çok iyi (dar scope) | Yok | Yok |
| `useState` + prop drill | Yüksek | İyi | Yok | Yok |
| React Context | Orta | Orta (re-render chain) | Yok | Yok |
| Global store (Redux/Zustand) | Düşük | İyi (selector) | Opsiyonel | Yok |
| URL state | Orta | İyi | Var | Var |
| Server state (React Query) | Orta | Çok iyi (cache) | Var | Yok |
| localStorage | Orta | İyi | Var | Yok |

**Genel kural:** En dar scope'tan başla, kanıtlandığı yere kadar genişlet. "İhtiyaç olursa global yaparız" > "Global koyalım, sonra baka".

## Stack-Specific: Next.js App Router

- **Server components:** State yok — bunlar data fetching için
- **Client components:** Normal React state, useReducer, store libraries
- **searchParams:** URL state için ideal — server component'ler doğrudan okuyabilir
- **cookies:** Persistent session state
- **Server actions + revalidate:** Mutation sonrası cache güncelleme

## Gotchas

- **Context re-render cascade:** Context değeri değiştiğinde her consumer re-render olur. Hot state context'te tutma
- **Stale closures:** `useEffect` içinde state'in eski versiyonunu yakalamak — dependency array doğru mu?
- **URL state type loss:** Query params her zaman string'dir, number/boolean convert unutma
- **LocalStorage sync issue:** İki tab açıksa biri değiştirince diğeri görmeyebilir — `storage` event kullan
- **SSR hydration mismatch:** Server'da rendered HTML ≠ client'ta rendered HTML → hydration error. localStorage SSR'da yok
- **Derived state out of sync:** Manual sync yaparsan kaçınılmaz stale. Derive et, tutma

## Connections

- Related: [[Data Flow]], [[Component Boundaries]], [[Rendering Strategy]]
- Leads to: [[Fetching Patterns]], [[Optimistic Updates]]
- Contrast with: God store pattern
- Used by: [[Adding a New Feature]], [[Form UX]]

## Real Examples (From My Projects)

- **MarketPulse:** Dashboard filters'ı başlangıçta `useState` ile yazıldı. Kullanıcı filter uygulayıp link paylaştığında karşı taraf boş filter görüyordu. → URL state'e taşındı, problem çözüldü
- **menzernaturkiye:** Product search query başlangıçta global store'daydı, her keystroke'ta tüm sidebar re-render oluyordu. → Local state'e indirildi, performance düzeldi
- **prompt_generator:** Current prompt editor content localStorage'da vardı ama server'a save'den sonra sync bozuluyordu. → Server state (React Query) ile localStorage arasındaki overlap silindi, sadece source of truth olarak server

## My Notes
- Buraya kendi gözlemlerini ekle
