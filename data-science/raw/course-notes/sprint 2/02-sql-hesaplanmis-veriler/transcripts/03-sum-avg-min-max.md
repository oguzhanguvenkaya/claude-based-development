---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 03-sum-avg-min-max
video_file: videos/03-sum-avg-min-max.mp4
duration_seconds: 147
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:18Z
tags: [transcript, sprint-2]
---

# Sum avg min max

> Otomatik transkript — kaynak: `videos/03-sum-avg-min-max.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

SQL'in toplama fonksiyonları yani sum, min, max ve avg gibi aggregate fonksiyonlarını kullanarak toplamlar, minimum ve maksimum değerleri doğrudan sorguların içinde hızlıca hesaplayabilirsin. Giriş. Sen bir abonelik uygulamasında veri analisti olarak çalışıyorsun. Ürün yöneticin sana şöyle soruyor. Toplam harcamamız ne kadar? En küçük ve en büyük siparişimiz hangisi? Ve ortalama sipariş tutarımız nedir? Bunları ürün bazında da görebilir miyiz? Bu soruya SQL'in özetleme makinesi yani aggregate fonksiyonlarla birkaç dakika içinde yanıt verebilirsin. Yöntem. Tek bir tablo kullanacağız. Purchases, Order ID, User ID, Product ID, Spend, Quantity, Purchase Date. Önce genel toplamları bulacağız, ardından ürün bazlı özetlere ve birkaç özel hesaplamaya geçeceğiz. Adım 1. Stamp. Toplam harcama. Select, Sum, Spend as Total Spend from Purchases. Örnek sonuç. 45.0. 0. kısma genelde sonuç float tipinde olduğu için görünür. Adım 2. Min ve Max. En küçük ve en büyük sipariş. Select, Min Spend as Min Spend, Max Spend as Max Spend, Min Quantity as Min Quantity. Bu sorgu sipariş bazında en düşük ve en yüksek harcamayı ve en küçük sipariş adetini döndürür. Adım 3. AVG ve İfadeler. Ortalama ve özel metrikler. AVG fonksiyonu aslında şunla eşdeğerdir. Sum Spend bölü Count Spend. Select, AVG Spend as AVG Spend from Purchases. Özel ifadelerse kendi metriklerini oluşturmanı sağlar. Yani analizlerin tarif defteri gibi düşün. Select, Max Spend eksi Min Spend as Spend Range, Min Spend bölü Null If Max Spend 0 as Min to Max Ratio. Burada toplam harcama aralığını ve minimumdan maksimuma oranı hesaplıyoruz. Hatırlatıcı, Aggregate fonksiyonlarını bir pivot tablo özetleme makinesi gibi düşünebilirsin. Özetle, Sum, Min, Max ve AVG fonksiyonlarıyla verinin genel durumunu birkaç satırlık SQL koduyla çıkartabilirsin.
