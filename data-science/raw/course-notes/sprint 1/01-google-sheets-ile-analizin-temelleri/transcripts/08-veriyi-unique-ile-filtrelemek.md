---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 08-veriyi-unique-ile-filtrelemek
video_file: videos/08-veriyi-unique-ile-filtrelemek.mp4
duration_seconds: 103
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:31Z
tags: [transcript, sprint-1]
---

# Veriyi unique ile filtrelemek

> Otomatik transkript — kaynak: `videos/08-veriyi-unique-ile-filtrelemek.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Dördüncü Adım: Unique Fonksiyonu ile Tekrarlardan Kurtulma
Bir veri analisti olarak bazen binlerce tekrarlı bilgilerle dolu listelerle karşılaşırım. Örneğin, 5.000 müşteri adayını içeren bir veri seti import ettim ve bir sütunda müşterilerin yaşadığı şehirler var. Sorun şu: Liste tekrarlardan geçilmiyor. Paris yüzlerce kez, London yüzlerce kez tekrar ediyor. Müşterilerimin hangi şehirlerde yoğunlaştığını görmek istesem, 5.000 satır arasında kaybolurum. Tam da bu noktada Unique fonksiyonunu kullanırım. Formül şöyle: eşittir Unique, kaynak.A1.A500. Yani, A sütünündaki tüm satırlara bak, her şehir adını yalnızca bir kez döndür, tekrarları kaldır. Enter'a bastığında Google Sheets anında sade bir liste oluşturur. 5.000 satır yerine belki sadece 50 farklı şehir ismi elde edersin. Artık müşteri adaylarının hangi şehirlerde yoğunlaştığını bir bakışta görebilirsin. Bu sayede segmentasyon da çok kolaylaşır. Artık Paris, London ve Berlin'i karşılaştırmak için kategorilerin hazır. Ne kaydırmaya ne de tahmin yürütmeye gerek var. Ana fikir şu: Unique fonksiyonu kontak listeni temizlemek gibidir, tekrarları ortadan kaldırır, analiz için net bir kategori listesi oluşturur. Özet: Filtreleme, ham veriler arasında boğulmakla yalnızca anlamlı olanı görmek arasındaki farktır. CRM veya e-mail sistemlerine veri yüklerken hataları önler. Manuel filtreler kısa süreli çözümler sunar ama filtre, query ve unique fonksiyonları süreci otomatik, ölçeklenebilir ve her zaman analize hazır hale getirir.
