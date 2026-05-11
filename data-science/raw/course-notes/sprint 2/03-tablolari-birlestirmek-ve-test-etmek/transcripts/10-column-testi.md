---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 10-column-testi
video_file: videos/10-column-testi.mp4
duration_seconds: 144
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:56Z
tags: [transcript, sprint-2]
---

# Column testi

> Otomatik transkript — kaynak: `videos/10-column-testi.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Veri kalitesini korumak için yapabileceğin bir diğer test ise sütun testidir. Bir veri tablosunu büyük bir bina gibi düşün. Her sütun, bu binayı taşıyan beton direklerden biridir. Binanın dışı güzel görünse bile, eğer direklerden biri çatlamışsa, yani sütun verilerinden biri hatalıysa, tüm yapı tehlikededir. Sütunlardaki nal ve aralık dışı değerleri erken fark etmek için basit SQL kontrolleri oluşturmalısın. Örneğin, bu sorgu, harcama değeri sıfır veya nal olan satırları bulur. Hazırladığın rapor sonucu, kampanya sonuçlarını veri ambarına yükleyeceksin. Bunu yapmadan önce kontrol etmen gereken bir şey var. Spent sütununun her zaman pozitif sayı olması gerekiyor. Bu sütundaki herhangi bir nal, sıfır ya da negatif değer raporları bozar ve metrikleri yanlış gösterir. Adım 1. Kuralı belirle. Sütun, spent. Kural, tüm değerler pozitif olmalı. Nal, sıfır veya negatif değerler bu kuralı ihlal eder. Adım 2. İhlal sorgusunu yaz. Amacın hatalı satırları bulmak. Doğru satırları doğrulamak değil. Eğer yazdığımız sorgu herhangi bir satır döndürüyorsa, bir sorun var demektir. Adım 3. Gözden geçir ve harekete geç. Eğer sorgu satır döndürürse, ya kaynak veriyi ya da veri akışını düzeltmelisin. Sorun çözülene kadar raporları şu şekilde filtreleyebilirsin. Bu filtre yalnızca pozitif harcama değerine sahip satırları dahil eder. Eğer sorgu hiç satır döndürmezse, sütun kontrolü geçmiş demektir. Adım 4. Önemli sütunlar için tekrarla. Raporları oluşturan diğer sütunlar için de sütun testi uygulamalısın. Sayısal aralıkları kontrol et. Örneğin, revenue sıfırdan küçük olmamalı. Gereken tarih alanlarının dolu olduğundan ve gelecekte bir tarihi göstermediğinden emin ol. Kategori değerlerinin izin verilen değerlerle eşleştiğini doğrula. ID alanlarının boş ya da yönelenmiş olmadığını kontrol et. Özetle, her kuralı açıkça tanımla ve ihlalleri bulmak için sorgular yaz. Koşulları basit ve birbirinden ayrık tut. Sorgudan hiç satır dönmemesi, sütunun temiz olduğu anlamına gelir. Verine güveni korumak için, bu kontrolleri tüm kritik sütunlarda tekrarlamalısın. Tüm sütun testlerini tamamladığında, binanın her direğini tek tek kontrol etmiş olursun. Artık dış cephesi kadar iç yapısı da güven veren sağlam bir bina karşında durur.
