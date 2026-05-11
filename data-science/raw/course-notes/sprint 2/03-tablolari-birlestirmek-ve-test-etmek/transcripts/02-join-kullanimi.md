---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 02-join-kullanimi
video_file: videos/02-join-kullanimi.mp4
duration_seconds: 149
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:40Z
tags: [transcript, sprint-2]
---

# Join kullanimi

> Otomatik transkript — kaynak: `videos/02-join-kullanimi.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

JOIN nasıl kullanılır? SQL'de ilişkili tabloları birleştirirken SELECT ifadesine JOIN ve bir ON koşulu ekleriz. Bu koşul bir tablodaki birincil anahtar ile diğer tablodaki yabancı anahtarı eşleştirir. Diyelim ki Products ve Purchases tablolarını birleştirmek istiyoruz. Purchases tablosunda her sipariş satırı için ID, Product ID ve Quantity sütunu var. Products tablosunda ise her ürün için ID, Name ve Price sütunu var. Satış tablosuna bakarken her satırda ilgili ürünün adını ve fiyatını da görmek için bu iki tabloyu birleştirmeliyiz. Bunu üç adımda yapalım. İlk adım, ana tabloyu belirle. Burada SELECT uygulamak istediğimiz tablo hangisi? Analiz etmek istediğimiz asıl veri satın alımlar olduğu için Purchases tablosu. Basit bir SELECT ifadesi yazalım. Ana tablodan istediğimiz satırları ekleyelim. Burada bir noktaya dikkat, sütunları yazarken tablo ismi belirtmeliyiz. Çünkü bu sorguda birleştirmeden dolayı iki tablo kullanacağız. Hangi sütunun hangi tablodan geleceğini belirtmemiz gerek. İkinci adım, JOIN aşaması. Ana tabloyu birleştirmek istediğim tablo olan Products ile JOIN Products diyerek birleştiriyorum. Üçüncü ve en önemli adım, ON koşulu belirleme. Bu iki tabloyu birleştirirken satırları nasıl eşleştireceğiz? Burada ihtiyacım olan iki tablo arasında ilişki kurabileceğim bir anahtar. Products tablosundaki Primary Key olan ID ile Purchases tablosundaki Foreign Key olan Product ID değerlerini birebir eşleştirebilirim. Böylece her bir sipariş satırı için Product ID değeri, Products tablosundaki ID ile eşleşir. Son olarak birleştirdiğimiz tablodan görmek istediğimiz sütunları da tablo ismi belirterek sorguya ekliyoruz. Sorgu son haliyle Purchases ve Products tablosunu Product ID üzerinden birleştirip Purchases tablosundan ID ve Quantity, Products tablosundan ise Name ve Price sütunlarını alıyor, sonucu tek bir tabloda temiz bir şekilde gösteriyor.
