---
sprint: 2
lesson_slug: 05-fonksiyonlar-ve-window
video_slug: 05-window-ile-farkli-detay-seviyelerinde-join
video_file: videos/05-window-ile-farkli-detay-seviyelerinde-join.mp4
duration_seconds: 212
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:28Z
tags: [transcript, sprint-2]
---

# Window ile farkli detay seviyelerinde join

> Otomatik transkript — kaynak: `videos/05-window-ile-farkli-detay-seviyelerinde-join.mp4` (ders: Fonksiyonlar Ve Window). Düzeltmeler için video referans alınmalıdır.

Sipariş düzeyindeki maliyetleri satır düzeyindeki satışlarla birleştirirken dikkatli olmalısın. Çünkü doğrudan birleştirme yaparsan, rakamlar kolayca bozulur. Window fonksiyonları bu noktada yardımımıza koşar. Böylece hem her satırın detayını korur, hem de toplamlar değişmeden kalır. Bir perakende kazar yerinde veri analistisın. Görevin, ürün bazında kargo ve lojistik maliyetlerini göstermek. İlk aklına gelen yöntem, sipariş seviyesindeki maliyetleri doğrudan satır detaylarına bağlamak olabilir. Ama burada bir tuzak vardır. Eğer bir sipariş birden fazla satır içeriyorsa, bu işlem her satıra aynı maliyeti tekrar tekrar yazar. Sonuç, toplam maliyet iki ya da üç katına çıkar. Bir başka seçenekte, önce siparişleri özetlemek, sonra bu özet tabloyu ürün satırlarına eklemek olur. Bu kez toplamlar doğru görünür, ancak hangi ürünün hangi siparişte olduğunu artık bilemezsin. Detay kaybolur. Sonuçta iki uç arasında kalırsın. Ya detayı koruyup yanlış toplama alırsın, ya da doğru toplama alıp detayı kaybedersin. Şimdi siparişi bir pasta gibi düşün. Window fonksiyonları bu pastayı eşit şekilde dilimleyen adil bir bıçak gibidir. Her satırın payını bulunduğu siparişin toplam ciro değerine göre hesaplarlar. Örneğin her sipariş için her satırın ciro payını bulmak istersin. Bunun anlamı şudur. Her satırın ciro tutarını o siparişin toplam ciro tutarına bölersin. Bu da sana o satırın sipariş içindeki katkı oranını verir. Diyelim sipariş 451'in iki satırı var. Biri 24, diğeri 15.4 birim ciro üretmiş. Toplam ciro 39.4. İlk satırın payı %60.9, ikinci satırın payı %39.1 olur. Eğer bu siparişin toplam lojistik maliyeti 7 birimse, maliyetleri aynı oranla paylaştırırsın. Yaklaşık 4.26 ve 2.74. Toplam yine 7 eder. Yani hiçbir şey kaybolmaz, hiçbir şey eklenmez. Artık her satırın payı hesaplandı. Şimdi bu payları sipariş tablosundaki kargo ve lojistik maliyetleriyle çarparsın. Sonuçta her ürün satırı kendi siparişindeki maliyetin adil bir payını taşır. Yani maliyetler doğru şekilde dağılmış olur, toplamlar da sipariş düzeyinde hala tutarlıdır. Bu yöntemin özünde iki adım vardır. Birincisi, window fonksiyonu sayesinde her siparişin toplam ciro değerini her satıra görünür hale getirmek. İkincisi, bu görünür toplam üzerinden oran hesaplayarak maliyetleri dağıtmak. Sonrasında veriyi tekrar kontrol edebilirsin. Eğer sipariş bazında toplarsan, dağıttığın maliyetlerin toplamı orijinal sipariş maliyetleriyle birebir eşleşir. Bu da yöntemin doğruluğunu kanıtlar. Farklı detay seviyelerine doğrudan birleştirmek genellikle tehlikelidir. Ya fazla sayarsın ya da bir şeyleri eksiltirsin. Ama window fonksiyonları bu soruna zarif bir çözüm getirir. Her satırın sipariş içindeki katkısını bulur, sonra maliyetleri bu katkıya göre adilce böler.
