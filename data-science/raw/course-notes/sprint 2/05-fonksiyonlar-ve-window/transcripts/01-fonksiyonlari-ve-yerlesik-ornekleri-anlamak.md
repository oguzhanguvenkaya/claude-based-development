---
sprint: 2
lesson_slug: 05-fonksiyonlar-ve-window
video_slug: 01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak
video_file: videos/01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak.mp4
duration_seconds: 127
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:12Z
tags: [transcript, sprint-2]
---

# Fonksiyonlari ve yerlesik ornekleri anlamak

> Otomatik transkript — kaynak: `videos/01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak.mp4` (ders: Fonksiyonlar Ve Window). Düzeltmeler için video referans alınmalıdır.

Bir fonksiyon, bir veya birden fazla girdi alır. Bu girdilere parametre diyoruz. Bu parametreler üzerinde bir işlem yapar ve bir çıktı üretir, yani return eder. Yani küçük bir makine gibi düşünebilirsin. İçine veri koyarsın, sana işlenmiş bir sonuç verir. Peki SQL'de bu ne işimize yarayacak? SQL yazarken çoğu zaman aynı işlemleri tekrar tekrar yaptığımızı fark etmişsinizdir. Mesela bir değeri yuvarlamak, tarih farkı almak ya da belirli bir kurala göre veri dönüştürmek gibi. İşte tam bu noktada SQL fonksiyonları devreye girer. SQL fonksiyonları, veriler üzerinde işlem yapmamızı sağlayan hazır araçlardır. Yani tek tek uzun işlemler yazmak yerine hazır bir fonksiyonu çağırarak işi kısaltırız. Fonksiyonlar bize üç temel şey sağlar. Kod yazmayı hızlandırır, daha okunabilir sorgular yazmamızı sağlar, aynı işlemi tekrar tekrar yazmamızı engeller. PostgreSQL'de çok sayıda hazır fonksiyon vardır. En sık kullanılanlardan bazıları round, upper, lower, length, now ve daha önce çokça kullandığımız aggregate fonksiyonları olan count, sum ve average'dir. Bunlar veriyle çalışırken sürekli elimizin altında olan araçlar gibi düşünebilirsin. Mesela bir sayıyı yuvarlamak istiyorsak bunu sıfırdan yazmayız. Onun yerine round fonksiyonu kullanırız. Round bir sayıyı alır ve belirttiğin basamak sayısına göre yuvarlayarak geri döner. Eğer ikinci parametreyi vermezsen en yakın tam sayıya yuvarlar. Round gibi kullanabileceğimiz bir sürü fonksiyon vardır. Hepsinin yaptığı iş farklı ama çalışma mantığı aynıdır. Veriyi alıp üzerinde belirli bir işlem uygular ve bize yeni bir sonuç üretirler. Özetle SQL fonksiyonları veriyi sadece çekmekle kalmayıp onu işlemek, dönüştürmek ve anlamlı hale getirmek için kullandığımız güçlü araçlardır.
