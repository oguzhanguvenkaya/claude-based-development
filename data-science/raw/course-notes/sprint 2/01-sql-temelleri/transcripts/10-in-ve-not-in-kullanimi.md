---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 10-in-ve-not-in-kullanimi
video_file: videos/10-in-ve-not-in-kullanimi.mp4
duration_seconds: 97
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:58Z
tags: [transcript, sprint-2]
---

# In ve not in kullanimi

> Otomatik transkript — kaynak: `videos/10-in-ve-not-in-kullanimi.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi uzun koşulları in ve not in kullanarak basitleştirelim. Bu kez yöneticin senden şöyle bir şey istiyor. New York, Boston veya Chicago'daki tüm müşterilerin listesini çıkarabilir misin? Bunu birden fazla or koşuluyla yazabilirsin. Bu koşul, şehir değeri New York, Boston veya Chicago olan kayıtları getirir. Ama liste uzadıkça bu yöntem karışık hale gelir. İşte burada in devreye giriyor. Bu ifade, bir değerin belirli bir liste içinde olup olmadığını çok daha temiz şekilde kontrol etmeni sağlar. Bu sorgu, şehir değeri listede verilen yani New York, Boston, Chicago şehirlerden biri olan müşterileri getirir. Şimdi çok basit. Müşterinin bulunduğu şehir listedeki şehirlerden biri olmalı. Tabii bazen yöneticin tam tersini ister. Bu üç şehirde olmayan herkesi getir. O zaman not in kullanmalısın. Bu koşu, şehir değeri listede verilen şehirler dışında kalan müşterileri getirir. Bunu bir etkinlikteki misafir listesi gibi düşün. In, kapıdaki görevlinin isimleri listede kontrol etmesi gibidir. Sadece listede olanlar içeri girer. Not in ise tam tersidir. Belirli isimlerin yasaklı olduğu bir liste düşün. Herkes içeri girebilir ama bu listedekiler hariç. Özetle, in ve not in sorgularını daha kısa, daha temiz ve okunabilir hale getirir. Özellikle belli bir değer grubuyla çalışıyorsan mutlaka kullanmalısın.
