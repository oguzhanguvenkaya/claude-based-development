---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 14-null-degerleri
video_file: videos/14-null-degerleri.mp4
duration_seconds: 112
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:05Z
tags: [transcript, sprint-2]
---

# Null degerleri

> Otomatik transkript — kaynak: `videos/14-null-degerleri.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Son olarak eksik verileri yani nal değerlerini nasıl yöneteceğini öğrenelim. Er ya da geç eksik verilerle karşılaşacaksın. SQL'de eksik ya da bilinmeyen değerler nal ile gösterilir. Ve şunu bilmek önemli. Nal sıfır değildir. Boş metin de değildir. Kelimenin tam anlamıyla bilinmiyor demektir. Diyelim ki yöneticin şöyle dedi. Telefon numarası kayıtlı olmayan tüm müşterileri göster. Burada şunu yazmak işe yaramaz. Phone number eşittir sıfır ya da phone number eşittir boş. Bu şekilde filtreleme yapamazsın. Bunun yerine is nal kullanmalısın. Bu sorgu telefon numarası olmayan müşterileri listeler. Eğer tersini yani telefon numarası olan müşterileri göstermek istiyorsan bu defa şöyle yazarsın. Bu koşul telefon numarası dolu olan müşterileri seçer. Bazen yöneticin eksik olanların bile doldurulmasını ister. Örneğin eğer telefon numarası yoksa unknown yaz diyebilir. İşte o zaman if nal ya da koalave fonksiyonlarını kullanırsın. Bu sorgu telefon numarası nal ise unknown gösterir. Ya da bu sorgu telefon numarası nal olduğunda unknown değerini döndürür. Nalı bir formdaki boş kutu gibi düşün. Bu kutu sıfır anlamına gelmez. Boş da değildir. Sadece henüz doldurulmamıştır. If nal ve koales gibi fonksiyonlar sana o boşlukta ne göstereceğini belirleme imkanı verir. Böylece raporların hem anlaşılır hem de tutarlı olur. Özetle nal bilinmeyen veriyi temsil eder, is nal ile bulur, if nal veya koales ile istediğin değeri gösterebilirsin.
