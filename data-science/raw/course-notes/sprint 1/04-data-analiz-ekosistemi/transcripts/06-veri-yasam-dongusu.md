---
sprint: 1
lesson_slug: 04-data-analiz-ekosistemi
video_slug: 06-veri-yasam-dongusu
video_file: videos/06-veri-yasam-dongusu.mp4
duration_seconds: 213
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:36Z
tags: [transcript, sprint-1]
---

# Veri yasam dongusu

> Otomatik transkript — kaynak: `videos/06-veri-yasam-dongusu.mp4` (ders: Data Analiz Ekosistemi). Düzeltmeler için video referans alınmalıdır.

Veri çok değerlidir, ancak ham haliyle genellikle dağınık, karışık ve kullanışsızdır. İşte bu noktada modern veri altyapısı devreye girer. Bu sistem tüm süreci uçtan uca düzenler. Veriyi toplamak ve depolamaktan, temizleyip dönüştürmeye, analiz etmeye ve içgörüleri iş araçlarına geri beslemeye kadar. Şimdi bu adımları birlikte inceleyelim. Adım 1. Toplama. Veriyi bir araya getirme. Öncelikle veriyi farklı kaynaklardan toplarız. Örneğin, müşteri siparişleri bir CRM'de, destek talepleri bir Helpdesk aracında, finansal kayıtlar ise başka bir sistemde durur. Kaynaklar MySQL, MongoDB, Elasticsearch gibi veri tabanları, CRM, pazarlama veya finans platformları gibi iş uygulamaları. Kullanılabilecek araçlar, Fivetran, Stitch, Supermetrics gibi yönetilen servisler, Airflow ve Airbyte gibi açık kaynak araçlar, bazen de özel yazılmış Python veya PHP skriptleri. Örneğin, bir CRM'den müşteri siparişlerini, Google Ads'den reklam harcamalarını çekip, tek bir merkezi noktada birleştirmek. Adım 2. Depolama ve Dönüştürme. Veriyi saklamak ve şekillendirme. Toplanan veri artık depolanır, temizlenir ve analiz için güvenilir modellere dönüştürülür. Platformlar Google BigQuery, Snowflake, Amazon Redshift ve Microsoft Azure gibi bulut veri ambarları. Kullanılabilecek araçlar, modelleme için SQL, dönüşüm yönetimi için DBT, ileri düzey analizler için Python. Örneğin, New York City ve New York değerlerini tek bir biçimde standart hale getirmek. Ardından her bölge için aylık satış toplamını hesaplamak. Adım 3. Orkestrasyon ve Dokümentasyon. Süreci otomatikleştirmek ve açıklamak. Her şeyi manuel yapmak mümkün değildir. Orkestrasyon araçları iş akışlarını otomatikleştirir ve hataları yakalar. Dokümentasyon ise modelleri, filtreleri ve iş kurallarını açıklar. Böylece herkes mantığı anlayabilir. Kullanılabilecek araçlar, orkestrasyon için Airflow. Örneğin, her sabah saat 6'da otomatik olarak yenilenen bir satış panosu ve yöneticilere metriklerin nasıl hesaplandığını adım adım anlatan bir dokümentasyon. Adım 4. Analiz. Veriyi içgörüye dönüştürme. Artık veri keşfe hazır hale gelir. Panolar ve raporlar eğilimleri ortaya çıkarır ve yeni sorulara yanıt bulmayı sağlar. Kullanılabilecek araçlar, Looker Studio, Power BI, Tableau, Looker, Metabase. Örneğin, bir pano satışları kanala göre gösterir ve yöneticilerin her bölgeyi ayrı ayrı incelemesine olanak tanır. Adım 5. Aktivasyon. İçgörüleri aksiyona dönüştürme. İçgörüler sadece panolarda kalmaz. İç araçlarına geri aktarılır, böylece ekipler hemen harekete geçebilir. Kullanılabilecek araçlar, Sensus, HiTouch gibi reverse ETL çözümleri veya özel skriptler. Örneğin, veri ambarındaki churn riski yüksek müşteriler listesini CRM'e gönderip satış ekibinin bu müşterilere hemen ulaşmasını sağlamak.
