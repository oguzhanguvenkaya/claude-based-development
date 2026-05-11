---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 11-takma-adlar-aliasing
video_file: videos/11-takma-adlar-aliasing.mp4
duration_seconds: 103
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:00Z
tags: [transcript, sprint-2]
---

# Takma adlar aliasing

> Otomatik transkript — kaynak: `videos/11-takma-adlar-aliasing.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Raporlarını alias'ız kullanarak daha düzenli hale getirelim. Yöneticin senden müşteri listesini içeren temiz bir rapor ister. Ancak sorgunu çalıştırdığında sütun adları First Name, Last Name, Cast ID gibi görünür. Veri tabanı için faydalı ama rapor sunumu için pek uygun değil. İşte tam bu noktada S ile aliasing devreye girer. S ifadesiyle çıktıda sütun adlarını yeniden isimlendirebilirsin. Bu sorgu ad ve soyadı sütunlarını sırasıyla name ve surname olarak yeniden adlandırır. Artık sonuçta sütun başlıkları name ve surname olarak görünür. Yöneticine teslim edeceğin bir rapor için çok daha anlaşılır bir görünüm sağlar. Alias'ız uzun tablo adlarıyla çalışırken sorgularını da kısaltır. Örneğin, bu sorgu customers ve orders tablolarını customer id üzerinden birleştirir ve kısa takma adlar c, o kullanır. Burada customers ve orders adlarını her seferinde yazmak yerine sadece c ve o kullandık. Daha temiz, hızlı ve yazım hatasına daha az açık. Aliasingi birine lakap takmak gibi düşün. Gerçek isim değişmez ama daha kısa veya anlaşılır bir versiyonla iletişim kurmak kolaylaşır. Yani sorgularının okunabilir olmasını istiyorsan veya uzun tablo adlarıyla uğraşıyorsan, S senin aracın. Hem profesyonel hem pratik sorgular yazmanı sağlar. Özetle, alias kullanarak verilerini daha okunabilir ve raporlarında daha sunulabilir hale getirmelisin.
