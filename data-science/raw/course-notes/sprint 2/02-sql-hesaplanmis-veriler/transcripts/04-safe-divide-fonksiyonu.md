---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 04-safe-divide-fonksiyonu
video_file: videos/04-safe-divide-fonksiyonu.mp4
duration_seconds: 175
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:19Z
tags: [transcript, sprint-2]
---

# Safe divide fonksiyonu

> Otomatik transkript — kaynak: `videos/04-safe-divide-fonksiyonu.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Giriş, temel fikir. BigQuery'de, eğer payda sıfırsa, bölme işlemi hataya neden olabilir. Safe Divide bu hatayı önler. Hata vermek yerine nal döndürür. Böylece sorgun kesilmez, çalışmaya devam eder. Senaryo. Bir abonelik uygulamasında veri analistiyim. Ürün yöneticim hızlı bir metrik istiyor. Eğer 100 dakikalık rehberlik süremiz varsa, her ebeveyn çocuk başına ortalama kaç dakika alır? Yani formülümüz 100 bölü number of children. Bu veri de people tablosunda yer alıyor. Adım 1. İlk deneme ve hata. Şöyle bir sorgu yazıyorum. Select 100 bölü number of children as time per child number of children from people. Bu sorgu number of children değeri sıfır olan satırlarda başarısız oluyor. Yani tek bir sıfıra bölme hatası tüm sorgunun çökmesine neden oluyor. Sonuç yok, içgörü yok. Adım 2. Daha güvenli yol. İlerleme. Bu sefer BigQuery'nin bölme işlemi için yerleşik güvenlik ağı olan safe divide'a geçiyorum. Select safe divide 100 number of children as time per child number of children from people. Artık number of children sıfırdan büyükse geçerli bir sonuç alıyorum. Number of children sıfır veya nullsa hata yerine null dönüyor. Sorgu çalışmaya devam ediyor. Bu sorgun için emniyet kemeri gibi. Safe divide eşittir böl ama çökme. Mantık olarak tür dönüşümleri için kullanılan safe cast ile benzer bir güvenlik yaklaşımı. Adım 3. Raporlamada kullanışlı hale getirmek. Başarı. Dashboard ihtiyaçlarına göre null değerleri nasıl göstereceğine karar vermelisin. Analiz amacıyla geçerli değil anlamında null bırakmak önerilen veya grafiklerde gösterim kolaylığı için sıfır ile değiştirmek. Select if null safe divide 100 number of children sıfır as time per child number of people from people. Küçük bir not. BigQuery'de tam nitelikli tablo adını kullanmayı unutma. Örneğin from project.dataset.people. Demo örneği. Select safe divide 100 number of children as time per child number of children from people. Hatırlatma benzetmesi. Safe divide eşittir güvenlik ağı. Null eşittir değer okunamadı. Yani sıfır değil. Özetle safe divide sıfıra bölme hatalarını güvenli şekilde önleyerek sorguların kesilmeden çalışmasını sağlar.
