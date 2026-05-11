---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 08-diger-anahtar-kelimelerle-filtreleme
video_file: videos/08-diger-anahtar-kelimelerle-filtreleme.mp4
duration_seconds: 138
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:59Z
tags: [transcript, sprint-2]
---

# Diger anahtar kelimelerle filtreleme

> Otomatik transkript — kaynak: `videos/08-diger-anahtar-kelimelerle-filtreleme.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi between, and, or ve not kullanarak daha esnek filtreleme yapmayı öğrenelim. Perakende sektöründe veri analisti olarak çalıştığını düşün. Müdürün senden bir tarih aralığına bakmanı istiyor. 1 Ocak ile 31 Ocak arasında verilen siparişleri göster. İşte burada between ifadesini kullanmalısın. Bu sorgu, 1 Ocak ile 31 Ocak tarihleri arasındaki siparişleri listeler. Sonra şöyle diyor, Boston dışındaki herkesi göster. Burada, dyt veya küçük tür devreye giriyor. Bu sorgu, şehir değeri Boston olmayan müşterileri getirir. Tarih ve zaman damgaları da sayılar gibi işler. Yani küçük tür, büyük tür ya da between ile kıyaslama yapılabilir. Sonra şunu istiyor, New York'taki ve harcaması yüzden fazla olan müşterileri göster. Bu durumda koşulları and ile birleştirirsin. Bu sorgu, New York şehrindeki ve harcaması yüzden fazla olan müşterileri listeler. Ya da şöyle der, New York veya Boston'daki müşterileri göster. O zaman sorgu şöyle olur. Bu sorgu, şehir değeri New York veya Boston olan müşterileri getirir. Tam tersini yapmak istersen, not ekleyebilirsin. Bu sorgu, şehir değeri Boston olmayan müşterileri listeler. Parantezler ise mantığın net biçimde kontrol etmene yarar. Bu sorgu, New York veya Boston'da olup harcaması yüzden fazla olan müşterileri gösterir. Özetle, where senin filtre kapındır. Bir satırı içeri almadan önce koşulları kontrol eder. Eşitlik, eşitsizlik, aralıklar, tarih karşılaştırmaları ve mantıksal operatörler sadece farklı kimlik kontrolleridir. Bunları ustalaşarak kullanırsan, müdürünün sana yönelttiği neredeyse her hedefli soruya yanıt verebilirsin. Önemli ipucu, her anahtar kelimeyi ezberlemeye vakit harcama. Yapay zekaya şöyle sorabilirsin. SQL siyalde 1 Ocak ile 31 Ocak arasında verilen siparişleri nasıl çekebilirim? AI sana söz dizimini verir ve iş tamamdır. Ana fikir, where ifadesiyle filtrelemeyi ve mantıksal bağlaçları birlikte kullanmak, veriden doğru kitleyi çekmenin temel yoludur.
