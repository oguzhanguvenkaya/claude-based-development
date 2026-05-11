---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 10-index-match-ile-analiz
video_file: videos/10-index-match-ile-analiz.mp4
duration_seconds: 198
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:38Z
tags: [transcript, sprint-1]
---

# Index match ile analiz

> Otomatik transkript — kaynak: `videos/10-index-match-ile-analiz.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Index match ile nasıl analiz yapılır? Veri analizinde iki tabloyu birleştirmek ve bilgi aramak sık yapılan işlerdendir. Birçok başlangıç seviyesi analist önce VLOOKUP'a yönelir ama bu fonksiyonun ciddi kısıtlamaları var. Arama sütunu her zaman tablonun ilk sütunu olmak zorunda. Dönüş değeri için sabit bir sütun numarası belirtmeniz gerekiyor. Tablo yapısı değişirse formülleriniz bozuluyor. İşte bu yüzden deneyimli analistler index match'e güveniyor. Daha esnek, daha güvenilir ve katı sütün sırasına bağlı değil. Adım 1. Problem Şöyle bir senaryo düşünün. Müşteri kayıtlarından oluşan bir veri setim var. A sütunu Note ID, B sütunu Device, C sütunu Country içeriyor. Görevim, belirli bir Note ID için Country bilgisini bulmak. VLOOKUP kullansaydım, Note ID'nin ilk sütun olduğundan emin olmam ve doğru sonucu döndürmek için sütunları saymam gerekirdi. Yarın tablo yapısı değişirse formüllerim çalışmayı durdurur. İkinci adım. Match. Pozisyonu bulma. Match fonksiyonu bana aradığım değerin bulunduğu satır numarasını verir. Söz dizimi şöyle. Eşittir match lookup value lookup range 0. Lookup value yani aradığım değer, lookup range yani arama yapacağım sütun, 0 ise tam eşleşme demek. Örnek olarak eşittir match 123 A2 100. Bu formül Note ID 123'ün göründüğü satır numarasını döndürür. Match'i arama motorunuz gibi düşünün. Size sonucun kendisini değil, nerede bulacağınızı söyler. Adım 3. Index. Değeri döndürme. Index fonksiyonu bu pozisyonu kullanarak gerçek değeri getirir. Söz dizimi eşittir index return range row number, column number. Örnek eşittir index C2 100. Bu C sütununun 5. satırındaki değeri döndürür. Bizim durumumuzda o kaydın country bilgisi. Index'i bir ızgara okumak gibi düşünün. Satır ve sütun koordinatları tam olarak istediğiniz hücreyi işaret eder. Adım 4. Index match ile birleştirme. İkisini bir araya getirdiğimizde şöyle oluyor. Söz dizimi eşittir index return range match lookup value lookup range 0. Örnek eşittir index C2 100 match 123 A2 100. Match önce A sütununda Note ID 123'ün bulunduğu satırı bulur. Index sonra bu satır numarasını kullanarak C sütunundan ilgili country bilgisini çeker. Sonuç olarak Note ID 123'ün country bilgisini sütun sırası konusunda endişelenmeden bulabiliyorum. Analistler neden index match'i tercih ediyor? Arama sütunu ilk sütun olmasa bile çalışır. Sütunlar kaysa da formüller bozulmaz, stabil kalır. Karmaşık veri setlerinde daha iyi ölçeklenir. Ana fikir. Index match analistlere VLOOKUP'tan daha fazla kontrol sağlar. Arama adımını yani match ile dönüş adımını yani index ayırarak esnek, stabil ve gerçek dünya veri setlerine hazır bir arama yöntemi elde edersiniz.
