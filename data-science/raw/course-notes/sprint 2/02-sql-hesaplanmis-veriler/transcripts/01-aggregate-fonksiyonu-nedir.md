---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 01-aggregate-fonksiyonu-nedir
video_file: videos/01-aggregate-fonksiyonu-nedir.mp4
duration_seconds: 223
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:16Z
tags: [transcript, sprint-2]
---

# Aggregate fonksiyonu nedir

> Otomatik transkript — kaynak: `videos/01-aggregate-fonksiyonu-nedir.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Aggregate fonksiyonu nedir? Temel fikir şu: Aggregate fonksiyon, çok sayıda satırı tek bir temsilci değere indirger. Mesela toplam, adet ya da ortalama gibi. Ama bu özetin doğru olması için verinin temiz, benzersiz ve eksiksiz olması gerekir. Senaryo: FreshCart adında çevrim içi bir markette yeni başlayan bir veri analistisiniz. Finans ekibi sizden şunu istiyor: Bu hafta ürün bazında toplam harcamamız ne kadar ve sipariş başına ortalama miktar nedir? Oldukça basit görünüyor. Tek yapmanız gereken veriyi aggregate etmek. Ancak Purchases tablonuz oldukça karışık. Tablodaki alanlar şöyle: ID, Buyer Name, Date, Product, Fruit, Quantity ve Spend. Şöyle bir adım yapalım şimdi. Adım 1: Aggregate Denemesi. Hızlıca bir pivot oluşturuyorsunuz. Pivot Table aslında bir özetleme makinası gibidir. Rows, Product, Values, Sum of Spend, Average of Quantity. Ya da formüllerle. Toplam harcama, is equal to, Sum, F2 til F. Sadece per ürünü için, is equal to, Sum F, F2F, E2E. Sonuçlar fena görünmüyor. Ta ki Buyer yani alıcı bazında denediğiniz ana kadar. Birden fazla Pole ve Julie görüyorsunuz. Bir satırda tarih bile eksik. Buyer'a ve güne göre toplamlar artık güvenilir görünmüyor. Adım 2: Neden hata verdiğini fark et. İsimler benzersiz değil. Pole ismiyle muz alan kişi, aynı isimde ama armut alan farklı bir kişi olabilir. Yani Sum by Name yaptığınızda veriler karışıyor. Temmuz 11'de iki ayrı Per satırı görmek, aynı Pole'un toplam 6 armutu iki işlemle alması da olabilir. İki farklı Pole'un ayrı siparişleridir. Eksik tarih, pivot içinde blank satırına gider ve bu da gün veya hafta bazında yaptığınız toplamları bozar. Kısaca özetleyelim. Aggregate bir blender gibidir. Birçok satırı tek bir smoothieye dönüştürür. Ama içine yanlış etiketli ya da eksik veri atarsanız o smoothienin tadı yani analiziniz hatalı olur. Adım 3: Eksiklikleri ve tutarsızlıkları düzelt. Eksik tarihleri doldurun. Boşlukları engellemek için data validation kullanın. Ürün isimlerini standartlaştırın. Pear ve Pears gibi. Data, Data Cleanup, Trim White Space ve Product alanı için doğrulama listesi oluşturun. Sayıların metin değil sayı formatında olduğundan emin olun. Is equal to value F2 till F. Artık aggregate'leri yeniden çalıştırın. Pivot'ta Rows, Product, Values, Sum of Spend, Average of Quantity. Eğer Buyer yapmak istiyorsanız Buyer Name yerine Buyer ID kullanmalısınız. Gerekirse Count of Orders ile Count Unique of ID plus Date karşılaştırması yaparak çift sayımları önden yakalayabilirsiniz. Artık ürün ve müşteri bazında toplamlarınız istikrarlı, anlamlı ve savunulabilir hale gelir. Analojiler. Aggregate Function, Blender veya Özetleyici. Birçok satırı tek bir değere dönüştürür. Pivot Table, Özet makinası, alanları sürük özetleri çıkar. Ana fikir. Aggregate Function verinizi özetler ama doğru özet ancak temiz, eksiksiz ve benzersiz veriyle mümkündür.
