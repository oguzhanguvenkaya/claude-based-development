---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 05-coklu-join-islemleri
video_file: videos/05-coklu-join-islemleri.mp4
duration_seconds: 170
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:45Z
tags: [transcript, sprint-2]
---

# Coklu join islemleri

> Otomatik transkript — kaynak: `videos/05-coklu-join-islemleri.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Birden fazla join kullanmak, dağılmış bilgileri, örneğin siparişler, alıcılar ve ürünleri, tek bir bütün tabloya getirir. Böylece hem yinelenen verileri hem de karışıklığı önlemiş olursun. Bir perakende pazar yerinde yeni başlayan bir veri analisti olarak, yöneticin senden her bir satın alımı içeren temiz bir rapor ister. Ne satın alındığı, kim satın aldı ve fiyatı neydi? Bu rapor için üç tabloyu join etmen gerekir. Adım 1. Hedefi belirle ve anahtar eşleşmelerini çıkar. Hedef alanlar, sipariş tablosundan Purchase ID, Quantity, Date, ürün tablosundan Product Name, Product Price ve alıcı tablosundan First Name, Surname ve Country. Bu üç tablo arasında foreign keyleri eşle. Purchases.buyerid, buyers.buyerid ile. Purchases.productid ise products.productid ile eşleşir. Hızlı kontrol, buyerid ve productid doğru foreign key mi? Yanlışlıkla p.id eşittir b.id gibi birleştirirsen, hatalı eşleşmeler ya da sıfır satır döndürürsün. On koşulunda buyerid ve productid'yi kullandığından emin ol. Adım 2. Alias ve nitelikli sütunlarla joinleri kur. Tabloyu inner join ile bağla, kısa bir alias, takma adı ver, on koşulunda doğru eşleşmeyi tanımla. Adım 3. Karışıklıkları önle ve doğrula. Birden fazla tabloda aynı isimde sütun varsa, mutlaka takma isimle birlikte yaz. Örneğin, name sütunu hem buyers hem products tablosunda varsa, bu sütunu seçerken select name demek yerine select products.name ya da takma ad kullanarak prod.name diyebiliriz. Aksi halde ambiguous kalım hatası alırız. Bu sorguyu çalıştırdığında bir daily sales yani günlük satış tablosu oluşturursun. Purchases temel tablo olur, buyers ve products tablolarından gelen bilgilerle zenginleşir. Her sütun açıkça etiketlenmiştir, karışıklık yoktur. Birden fazla join kullanmak, tren vagonlarını birbirine bağlamak gibidir. Purchases lokomotif, buyers ve products ise arkasına eklediğin vagonlardır. Her on ifadesi de bu vagonları birbirine kilitleyen bağlantıdır. Özetle, temel tablo olarak purchases'tan başla, inner joinlerle buyers ve products tablolarını doğru foreign keylerle birbirine bağla. Sütunları, alias ve nitelendirmelerle netleştir, böylece her satın alım için tek bir doğru satır elde edersin. Birden fazla inner join kullanmak, doğru anahtarlar, net alias'lar ve nitelikli sütun adlarıyla yapıldığında güvenli ve güçlüdür. Bu sayede analiz için hazır, temiz ve karışıklık içermeyen bir veri kümesi elde etmiş olursun.
