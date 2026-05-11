---
sprint: 3
lesson_slug: 01-ileri-seviye-sql
video_slug: 06-karma-tablo-ve-gorunum-yaklasimi
video_file: videos/06-karma-tablo-ve-gorunum-yaklasimi.mp4
duration_seconds: 179
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:41Z
tags: [transcript, sprint-3]
---

# Karma tablo ve gorunum yaklasimi

> Otomatik transkript — kaynak: `videos/06-karma-tablo-ve-gorunum-yaklasimi.mp4` (ders: Ileri Seviye Sql). Düzeltmeler için video referans alınmalıdır.

Ağır ve tekrar kullanılabilir dönüşümleri tablo olarak sakla. Üstüne daha hafif ve esnek analizler için viyular ekle. Böylece performans, maliyet ve çeviklik arasında denge kur. Ben bir abonelik tabanlı SaaS şirketinde çalışan veri analistiyim. BigQuery kullanıyoruz. Pazarlama, finans ve ürün ekiplerinin her gün ihtiyaç duyduğu KPI'lar var. Ancak panolar yavaş çalışıyor ve sorgu maliyetleri hızla artıyor. Bugün bunu hem maliyeti düşürmek hem de çevik analizi korumak için Materialize Table ve viyuları birlikte kullanarak çözeceğim. Adım 1. Ham veriden başla, temiz viyu oluştur. Uygulama olayları ve ödeme tablolarını bağlarım. Türleri standartlaştırır, kolonları yeniden adlandırır ve bozuk satırları filtrelerim. Bu hafif ve geri alınabilir bir işlem olduğu için bunu bir viyu olarak yaparım. Neden viyu? Çünkü ham verinin şeması değişse bile güncel ve esnek kalır. Adım 2. KPI ve metriklerle zenginleştir. Tekrar kullanılıyorsa tabloya dönüştür. İş mantığını bir kez hesaplarım. Churn flagler, aktif aboneler, MRR, LTV gibi metrikler. Farklı ekipler bu zenginleştirilmiş katmanı her gün tekrar kullandığı için bunu Partition Table olarak saklar ve kademeli şekilde yenilerim. Bu bizim Canonical Datasetimiz olur. Ağır işlem bir kez yapılır, herkes hızlıca tüketebilir. Adım 3. Aşağı akış işleri için viyu katmanları oluştur. B.I. tarafında panolara özel olarak aggregate eden, lookup tablolarla join yapan ve veriyi yeniden şekillendiren viyular kurarım. Böylece her bir dashboardda veriyi yeniden temizlemek ya da zenginleştirmek zorunda kalmam. Viyular zenginleştirilmiş tabloya oturur ve hızlı çalışır. Adım 4. Maliyet ve performansı dengele. Zenginleştirilmiş tabloyu oluşturmanın maliyetini bir kez ödersin. Daha sonra küçük, seçilmiş veri seti üzerinde viyu ile hafif sorgular çalıştırırsın. Daha az byte taranır, yükleme süresi kısalır. Büyük tabloları yeniden yazmadan sadece viyular aracılığıyla şema veya iş kurallarında değişiklik yapabilirsin. Sonuç, daha düşük işlem maliyeti, daha az tekrar, daha hızlı dashboardlar. Adım 5. Table mı, viyu mu? Table olarak sakla eğer dönüşümler ağır, stabil ve sıkça tekrar kullanılıyorsa, veri hacmi büyük ve sorgular karmaşıksa, belirli bir yenileme takvimin varsa. Viyu olarak bırak eğer iş mantığı hafifse, tazelik önemliyse ya da hala değişiyorsa, henüz iş tanımlarını veya B.I. modellerini test ediyorsan, veri seti küçükse veya nadiren tekrar kullanılıyorsa. Özet, ağır ve tekrar kullanılabilir dönüşümleri kalıcı bir tabloya dönüştür. Hafif, değişen analizleri ise viyularla yönet. Ana fikir, büyük işi bir kez yap, kalan her şeyde hızlı ve esnek kal.
