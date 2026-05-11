---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 06-where-ve-having-ile-filtreleme
video_file: videos/06-where-ve-having-ile-filtreleme.mp4
duration_seconds: 238
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:28Z
tags: [transcript, sprint-2]
---

# Where ve having ile filtreleme

> Otomatik transkript — kaynak: `videos/06-where-ve-having-ile-filtreleme.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Bir perakende pazar yerinde, yeni veri analisti olarak senden şu soruyu yanıtlaman isteniyor: Geçen hafta toplamda 10 dolardan fazla harcama yapan alıcılar kimler? Buradaki fark şu: Bir alıcı birden fazla alışveriş yapmış olabilir. Bugün öğreneceğimiz konu, SQL'de WHERE ile HAVING farkı. WHERE, gruplanmadan önce tekil satırları filtreler, HAVING ise GROUP BY işleminden sonra oluşan grupları filtreler. Bu fark, SQL motorunun sorguyu çalıştırma sırasından kaynaklanır. Yöntem, SQL'i bir motor gibi düşün. SQL'in yürütme sırası şöyledir: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. Bunun bazı önemli sonuçları var. WHERE, SELECT'ten önce çalıştığı için SELECT içindeki alias'lar, takma adlar WHERE içinde kullanılamaz. SUM, COUNT, AVG gibi toplama fonksiyonları WHERE içinde kullanılamaz. Bunlar HAVING içinde kullanılmalıdır. Kısacası, WHERE satırları önceden filtreler, HAVING ise grupları sonradan filtreler. Demo, tek veri seti, üç soru. Tablomuz, Purchases, Buyer, Spend. Örnek satırlar. Julie, 7-5, Pauline, 11, Max, 4. Adım 1. Her alıcının toplam harcamasını hesapla. SELECT, Buyer, SUM of Spend as Total Spend from Purchases, GROUP BY, Buyer. Adım 2. Grupları topladıktan sonra filtreleme. İlk iş sorusu. Soru toplam harcaması 10 dolardan fazla olan alıcılar kim? SELECT, Buyer, SUM of Spend as Total Spend from Purchases, GROUP BY, Buyer, HAVING, SUM of Spend büyüktür 10. Sonuç Julie 7 artı 5 ve Pauline 11, Max elenir. Bazı sistemlerde bu noktada alias yani sütun takma adını Total Underscore Spend doğrudan HAVING içinde kullanabilirsin. Ama en güvenli ve evrensel yöntem fonksiyonu tekrar yazmaktır. HAVING, SUM, SPEND büyük 10. Adım 3. Yaygın bir hata. Bazen geliştiriciler bu sorguyu yanlışlıkla şöyle yazar. WHERE, TOTAL SPEND büyüktür 10. Ancak bu hata verir. Çünkü WHERE, SELECT'ten önce çalıştığı için o anda TOTAL SPEND henüz hesaplanmamıştır. Yani sorgu tanımlanmamış bir değere ulaşmaya çalışır. Bu hatayı önlemenin yolu toplam gibi özet değerleri her zaman HAVING içinde kullanmaktır. Adım 4. Farklı bir soru, bireysel satırları önceden filtreleme. Bu defa iş sorusu şu olsun. 10 dolardan fazla olan alışverişlerle ilgileniyoruz. Sonra alıcı bazında toplam istiyoruz. SELECT, BUYER, SUM of SPEND as TOTAL SPEND, WHERE, SPEND büyüktür 10. Sonuç sadece Pauline. Çünkü sadece onun tek alışverişi 10 dolardan büyüktü. Julie'nin 7 ve 5 dolarlık alışverişleri toplama girmeden önce elendi. Yani bu tamamen farklı bir iş sorusuna yanıt verir. Benzetme, hızlı hatırlama yöntemi. WHERE, kapıdaki güvenlik görevlisi. Yalnızca belirli satırlar içeri girer. GROUP BY, etkinliği düzenleyen kişi. Gelenleri gruplara ayırır. HAVING, etkinlik sonrası yöneticisi. Hedefi tutturamayan grupları eler. Basit formül. WHERE, satırları önceden filtreler. HAVING, grupları sonradan filtreler. Özetle, WHERE, bireysel kayıtları. HAVING ise gruplanmış sonuçları filtrelemeni sağlar.
