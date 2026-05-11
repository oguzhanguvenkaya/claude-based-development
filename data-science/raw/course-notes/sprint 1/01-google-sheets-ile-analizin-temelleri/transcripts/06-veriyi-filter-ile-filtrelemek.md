---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 06-veriyi-filter-ile-filtrelemek
video_file: videos/06-veriyi-filter-ile-filtrelemek.mp4
duration_seconds: 119
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:24Z
tags: [transcript, sprint-1]
---

# Veriyi filter ile filtrelemek

> Otomatik transkript — kaynak: `videos/06-veriyi-filter-ile-filtrelemek.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Google Sheets'te verileri filtrelemek, inbox'ını sadece önemli mailleri gösterecek şekilde ayarlamak gibidir. Gereksiz kalabalığı kaldırıp sadece önemli olanı görürsün.

Satış ekibi benden LinkedIn'den gelen müşteri adaylarını analiz etmemi istedi. LinkedIn'den çekilmiş bir müşteri adayı veri setini içeri aktardım.

Birkaç sorunla karşılaştım. Bazı satırlarda e-posta adresi yok, bu e-posta sistemimin düzenini bozar. Bazı müşterilerin profil fotoğrafı eksik ve ben sadece Londra'daki müşterileri analiz etmek istiyorum. Yani verimi adım adım filtrelemem gerekiyor.

Birinci adım manuel filtreleme. En basit yöntem Sheets'in yerleşik filtre aracıdır. Örneğin M sütununa gidip değeri 1 olan satırları filtreleyebilirim. Bu hızlı kontroller için işe yarar ama tekrarlanabilir değildir. Yeni veri eklendiğinde her seferinde aynı işlemi el ile yapmak gerekir. İşte bu noktada otomasyon devreye girer.

İkinci adım filter fonksiyonuyla otomatik filtreleme. Satırları elle seçmek yerine filter fonksiyonunu kullanabilirim. Basitçe bu formül şunu yapar. Kaynak sayfasındaki A1 ile P5000 arasındaki tüm satırlara bak. Kaynak sayfasındaki J1 ile J5000 arasındaki sadece Londra değerine ait satırları al. Sonuç, şehir sütunu Londra olan tüm satırların alt kümesini elde edersin. Yani sadece Londra'da yaşayan kullanıcılar görüntülenir. Eğer kaynak dosyaya yeni satırlar eklenirse filtrelenmiş görünüm otomatik olarak güncellenir. Ayrıca koşulları da birleştirebilirim. Örneğin yıl eşittir 2024 ve ay eşittir January gibi. Özetle filter dinamik ve otomatik bir filtreleme aracıdır. Manuel hataları ortadan kaldırır. Devam etmeden önce bir iki egzersiz yapalım.
