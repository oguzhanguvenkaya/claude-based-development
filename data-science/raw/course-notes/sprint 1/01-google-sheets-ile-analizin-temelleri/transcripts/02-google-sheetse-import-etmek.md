---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 02-google-sheetse-import-etmek
video_file: videos/02-google-sheetse-import-etmek.mp4
duration_seconds: 155
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:21:57Z
tags: [transcript, sprint-1]
---

# Google sheetse import etmek

> Otomatik transkript — kaynak: `videos/02-google-sheetse-import-etmek.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

İlk adımla başlayalım, veriyi Google Sheets'e almak. Bunun iki yolu var, bir manuel, iki otomatik. Salesforce'da çalışan bir veri analistiyim. Müşteri kayıtlarını içeren bir dosya aldım ve ilk görevim bu veriyi Google Sheets'e aktarmak. Birinci yöntem, manuele içe aktarma. CSV dosyasını doğrudan Sheets'de açıyorum. Tüm değerler tek bir sütunda, birbirine yapışmış halde görünüyor. Sorun değil, Data, Split Text to Columns seçeneğini kullanarak veriler sütunlara düzgün biçimde ayrılıyor. Harika, artık dosya okunabilir durumda. İkinci yöntem, otomatik içe aktarma. Peki, bu dosya her gün güncelleniyorsa ne olacak? Her seferinde kopyala yapıştır yapmak vakit kaybı. Bunun yerine başka bir tablodaki veriyi canlı olarak çeken Import Range fonksiyonunu kullan. Önce verinin bulunduğu dosyanın bağlantısını tırnak içinde yapıştırıyorum, ardından hangi sayfadan ve hangi aralıktan veri alacağımı belirtiyorum. İşte bu kadar, sayfam anında güncellendi. Kaynak dosya değiştikçe, senin tablon da otomatik yenilenecek. Web üzerinde herkese açık bir CSV dosyası örneği üzerinden gidelim. Bazen de veriyi doğrudan web üzerindeki bir CSV dosyasından çekmen gerekir. Burada da Import Data imdadımıza yatışıyor. CSV bağlantısını yapıştırıyorum, Sheets veriyi doğrudan sütunlara çekiyor. Import Range, iki depo arasında bir boru gibidir. İlk depo yani kaynak dolduğunda, ikinci depo yani senin sheet, otomatik olarak yenilenir. Import Data ise bir küvete boşalan musluk gibidir. Çalıştırdığında, webdeki CSV verisi doğrudan sayfana akar. Özetle, veriyi Sheets'e manuel olarak veya otomatik formüllerle aktarabilirsin. Verin güncel kalır, sen de zaman kazanırsın. Bitirirken önemli bir bilgi vereyim. Bazen formülleri yanlış yazacaksın ve ekrandaki gibi hatalar alacaksın. Böyle durumlarda şunu yap. Formülünü kopyala, ardından hatayı da kopyala, sonra ikisini de yapay zekaya yapıştır ve sor. Neden hata veriyor? Yapay zeka sana iyi bir yönlendirme yapacaktır.
