---
sprint: 2
lesson_slug: 05-fonksiyonlar-ve-window
video_slug: 04-partition-by-ve-over-kullanimi
video_file: videos/04-partition-by-ve-over-kullanimi.mp4
duration_seconds: 136
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:22Z
tags: [transcript, sprint-2]
---

# Partition by ve over kullanimi

> Otomatik transkript — kaynak: `videos/04-partition-by-ve-over-kullanimi.mp4` (ders: Fonksiyonlar Ve Window). Düzeltmeler için video referans alınmalıdır.

Window fonksiyonları her satırın detayını korurken toplamlar, ortalamalar ya da sıralamalar gibi özetleri satırın yanına ekler. Çevrim içi bir giyim mağazasında veri analistisın. Depo müdürün şunu istiyor. Her ürün satırı görünsün, aynı zamanda ürün türüne göre toplam stoklar ve her satırın bu toplam içindeki payı da o satırda yazsın. Yani tek tablo içinde hem detay hem özet. Window fonksiyonları burada devreye girer. Mantık basit. Toplama işlemini bir pencere üzerinde yapar ancak satırları birleştirmez. Over ifadesi bu pencerenin kapsamını tanımlar. Partition by yoksa pencere tüm tablo olur. Böylece her satır kendi değerini korur, yanında tüm tablo toplamı ekrana gelir. Bu sayede örneğin her satırda genel toplam stoğu görebilir ve satırın genel içindeki yüzdesini hesaplayabilirsin. Yüzdeyi kurarken pay satırdaki stok, payda over ile hesaplanan genel toplam olur. Payı paydaya bölüp gerektiğinde yüzde ile çarparsın. Kod okumadan düşün, her satırda benim stoğum kaç ve tüm stok kaç yazar? Birini diğerine bölersin. Çözümü bir seviye ileri taşıyalım. Partition by model type dediğinde pencere artık her ürün türü için ayrı ayrı çalışır. Yani t-shirts kendi toplamını, accessories kendi toplamını üretir. Her satırda iki bilgi olur. Satırın kendi stok değeri ve ait olduğu türün toplam stoğu. Yüzdeyi de aynı şekilde kurarsın ancak bu kez paydaya genel toplam değil o türün toplamı yerleşir. Over ifadesi tek başına kullanıldığında genel tablo bağlamını verir. Bu tüm tabloya göre yüzdeler ve paylaşımlar için idealdir. Partition by bu bağlamı gruplara böler. Bu da kategori içi yüzdeler ve karşılaştırmalar için mükemmeldir. Her iki durumda da satırları birleştirmediğin için detay görünür kalır. Özeti ise satırın yanına eklenir. Bu yaklaşımı benimsediğinde aynı tabloda hem mikroskop hem de dürbün etkisini birlikte yakalarsın. Satırların ayrıntısını korur, toplu resmi kaybetmezsin.
