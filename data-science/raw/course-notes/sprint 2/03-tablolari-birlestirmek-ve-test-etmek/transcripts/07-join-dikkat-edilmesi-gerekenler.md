---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 07-join-dikkat-edilmesi-gerekenler
video_file: videos/07-join-dikkat-edilmesi-gerekenler.mp4
duration_seconds: 163
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:51Z
tags: [transcript, sprint-2]
---

# Join dikkat edilmesi gerekenler

> Otomatik transkript — kaynak: `videos/07-join-dikkat-edilmesi-gerekenler.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Tabloları join ederken, önce aynı detay seviyesinde yani aynı grain toplama düzeyinde olduklarından emin olmalısın. Sonra da doğru join türünü seçmelisin. Hızla büyüyen bir e-ticaret markasında veri analisti olarak çalışıyorsun. Müdürün senden hızlı bir sipariş bazında kar raporu istiyor. Eğer yanlış join türünü seçersen, fark etmeden kayıtları çoğaltabilir veya bazılarını düşürebilirsin. Bu da kar hesaplarını tamamen bozabilir. Birinci bölüm hatalı join. İki tablon var. Sales, Operations bu iki tabloyu Orders ID üzerinden join edip toplamları alıyorsun. Görüntüde her şey düzgün gibi ama kargo maliyeti şişmiş durumda. Her satır bazında tekrarlanıyor. Adım 1. Grain'i belirle. Grain yani satır başına şey kavramını tanımla. Bu tablo bir satırda ürün mü, sipariş mi yoksa müşteri mi tutuyor? Sorguda bu bilgiyi yorum satırı olarak belirt. Adım 2. Join öncesi hızlı kontroller. Join yapmadan önce satır sayılarını ve Distinct Key'leri karşılaştır. Şunu çalıştırmalısın. Bu iki sorgu Sales ve Operational tablolarındaki toplam satır sayısını ve benzersiz Orders ID sayısını hesaplar. Eğer Sales tablosu daha fazla satır içeriyorsa büyük ihtimalle Many to One bir join yapıyorsun demektir. Bu durumda toplam almada dikkatli olmalısın. Örnek hatalı join sorgusu. Farklı grain seviyelerini birleştirip sonra da toplam almak kargo bilgisini şişiriyor. Bu sorgu neden hatalı? Çünkü ShipCost sipariş seviyesinde bir alan yani sipariş başına bir satır ama join sonrası her ürün satırıyla tekrarlanıyor. Sonra SUM bu değeri katlıyor. Adım 3. Grainleri hizalayarak düzelt. Bunun yerine önce Sales tablosunu sipariş bazında her sipariş için tek satır olacak şekilde özetle. Şimdi bu sipariş seviyesindeki tabloyu zaten sipariş seviyesinde olan Operations ile join et. Adım 4. Doğru join türünü seç kayıp sipariş olmasın. Tüm Operations kayıtlarını korumak için Left Join kullanmalısın. Bu şekilde tüm siparişler korunur. Özetle, join yapmadan önce grain düzeyini hizalamak ve doğru join türünü seçmek küçük veri hatalarının büyük iş hatalarına dönüşmesini engeller.
