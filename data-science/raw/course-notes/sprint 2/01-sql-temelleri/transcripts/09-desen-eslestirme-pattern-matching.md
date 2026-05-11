---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 09-desen-eslestirme-pattern-matching
video_file: videos/09-desen-eslestirme-pattern-matching.mp4
duration_seconds: 117
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:58Z
tags: [transcript, sprint-2]
---

# Desen eslestirme pattern matching

> Otomatik transkript — kaynak: `videos/09-desen-eslestirme-pattern-matching.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi like ifadesini kullanarak desenlerle arama yapma zamanı. Yöneticinden yeni bir istek geldi, adı C harfiyle başlayan tüm müşterilerin listesini verebilir misin? Her ismi tek tek yazmak tabii ki mantıklı olmaz. Bunun yerine SQL bize like operatörüyle desen eşleştirme imkanı sunar. Şöyle çalışır. Yüzde işareti, yüzde herhangi bir sayıda karakter anlamına gelir. Yani şunu yazarsan, bu sorgu adı C harfiyle başlayan tüm müşterileri listeler. Clara, Chris, Charlotte yani adı C ile başlayan herkesi getirir. Bitişleri de eşleştirebilirsin. Bu koşul soyadı son ile biten kayıtları döndürür. Bu da Johnson, Anderson gibi soyadları döndürür. Baştaki yüzde son kelimesinden önce ne olursa olsun eşleşsin demektir. Bir metnin içini de arayabilirsin. Bu koşul içinde an geçen adları bulur. Bu Hannah, Daniel ya da Fernando gibi içinde an geçen isimleri bulur. Bir de tam bir karakteri temsil eden alt çizgi vardır. Örneğin, bu koşul A ile başlayıp ardından tek bir karakter ve 1 ile biten kodları eşleştirir. Bu A11, AB1 gibi kodları eşleştirir ama A1 yüzü eşleştirmez. Yani yüzde bir arama motorundaki joker karakter gibidir. Boşlukları istediğin şeyle doldur der. Alttan tire ise daha hassastır. Yalnızca bir karakterlik bir kutuyu doldurmanı ister. Kısacası, yöneticin bir filtre ister ama tam yazımı bilmiyorsa like tam da bu durum için idealdir. Bu ifade sana yalnızca birebir eşleşmeleri değil desenleri de yakalama esnekliği sağlar. Ana fikir like verilerinde adı tam hatırlanmayan veya kısmen bilinen değerleri bulmak için en esnek arama aracındır.
