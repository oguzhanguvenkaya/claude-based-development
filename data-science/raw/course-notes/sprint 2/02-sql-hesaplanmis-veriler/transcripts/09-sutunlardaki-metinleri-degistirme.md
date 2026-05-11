---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 09-sutunlardaki-metinleri-degistirme
video_file: videos/09-sutunlardaki-metinleri-degistirme.mp4
duration_seconds: 183
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:35Z
tags: [transcript, sprint-2]
---

# Sutunlardaki metinleri degistirme

> Otomatik transkript — kaynak: `videos/09-sutunlardaki-metinleri-degistirme.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Replace ifadesiyle bir sütundaki karakterleri veya kelimeleri sistematik biçimde değiştirebilir, silebilir ya da düzeltebilirsin. Metinler tutarlı hale gelir ve analize hazır olur. Ben FreshCart isimli çevrim içi market girişiminde veri analistiyim. Dün düzgün tarih metinleri oluşturmak için yıl, ay, gün değerlerini birleştirmiştim. Bugün purchases ile product katalog arasında yaptığım join çalışmıyor. Neden? Metinler dağınık, fazladan boşluklar, karışık ayırıcılar, SKU 123 yerine SKU 123 gibi ve yinelenen bir yazım hatası. Apple şimdi replace zamanı. Adım 1. Değişiklikleri güvenli şekilde dene. Önce select. Amaç veriyi değiştirmeden düzeltmeleri test etmek. Karakterleri sütun genelinde değiştirme. Bu sorgu, ürün adındaki tüm A harflerini I ile değiştirerek sonucu gösterir. Örnekler, banana binini, apple iple. SKU formatlarını eşitleme. Bu sorgu, SKU alanındaki tireleri ve boşlukları kaldırarak temiz bir SKU anahtarı oluşturur. Yazım hatasını düzeltme. Bu sorgu, apple yazım hatasını apple olarak düzeltir. Kısa not. Bu örnek, null değerleri boş metinle değiştirerek apple hatalarını düzeltir. Adım 2. Değişiklikleri dikkatli uygula. Amaç veriyi temizlemek ama orijinal tabloyu bozmamak. Seçenek A. En güvenli yaklaşım, ham tabloyu değiştirmek yerine geçici bir temiz versiyon oluşturmaktır. Bu geçici sorgu, SKU ve ürün adlarını replace ile temizleyip sonucu gösterir. Böylece hiçbir veriyi kalıcı olarak etkilemeden çıktığını kontrol edebilirsin. Bu yapıyı bir clean data view yani temiz veri görünümü gibi düşünebilirsin. Henüz kalıcı bir nesne değildir ama tekrar tekrar kullanabileceğin sürekli doğru sonuç veren bir sorgudur. İlerleyen konularda bu görünümü kalıcı hale getirmenin yani bir view olarak kaydetmenin yollarını öğreneceksin. Seçenek B. Gerçek güncelleme gerekiyorsa önce test et. Bu sorgu, Apple içeren satırların sayısını kontrol eder. Bu komut yalnızca Apple içeren satırlarda düzeltme yapar. Doğrulama önerileri. Güncelleme öncesi ve sonrası sayıları group by ile karşılaştır. Join'i yeniden çalıştır. Eşleşmeyen satırlar azalmalı. Benzetme. Concat, Lego bloklarını birleştirmek gibidir. Replace ise hatalı parçayı çıkarıp yenisiyle değiştiren bir tamir aracıdır. Özetle, Replace metinleri düzenlemek ve veri bütünlüğünü arttırmak için basit ama güçlüdür.
