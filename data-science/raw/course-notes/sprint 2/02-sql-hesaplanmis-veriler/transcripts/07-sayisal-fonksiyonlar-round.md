---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 07-sayisal-fonksiyonlar-round
video_file: videos/07-sayisal-fonksiyonlar-round.mp4
duration_seconds: 195
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:28Z
tags: [transcript, sprint-2]
---

# Sayisal fonksiyonlar round

> Otomatik transkript — kaynak: `videos/07-sayisal-fonksiyonlar-round.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Temel fikir, SQL'de sayıları düzgün biçimde göstermek için round, kolon, ondalık sayı kullanmalısın. Belirli bir ondalık basamak sayısına ya da en yakın tam sayıya yuvarlayabilirsin. Giriş Perakende e-ticaret şirketinde çalışan bir junior veri analistisiniz. Proje yöneticiniz bir gösterge paneli istiyor. Günlük siparişleri tam sayılarla EOV yani Average Order Value'yu para birimi formatında iki ondalıkla göstermeniz gerekiyor. Elinizdeki veri tablosu Purchases'da ham tutarları içeren bir Spend kolonu var. Şimdi bu değerleri görüntülemeye hazır hale getirmek için round kullanacağız. Adım adım yöntem Adım 1 Toplamları yalnızca gerektiğinde yuvarla. Amaç, bazı sayısal kolonlar örneğin Spend veya Quantity fazla uzun ondalıklar gösterebilir. Görsel olarak temiz yani tam sayı görünmesini istediğinde round, kolon, sıfır kullanmalısın. Bu sorgu, Purchases tablosundaki Spend değerlerini en yakın tam sayıya yuvarlayarak Rounded Spend olarak gösterir. Bu sorgu, Spend değerlerini yuvarlayıp Rounded Spend başlığıyla sunar. İpucu Sayma işlemlerinde round gerekmez. Count zaten tam sayı döndürür. Adım 2 Para birimi değerlerini iki ondalığa yuvarla. Amaç, parayı 3.15 gibi göstermek, 3.1457 gibi değil. Bu sorgu, Spend değerlerini iki ondalık basamağa yuvarlar. Parasal değerlerin okunaklı olabilmesi için genellikle iki ondalık basamak yeterlidir. Bu durumda round fonksiyonunu ikinci argüman olarak iki değeriyle kullanırsın. Böylece 3.1457 gibi bir sayı 3.15 olarak görünür. Bu, raporlarda ve panellerde profesyonel bir görünüm sağlar. Örneğin, bir ürünün ortalama fiyatını 3.1457 yerine 3.15 şeklinde göstermek hem daha temiz hem daha kullanıcı dostudur. Pratik alışkanlık, para birimi için decimal veya numerik tipleri daha güvenlidir. Böylece binary float türlerinden kaynaklı küçük hatalardan kaçınırsın. Adım 3 Yuvarlamayı doğru yerde uygula. Kural Round ifadesini raporlamaya yönelik alanlarda, yani son select içinde kullan. Ham veriler üzerinde yapılan hesaplamaları yuvarlama. Yuvarlamayı en sonda, sonuçları gösterirken yap. Bu sorgu, siparişleri tarih bazında gruplayarak her günün sipariş sayısını ve ortalama spend'i hesaplar. Ortalama değeri iki ondalıkla gösterir. Bu sorgular, harcama değerlerine hem tam sayıya hem de iki ondalığa yuvarlanmış şekilde gösterir. Benzerlik Round fonksiyonunu verin için bir fiyat etiketi gibi düşün. Ham rakamları değiştirmeden saklarsın. Müşteriye göstereceğin etiketi düzenli ve okunaklı basarsın. Sayımlar için tam sayılar, para birimleri için iki ondalık. Özetle, ham veriyi olduğu gibi bırak, görsel sunumda round ile uygun sayısal biçimi kullan.
