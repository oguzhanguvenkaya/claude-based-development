---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 09-lookup-kullanarak-veri-temizleme
video_file: videos/09-lookup-kullanarak-veri-temizleme.mp4
duration_seconds: 163
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:41Z
tags: [transcript, sprint-1]
---

# Lookup kullanarak veri temizleme

> Otomatik transkript — kaynak: `videos/09-lookup-kullanarak-veri-temizleme.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Veri setini VLOOKUP ile zenginleştir. Şimdi bunu öğrenelim. Veri analisti olarak, ilk bakışta eksiksiz görünen ama kullanışlı detayları eksik olan veri setleriyle sık sık karşılaşıyorum. Örneğin, elimde isim, e-posta ve şehir sütunlarını içeren bir tablo olabilir. Sorun şu, yönetim sonuçları bölge bazında, yani kuzey ve güney olarak karşılaştırmak istiyor ama benim verimde sadece şehir bilgisi var. Bunu manuel olarak yapmak, yani her satırın yanına kuzey veya güney eklemek saatler alır ve her yeni veri geldiğinde tekrar yapılması gerekir. Bunun yerine, bir lookup tablosu oluşturup VLOOKUP kullanarak işi otomatikleştiriyorum. Adım 1. Lookup tablosunu oluşturma. İlk olarak, veri setimde bulunan tüm benzersiz şehirlerin listesine sahip olduğumdan emin oluyorum. Unique fonksiyonu ile bu listeyi hızlıca oluşturabilirim. Artık temiz bir şehir listem var. Her şehrin yanına bölgesini ekliyorum, yani kuzey veya güney. İşte lookup tablom hazır. A sütunu şehir, B sütunu bölge içeriyor. Ana veri setim için yeni bir şehir göründüğünde, burada belirir ve bölgesini sadece bir kez atarım. Adım 2. Veri setini VLOOKUP ile zenginleştir. Ana sayfaya geri dönüp region yani bölge adında yeni bir sütun ekliyorum. Sonra şu formülü kullanıyorum. Bu ne anlama geliyor? C2 mevcut satırdaki şehir. Lookup.a şehir ve bölge içeren lookup tablosu. 2 rakamı VLOOKUP'a ikinci sütunu yani bölgeyi getirmesini söylüyor. False ise sadece tam eşleşme yapmasını sağlıyor. Bir anda lead sayfamdaki her satırın bölge bilgisi otomatik olarak doluyor. Adım 3. Eksik değerleri zarif şekilde yönetme. Bazı enşehir henüz lookup tablomda olmayabilir. Normalde VLOOKUP hata gösterir. Bunun yerine formülü ifError içine alıyorum. Artık lookup şehri bulamazsa to be defined gösteriyor. Bu da lookup tablomun güncelleme gerektiğinin açık bir işareti. Adım 4. Tüm sütun için otomatikleştirme. Formülü binlerce satırı aşağı sürüklemek zor olurdu. Array formula ile tek seferde tüm sütuna uygulayabilirim. Böylece yeni satırlar eklendiğinde otomatik olarak bölge verisiyle zenginleştiriliyorlar. Adım 5. Bunun önemi. Artık verim bölge bilgisi içerdiği için neler yapabilirim? Kuzey ve güney performansını karşılaştıran pivot tablolar oluşturabilirim. Yeni veri geldikçe otomatik güncellenen dashboardlar hazırlayabilirim. Temizlemeye daha az, analize daha çok zaman harcıyorum. Özetle, lookup tabloları ve VLOOKUP sayesinde ham şehir isimlerini otomatik olarak yapılandırılmış bölgelere dönüştürüyorum. Veri setim temiz, zenginleştirilmiş ve analize hazır kalıyor. Üstelik tekrarlayan manuel işlerle uğraşmıyorum.
