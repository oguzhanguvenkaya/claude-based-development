---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 01-joine-giris
video_file: videos/01-joine-giris.mp4
duration_seconds: 152
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:36Z
tags: [transcript, sprint-2]
---

# Joine giris

> Otomatik transkript — kaynak: `videos/01-joine-giris.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Joinler, tabloları birincil ve yabancı anahtarları üzerinden birbirine bağlamanı sağlar. Böylece ilişkili bilgileri tek, verimli bir veri setinde birleştirirsin. Üstelik veriyi çoğaltmana gerek kalmaz. Ben taze ürünler satan bir e-ticaret girişiminde veri analistiyim. Yöneticim sipariş verilerini alıcı ve ürün detayları ile birlikte hızlıca görmek istiyor. Verilerimiz üç tabloya dağılmış durumda. Products, Buyers ve Purchases. Burada joinler devreye giriyor. Bu tablolar arasındaki adeta birer köprü gibi çalışacak. Adım 1. Primary ve Foreign Key'leri bağla. Bizim örneğimizde Products tablosunda Products ID birincil anahtar, Purchases tablosundaki Purchases.Product ID ise bununla ilişkili yabancı anahtar. Buyers tablosunda Buyers.ID birincil anahtar, Purchases.Buyer ID ise bununla ilişkili yabancı anahtar. İkinci adım, ilk siparişin alıcı ve ürün detaylarına bakalım. Purchases tablosunun birinci satırı, Buyer ID 2, Product ID 1, Quantity 2, Date 2020-03-03. Buyers.ID 2 yani Clara, İtalya. Products.ID 1 yani Apple, fiyatı da 0.50. İki elmanın toplam fiyatı 1 dolar. Üçüncü adım, detayları birleştirelim. Joinler bir fermuar gibidir. ID'ler eşleştiğinde satırları hizalar. Böylece bilgiler birlikte hareket eder. Bu fermuar alıcı ve ürün bilgilerini her bir siparişe ekler. Yani Clara iki elma satın alıyor. Purchases tablosu sadece şunu söylüyor. Buyer 2, Product 1, Quantity 2. Böyle bakınca fazla anlamlı değil. Ama Buyers ve Products tablolarıyla join yaptığında tablo canlanıyor. Clara, İtalya'dan, birim fiyatı 0.50 euro olan iki elma almış. Toplam 1 euro. İşte fermuar etkisi bu. Metinler ve sayılar birleşip net bir hikayeye dönüşüyor. Özetle, SQL joinler normalize edilmiş tabloları birbirine bağlayarak veriyi çoğaltmadan paylaşmayı sağlar. Sonuç olarak aynı bilgiyi birden fazla tabloda saklama. Bunun yerine tablolar arasında köprü kurmak için join kullan. Gerektiğinde birleştir ve doğru esnek analizler oluştur.
