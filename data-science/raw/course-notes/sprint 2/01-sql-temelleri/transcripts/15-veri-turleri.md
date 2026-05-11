---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 15-veri-turleri
video_file: videos/15-veri-turleri.mp4
duration_seconds: 112
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:06Z
tags: [transcript, sprint-2]
---

# Veri turleri

> Otomatik transkript — kaynak: `videos/15-veri-turleri.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Analizini güçlendiren ya da tamamen bozan şeylerden biriyle başlayalım. Veri tipleri. Sen bir SaaS şirketi olan Insider'da analistsin. Yöneticin senden geçen ayın ortalama sipariş tutarını hesaplamanı istiyor. Bu kulağa basit geliyor olabilir ama aslında yalnızca Order Amount sütunu sayısal bir tip olarak kaydedildiyse işe yarar. Eğer bu sütun metin olarak tutuluyorsa, SQL o değerleri nasıl toplayacağını bilemez. SQL'de her sütunun tanımlı bir tipi vardır. Örneğin, sayısal tipler, miktarlar ve fiyatlar için integer veya float. Metin tipleri, isimler ve adresler için string. Tarih ve zaman tipleri, date, timestamp ya da datetime. Her veri tipi kendine özel fonksiyonlar kümesiyle birlikte gelir. Mesela avgOrderAmount fonksiyonu yalnızca Order Amount sayısal bir tipse çalışır. Eğer metin üzerinde denersen, SQL hata verir. Benzer şekilde, dateDiff fonksiyonu sadece date veya timestamp sütunlarında kullanılabilir. Bazen insanlar tarihleri metin olarak kaydeder. İlk bakışta normal görünür, ta ki sıralama yapana kadar. Ocağın Şubat'tan önce gelmesi gerekirken, alfabetik sıralamada Nisan, Ağustos, Aralık gibi bir sonuç çıkar. Bu sütunun yanlış tipte olduğunu gösteren ciddi bir işarettir. Veri tiplerini mutfaktaki kaplar gibi düşün. Çorbayı süzgece, unu da su şişesine koymazsın. Her malzeme için doğru kap gerekir. Aynı şekilde her veri türü için de doğru veri tipi gerekir. Ana fikir, herhangi bir fonksiyon çalıştırmadan önce veri tiplerini mutlaka kontrol etmelisin. Yanlış tip, yanlış sonuçlara yol açar. Ve bazen bunu fark ettiğinde çok geç olabilir.
