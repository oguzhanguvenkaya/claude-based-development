---
sprint: 2
lesson_slug: 04-subquery-ve-with-as
video_slug: 02-ic-ice-query-nested-query
video_file: videos/02-ic-ice-query-nested-query.mp4
duration_seconds: 139
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:05Z
tags: [transcript, sprint-2]
---

# Ic ice query nested query

> Otomatik transkript — kaynak: `videos/02-ic-ice-query-nested-query.mp4` (ders: Subquery Ve With As). Düzeltmeler için video referans alınmalıdır.

İçiçe alt sorgular yani nested subqueries, bir tabloyu başka bir tablonun sonucuna göre filtrelememizi sağlar. Diyelim ki bir yemek teslimatı girişiminde veri analistisiniz. Pazarlama, Happy Hour promosyonunu yeni çalıştırdı. Yöneticin senden Happy Hour kodunu kullanan siparişlerle ilişkili satışları göstermenizi istedi. Yani Sales tablosunu, Orders tablosundaki promosyon kodu Happy Hour olan siparişlerin kimliklerine göre filtreleyeceğiz. Bunu yapmak için Where ifadesinde bir alt sorgu kullanacağız. İlk adım, ana sorguyu başlat. Bizim durumumuzda ana sorgunun tablosu Sales tablosu. Çünkü almak istediğimiz satış bilgileri aslen bu tabloda. Sales tablosundan üç sütun seçeceğiz. Order ID, Margin ve Turnover. Margin ve Turnover'ı satış bilgileri için seçiyoruz. Order ID'yi ise Order tablosundan filtreleme yapacağımız için. İkinci adım, ana sorguya bir Where filtresi ekle. Ana sorgudan dönen Order ID'yi kullanarak Where filtresi yazıyoruz. Bu In operatörü, bu Order ID'lerin alt sorgunun döndürdüğü liste içinde olup olmadığını kontrol edecek. Son adım, alt sorguyu oluştur. Burada Orders tablosunu kullanacağız çünkü filtreleme yapacağımız promosyon kodu sütunu bu tabloda. Alt sorguda Orders tablosundaki promosyon kodu Happy Hour olan kayıtların Order ID değerlerini getiriyoruz. Son haliyle iç sorgu, Happy Hour promosyonuna sahip Order ID değerlerinden kısa bir liste oluşturur. Dış sorgu ise Order ID'si bu listedeki değerlerle eşleşen satışları alır. Sonuç olarak Sales tablosundaki yalnızca Happy Hour siparişlerine ait satırlar listelenir. İşte alt sorgu oluşturmak bu kadar kolay. Fakat bunu yaparken aklında tutman gereken bazı önemli faktörler var. Alt sorguları daha küçük ve hedefli filtrelerde kullanman daha uygundur. Mantık katmanları arttıkça okumak güçleşir. Eğer filtre sayısı, toplama işlemleri ya da karmaşık koşullar artıyorsa, anlaşılır olması için Join ya da Exist yapısını tercih etmelisin. Birden fazla iç içe alt sorguyu üst üste yazmamaya dikkat et. Çünkü kodun okunabilirliği çok hızlı düşer. Eğer çok adımlı bir mantık kurman gerekiyorsa yine Join kullanman daha iyi olur.
