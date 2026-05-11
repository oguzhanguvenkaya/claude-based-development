---
sprint: 2
lesson_slug: 05-fonksiyonlar-ve-window
video_slug: 02-sqlde-fonksiyon-tanimlama-ve-cagirma
video_file: videos/02-sqlde-fonksiyon-tanimlama-ve-cagirma.mp4
duration_seconds: 149
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:14Z
tags: [transcript, sprint-2]
---

# Sqlde fonksiyon tanimlama ve cagirma

> Otomatik transkript — kaynak: `videos/02-sqlde-fonksiyon-tanimlama-ve-cagirma.mp4` (ders: Fonksiyonlar Ve Window). Düzeltmeler için video referans alınmalıdır.

Fonksiyonlar, tekrarlayan hesaplamaları veya sınıflandırmaları bir kez tanımlayıp her yerde aynı şekilde kullanmanı sağlar. Bir e-ticaret ekibinde veri analistisin. Raporlarını incelerken bazı hesaplamaları tekrar tekrar yazdığını fark ediyorsun. Örneğin, gelirden maliyeti çıkararak marj bulmak ya da kullanıcıları yaş aralıklarına göre sınıflandırmak. Bu işlemleri standartlaştırmak ve hata riskini azaltmak için bir fikir geliştiriyorsun. Bu mantıkları fonksiyonlara dönüştürmek. PostgreSQL'de bu işlemi yapmak için create function yapısını kullanırsın. Bu komut, veri tabanına tekrar kullanılabilir bir hesaplama eklemek gibidir. Önce create function ile fonksiyonun adını ve alacağı parametreleri tanımlarsın. Parantez içinde her parametrenin ismini ve veri tipini belirtirsin. Ardından returns kısmında fonksiyonun hangi türde bir değer döndüreceğini söylersin. Sonrasında as $$ bloğu gelir. Bu blok içinde fonksiyon çalıştığında yürütülecek SQL sorgusunu yazarsın. SQL fonksiyonlarında return yazmana gerek yoktur. Select sonucu doğrudan döndürülür. En sonda ise language SQL ifadesiyle bu fonksiyonun SQL diliyle yazıldığını belirtirsin. Bu örnekte tanımlanan margin fonksiyonu turnover değerinden purchase cost değerini çıkarır ve sonucu döndürür. Böylece aynı işlemi her seferinde yeniden yazmak yerine sadece fonksiyonu çağırarak daha kısa, daha okunabilir ve daha az hataya açık sorgular yazabilirsin. Şimdi ikinci örneğe geçelim. Yaş kategorisi belirleme. Sık sık case when yapısını kullanarak doğum tarihine göre yaş aralığı belirliyorsan bunu bir fonksiyonla sadeleştirebilirsin. Bu fonksiyon doğum tarihine bakar ve belirli bir aralıkta olup olmadığına göre kişiyi wise, medium, young veya child olarak etiketler. Bu sayede aynı koşullu ifadeyi her sorguda yazmak yerine sadece age category fonksiyonunu çağırman yeterlidir. Kullanım örneğinde bir tablodaki her satır için doğum tarihini fonksiyona verirsin. Fonksiyon o kişinin yaş kategorisini döndürür. Elde edilen yeni sütuna da as age category diyerek okunabilir bir takma adı verirsin. Özetle, tekrarlayan hesaplamaları, açıklayıcı isimler ve doğru veri tipleriyle tanımlayarak SQL fonksiyonlarına dönüştürürsen hem analiz sürecin hızlanır hem de sorguların daha temiz ve sürdürülebilir olur.
