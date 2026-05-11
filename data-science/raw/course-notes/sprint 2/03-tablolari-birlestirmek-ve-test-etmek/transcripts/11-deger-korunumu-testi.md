---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 11-deger-korunumu-testi
video_file: videos/11-deger-korunumu-testi.mp4
duration_seconds: 145
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:58Z
tags: [transcript, sprint-2]
---

# Deger korunumu testi

> Otomatik transkript — kaynak: `videos/11-deger-korunumu-testi.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Her zaman, join işlemlerinin ana metrikleri koruduğundan emin olmalısın. Bunu da karşılaştırmalı toplamlarla test edebilirsin. Nimbus Commerz şirketinde çalışıyorsun. Finans ekibinin toplam shipping cost verisine ihtiyacı var. Senin görevin, orders ve shipping tablolarını birleştirmek ama bunu yaparken shipping cost toplamını değiştirmemek. Join işleminden önce ve sonra shipping cost değerini toplayarak herhangi bir istenmeyen tekrar veya veri kaybı olup olmadığını kolayca tespit edebilirsin. Toplam değişiyorsa ya veri tekrarı oluşmuştur ya da veri kaybı vardır. Adım 1. Başlangıç toplamını hesapla. Ölçülecek metrik shipping cost. Bu değerin toplamını doğrudan shipping fax tablosundan hesapla. Bu sonucu referans olarak yani başlangıç değeri olarak kaydet. Bu sorgu shipping tablosundaki toplam shipping cost değerini hesaplar. Adım 2. Join işleminden sonra tekrar topla. Orders tablosunu shipping fax ile order id üzerinden birleştir. Join sonrası shipping cost toplamını yeniden hesapla. Eğer bu toplam ilk hesapladığın değerle aynı değilse veriye çoğalmış ya da kaybolmuştur. Böyle bir durumda raporlamaya geçmeden önce durup sebebini araştırmalısın. Bu sorgu orders ve shipping tablolarını birleştirerek shipping cost toplamını kontrol eder. Adım 3. Toplamlar farklıysa veriye dön ve sorunu tespit et. Bazen bir siparişin birden fazla sevkiyatı olabilir ve bu da satırların çoğalmasına neden olur. Önce bir siparişin kaç sevkiyat kaydı olduğunu kontrol et. Bu sorgu her order id için kaç adet shipping kaydı olduğunu gösterir. Eğer aynı sipariş için birden fazla kayıt varsa veriyi doğru seviyede eşleştirmen gerekir. Join işleminden önce order id bazında shipping cost değerlerini toplayarak tekleştir. Ardından toplamı tekrar hesapla. Özetle, join işleminden önce ve sonra toplamları daima karşılaştır. Fark varsa ya veri çoğalmıştır ya da kaybolmuştur. Join seviyelerini doğru hizala. Toplamlar birebir eşleştiğinde raporlamayı güvenle yapabilirsin.
