---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 06-distinct
video_file: videos/06-distinct.mp4
duration_seconds: 101
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:53Z
tags: [transcript, sprint-2]
---

# Distinct

> Otomatik transkript — kaynak: `videos/06-distinct.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi sonuçlarımızı distinct ifadesiyle biraz düzenleyelim. Artık tekrar eden satırlar yok. Perakende şirketinde analist rolümüzde devam edelim. Bu sefer yönetici şöyle diyor. Bana müşterilerimizin yaşadığı tüm şehirlerin listesini verebilir misin? Bu sorgu customers tablosundaki tüm şehir isimlerini listeler. Ama sorguyu çalıştırdığında listede aynı şehirlerin tekrar tekrar göründüğünü fark ediyorsun. Yani yöneticinin istediği şey bu değil. O sadece benzersiz şehir isimlerini görmek istiyor. İşte tam burada distinct devreye giriyor. Bu anahtar kelimeyi eklediğinde SQL'e şunu söylüyorsun. Her değerden sadece bir tane göster. Bu sorgu şehir isimlerini yinelenmeden benzersiz biçimde listeler. Ve sonuç pırıl pırıl hale geliyor. Her şehir yalnızca bir kez görünüyor. O şehirde kaç müşteri olursa olsun. Distinct telefon rehberini temizlemek gibidir. Mesela Emma'yı üç kere kaydettiysen artık listede sadece bir tanesi kalır. Ama önemli bir noktaya dikkat etmelisin. Distinct seçtiğin tüm sütunlar üzerinde birlikte çalışır. Yani şöyle yazarsan bu sorgu isim ve şehir sütunlarını birlikte değerlendirir ve her benzersiz kombinasyonu bir kez gösterir. SQL isim ve şehir çiftlerini benzersiz olarak getirir. Bu da şu anlama gelir Clara New York ve Clara Boston ikisi de görünür ama Clara New York sadece bir kere listelenir. Özetle raporunda sadece benzersiz değerleri göstermen istendiğinde kullanacağın anahtar kelime distinct olmalı.
