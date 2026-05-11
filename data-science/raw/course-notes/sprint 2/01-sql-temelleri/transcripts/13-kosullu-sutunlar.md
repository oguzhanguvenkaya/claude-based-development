---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 13-kosullu-sutunlar
video_file: videos/13-kosullu-sutunlar.mp4
duration_seconds: 105
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:05Z
tags: [transcript, sprint-2]
---

# Kosullu sutunlar

> Otomatik transkript — kaynak: `videos/13-kosullu-sutunlar.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

IF ve CASE WHEN ifadeleriyle verilerimize biraz mantık ekleyelim. Diyelim ki bir satış raporu üzerinde çalışıyorsun ve yöneticin şöyle diyor. Yüksek değerli siparişleri işaretleyebilir misin? Verinin kendisinde böyle bir sütun yok ama SQL bunu IF ifadesiyle anlık olarak oluşturmanı sağlar. Şöyle görünür. Bu sorgu tutarı 100'ün üzerinde olan siparişleri HIGH, diğerlerini LOW olarak etiketler. Bu sorgu her siparişi kontrol eder. Tutar 100'den büyükse HIGH, değilse LOW olarak etiketler. Yani içinde mantık barındıran yeni bir sütun yaratmış oluyorsun. Peki iki kategoriden fazlasına ihtiyacın olduğunda ne olacak? İşte o zaman CASE WHEN en iyi yardımcın olur. Örneğin, bu sorgu siparişleri tutar eşiklerine göre premium, high veya standart kategorilerine ayırır. Burada birden fazla kural tanımlayabilirsin. 500 üstü siparişler premium, 100 üzeri olanlar high, diğerleri ise standart olur. IF ifadesini basit bir ışık düğmesi gibi düşün. Sadece iki sonuç, açık ya da kapalı. CASE WHEN ise trafik lambası gibidir. Kırmızı, sarı, yeşil gibi birden fazla koşula göre değişir. En büyük avantajı şu, verinin kendisini değiştirmeden raporunda görünümünü şekillendirebilirsin. Yani tabloya yeni bir sütun eklemiyorsun. Sadece o anda dinamik olarak oluşturuyorsun. Bu yüzden yöneticin senden veride henüz olmayan kategori veya koşullar istediğinde, bunu gerçekleştirmenin yolu IF ve CASE WHEN kullanmaktır. Ana fikir, verilerini şartlara göre sınıflandırmak istiyorsan, IF iki seçenek için, CASE WHEN ise çoklu durumlar için en uygun çözümdür.
