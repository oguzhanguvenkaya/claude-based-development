---
sprint: 3
lesson_slug: 01-ileri-seviye-sql
video_slug: 05-gorunumler-ve-tablolar-arti-eksi
video_file: videos/05-gorunumler-ve-tablolar-arti-eksi.mp4
duration_seconds: 172
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:40Z
tags: [transcript, sprint-3]
---

# Gorunumler ve tablolar arti eksi

> Otomatik transkript — kaynak: `videos/05-gorunumler-ve-tablolar-arti-eksi.mp4` (ders: Ileri Seviye Sql). Düzeltmeler için video referans alınmalıdır.

Veri analizinde tazelik ile maliyet arasında bir denge kurmak gerekir. Her zaman güncel kalan sorgular için View kullanmalı, sık tekrarlanan ama biraz daha eski sonuçların yeterli olduğu durumlarda ise Materialized Table yani önceden oluşturulmuş tablolar tercih edilmelidir. Bir abonelik uygulamasında veri analistisiniz. Pazarlama ekibi her saat güncellenen kanala göre yeni kayıtlar panosunu istiyor. Finans ekibi ise haftalık bir yönetici raporu hazırlıyor. Milyarlarca satır arasında ağır join işlemleri yapıyor. Sizin göreviniz şu, pazarlamanın verileri taze kalsın ama bütçe yanmasın. Finans ekibinin sorguları hızlı çalışsın ama her rapor açıldığında milyarlarca satırı tekrar taramak zorunda kalmasın. Adım 1. View ile başla. Tazelik öncelikli. İlk olarak Home Events, Users ve Campaigns tablolarını birleştiren bir View oluşturuyorsun. Pazarlama ekibi BI aracını her açtığında bu sorgu canlı olarak çalışıyor. Sonuç, veriler her zaman güncel ama her erişimde hum tablolar yeniden taranıyor. Trafik arttıkça maliyet ve gecikme de artıyor. Adım 2. Materialize et ve yeniden kullan. Maliyet kontrolü. Finans ekibinin haftalık raporu için bu sonuçları bir tabloya materialize ediyorsun. Yani sorguyu çalıştırıp sonucu fiziksel bir tabloda saklıyorsun. Bu tabloyu her gece veya haftada birkaç kez otomatik olarak yenilemeyi planlıyorsun. Sonuç, finans sorguları artık hızlı ve ucuz. Veriler son yenileme anına kadar haftalık kararlar için fazlasıyla yeterli. Adım 3. Doğru karışımı bul, karar kuralları. Gerçek zamanlı veriye ihtiyacın varsa View kullan. Sorgu ağırsa ve sık sık tekrar çalıştırılıyorsa Table kullan. Böylece hem veriler zamanında olur hem de maliyetler kontrol altında kalır. Hatırlamak için benzetmeler. View, canlı kamera yayını. Her zaman güncel ama her izlediğinde pil yani hesaplama gücü harcar. Materialize Table, yüksek çözünürlüklü ekran görüntüsü. Canlı değildir ama paylaşması kolay, ucuz ve tekrarlanabilir. Özet, sadece View yaklaşımı, en taze veri, daha az depolama ama her erişimde yüksek hesaplama maliyeti. Table veya View Table yaklaşımı, planlı yenilemeler, tekrar kullanılabilir sonuçlar, daha ucuz ve hızlı okuma ama veriler biraz daha eski. Sonuç, tazelik, sıklık ve maliyeti dengele. Gerçek zamanlılık için View, tekrarlanan ve sabit sonuçlar için Table kullan. Veriyi ne kadar sık ve ne kadar güncel görmeniz gerektiğine göre doğru karışımı seçmelisiniz.
