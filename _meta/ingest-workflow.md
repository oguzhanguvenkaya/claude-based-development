# Ingest Workflow — Transcripts → Wiki Pages

> **Amaç:** 108 transkripti (10 ders, ~35.200 kelime) `data-science/pages/{category}/` altında **kalıcı, çapraz-bağlı wiki sayfalarına** dönüştürmek. Karpathy LLM Wiki desenini uygulayarak her ingest'in mevcut wiki'yi zenginleştirmesini sağlamak.

---

## Çalışma Modeli

**Per-lesson ingest:** 1 oturumda 1 ders. 10 aktif ders var → 10 iterasyon.

Sıralama (basitten karmaşığa, biriken çapraz-bağ avantajıyla):

1. Sprint 2 / Ders 1 — SQL'in Temelleri *(17 video, en temel teknik içerik)*
2. Sprint 2 / Ders 2 — SQL'de Hesaplanmış Veriler *(11)*
3. Sprint 2 / Ders 3 — Tabloları Birleştirmek ve Test *(11)*
4. Sprint 2 / Ders 4 — Subquery ve With As *(6)*
5. Sprint 2 / Ders 5 — Fonksiyonlar ve Window *(5)*
6. Sprint 3 / Ders 1 — İleri Seviye SQL + Data Warehouse *(13)*
7. Sprint 1 / Ders 1 — Google Sheets ile Analizin Temelleri *(11)*
8. Sprint 1 / Ders 2 — KPI'ın Temelleri *(13)*
9. Sprint 1 / Ders 3 — İleri Seviye KPI'lar *(10)*
10. Sprint 1 / Ders 4 — Data Analiz Ekosistemi *(11)*

> **Niçin Sprint 2 öncelikli?** SQL içeriği teknik ve kavramlar net; pilot için iyi. KPI/business analytics dersleri daha "yumuşak" — onları SQL temeli oturduktan sonra cross-reference'larla zenginleştirebiliriz.

> İstersen klasik sıralama (Sprint 1 → 2 → 3) da yapabiliriz; karar başlangıçta verilir.

---

## İterasyon Akışı (8 Adım)

### 1. Discovery (read-only)
- Hedef dersin tüm `<lesson>/transcripts/*.md` dosyalarını oku
- README.md'yi oku (URL, proje listesi, ders başlığı için)
- Mevcut `data-science/index.md` ve `data-science/pages/*` listesini gözden geçir (örtüşme tespiti için)

### 2. Concept Extraction (draft)

Her transkriptin **ana konsept(ler)ini** çıkar. Kurallar:

| Durum | Aksiyon |
|-------|---------|
| Bir transkript → bir ana kavram (ör. "PIVOT TABLE nedir") | 1 sayfa adayı |
| Bir transkript → birden çok kavram (ör. "WHERE + diğer filtreler") | Konsept başına 1 sayfa adayı VEYA tek bir umbrella sayfa |
| Birden çok transkript → aynı kavram (ör. JOIN 6 video boyunca açıklanıyor) | **Tek bir sayfa**, kaynaklarda multi-source |
| Konu mevcut sayfayla örtüşüyor (ör. `descriptive-statistics`) | UPDATE, yeni sayfa açma |
| Konu çok küçük (≤200 kelime) ya da bağımsız değil (ör. "alias kullanımı") | Üst kavram sayfasına subsection olarak ekle |

**Çıktı:** Taslak sayfa listesi
```
1. select-statement          (sources: 05-select)
2. distinct-and-deduplication (sources: 06-distinct)
3. filtering-where           (sources: 07-where, 08-other-filters)
4. pattern-matching-sql      (sources: 09-pattern, 10-in-notin)
5. data-types-and-casting    (sources: 15-data-types, 16-casting)
...
```

### 3. Category Decision

CLAUDE.md'deki taksonomi: `statistics`, `machine-learning`, `math-foundations`, `sql-bigquery`, `python-data`, `projects`.

Genişletme kuralı: **Bir kategori en az 2 sayfa içerirse aç.** Aksi halde mevcut umbrella'ya bas.

| Ders | Önerilen Kategori | Yeni mi? |
|------|-------------------|----------|
| Sprint 2 / 1-5, Sprint 3 / 1 | `sql-bigquery/` | Var (boş) |
| Sprint 1 / 1 (Google Sheets) | `data-analysis/` | **Yeni** (≥4 sayfa beklenir) |
| Sprint 1 / 2, 3 (KPI) | `business-analytics/` | **Yeni** (≥3 sayfa beklenir) |
| Sprint 1 / 4 (Data ecosystem) | `data-roles/` veya `business-analytics/`'e dahil | Karar runtime'da |

CLAUDE.md'deki kategori listesini bu kararlardan sonra güncelleyeceğiz.

### 4. User Approval Gate

Taslak liste + kategori önerisi `AskUserQuestion` ile sunulur. Kullanıcı:
- Sayfa adlarını/slug'ları onaylar/değiştirir
- Sayfa sayısını azaltır/artırır
- Kategori kararını netleştirir
- Belirli bir sayfanın "skip" ya da "merge into X" olduğunu söyler

**Yazıma onay olmadan geçilmez.**

### 5. Page Authoring

Her onaylanan sayfa için aşağıdaki şablonu kullan (mevcut `descriptive-statistics.md`'den türetildi — `_templates/wiki-page.md` henüz yok, oluşturmak isteğe bağlı):

```markdown
---
title: "Title Case Name"
domain: data-science
category: <category-slug>
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[raw/course-notes/sprint X/<lesson>/transcripts/NN-slug]]"
  - "[[raw/course-notes/sprint X/<lesson>/transcripts/NN-slug2]]"
tags:
  - <category-tag>
  - <concept-tag-1>
  - <concept-tag-2>
---

# Title

> One-line summary: <concept ne işe yarar, tek cümle>

## Core Concept

<200-300 words: What is it? Why does it exist? What problem does it solve?>

## How It Works

<300-500 words: Mechanics, syntax, examples. Use code blocks for SQL/code, tables for comparisons.>

## Key Parameters

<100-200 words OR bulleted list: Important variables, options, constants, thresholds>

## When To Use

<100-200 words OR bulleted scenarios: Real-world triggers for using this concept>

## Connections

- Related: [[Page A]], [[Page B]]
- Builds on: [[Prerequisite Page]]
- Compare with: [[Alternative Concept]] (and how they differ)
- Used by: [[Higher-Level Page]]

## My Notes

<Personal observations, gotchas, anti-patterns, interview tips, links to projects in raw/course-notes/sprint X/>
```

**Dil:** İngilizce (CLAUDE.md kuralı). Türkçe transkriptlerden İngilizce wiki üretiyoruz; bu çeviri+sentez işlemi.
**Uzunluk:** Her sayfa ≤1000 kelime (CLAUDE.md kuralı). Aşarsa böl.
**Naming:** Dosya `lowercase-with-hyphens.md`, başlık Title Case.

### 6. Cross-Reference Pass

CLAUDE.md kritik kuralı: *"After creating new pages, revise 10-15 existing related pages to add context and cross-references."*

Her ingest sonunda:
- Yeni sayfalardan eskilere `[[wikilink]]` ekle (Connections bölümlerinde)
- Eski sayfalara yeni sayfalara referans ekle (özellikle Connections, ilgili paragraflar)
- İlk birkaç ingest'te bu sayı düşük olacak (3 mevcut sayfa); zamanla 10-15'e ulaşacak
- Statistics sayfalarına da bağ kur (örn. SQL aggregation → measures of central tendency)

### 7. Index + Log Update

**`data-science/index.md`:**
- Yeni kategori section'ı (yoksa) oluştur
- Yeni sayfaları listele: `- [[Page Title]] — one-line summary from blockquote`
- `updated`, `total_pages` frontmatter alanlarını güncelle

**`data-science/log.md`:**
Append:
```markdown
## [YYYY-MM-DD] ingest | Sprint X / Lesson Y — <Lesson Title>
- Source: `<lesson>/transcripts/` (N transcripts, ~K words)
- Pages created: [[Page A]], [[Page B]], [[Page C]]
- Pages revised: [[Existing Page X]] (added link to [[Page A]]), …
- Wikilinks added: total N
- Key takeaways: <3-5 bullet points of core insights from the lesson>
- Open questions: <if any concept needs more research or future lesson coverage>
```

### 8. Report to User

İterasyon sonunda kısa rapor:
```
Sprint 2 / Ders 1 — SQL'in Temelleri ingest tamamlandı

Yaratılan: 5 sayfa
  - data-science/pages/sql-bigquery/select-statement.md
  - data-science/pages/sql-bigquery/filtering-where.md
  - ...
Revize edilen: 3 sayfa
  - data-science/pages/statistics/descriptive-statistics.md (SQL bağlamı eklendi)
  - ...
Toplam wikilink: 14 yeni
Sıradaki: Sprint 2 / Ders 2 — SQL'de Hesaplanmış Veriler
```

---

## Per-Lesson Beklenen Sayfa Sayıları (Tahmin)

| # | Ders | Transcript | Kategori | Tahmini Sayfa |
|---|------|------------|----------|---------------|
| 1 | Sprint 2/1 — SQL'in Temelleri | 17 | sql-bigquery | 6-8 |
| 2 | Sprint 2/2 — Hesaplanmış Veriler | 11 | sql-bigquery | 4-5 |
| 3 | Sprint 2/3 — JOINs ve Test | 11 | sql-bigquery | 3-4 |
| 4 | Sprint 2/4 — Subquery + CTE | 6 | sql-bigquery | 2-3 |
| 5 | Sprint 2/5 — UDF + Window | 5 | sql-bigquery | 2-3 |
| 6 | Sprint 3/1 — Adv SQL + DW | 13 | sql-bigquery + (yeni?) `data-engineering` | 5-7 |
| 7 | Sprint 1/1 — Google Sheets | 11 | yeni `data-analysis` | 4-6 |
| 8 | Sprint 1/2 — KPI Temelleri | 13 | yeni `business-analytics` | 4-5 |
| 9 | Sprint 1/3 — İleri Seviye KPI | 10 | business-analytics | 3-4 |
| 10 | Sprint 1/4 — Veri Ekosistemi | 11 | data-analysis veya yeni `data-roles` | 3-5 |

**Toplam tahmin:** ~36-50 yeni wiki sayfası, ~3 mevcut statistics sayfası revize.

---

## Kalite Kapıları

Her sayfa yazımdan sonra kontrol:
- [ ] Frontmatter: title, domain, category, created, updated, sources, tags (≥3)
- [ ] One-line summary blockquote var
- [ ] 6 standart section var: Core Concept, How It Works, Key Parameters, When To Use, Connections, My Notes
- [ ] ≤1000 kelime
- [ ] En az 2 `[[wikilink]]` (yoksa orphan)
- [ ] Sources listesinde geçerli transcript wikilink'i
- [ ] Filename `lowercase-with-hyphens.md` formatında
- [ ] Title Case başlık (h1)

İterasyon sonunda toplu kontrol:
- [ ] index.md güncellenmiş, frontmatter `total_pages` doğru
- [ ] log.md'ye entry eklenmiş
- [ ] Yeni kategori varsa CLAUDE.md taksonomisi güncellenmiş
- [ ] Cross-reference sayısı raporlanmış (CLAUDE.md "10-15" kuralı — başlangıçta düşük, kabul edilir)

---

## Çıktı Yapısı (Hedef Son Durum)

```
data-science/
├── pages/
│   ├── statistics/                  (mevcut + revize)
│   │   ├── descriptive-statistics.md
│   │   ├── measures-of-central-tendency.md
│   │   └── measures-of-spread.md
│   ├── sql-bigquery/                (yeni, ~20-25 sayfa)
│   │   ├── select-statement.md
│   │   ├── filtering-where.md
│   │   ├── pattern-matching.md
│   │   ├── aggregations.md
│   │   ├── group-by.md
│   │   ├── joins.md
│   │   ├── window-functions.md
│   │   ├── ctes-and-subqueries.md
│   │   ├── data-warehouse-cost-model.md
│   │   └── ...
│   ├── data-analysis/               (yeni, ~6-10 sayfa)
│   │   ├── data-analysis-workflow.md
│   │   ├── pivot-tables.md
│   │   ├── lookup-functions.md
│   │   └── ...
│   ├── business-analytics/          (yeni, ~7-9 sayfa)
│   │   ├── kpi-fundamentals.md
│   │   ├── customer-acquisition-funnel.md
│   │   ├── rfm-segmentation.md
│   │   ├── cohort-analysis.md
│   │   └── ...
│   └── (opsiyonel: data-engineering/, data-roles/)
├── index.md                          (revize: 6+ kategori section)
├── log.md                            (10 yeni ingest entry)
└── CLAUDE.md                         (revize: yeni kategoriler eklendi)
```

---

## Pilot İterasyon: Sprint 2 / Ders 1 — SQL'in Temelleri

**Beklenen draft sayfa listesi** (kullanıcı onayına sunulacak):

1. **select-statement** — SELECT, FROM, basic projection (sources: 05-select)
2. **distinct-and-deduplication** — DISTINCT keyword (sources: 06-distinct)
3. **filtering-where** — WHERE clause + comparison operators (sources: 07-where, 08-other-filters)
4. **pattern-matching-sql** — LIKE, REGEXP (sources: 09-pattern)
5. **in-and-not-in** — IN/NOT IN with sets and subqueries (sources: 10-in-notin)
6. **column-aliasing-and-ordering** — AS, ORDER BY (sources: 11-aliasing, 12-order-by)
7. **conditional-expressions-sql** — CASE WHEN (sources: 13-kosullu-sutunlar)
8. **null-handling-sql** — IS NULL, COALESCE (sources: 14-null)
9. **sql-data-types-and-casting** — Data types + CAST/SAFE_CAST (sources: 15-data-types, 16-casting)
10. **create-update-delete** — DDL/DML basics (sources: 17-create-update-delete)

**Umbrella sayfa (opsiyonel):**
- **sql-fundamentals-overview** — Tüm sayfaları bağlayan kısa giriş, tablo, anahtar, OLTP/OLAP konseptleri (sources: 01-04 intro videos)

**Tahmini toplam:** 10 sayfa + 1 umbrella = **11 sayfa**

**Yeni kategori:** `sql-bigquery/` (boş, içerikle dolacak)

---

## Kullanıcı Kararları (Onaylandı)

| Konu | Karar |
|------|-------|
| **Sıralama** | Sprint 2 öncelikli (teknik temel önce); sırayla 2/1 → 2/5, sonra 3/1, sonra 1/1 → 1/4 |
| **Pilot sayfa sayısı** | 11 sayfa (Sprint 2/1 için kabul edildi) |
| **Umbrella sayfası** | Sadece **10+ sayfa üreten** derslerde (Sprint 2/1 için evet; diğerleri runtime'da karar) |
| **Dil** | İngilizce; Türkçe parantez ipucu **YOK** |
| **Proje referansları** | Wiki sayfalarının "My Notes" bölümünde URL'li link olarak |
| **Template** | `_templates/wiki-page.md` kalıcı dosya olarak oluşturulacak (bu workflow'dan önce) |

---

## Çalıştırma

Yeni ingest başlatmak için sadece:
> "Sprint 2 / Ders 1 ingest başlat"

Veya kısaca:
> "/ingest sprint2-1"

Şu anda manuel komut; tam otomatize edilirse `tools/ingest.py` yazılabilir (LLM API çağrısı + dosya yazımı). **Bu plan kapsamı dışı**, ilerde değerlendirilir.

---

## İlerleme Takibi

Her iterasyondan sonra bu dokümanın altına ekleyeceğiz:

```markdown
## Iteration History

| # | Tarih | Ders | Yaratılan | Revize | Notlar |
|---|-------|------|-----------|--------|--------|
| 1 | YYYY-MM-DD | Sprint 2/1 | 11 | 3 | ... |
| 2 | ... | ... | ... | ... | ... |
```

---

## Bağlı Plan Dosyası

Bu workflow, üst-seviye plan dosyasının Task 3 bölümünün **detaylandırılmış hali**:
`/Users/projectx/.claude/plans/data-science-klas-r-de-i-ti-tekrar-linked-feather.md`
