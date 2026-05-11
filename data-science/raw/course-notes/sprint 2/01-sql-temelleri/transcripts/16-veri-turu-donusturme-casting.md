---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 16-veri-turu-donusturme-casting
video_file: videos/16-veri-turu-donusturme-casting.mp4
duration_seconds: 118
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:11Z
tags: [transcript, sprint-2]
---

# Veri turu donusturme casting

> Otomatik transkript — kaynak: `videos/16-veri-turu-donusturme-casting.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi, CAST ve SAVE CAST kullanarak uyuşmayan veri formatlarını düzeltelim. Bazen elindeki veriler ihtiyacın olan formatta olmaz. Diyelim ki, her müşterinin aboneliğinin bitmesine kaç gün kaldığını hesaplaman gerekiyor. Bunun için END DATE sütununun DATE formatında olması lazım. Ama kontrol ettiğinde aslında tekst olarak saklandığını görüyorsun. Örneğin, 2024-12-31 gibi. Bu sorgu END DATE alanını DATE tipine dönüştürerek tarih fonksiyonlarının kullanılmasına izin verir. Artık SQL bu değerleri gerçek tarihler olarak algılar, böylece DATE diff gibi tarih fonksiyonlarını kullanabilirsin. Ama burada bir sorun var, her değer dönüştürülemeyebilir. Belki bir satırda tarih yerine UNKNOWN yazıyor. Bu durumda CAST kullanırsan SQL hata verir ve sorgu tamamen durur. İşte bu yüzden SAVE CAST vardır. Aynı şekilde çalışır ama geçersiz bir değerle karşılaşınca hataya düşmek yerine nal döner. Bu sorgu geçersiz talih değerlerinde hata yerine nal döndürerek sorgunun çalışmaya devam etmesini sağlar. Bu sayede sorgun çalışmaya devam eder ve bu nal değerleri sonradan nasıl yöneteceğine sen karar verebilirsin. En iyi uygulama yöntemi şu. Önce normal CAST ile dene, eğer hata alırsan SAVE CAST'e geç. Böylece sorgunun geri kalanı sorunsuz çalışır. Bunu bir çevirmen gibi düşün. CAST katı bir çevirmen gibidir. Anlamadığı bir kelime görünce bütün konuşmayı durdurur. SAVE CAST ise daha esnek bir çevirmen gibidir. Bilmediği kelimeyi boş bırakır ama konuşmaya devam eder. Yani verileri bir tipten diğerine taşırken, örneğin metinden sayıya ya da stringden tarihe CAST ve SAVE CAST en sık kullanacağın araçlardır. Özetle, CAST veri tipini dönüştürür, SAVE CAST ise hatalı değerlerde sorgunun durmasını önler.
