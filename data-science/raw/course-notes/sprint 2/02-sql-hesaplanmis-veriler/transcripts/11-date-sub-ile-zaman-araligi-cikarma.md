---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 11-date-sub-ile-zaman-araligi-cikarma
video_file: videos/11-date-sub-ile-zaman-araligi-cikarma.mp4
duration_seconds: 84
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:33Z
tags: [transcript, sprint-2]
---

# Date sub ile zaman araligi cikarma

> Otomatik transkript — kaynak: `videos/11-date-sub-ile-zaman-araligi-cikarma.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Date Sub, SQL içinde takvim geri sarma tuşudur. Bir tarihten gün, ay veya yıl çıkararak geçmiş tarihleri hesaplar ve referans tarihe göre filtrelersin. Pazarlama ekibi 2020-06-20 için kampanya planlıyor. Promodan önceki 5 gün içindeki alışverişleri göster. Her siparişin tarihinden 5 gün eksiğini de görüntüle. Adım 1. Kalıbı tanı. Söz dizimi Date Sub, Date Value or Column, Interval, N, Day, Month, Year. Adım 2. Kaydırılmış tarihi seç ve alias kullan. Bu sorgu Purchase Date ve 5 gün öncesini birlikte listeler. Örnek, Purchase Date 2021-06-03 ise, 5 days before 2021-05-29 olur. Adım 3. Referans tarihe göre filtrele. Bu sorgu 20 Haziran 2020'nin 5 gün öncesi ve sonrası için alışveriş kayıtlarını getirir. Hızlı Pratik, 30 günlük hareketli pencere. Bu sorgu son 30 gün içindeki alışverişleri seçer. Benzetme, Date Sub, zaman çizelgen için geri sarma tuşu gibidir. Özetle, Date Sub, tarih tabanlı analizlerde geçmiş aralıkları hesaplamak ve esnek filtreleme yapmak için idealdir.
