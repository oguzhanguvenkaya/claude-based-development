---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 03-oltp-ve-olap-sistemleri
video_file: videos/03-oltp-ve-olap-sistemleri.mp4
duration_seconds: 117
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:49Z
tags: [transcript, sprint-2]
---

# Oltp ve olap sistemleri

> Otomatik transkript — kaynak: `videos/03-oltp-ve-olap-sistemleri.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi veritabanlarının iki dünyasını inceleyelim. OLTP ve OLAP sistemleri. Anahtarların ötesinde veritabanlarının amaçları da farklıdır. OLTP sistemleri yani relational databases küçük ama çok sık yapılan işlemler içindir. Günlük iş süreçleri için tasarlanmıştır. Her ATM çekimi, her rezervasyon, her satın alma hızlı ve doğru şekilde kaydedilir. Bir veri analisti olarak genelde bu sistemlerde analiz yapmamalısın çünkü bunlar veri sorgularından ziyade işlem hızına ve doğruluğa odaklıdır. OLAP sistemleri yani analytical databases ise büyük ve geçmişe dönük veri setlerini barındırır. Bu veriler sorgulama ve analiz için özetlenmiş ve yapılandırılmıştır. Bir veri analisti olarak zamanının çoğunu OLAP sistemlerinde geçirirsin çünkü analiz ve raporlama için veriler orada tutulur. Hem OLTP hem de OLAP sistemlerinde ortak dil SQL'dir. OLTP tarafında SQL genellikle hızlı işlemler için kullanılır. Insert into orders, customer id, product id, date, values, 123, 45, 2025, 09. Bu komut tek bir işlemi kaydeder. OLAP tarafında ise SQL yoğun analizler için kullanılır. Select region, some sales, from orders, group by region. Bu sorgu binlerce hatta milyonlarca işlemi özetleyerek eğilimleri gösterir. Ana fikir SQL bir araç kutusudur. OLTP günlük işlemlerin kaydedildiği yerdir. OLAP ise analistlerin bu kayıtları sorgulayıp özetleyerek içgörü ürettiği yerdir.
