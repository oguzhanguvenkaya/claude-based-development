# NotebookLM Video Catalog — 108 Bootcamp Videos

> **Companion to `notebooklm-context.md`.** This is the flat, per-video index. Each row is one video file. Fields: video slug, Turkish title, sprint / lesson / topic position, English concept summary, wiki page (if ingested), transcript path.

---

## How to read this catalog

| Column | Meaning |
|--------|---------|
| **Pos** | Sprint.Lesson.Topic.VideoOrder (e.g., `S2.L1.T1.v01` = Sprint 2, Lesson 1, Topic 1, video 1) |
| **Slug** | The filename slug (matches `{slug}.mp4`) |
| **Title (TR)** | The Turkish title as it appears in the course |
| **Concept** | One-line English summary of what the video teaches |
| **Wiki** | Linked wiki page in `data-science/pages/sql-bigquery/` (if ingested) — `—` means not yet ingested |

The full file path is:
```
data-science/raw/course-notes/sprint X/<lesson-folder>/videos/<slug>.mp4
```

And the transcript path is:
```
data-science/raw/course-notes/sprint X/<lesson-folder>/transcripts/<slug>.md
```

---

## Sprint 1 / Lesson 1 — Google Sheets ile Analizin Temelleri (11 videos)

Folder: `sprint 1/01-google-sheets-ile-analizin-temelleri/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S1.L1.T1.v01 | `01-veri-analizinin-asamalari` | Veri analizinin aşamaları | The phases of a typical data analysis workflow | — |
| S1.L1.T1.v02 | `02-google-sheetse-import-etmek` | Verileri Google Sheets'e import etmek | Loading data into Google Sheets from CSV/external sources | — |
| S1.L1.T1.v03 | `03-veri-kesfi-ve-temizlenmesi` | Verilerin keşfi ve temizlenmesi | Exploratory data review and cleaning in Sheets | — |
| S1.L1.T2.v04 | `04-lookup-fonksiyonlari` | Lookup Fonksiyonları | VLOOKUP / HLOOKUP / XLOOKUP for table lookups | — |
| S1.L1.T2.v05 | `05-pivot-tablo` | Pivot Tablo | Building pivot tables to summarize data | — |
| S1.L1.T3.v06 | `06-veriyi-filter-ile-filtrelemek` | Veriyi FILTER ile filtrelemek | The FILTER function for conditional row selection | — |
| S1.L1.T3.v07 | `07-veriyi-query-ile-filtrelemek` | Veriyi QUERY ile filtrelemek | The QUERY function (SQL-like syntax in Sheets) | — |
| S1.L1.T3.v08 | `08-veriyi-unique-ile-filtrelemek` | Veriyi UNIQUE ile filtrelemek | UNIQUE function for deduplication | — |
| S1.L1.T4.v09 | `09-lookup-kullanarak-veri-temizleme` | Lookup kullanarak veri temizleme | Using lookup formulas to clean and reconcile data | — |
| S1.L1.T4.v10 | `10-index-match-ile-analiz` | INDEX-MATCH ile Analiz | INDEX + MATCH combo for flexible lookups | — |
| S1.L1.T4.v11 | `11-veriyi-gorsellestirme` | Veriyi Görselleştirme | Visualizing data with Sheets charts | — |

---

## Sprint 1 / Lesson 2 — KPI'ın Temelleri (13 videos)

Folder: `sprint 1/02-kpi-temelleri/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S1.L2.T1.v01 | `01-adim-1-sorular-sor` | Adım 1: Sorular Sor | Step 1 of the 7-step analysis framework: ask the right questions | — |
| S1.L2.T1.v02 | `02-adim-2-veri-ihtiyaclarini-belirle` | Adım 2: Veri İhtiyaçlarını Belirle | Step 2: identify the data you need | — |
| S1.L2.T1.v03 | `03-adim-3-analiz-turunu-sec` | Adım 3: Analiz Türünü Seç | Step 3: choose the analysis type (descriptive, diagnostic, predictive, prescriptive) | — |
| S1.L2.T1.v04 | `04-adim-4-veriyi-kesfet` | Adım 4: Veriyi Keşfet | Step 4: explore the data | — |
| S1.L2.T1.v05 | `05-adim-5-verileri-temizle` | Adım 5: Verileri Temizle | Step 5: clean the data | — |
| S1.L2.T1.v06 | `06-adim-6-icgorulerini-ozetle` | Adım 6: İçgörülerini Özetle | Step 6: summarize the insights | — |
| S1.L2.T1.v07 | `07-adim-7-sonuclari-gorsellestir` | Adım 7: Sonuçları Görselleştir | Step 7: visualize the results | — |
| S1.L2.T1.v08 | `08-sonuc-ve-yinelemenin-onemi` | Sonuç ve Yinelemenin Önemi | Closing: why iteration matters | — |
| S1.L2.T2.v09 | `09-kpi-nedir` | KPI Nedir | What a KPI is and why it matters | — |
| S1.L2.T2.v10 | `10-kpi-metrik-farki` | KPI Metrik Farkı | KPI vs metric — the distinction | — |
| S1.L2.T3.v11 | `11-finans-kpilari` | Finans KPI'ları | Financial KPIs (revenue, margin, CAC, LTV) | — |
| S1.L2.T3.v12 | `12-envanter-kpilari` | Envanter KPI'ları | Inventory KPIs (turnover, stock days, fill rate) | — |
| S1.L2.T3.v13 | `13-kalite-kpilari` | Kalite KPI'ları | Quality KPIs (defect rate, NPS, error rate) | — |

---

## Sprint 1 / Lesson 3 — İleri Seviye KPI'lar (10 videos)

Folder: `sprint 1/03-ileri-seviye-kpi/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S1.L3.T1.v01 | `01-farkli-sirketler-farkli-kpilar` | Farklı Şirketler Farklı KPI'lar | Different companies need different KPIs | — |
| S1.L3.T1.v02 | `02-is-modeli-ve-kpi` | İş Modeli ve KPI | Business model dictates which KPIs matter | — |
| S1.L3.T1.v03 | `03-ticari-model-ve-olgunluk-seviyesi` | Ticari Model & Olgunluk Seviyesi | Maturity level shifts KPI focus (growth → retention → profit) | — |
| S1.L3.T2.v04 | `04-farkli-takimlar-farkli-kpilar` | Farklı Takımlar-Farklı KPI'lar | Different teams optimize different KPIs | — |
| S1.L3.T2.v05 | `05-kpi-seciminde-kacinilmasi-gerekenler` | KPI Seçiminde Kaçınılması Gerekenler | Anti-patterns in KPI selection (vanity metrics, Goodhart's Law) | — |
| S1.L3.T3.v07 | `07-musteri-kazanim-kanallari` | Müşteri Kazanım Kanalları | Customer acquisition channels (organic, paid, referral) | — |
| S1.L3.T3.v08 | `08-genisleme-hunisi` | Genişleme Hunisi | Expansion funnel (upsell, cross-sell, retention) | — |
| S1.L3.T4.v09 | `09-segmentasyon-nedir` | Segmentasyon Nedir? | Customer segmentation introduction | — |
| S1.L3.T4.v10 | `10-segmentasyon-rfm-yontemi` | Segmentasyon RFM yöntemi | RFM segmentation (Recency, Frequency, Monetary) | — |
| S1.L3.T4.v11 | `11-cohort-analizi` | Cohort Analizi | Cohort analysis — track groups over time | — |

> Note: Video 06 (`06-musteri-kazanim-hunisi`) is missing from the local archive but referenced in the syllabus (clip ID collides with v05 — a likely typo in the source).

---

## Sprint 1 / Lesson 4 — Data Analiz Ekosistemi (11 videos)

Folder: `sprint 1/04-data-analiz-ekosistemi/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S1.L4.T1.v01 | `01-veri-uzmanlarinin-rolu` | Veri Uzmanlarının Rolü | The role of data professionals in modern organizations | — |
| S1.L4.T1.v02 | `02-is-ve-veri-ekipleri-arasindaki-isbirligi` | İş ve Veri Ekipleri Arasındaki İşbirliği | Collaboration between business and data teams | — |
| S1.L4.T2.v03 | `03-muze-vaka-analizi` | Müze Vaka Analizi | Case study: data analysis at a museum | — |
| S1.L4.T2.v04 | `04-nestle-musteri-verisi-stratejisi` | Nestlé'nin Müşteri Verisi Stratejisi | Case study: Nestlé's customer data strategy | — |
| S1.L4.T2.v05 | `05-vodafone-yapay-zeka-botlari` | Vodafone Yapay Zeka Botları | Case study: Vodafone's AI chatbots | — |
| S1.L4.T3.v06 | `06-veri-yasam-dongusu` | Veri Yaşam Döngüsü | The data lifecycle (collect → store → process → analyze → archive) | — |
| S1.L4.T3.v07 | `07-veri-rolleri-i` | Veri Rolleri I | Data roles part 1 (analyst, scientist) | — |
| S1.L4.T3.v08 | `08-veri-rolleri-ii` | Veri Rolleri II | Data roles part 2 (engineer, architect) | — |
| S1.L4.T3.v09 | `09-veri-rolleri-iii` | Veri Rolleri III | Data roles part 3 (ML/AI, governance) | — |
| S1.L4.T4.v10 | `10-olgunluk-duzeyine-gore-veri-ekip-yapisi` | Olgunluk Düzeyine Göre Veri Ekip Yapısı | Team structure by data maturity level | — |
| S1.L4.T4.v11 | `11-magaza-ici-satislarin-artirilmasi` | Mağaza İçi Satışların Artırılması | Real-world example: increasing in-store sales | — |

---

## Sprint 2 / Lesson 1 — SQL'in Temelleri (17 videos)

Folder: `sprint 2/01-sql-temelleri/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S2.L1.T1.v01 | `01-tanitim-ve-amaci` | Tanıtım ve Amacı | Why SQL exists; vs spreadsheets | `sql-fundamentals-overview` |
| S2.L1.T1.v02 | `02-tablolar-anahtarlar` | Tablolar, Anahtarlar | Tables, rows, columns, PK, FK | `relational-data-model` |
| S2.L1.T1.v03 | `03-oltp-ve-olap-sistemleri` | OLTP ve OLAP Sistemleri | Operational vs analytical databases | `oltp-vs-olap` |
| S2.L1.T1.v04 | `04-entity-iliski-diyagramlari-erd` | Entity–İlişki Diyagramları (ERD) | Visual schema notation | `entity-relationship-diagrams` |
| S2.L1.T2.v05 | `05-select` | SELECT | The SELECT clause; FROM | `select-statement` |
| S2.L1.T2.v06 | `06-distinct` | DISTINCT | Deduplicating query results | `distinct-and-deduplication` |
| S2.L1.T2.v07 | `07-verileri-filtreleme-where` | Verileri filtreleme: WHERE | WHERE clause basics | `filtering-where` |
| S2.L1.T2.v08 | `08-diger-anahtar-kelimelerle-filtreleme` | Diğer Anahtar Kelimelerle Filtreleme | AND, OR, NOT, BETWEEN combinators | `filtering-where` |
| S2.L1.T3.v09 | `09-desen-eslestirme-pattern-matching` | Desen Eşleştirme (Pattern Matching) | LIKE with % and _ wildcards | `pattern-matching-sql` |
| S2.L1.T3.v10 | `10-in-ve-not-in-kullanimi` | IN ve NOT IN Kullanımı | Set-membership filtering | `in-and-not-in` |
| S2.L1.T3.v11 | `11-takma-adlar-aliasing` | Takma Adlar (Aliasing) | AS keyword for columns | `column-aliasing-and-ordering` |
| S2.L1.T3.v12 | `12-order-by-ile-siralama` | ORDER BY ile Sıralama | Sorting query results | `column-aliasing-and-ordering` |
| S2.L1.T3.v13 | `13-kosullu-sutunlar` | Koşullu Sütunlar | CASE WHEN, IF | `conditional-expressions-sql` |
| S2.L1.T3.v14 | `14-null-degerleri` | NULL Değerleri | NULL semantics, IS NULL, COALESCE | `null-handling-sql` |
| S2.L1.T4.v15 | `15-veri-turleri` | Veri Türleri | INT64, STRING, DATE, BOOL, etc. | `sql-data-types-and-casting` |
| S2.L1.T4.v16 | `16-veri-turu-donusturme-casting` | Veri Türü Dönüştürme (Casting) | CAST and SAFE_CAST | `sql-data-types-and-casting` |
| S2.L1.T4.v17 | `17-create-update-delete` | Kalıcı Değişiklikler: CREATE-UPDATE-DELETE | DDL + DML basics | `create-update-delete` |

---

## Sprint 2 / Lesson 2 — SQL'de Hesaplanmış Veriler (11 videos)

Folder: `sprint 2/02-sql-hesaplanmis-veriler/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S2.L2.T1.v01 | `01-aggregate-fonksiyonu-nedir` | Aggregate Fonksiyonu Nedir | The general concept of aggregation | `sql-computed-data-overview` |
| S2.L2.T1.v02 | `02-count-countif` | COUNT, COUNTIF | Row counting with conditions | `count-and-countif` |
| S2.L2.T1.v03 | `03-sum-avg-min-max` | SUM, AVG, MIN/MAX | The four canonical numeric aggregates | `sum-avg-min-max` |
| S2.L2.T2.v04 | `04-safe-divide-fonksiyonu` | SAFE_DIVIDE Fonksiyonu | NULL-on-zero division | `safe-divide` |
| S2.L2.T2.v05 | `05-group-by` | GROUP BY | Bucketing rows by a column | `group-by` |
| S2.L2.T2.v06 | `06-where-ve-having-ile-filtreleme` | WHERE ve HAVING ile Filtreleme | Row filter vs group filter | `where-vs-having` |
| S2.L2.T3.v07 | `07-sayisal-fonksiyonlar-round` | Sayısal Fonksiyonlar: ROUND | Number formatting (ROUND, CEIL, FLOOR) | `numeric-functions-round` |
| S2.L2.T3.v08 | `08-concat-ile-sutunlari-birlestirme` | CONCAT() ile Sütunları Birleştirme | String concatenation | `string-concatenation-concat` |
| S2.L2.T3.v09 | `09-sutunlardaki-metinleri-degistirme` | Sütunlardaki Metinleri Değiştirme | REPLACE for substring substitution | `string-cleaning-replace-and-case` |
| S2.L2.T3.v10 | `10-buyuk-kucuk-harf-bicimi` | Metinlerin Büyük/Küçük Harf Biçimini Değiştirme | LOWER, UPPER, INITCAP | `string-cleaning-replace-and-case` |
| S2.L2.T3.v11 | `11-date-sub-ile-zaman-araligi-cikarma` | DATE_SUB ile Tarihlerden Zaman Aralığı Çıkarma | Date arithmetic in BigQuery | `date-arithmetic-date-sub` |

---

## Sprint 2 / Lesson 3 — Tabloları Birleştirmek ve Test Etmek (11 videos)

Folder: `sprint 2/03-tablolari-birlestirmek-ve-test-etmek/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S2.L3.T1.v01 | `01-joine-giris` | JOIN'e Giriş | Concept of joining tables | `joins-fundamentals` |
| S2.L3.T1.v02 | `02-join-kullanimi` | JOIN Kullanımı | ON clause syntax | `joins-fundamentals` |
| S2.L3.T1.v03 | `03-table-aliasing` | Table Aliasing | Short table aliases in JOINs | `joins-fundamentals` |
| S2.L3.T1.v04 | `04-join-turleri` | JOIN Türleri | INNER, LEFT, RIGHT, FULL OUTER | `join-types` |
| S2.L3.T2.v05 | `05-coklu-join-islemleri` | Çoklu JOIN İşlemleri | Chaining 3+ tables | `multiple-joins` |
| S2.L3.T2.v06 | `06-join-ve-group-by` | JOIN ve GROUP BY | Aggregating joined data, common mistakes | `joins-with-group-by` |
| S2.L3.T2.v07 | `07-join-dikkat-edilmesi-gerekenler` | JOIN: Dikkat Edilmesi Gerekenler | Grain mismatch, fan-out, wrong join type | `join-pitfalls-grain-and-fan-out` |
| S2.L3.T3.v08 | `08-neden-test-ediyoruz` | Neden Test Ediyoruz? | Motivation for SQL data testing | `testing-data-pipelines` |
| S2.L3.T3.v09 | `09-primary-key-testi` | Primary Key Testi | PK uniqueness test | `primary-key-test` |
| S2.L3.T3.v10 | `10-column-testi` | Column Testi | NULL, range, accepted-values tests | `column-test` |
| S2.L3.T3.v11 | `11-deger-korunumu-testi` | Değer Korunumu Testi | Value preservation across joins | `value-preservation-test` |

---

## Sprint 2 / Lesson 4 — Subquery ve With As (6 videos)

Folder: `sprint 2/04-subquery-ve-with-as/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S2.L4.T1.v01 | `01-with-as-ile-query-tanimlama` | WITH AS ile query tanımlama | Defining CTEs (Common Table Expressions) | — |
| S2.L4.T1.v02 | `02-ic-ice-query-nested-query` | İç İçe Query Kullanma | Nested subqueries | — |
| S2.L4.T2.v03 | `03-join-vs-nested-subquery` | JOIN vs. Nested Subquery | When to choose each | — |
| S2.L4.T2.v04 | `04-union` | UNION | Combining rows from multiple SELECTs | — |
| S2.L4.T3.v05 | `05-bigquery-insert-ve-cast-islemleri` | BigQuery Insert ve Cast İşlemleri | INSERT and CAST in BigQuery specifics | — |
| S2.L4.T3.v06 | `06-temiz-kodun-onemi` | Temiz Kodun Önemi | Clean SQL coding conventions | — |

---

## Sprint 2 / Lesson 5 — Kullanıcı Tanımlı Fonksiyonlar ve Window Fonksiyonları (5 videos)

Folder: `sprint 2/05-fonksiyonlar-ve-window/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S2.L5.T1.v01 | `01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak` | Fonksiyonları ve Yerleşik Örnekleri Anlamak | Built-in vs user-defined functions overview | — |
| S2.L5.T1.v02 | `02-sqlde-fonksiyon-tanimlama-ve-cagirma` | SQL'de Fonksiyon Tanımlama ve Çağırma | CREATE FUNCTION (UDF) | — |
| S2.L5.T2.v03 | `03-neden-window-fonksiyonlarina-ihtiyacimiz-var` | Neden Window Fonksiyonlarına İhtiyacımız Var? | Motivation for window functions | — |
| S2.L5.T2.v04 | `04-partition-by-ve-over-kullanimi` | PARTITION BY ve OVER Kullanımı | The OVER clause and partitioning | — |
| S2.L5.T2.v05 | `05-window-ile-farkli-detay-seviyelerinde-join` | Window Fonksiyonlarıyla Farklı Detay Seviyelerinde Join | Window functions across grain levels | — |

---

## Sprint 3 / Lesson 1 — İleri Seviye SQL (13 videos)

Folder: `sprint 3/01-ileri-seviye-sql/`

| Pos | Slug | Title (TR) | Concept | Wiki |
|-----|------|------------|---------|------|
| S3.L1.T1.v01 | `01-veri-hatti-genel-bakis` | Veri Hattı (Data Pipeline) Genel Bakışı | Pipeline overview | — |
| S3.L1.T1.v02 | `02-donusum-asamalari-ve-veri-modelleme` | Dönüşüm Aşamaları ve Veri Modelleme | Transformation stages and data modeling | — |
| S3.L1.T1.v03 | `03-cok-tablo-maliyet-etkileri` | Çok Sayıda Tablo Kullanımının Maliyet Etkileri | Cost impact of using many tables | — |
| S3.L1.T2.v04 | `04-gorunumler-view-ve-veri-hatlari` | Görünümler (View) ve Veri Hatları | SQL views in pipelines | — |
| S3.L1.T2.v05 | `05-gorunumler-ve-tablolar-arti-eksi` | Görünümler ve Tabloların Artı/Eksi Yönleri | Views vs tables tradeoffs | — |
| S3.L1.T2.v06 | `06-karma-tablo-ve-gorunum-yaklasimi` | Karma (Tablo ve Görünüm) Yaklaşımı | Hybrid table+view approach | — |
| S3.L1.T3.v07 | `07-veri-platformu-genel-bakisi` | Veri Platformu Genel Bakışı | Modern data platform overview | — |
| S3.L1.T3.v08 | `08-depolama-ve-isleme-ucretleri` | Depolama ve İşleme Ücretleri | Storage vs compute pricing | — |
| S3.L1.T3.v09 | `09-fiyatlandirma-modelleri` | Fiyatlandırma Modelleri | Cloud warehouse pricing models | — |
| S3.L1.T3.v10 | `10-modern-veri-ambarlarinin-karsilastirilmasi` | Modern Veri Ambarlarının Karşılaştırılması | BigQuery vs Snowflake vs Redshift vs Databricks | — |
| S3.L1.T4.v11 | `11-bigquery-sorgu-maliyetleri` | BigQuery'de Sorgu Maliyetleri | BigQuery query cost model | — |
| S3.L1.T4.v12 | `12-sutun-ve-satir-bazli-maliyetler` | Sütun ve Satır Bazlı Maliyetler | Column vs row storage cost implications | — |
| S3.L1.T4.v13 | `13-veri-bolumlendirme-partitioning` | Veri Bölümlendirme (Partitioning) | Table partitioning for cost optimization | — |

---

## Summary Counts

| Sprint | Lessons | Videos | Wiki-ingested | Pending |
|--------|---------|--------|---------------|---------|
| Sprint 1 | 4 | 45 | 0 | 45 |
| Sprint 2 | 5 | 50 | 39 (lessons 1–3) | 11 (lessons 4–5) |
| Sprint 3 | 1 of 5 held | 13 | 0 | 13 |
| **Total** | **10 active** | **108** | **39** | **69** |

---

## Suggested Order to Watch (if studying from scratch)

1. **Sprint 1 Lesson 4** (data ecosystem) — frames the discipline
2. **Sprint 1 Lesson 2** (KPI basics) — defines what we measure
3. **Sprint 1 Lesson 1** (Google Sheets) — practical first taste
4. **Sprint 2 Lesson 1** (SQL fundamentals) — the technical foundation
5. **Sprint 2 Lesson 2** (computed data) — aggregations + scalar functions
6. **Sprint 2 Lesson 3** (joins + tests) — combining tables safely
7. **Sprint 2 Lesson 4** (subqueries + CTEs) — query composition
8. **Sprint 2 Lesson 5** (window functions) — advanced aggregation
9. **Sprint 1 Lesson 3** (advanced KPI) — applying SQL to business analytics
10. **Sprint 3 Lesson 1** (advanced SQL + warehouse cost) — production thinking

Sprint 3 Lessons 2–5 are not yet held; they will cover Git, dbt installation, dbt models, dbt Cloud, and a capstone project.
