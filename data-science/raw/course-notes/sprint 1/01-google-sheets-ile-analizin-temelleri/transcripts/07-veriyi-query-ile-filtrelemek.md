---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 07-veriyi-query-ile-filtrelemek
video_file: videos/07-veriyi-query-ile-filtrelemek.mp4
duration_seconds: 112
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:30Z
tags: [transcript, sprint-1]
---

# Veriyi query ile filtrelemek

> Otomatik transkript — kaynak: `videos/07-veriyi-query-ile-filtrelemek.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Adım 3. Query fonksiyonuyla karmaşık koşullar. Ertesi gün pazarlama müdürü benden daha kapsamlı bir analiz istedi. Firmanın CRM aracından 100 bin müşteri adayı satırı import ettim. Büyük veri setleriyle uğraşmak bir data analisti için günlük rutindir. Buradaki istek, sadece 2024 yılına ait Paris müşterilerini görmek ve başlangıç için yalnızca 100 satırlık bir örnek yeterli. Manuel kaydırma ve filtreleme çok zaman alır. İşte bu nedenle Query fonksiyonunu kullanırım. Formül şöyle, eşittir, query, kaynak, A sütunundan N sütununa, tırnak içinde, select yıldız işareti, ver, kol 10 eşittir Paris, end kol 11 eşittir 2024, limit 100,1. Bu sorgu Google Sheets'e şunu söyler. Select yıldız işareti, tüm sütunları göster demek. Ver, kol 10 eşittir Paris, end kol 11 eşittir 2024 ise, sadece city sütunu Paris olan ve yıl sütunu 2024 olan satırları dahil et demektir. Limit 100 ve sadece ilk 100 satırı getir anlamına gelir. Enter'a bastığında Google Sheets devasa tablonu saniyeler içinde tüm koşulları karşılayan küçük, yönetilebilir bir veri kümesine dönüştürür. Artık 100 bin satır yerine, yalnızca 2024 yılı Paris müşterilerinden oluşan tertemiz 100 satırlık bir tablo görürsün. Query'nin gücü burada. Adeta sheetle konuşuyormuş gibi olur. İstediğimi seç, koşullarıma uyanları getir ve göstereceğin miktarı sınırla. Ana fikir, Query sadece bir fonksiyon değil, büyük veri setlerinde hayat kurtaran bir araç. Gereksiz karmaşayı eler ve tam ihtiyacın olan dilimi sunar.
