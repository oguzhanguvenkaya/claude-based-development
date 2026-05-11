---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 12-order-by-ile-siralama
video_file: videos/12-order-by-ile-siralama.mp4
duration_seconds: 117
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:05Z
tags: [transcript, sprint-2]
---

# Order by ile siralama

> Otomatik transkript — kaynak: `videos/12-order-by-ile-siralama.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Son olarak, sonuçları düzenli bir şekilde sıralamayı Order By ifadesiyle öğrenelim. Diyelim ki yöneticin şöyle diyor: Müşteri listesini gönderir misin ama soyadına göre sıralanmış olsun. Şu anda SQL satırları belirli bir sırada döndürmez. Sonuçların sırasını kontrol etmek için Order By kullanmalısın. Temel yazımı şöyle: Bu sorgu, sonuçları soyadına göre artan şekilde sıralar. Varsayılan olarak SQL artan şekilde sıralar A'dan Z'ye, 0'dan 9'a. Tersine sıralamak istersen, desk eklemen yeterli. Bu ifade sıralamayı soyadına göre azalan yapar. Bu şekilde sonuçlar Z'den A'ya gelir. Sayısal değerleri de sıralayabilirsin, örneğin sipariş tutarlarına göre. Bu sorgu, siparişleri tutara göre azalan biçimde sıralar ve en yüksek tutarları üste getirir. Bu, en çok harcama yapanları en üste gösterir. İş dünyasında sık istenen bir rapor türüdür. Ayrıca tek bir sütunla sınırlı değilsin. Yöneticin şöyle de diyebilir: Şehre göre sırala, her şehir içinde de soyadına göre. Bu ifade, önce şehre göre, her şehir içinde de soyadına göre sıralar. Bir kısa yolda var. Sıralamayı Select listesindeki sütunun konumuna göre yapabilirsin. Örneğin, Order By 2 ifadesi seçilen ikinci sütuna göre sıralama yapar. Ama dikkatli olmalısın. Genellikle sütun takma adlarını ya da açık isimleri kullanmak daha net ve güvenlidir. Order By'ı bir tomar kağıdı düzenlemek gibi düşün. Kullanmazsan kağıtlar karışık bir halde durur. Kullanırsan harp sırasına, tarihe ya da değere göre düzenleyebilirsin. Rapor için hangisi mantıklıysa. Ana fikir, Order By sonuçların sırasını tamamen senin kontrol etmeni sağlar.
