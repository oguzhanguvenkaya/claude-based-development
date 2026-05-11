---
sprint: 2
lesson_slug: 04-subquery-ve-with-as
video_slug: 01-with-as-ile-query-tanimlama
video_file: videos/01-with-as-ile-query-tanimlama.mp4
duration_seconds: 192
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:04Z
tags: [transcript, sprint-2]
---

# With as ile query tanimlama

> Otomatik transkript — kaynak: `videos/01-with-as-ile-query-tanimlama.mp4` (ders: Subquery Ve With As). Düzeltmeler için video referans alınmalıdır.

With AS ifadesi yani Common Table Expression adlandırılmış bir alt sorgu tanımlamanı sağlar. Bu yapıyı pre-aggregations veya karmaşık hesaplamalar için kullanabilir, ardından ana SQL sorgunda buna bağlanabilir ya da üzerinden sorgu çalıştırabilirsin. Kodunu sadeleştirir, tekrar eden satırları önler ve geçici tablolar oluşturma ihtiyacını ortadan kaldırır. Bir e-ticaret markasında veri analistiyim. KPI yani hedef göstergem zamanında kargo göndermek. Analiz ettiğim metrik ise sipariş başına kargo ücreti. Elimde satış satırlarından toplam ciroyu ve kargo tablosundan da kargo ücretini getirmem gereken iki tablo var. Eğer satış satırlarını doğrudan kargo tablosuna join edersem, her siparişin birden fazla satış satırı olduğu için kargo ücreti her satırda tekrar eder. Rakamlar şişer. Bu klasik bir many-to-one join hatasıdır. Önce toplulaştırma yapacak, sonra birleştireceğim. İşte burada WITH AS devreye giriyor. WITH AS için temel sintaks bu şekilde. WITH, geçici alt sorguya verdiğin bir isim, AS, alt sorgunun içeriği ve son olarak az önce tanımladığımız geçici sorguyu kullanan üst sorgu. Adım 1. Geçici sonucu WITH ile oluştur. Önce sipariş bazında satış toplamını gruplayor ve hesaplıyoruz. Unutma, alt sorguyu her zaman parantez içine almalısın. Bu kod adım adım şunları yapar. Orders subquery adında bir alt sorgu oluşturur. Satışları orders id'ye göre gruplayarak her siparişi tek satıra indirger. Sum turnover ile toplam ciroyu hesaplar. Böylece ileride satır bazında tekrar oluşmaz. Adım 2. Join etmeden önce CTE'nin tekrarlı satırları giderip gidermediğini kontrol et. Bu sorgu her siparişin toplam cirosunu gösterir ve sipariş bazında veri setini indirger. Burada artık her orders id sadece bir kez görünür. Veri setin artık doğru bilgiyi sunuyor. Adım 3. Geçici sonucu ana sorguda kullan. Şimdi bu temiz, tekrarsız sonucu kargo tablosu ile birleştiriyoruz. Bu sorgu her siparişin toplam cirosunu gönderi ücreti ile birleştirir ve tek satırlık sonuçlar üretir. Bu sorgu şunları döndürür. Her sipariş için sales tablosundan toplam ciroyu ve orders ship tablosundan da shipping fee'yi. Dönen tabloda hiçbir satır duplike edilmemiş, temiz bir join ve doğru metrikler. Peki with ne zaman ve neden kullanılır? 1. Çoğaltılmış ve şişmiş veri setlerini önlemek için joinden önce toplulaştırma yaparken. 2. Karmaşık ifadeleri örneğin turnover eksi purchase cost bilgisine tek yerde tanımlayıp her yerde tekrar kullanmak için. 3. SQL kodunu daha okunabilir ve sürdürülebilir hale getirmek için. Özetle with ifadesini toplulaştırmayı önceden yapıp joinleri sadeleştirmek için kullanmalısın. Sonuç doğru toplamlar, temiz SQL ve gereksiz geçici tablolarla uğraşmadan düzenli bir kod.
