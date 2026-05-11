# NotebookLM Context — Data Analytics Bootcamp Videos

> **Purpose of this document.** This file is the source of truth for NotebookLM (or any other LLM-based knowledge tool) about the 108 lecture videos uploaded as sources. The videos are individual lessons; this document explains what curriculum they belong to, how they are organized, which lesson and topic each falls under, and how the concepts relate to one another. Upload this file alongside the videos so the LLM can reason about the corpus as a whole.

---

## 1. Course Overview

- **Platform:** WorkInTech NextGen (`nextgen.workintech.com.tr`)
- **Track:** Data Analytics Bootcamp
- **Format:** Live online lectures (recorded), augmented by hands-on projects
- **Total duration of uploaded videos:** ~4.65 hours (≈279 minutes) split across 108 clips
- **Lecture language:** Turkish (technical terms in English: SELECT, GROUP BY, JOIN, KPI, OLAP, etc.)
- **Audience level:** Junior / entry-level data analysts; assumes spreadsheet familiarity, no prior SQL
- **Pedagogy:** Each lesson follows a scenario-based style — an analyst is given a business question, learns a concept by solving it, then practices in a project

The bootcamp is organized into three **sprints**, each spanning roughly 4–5 weeks. Each sprint contains several **lessons**, each lesson is split into 2–4 **topic groups**, and each topic group contains 2–6 short **videos** (typically 2–5 minutes each).

---

## 2. Sprint Tree

```
Data Analytics Bootcamp
├── Sprint 1 — Veri Analizinin Temelleri (Data Analysis Fundamentals)
│   Start: 7 Mar 2026   |   4 lessons   |   45 videos
│
├── Sprint 2 — SQL ile Veritabanı Sorguları (SQL Database Querying)
│   Start: 4 Apr 2026   |   5 lessons   |   50 videos
│
└── Sprint 3 — DBT ile Dönüşüm Otomasyonu (DBT Transformation Automation)
    Start: 2 May 2026   |   5 lessons (1 held, 4 upcoming)   |   13 videos (so far)
```

### What each sprint teaches at a glance

| Sprint | Theme | What you can do after it |
|--------|-------|--------------------------|
| **Sprint 1** | Spreadsheets & business metrics | Clean a sheet, build pivot tables, compute KPIs, understand data team roles |
| **Sprint 2** | SQL on BigQuery | Query a relational warehouse end-to-end: SELECT, JOIN, GROUP BY, CTEs, window functions, write tests |
| **Sprint 3** | Modern warehouse & dbt | Reason about pipeline cost, use Git, build dbt models, deploy production transformations |

---

## 3. Lesson and Topic Tree (with video counts)

### Sprint 1: Veri Analizinin Temelleri (45 videos across 4 lessons)

```
Lesson 1 — Google Sheets ile Analizin Temelleri (11 videos)
├── Topic 1.1: Veri Analizine Giriş ve Google Sheets (3 videos)
│   01 Veri analizinin aşamaları
│   02 Verileri Google Sheets'e import etmek
│   03 Verilerin keşfi ve temizlenmesi
├── Topic 1.2: Verilerin Analizi (2 videos)
│   04 Lookup Fonksiyonları
│   05 Pivot Tablo
├── Topic 1.3: Veriyi Filtrelemek (3 videos)
│   06 Veriyi FILTER ile filtrelemek
│   07 Veriyi QUERY ile filtrelemek
│   08 Veriyi UNIQUE ile filtrelemek
└── Topic 1.4: Verileri Analiz Etmek (3 videos)
    09 Lookup kullanarak veri temizleme
    10 INDEX-MATCH ile Analiz
    11 Veriyi Görselleştirme

Lesson 2 — KPI'ın Temelleri (13 videos)
├── Topic 2.1: Veri Analizi 7 Adım (8 videos)
│   01 Adım 1: Sorular Sor
│   02 Adım 2: Veri İhtiyaçlarını Belirle
│   03 Adım 3: Analiz Türünü Seç
│   04 Adım 4: Veriyi Keşfet
│   05 Adım 5: Verileri Temizle
│   06 Adım 6: İçgörülerini Özetle
│   07 Adım 7: Sonuçları Görselleştir
│   08 Sonuç ve Yinelemenin Önemi
├── Topic 2.2: KPI'ların Temeli ve Önemi (2 videos)
│   09 KPI Nedir
│   10 KPI Metrik Farkı
└── Topic 2.3: Departman KPI'larına Bakış (3 videos)
    11 Finans KPI'ları
    12 Envanter KPI'ları
    13 Kalite KPI'ları

Lesson 3 — İleri Seviye KPI'lar (10 videos)
├── Topic 3.1: Şirkete Göre KPI Oluşturma (3 videos)
│   01 Farklı Şirketler Farklı KPI'lar
│   02 İş Modeli ve KPI
│   03 Ticari Model & Olgunluk Seviyesi
├── Topic 3.2: KPI Amaç ve Seçimleri (2 videos)
│   04 Farklı Takımlar-Farklı KPI'lar
│   05 KPI Seçiminde Kaçınılması Gerekenler
├── Topic 3.3: Müşteri Yolculuğu (2 videos, missing video 06 in catalog)
│   07 Müşteri Kazanım Kanalları
│   08 Genişleme Hunisi
└── Topic 3.4: Müşteri Yolculuğu II (3 videos)
    09 Segmentasyon Nedir?
    10 Segmentasyon RFM yöntemi
    11 Cohort Analizi

Lesson 4 — Data Analiz Ekosistemi (11 videos)
├── Topic 4.1: Veri Stratejileri ve Uygulama Örnekleri (2 videos)
│   01 Veri Uzmanlarının Rolü
│   02 İş ve Veri Ekipleri Arasındaki İşbirliği
├── Topic 4.2: Veri Stratejileri ve Uygulama Örnekleri - 2 (3 videos)
│   03 Müze Vaka Analizi
│   04 Nestlé'nin Müşteri Verisi Stratejisi
│   05 Vodafone Yapay Zeka Botları
├── Topic 4.3: Veri Yaşam Döngüsü ve Ekip Dinamikleri (4 videos)
│   06 Veri Yaşam Döngüsü
│   07 Veri Rolleri I
│   08 Veri Rolleri II
│   09 Veri Rolleri III
└── Topic 4.4: Ekip Dinamikleri - 2 (2 videos)
    10 Olgunluk Düzeyine Göre Veri Ekip Yapısı
    11 Gerçek Dünya Örneği: Mağaza İçi Satışların Artırılması
```

### Sprint 2: SQL ile Veritabanı Sorguları (50 videos across 5 lessons)

```
Lesson 1 — SQL'in Temelleri (17 videos)
├── Topic 1.1: SQL'e Giriş (4 videos)
│   01 Tanıtım ve Amacı
│   02 Tablolar, Anahtarlar
│   03 OLTP ve OLAP Sistemleri
│   04 Entity–İlişki Diyagramları (ERD)
├── Topic 1.2: SQL Dili — Reading Basics (4 videos)
│   05 SELECT
│   06 DISTINCT
│   07 Verileri filtreleme: WHERE
│   08 Diğer Anahtar Kelimelerle Filtreleme (AND/OR/NOT/BETWEEN)
├── Topic 1.3: SQL — Searching and Sorting (6 videos)
│   09 Desen Eşleştirme (Pattern Matching, LIKE)
│   10 IN ve NOT IN Kullanımı
│   11 Takma Adlar (Aliasing, AS)
│   12 ORDER BY ile Sıralama
│   13 Koşullu Sütunlar (CASE WHEN, IF)
│   14 NULL Değerleri
└── Topic 1.4: SQL — Types and Mutation (3 videos)
    15 Veri Türleri (INT64, STRING, DATE, etc.)
    16 Veri Türü Dönüştürme (CAST, SAFE_CAST)
    17 Kalıcı Değişiklikler (CREATE, UPDATE, DELETE)

Lesson 2 — SQL'de Hesaplanmış Veriler (11 videos)
├── Topic 2.1: Aggregation Fonksiyonları (3 videos)
│   01 Aggregate Fonksiyonu Nedir
│   02 COUNT, COUNTIF
│   03 SUM, AVG, MIN/MAX
├── Topic 2.2: Aggregation Fonksiyonları - 2 (3 videos)
│   04 SAFE_DIVIDE Fonksiyonu
│   05 GROUP BY
│   06 WHERE ve HAVING ile Filtreleme
└── Topic 2.3: Veri Türleri ve Fonksiyonlar (5 videos)
    07 Sayısal Fonksiyonlar: ROUND
    08 CONCAT() ile Sütunları Birleştirme
    09 Sütunlardaki Metinleri Değiştirme (REPLACE)
    10 Metinlerin Büyük/Küçük Harf Biçimini Değiştirme (LOWER, UPPER, INITCAP)
    11 DATE_SUB ile Tarihlerden Zaman Aralığı Çıkarma

Lesson 3 — Tabloları Birleştirmek ve Test Etmek (11 videos)
├── Topic 3.1: SQL'de tabloları birleştirmek: JOIN (4 videos)
│   01 JOIN'e Giriş
│   02 JOIN Kullanımı (ON clause)
│   03 Table Aliasing
│   04 JOIN Türleri (INNER, LEFT, RIGHT, FULL OUTER)
├── Topic 3.2: JOIN - 2 (3 videos)
│   05 Çoklu JOIN İşlemleri
│   06 JOIN ve GROUP BY
│   07 JOIN: Dikkat Edilmesi Gerekenler (grain, fan-out)
└── Topic 3.3: SQL'de test yazmak (4 videos)
    08 Neden Test Ediyoruz?
    09 Primary Key Testi
    10 Column Testi (NULL, range, accepted-values)
    11 Değer Korunumu Testi (value preservation)

Lesson 4 — Subquery ve With As (6 videos)
├── Topic 4.1: Query birleştirme Yöntemleri (2 videos)
│   01 WITH AS ile query tanımlama (CTEs)
│   02 İç İçe Query Kullanma (Nested Query)
├── Topic 4.2: Ne zaman join ne zaman sub-query (2 videos)
│   03 JOIN vs. Nested Subquery
│   04 UNION
└── Topic 4.3: Temiz Kod (2 videos)
    05 BigQuery Insert ve Cast İşlemleri
    06 Temiz Kodun Önemi

Lesson 5 — Kullanıcı Tanımlı Fonksiyonlar ve Window Fonksiyonları (5 videos)
├── Topic 5.1: User-Defined Functions (2 videos)
│   01 Fonksiyonları ve Yerleşik Örnekleri Anlamak
│   02 SQL'de Fonksiyon Tanımlama ve Çağırma (CREATE FUNCTION)
└── Topic 5.2: Window Fonksiyonları (3 videos)
    03 Neden Window Fonksiyonlarına İhtiyacımız Var?
    04 PARTITION BY ve OVER Kullanımı
    05 Window Fonksiyonlarıyla Farklı Detay Seviyelerinde Join
```

### Sprint 3: DBT ile Dönüşüm Otomasyonu (13 videos held, more upcoming)

```
Lesson 1 — İleri Seviye SQL (13 videos)
├── Topic 1.1: Data Pipelines (3 videos)
│   01 Veri Hattı (Data Pipeline) Genel Bakışı
│   02 Dönüşüm Aşamaları ve Veri Modelleme
│   03 Çok Sayıda Tablo Kullanımının Maliyet Etkileri
├── Topic 1.2: Data Pipelines - 2 (3 videos)
│   04 Görünümler (View) ve Veri Hatları
│   05 Görünümler ve Tabloların Artı/Eksi Yönleri
│   06 Karma (Tablo ve Görünüm) Yaklaşımı
├── Topic 1.3: Maliyet ve Bölümlendirme (4 videos)
│   07 Veri Platformu Genel Bakışı
│   08 Depolama ve İşleme Ücretleri
│   09 Fiyatlandırma Modelleri
│   10 Modern Veri Ambarlarının Karşılaştırılması
└── Topic 1.4: Maliyet ve Bölümlendirme - 2 (3 videos)
    11 BigQuery'de Sorgu Maliyetleri
    12 Sütun ve Satır Bazlı Maliyetler
    13 Veri Bölümlendirme (Partitioning)

Lessons 2–5 — UPCOMING (not yet held; placeholders in syllabus)
    L2 Versiyon Kontrol Sistemi: Git, GitHub  (12 Mayıs 2026)
    L3 DBT'ye Giriş ve Data Katmanları       (14 Mayıs 2026)
    L4 İleri Seviye DBT                       (21 Mayıs 2026)
    L5 Proje ve Sunum                         (2 Haziran 2026)
```

---

## 4. Cross-Cutting Concept Map

The 108 videos cover concepts that recur across lessons. This is the **conceptual graph**, not the chronological order:

### Data Fundamentals
- The relational model (Sprint 2 L1 videos 02–04) is the foundation for every SQL lesson and the dbt warehouse layer in Sprint 3
- OLTP vs OLAP (Sprint 2 L1 video 03) explains why BigQuery exists and why Sprint 3 is about warehouse cost
- Data lifecycle and roles (Sprint 1 L4 videos 06–10) provide organizational context

### Data Wrangling (spreadsheet → SQL)
- Spreadsheet techniques (Sprint 1 L1): FILTER, QUERY, UNIQUE, INDEX-MATCH, pivot tables — these are the *concepts* that SQL's SELECT/WHERE/DISTINCT/JOIN/GROUP BY map onto
- SQL equivalents (Sprint 2): each spreadsheet feature has a stronger SQL counterpart taught later

### Aggregation and Reduction
- Pivot tables in Sheets (Sprint 1 L1 video 05) → GROUP BY + aggregates in SQL (Sprint 2 L2 videos 02–06)
- Conditional counts (COUNTIF) appear in both Sheets and SQL
- The seven-step analysis framework (Sprint 1 L2 Topic 2.1) is the workflow into which every concept fits

### KPI / Business Analytics
- KPI basics (Sprint 1 L2) → company-specific KPIs (Sprint 1 L3)
- Customer journey funnels and cohort/RFM analysis (Sprint 1 L3 Topics 3.3–3.4) — depend on SQL window functions (Sprint 2 L5) to compute at scale

### Joining and Reshaping
- JOINs and their pitfalls (Sprint 2 L3 Topics 3.1–3.2)
- SQL testing of joined data (Sprint 2 L3 Topic 3.3)
- Subqueries and CTEs (Sprint 2 L4) — alternative ways to compose multi-step transformations

### Pipelines and Cost
- Modern data pipelines (Sprint 3 L1 Topics 1.1–1.2)
- BigQuery cost model and partitioning (Sprint 3 L1 Topics 1.3–1.4)
- dbt as the orchestration layer (Sprint 3 L3–L4, upcoming)

---

## 5. Video Naming Convention

Each video file is named as:
```
{NN}-{slug-in-kebab-case}.mp4
```

- `NN` = sequence number **within the lesson** (01–17, depending on lesson length)
- `slug` = a Turkish-to-ASCII transliteration of the concept (e.g., `01-veri-analizinin-asamalari`, `05-select`, `09-primary-key-testi`)
- Path: `data-science/raw/course-notes/sprint X/<lesson-folder>/videos/{NN}-{slug}.mp4`

For the full filename-to-title mapping, see the companion file `notebooklm-video-catalog.md`.

---

## 6. Wiki Knowledge Already Built (Reference)

We have authored 33 long-form wiki pages from the lecture transcripts of Sprint 2 Lessons 1–3. NotebookLM can use the videos directly; the wiki is for human reading and is summarized here so the LLM understands what's already been distilled.

| Topic | Wiki Page | Source Videos |
|-------|-----------|---------------|
| **Sprint 2 Lesson 1: SQL Fundamentals** | | |
| Relational model | `relational-data-model.md` | S2L1 02 |
| OLTP vs OLAP | `oltp-vs-olap.md` | S2L1 03 |
| ERD | `entity-relationship-diagrams.md` | S2L1 04 |
| SELECT | `select-statement.md` | S2L1 05 |
| DISTINCT | `distinct-and-deduplication.md` | S2L1 06 |
| WHERE | `filtering-where.md` | S2L1 07, 08 |
| LIKE / pattern | `pattern-matching-sql.md` | S2L1 09 |
| IN / NOT IN | `in-and-not-in.md` | S2L1 10 |
| AS / ORDER BY | `column-aliasing-and-ordering.md` | S2L1 11, 12 |
| CASE WHEN | `conditional-expressions-sql.md` | S2L1 13 |
| NULL | `null-handling-sql.md` | S2L1 14 |
| Data types / CAST | `sql-data-types-and-casting.md` | S2L1 15, 16 |
| DDL/DML | `create-update-delete.md` | S2L1 17 |
| Lesson umbrella | `sql-fundamentals-overview.md` | S2L1 01 |
| **Sprint 2 Lesson 2: Computed Data** | | |
| COUNT | `count-and-countif.md` | S2L2 02 |
| SUM/AVG/MIN/MAX | `sum-avg-min-max.md` | S2L2 03 |
| SAFE_DIVIDE | `safe-divide.md` | S2L2 04 |
| GROUP BY | `group-by.md` | S2L2 05 |
| WHERE vs HAVING | `where-vs-having.md` | S2L2 06 |
| ROUND etc. | `numeric-functions-round.md` | S2L2 07 |
| CONCAT | `string-concatenation-concat.md` | S2L2 08 |
| REPLACE + CASE | `string-cleaning-replace-and-case.md` | S2L2 09, 10 |
| DATE arithmetic | `date-arithmetic-date-sub.md` | S2L2 11 |
| Lesson umbrella | `sql-computed-data-overview.md` | S2L2 01 |
| **Sprint 2 Lesson 3: JOINs + Testing** | | |
| JOIN fundamentals | `joins-fundamentals.md` | S2L3 01, 02, 03 |
| JOIN types | `join-types.md` | S2L3 04 |
| Multiple JOINs | `multiple-joins.md` | S2L3 05 |
| JOIN + GROUP BY | `joins-with-group-by.md` | S2L3 06 |
| Pitfalls | `join-pitfalls-grain-and-fan-out.md` | S2L3 07 |
| Testing motivation | `testing-data-pipelines.md` | S2L3 08 |
| PK test | `primary-key-test.md` | S2L3 09 |
| Column test | `column-test.md` | S2L3 10 |
| Value preservation test | `value-preservation-test.md` | S2L3 11 |
| **Statistics (separate domain)** | | |
| Descriptive statistics overview | `descriptive-statistics.md` | (separate raw source) |
| Central tendency | `measures-of-central-tendency.md` | (same) |
| Spread | `measures-of-spread.md` | (same) |

**Not yet ingested into wiki:** Sprint 1 (all 4 lessons, 45 videos), Sprint 2 Lessons 4–5 (11 videos), Sprint 3 Lesson 1 (13 videos). Total = 69 videos pending ingestion.

---

## 7. How to Use This Document with NotebookLM

When asking NotebookLM about the videos:

- **"What does video X teach?"** → NotebookLM will use its own transcript-derived understanding plus this document's lesson/topic context
- **"How does video X relate to video Y?"** → use the Cross-Cutting Concept Map (section 4) to reason about prerequisites and follow-ups
- **"What's the prerequisite for understanding this video?"** → look at the lesson it lives in and the sprint that came before
- **"Show me all videos about JOINs"** → Sprint 2 Lesson 3 Topics 3.1–3.2 (videos 01–07 of that lesson)
- **"What's the order to study?"** → follow Sprint 1 → 2 → 3, within each sprint follow lesson numbers, within each lesson follow topic numbers

If you want NotebookLM to also see the long-form wiki notes, upload the markdown files listed in section 6 in addition to this document.

---

## 8. Important Caveats

1. **Lesson 3 of Sprint 1 has a possibly duplicated clip ID:** the transcript "Müşteri Kazanım Hunisi" and "KPI Seçiminde Kaçınılması Gerekenler" share the same clip ID (1128686083) in the source — this is a likely typo in the syllabus; the actual videos may be different.
2. **Some videos in the syllabus are marked as "Videosu indi"/"indir"** (download manually) — these are present in the local archive and have been transcribed.
3. **Transcripts are AI-generated** (OpenAI gpt-4o-transcribe). Quality is high but some technical terms are phonetically misspelled (e.g., "SQL" → "eskiyel" in a few places).
4. **Sprint 3 is incomplete:** only 1 of 5 lessons has been held as of 11 May 2026. The remaining 4 lessons will add ~30–40 more videos when complete.
5. **Course platform:** all video URLs follow the pattern `https://nextgen.workintech.com.tr/lesson/{course_id}/{lesson_id}` — these are not public; the videos in NotebookLM are the local archive of the recordings.

---

## 9. Glossary (key terms used across the corpus)

| Turkish | English | Meaning |
|---------|---------|---------|
| Veri Analizi | Data Analysis | The discipline of extracting insight from data |
| Sorgu | Query | A SQL question against a database |
| Tablo | Table | A relational data store |
| Sütun | Column | A field in a table |
| Satır | Row | A record in a table |
| Birincil Anahtar | Primary Key (PK) | The column that uniquely identifies a row |
| Yabancı Anahtar | Foreign Key (FK) | A column that references another table's PK |
| Birleştirme | JOIN | Combining rows from multiple tables |
| Gruplandırma | Grouping (GROUP BY) | Aggregating rows by category |
| Süzme / Filtreleme | Filtering (WHERE / HAVING) | Restricting which rows participate |
| Aggregate / Toplama Fonksiyonu | Aggregate function | SUM, COUNT, AVG, MIN, MAX |
| Pencere Fonksiyonu | Window function | Aggregate that keeps row identity |
| KPI | Key Performance Indicator | A business metric tracked over time |
| Segmentasyon | Segmentation | Grouping customers by behavior |
| Cohort | Cohort | A group of customers with a shared start event |
| Veri Hattı | Data Pipeline | A multi-step data transformation flow |
| Veri Ambarı | Data Warehouse | An OLAP system for analytical queries |
| Görünüm | View | A saved query that behaves like a table |
| Bölümlendirme | Partitioning | Splitting a table by a column (often date) for cost |

---

## 10. Document Version

- **Created:** 11 May 2026
- **Total videos covered:** 108
- **Wiki pages cross-referenced:** 33 (Sprint 2 Lessons 1–3 fully ingested)
- **Ingestion status:** ~36% (39/108 videos turned into long-form wiki pages); remaining 69 videos are transcribed but not yet structured into wiki entries

For the flat per-video catalog with file paths and titles, see `_meta/notebooklm-video-catalog.md`.
