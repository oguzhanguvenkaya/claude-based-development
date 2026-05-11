---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 02-count-countif
video_file: videos/02-count-countif.mp4
duration_seconds: 216
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:17Z
tags: [transcript, sprint-2]
---

# Count countif

> Otomatik transkript — kaynak: `videos/02-count-countif.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

BigQuery'nin COUNT ve COUNTIF fonksiyonları, veri sayımı için temel araçlardır. Null olmayan değerleri, benzersiz girdileri, toplam satırları veya belli bir koşulu sağlayan satırları saymak için kullanılırlar. Yani farklı kontrol noktalarına yerleştirilmiş tıklama sayaçları gibi düşünebilirsin. Bir e-ticaret pazar yerinde veri analistiyim. Müdürüm bana şunları soruyor. Kaç adet buyer kaydımız var? Kaç farklı buyer var? Eksik tarih bilgisi olan kayıt var mı? Kaç siparişte kuantiti üçten büyük? Ve özel olarak Julie için büyük siparişlerinden kaç tane var? Yöntem. Adım 1. Buyer kayıtlarını say. Amaç, kaç satırda buyer bilgisi gerçekten dolu, bunu bulmak. COUNT BUYER, null değerleri yok sayar, yalnızca buyer değeri dolu satırları sayar. SELECT COUNT BUYER AS COUNT FROM PURCHASES Örnek 10. Not, bu sayı benzersiz alıcıları değil, sadece null olmayan kayıtları gösterir. Adım 2. Benzersiz buyer sayısını bul. Amaç, kaç tane eşsiz buyer var? COUNT DISTINCT BUYER ifadesi, tekrarsız ve null olmayan değerleri sayar. SELECT COUNT DISTINCT BUYERS AS UNIQUE BUYERS FROM PURCHASES Adım 3. Null olmayan tarihleri say. Amaç, eksik tarihleri tespit etmek. COUNT DATE, yalnızca tarih değerine sahip satırları sayar. Eğer bir satırda tarih null ise sayılmaz. SELECT COUNT DATE AS COUNT FROM PURCHASES Örnek, bir satırda null tarih varsa sonuç 9 döner. Adım 4. Toplam satır sayısını bul. Null dahil. Amaç, tablo içindeki tüm satırların toplamını bulmak. COUNT STAR, her satırı sayar. Null olsa bile. SELECT COUNT STAR AS TOTAL ROWS FROM PURCHASES Örnek, 10 satır döner. Adım 5. COUNT IF ile koşullu sayım. Amaç, belirli bir koşulu sağlayan satırları saymak. BigQuery söz dizimi COUNT IF koşul. SELECT COUNT IF QUANTITY BÜYÜK 3 AS COUNT FROM PURCHASES Örnek sonuç 5. QUANTITY 3'den büyük olan 5 satır. Koşulları birleştirebilirsin. COUNT IF QUANTITY BÜYÜK 3 OR BUYER JULIE COUNT IF BUYER JULIE COUNT IF BUYER JULIE AND QUANTITY BÜYÜK 3 Örnekler. COUNT IF BUYER JULIE, Julie'nin tüm siparişleri örneğin 4. COUNT IF BUYER JULIE AND QUANTITY BÜYÜK 3, Julie'nin büyük siparişleri örneğin 2. NOT. Eşleşmeler birebir olmalı. Julie, Juliet ile eşleşmez. Büyük küçük harf duyarsız karşılaştırma için LOWER BUYER eşittir Julie ifadesini kullanmalısın. BENZETME. Sayım kapısı. COUNT STAR, kapıdan geçen herkesin sayımı, her satır. COUNT KALIM, formda ismini yazanların sayısı, null olmayanlar. COUNT DISTINCT KALIM, tekil kimlik kartlarına sahip kişiler, tekrarsız. COUNT IF KOŞUL, mavi şapka takanlar, koşula bağlı sayım. Özetle, COUNT ve COUNT IF fonksiyonları, verini farklı açılardan saymanı sağlar. İster toplam, ister benzersiz, ister belirli koşula göre.
