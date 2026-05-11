---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 06-join-ve-group-by
video_file: videos/06-join-ve-group-by.mp4
duration_seconds: 137
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:47Z
tags: [transcript, sprint-2]
---

# Join ve group by

> Otomatik transkript — kaynak: `videos/06-join-ve-group-by.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Join ile groupby kullanırken en sık yapılan hatalardan biri, gruplanmayan sütunları select içinde kullanmaktır. Elimizde 3 tablo var. Purchases, Products ve Buyers. Bu tabloları birleştirip hangi kullanıcının hangi üründen ne kadar aldığını görmek istiyoruz. Önce tabloları join ile birleştirelim. Ana tabloyu Purchases olarak alıp Product ID ve Buyer ID sütunlarından joinleri kuruyoruz. Purchases tablosundan ID, Buyer ID, Quantity ve Date, Products tablosundan Name ve Price ve son olarak Buyers tablosundan Name sütunlarını alıyoruz. Buraya kadar her şey doğru. Bu sorgu bize tüm satın alımları detaylı şekilde verir. Şimdi diyelim ki bu veriyi özetlemek istiyoruz. Yani her kullanıcı için her üründen toplam ne kadar alındığını görmek istiyoruz. Bunun için Buyers.Name ve Products.Name sütunlarıyla bir grupby ekleyelim. Bu sorgu hata verecektir. Peki neden? Çünkü grupby ile şunu diyoruz. Bu satırları Buyer Name ve Product Name'e göre grupla. Yani aynı alıcı ve ürünü tek bir satıra indir. Aynı kullanıcı aynı üründen birden fazla kez satın almış olabilir. Grupby yaptıktan sonra bu tek satır olur. Şimdi sorun şu. Bu tek satır için Quantity kaç olacak? Bir mi? İki mi? SQL burada karar veremez. Çünkü birden fazla değer var. Ama sen tek satıra indirgemek istiyorsun. Quantity değerini burada toplayıp gösterseydik bu sorun olmazdı. Bu yüzden grupby kullandığımızda SQL bizden şunu ister. Select içinde kullandığımız her sütun ya grupby içinde olmalı ya da bir aggregate fonksiyonu ile kullanılmalıdır. Bizim sorgumuzdaysa ID, Quantity, Date, Price gibi sütunlar ne gruplanmış ne de özetlenmiş durumda. Bu problemi veriyi gerçekten özetleyerek çözelim. Yani detay satırları yerine anlamlı bir sonuç üreteceğiz. Şöyle düzeltelim. Buyers.name ve products.name ile grupladık ve purchase.quantity için sum kullanarak toplama aldık. Artık her grup için tek bir değer var. SQL ne alacağını biliyor. Özetle, groupby kullanıyorsan select içindeki her alan kontrol edilmelidir. Ya groupby'da olmalı ya da sum, count gibi bir fonksiyonla özetlenmelidir. Aksi halde SQL hangi değeri seçeceğini bilemez ve hata verir.
