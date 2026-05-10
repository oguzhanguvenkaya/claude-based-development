---
title: "Loading Empty Error States"
domain: fullstack-dev
category: 3-frontend-systems-ux
type: concept
level: pattern
created: 2026-04-13
updated: 2026-04-13
sources: []
tags:
  - frontend
  - ux
  - states
  - reliability
---

# Loading, Empty & Error States — The 4 Modes

> One-line summary: Her data-driven ekranın 4 hali vardır — loading, empty, error, success. Junior'lar sadece success yazar, senior'lar 4'ünü de tasarlar.

## Why It Matters (Senior Perspective)

Bir ekran 4 mod'da olabilir:
1. **Loading** — Veri geliyor, bekliyoruz
2. **Empty** — Veri geldi ama boş
3. **Error** — Veri gelemedi
4. **Success** — Veri geldi, gösteriliyor

AI genelde sadece 4. modu (`.map(...)`) yazar. Diğer 3 mod UX'i kıran, frustrasyon yaratan yerdir. Senior refleksi: **her data-driven component'te 4 modu da ele almak** — bu bir best practice değil, minimum şart.

> "Yeni kayıt olan kullanıcının ilk izlenimini düşün" — yeni kullanıcı her ekranda empty state görecek. Empty state yoksa app "bozuk" görünür.

## Core Concept — The 4 Modes

Her async data fetch'i bir state machine olarak düşün:

```
idle → loading → [empty | error | success]
```

Her state'in kendi UI'ı, kendi copy'si, kendi interaction pattern'i olmalıdır. "Default" hali "success" değildir — state'siz gösterim bir bug'dır.

## The Decision Framework

Her data-driven screen için sor:

1. **Loading** — Kullanıcı ne kadar bekleyecek? Skeleton mı, spinner mı, optimistic mi?
2. **Empty** — Neden boş? İlk kez mi (new user), filter sonucu mu, data mı silindi?
3. **Error** — Hangi hata? Network? Auth? Server? Kullanıcı ne yapabilir? Retry var mı?
4. **Success** — Kaç item var? Pagination nerede? Sort nerede?

Her soru UI tasarımı etkiler. Atlanırsa, gap'ler runtime'da görünür.

## Loading State

### Variants
- **Skeleton**: Gerçek UI'ın şeklinde placeholder — perceived performance çok iyi
- **Spinner**: Generic loading — hızlı UI'lar için OK
- **Progress bar**: Uzun operation'lar için (upload, download)
- **Optimistic**: Veri gelmeden UI'ı güncelle, gerçek cevapla doğrula
- **Inline**: Button'da spinner, sadece o parça loading

### When
- Fetch > 200ms süreceğini düşünüyorsan → mutlaka loading
- Fetch > 1s → skeleton tercih edilir (spinner yavaş hissettirir)
- Fetch < 200ms → loading göstermeyebilirsin (flicker olur)

## Empty State

### Three Types
1. **First-use empty** — Yeni kullanıcı, hiç data yok
2. **Filtered empty** — Data var ama filter/search match etmiyor
3. **Cleared empty** — Kullanıcı sildi, şimdi boş

Her biri farklı copy ister:
- First-use: "Başlamak için ilk projeyi oluştur" + CTA button
- Filtered: "Aramayla eşleşen sonuç yok" + "filtreyi temizle" button
- Cleared: "Henüz bir şey yok" (genelde minimal)

### Anti-Pattern
Empty state'i unutmak = boş ekran → kullanıcı "bozuk" zannetmesi.

### Pattern
Her liste için empty state zorunlu. "Never show empty list with no explanation."

## Error State

### Information Needed
- **Ne oldu** (nicely worded, not "Error: 500")
- **Neden olmuş olabilir** (network, server, auth)
- **Kullanıcı ne yapabilir** (retry, refresh, contact support)
- **Recovery action** (button to try again)

### Error Taxonomy
- **Transient**: Network, timeout → "retry" düğmesi
- **Permanent**: 404, deleted → "go back" veya "home"
- **Auth**: 401 → redirect to login
- **Permission**: 403 → "contact admin" mesajı
- **Validation**: 400 → form field error'ları, global değil
- **Server**: 500 → "bir şey bozuldu, sonra tekrar dene"

### Show Details (Optional)
Dev mode'da stack trace, prod'da kullanıcıya friendly mesaj. Error tracking service (Sentry) detayları kaydeder.

## Success State

### Not Just "Map"
Success state de kendi complexity'sini taşır:
- **Pagination** — kaç sayfa?
- **Sort** — hangi sıra?
- **Filter** — hangi filtreler aktif?
- **Selection** — bulk actions var mı?
- **Item states** — selected, highlighted, disabled?

### Infinite Scroll vs Pagination
Büyük liste — infinite scroll mu, pagination mu, "load more" button mu? Kullanım paterni'ne göre seç.

## Patterns (Do This)

### 1. State-First Component Design
Component yazarken önce 4 mod'un JSX'lerini yaz, sonra logic'i bağla.

```tsx
function UserList() {
  const { data, isLoading, error } = useUsers();
  
  if (isLoading) return <UserListSkeleton />;
  if (error) return <ErrorState error={error} retry={() => refetch()} />;
  if (!data || data.length === 0) return <EmptyState />;
  return <UserListContent users={data} />;
}
```

### 2. Generic State Components
`<EmptyState>`, `<ErrorState>`, `<LoadingSkeleton>` generic component'leri — her ekranda tekrar kullan.

### 3. React Query / SWR Provides This
`isLoading`, `isError`, `data` — library bu state'leri zaten veriyor. Kullan.

### 4. Skeleton Matching Real UI
Skeleton, gerçek UI'ın şekli ve boyutlarıyla eşleşmeli. Layout shift yok (CLS düşer).

### 5. Error Boundaries
Bir component çöktüğünde tüm sayfa çökmesin. `<ErrorBoundary>` ile contain et.

### 6. Retry in Error State
Her error UI'sinde "retry" olsun (transient error'larda). Kullanıcı manuel F5 atmak zorunda kalmasın.

### 7. Optimistic UI for Fast Actions
Delete button'a bastı → UI'dan anında sil, background'da server'a yaz, fail olursa geri koy.

## Anti-Patterns (Don't Do This)

### Direct Map Without Guards
```tsx
// ❌
function List() {
  const data = useFetch();
  return data.items.map(item => <Item {...item} />);
}
// isLoading → null? length → 0? error → crash?
```

### Spinner for Everything
Skeleton daha iyi UX verir. Generic spinner hızlı iş yapıyor izlenimi vermez.

### Silent Error Swallow
`.catch(() => [])` → error var ama kullanıcı görmez, empty state gibi görünür.

### Nested Loading States
Parent loading + child loading + grandchild loading. 3 spinner aynı anda → berbat UX.

### Missing Loading Indication on Fast Actions
Submit button'a bastı, 500ms hiçbir şey olmadı → kullanıcı tekrar bastı → duplicate submit.

### Empty State = Blank
Hiçbir şey göstermemek. Kullanıcı "bozuk" zannetmesi.

### Error Messages Like "Error: 500"
Teknik mesaj kullanıcıya gösterilmez. "Bir şey bozuldu, tekrar deneyin."

## Trade-offs

| Strategy | Effort | UX | Perceived Speed |
|----------|--------|-----|-----------------|
| No states (just map) | Çok düşük | Çok kötü | Çok kötü |
| Generic spinner | Düşük | Orta | Orta |
| Skeleton UI | Orta | İyi | İyi |
| Optimistic + skeleton | Yüksek | Çok iyi | Çok iyi |

## Gotchas

- **Flicker**: 50ms loading → hemen success → UI titrer. Minimum 200ms loading show'u
- **Skeleton mismatch**: Skeleton ≠ real UI boyutu → layout shift → CLS score düşer
- **Empty vs Loading confusion**: `data === []` loading mi bitti mi? State machine doğru olmalı
- **Error state loop**: Error → retry → error → retry → retry loop UI'sı
- **Wrong error types**: 404'te "retry" button → anlamsız
- **Double fetch**: First render + StrictMode double render → 2 fetch → 2 loading

## Connections

- Related: [[Edge Case Thinking]], [[Form UX]], [[Perceived Performance]]
- Leads to: [[Accessibility]], [[Failure Modes]]
- Used by: [[Adding a New Feature]] (pre-ship checklist)
- Contrast with: Pure success-path rendering

## Real Examples (From My Projects)

- **MarketPulse:** Dashboard'ta initial load'ta 4-5 saniyelik boş ekran vardı. Kullanıcılar "bozuk" diye bildirdi. Skeleton UI eklendi, aynı 4 saniye ama şimdi "yükleniyor" hissi güçlü.
- **menzernaturkiye:** Product filter'ı aktif olunca, sonuç boşsa empty state yoktu → boş grid. "Filtrenize uygun sonuç yok, filtreleri temizle" mesajı + button eklendi.
- **prompt_generator:** Prompt list error durumunda sayfa tamamen çöküyordu (error boundary yoktu). Error boundary + "retry" button eklendi, component-level error handling.

## My Notes
- Buraya kendi gözlemlerini ekle
