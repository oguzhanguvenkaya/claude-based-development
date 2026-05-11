---
sprint: 2
lesson_slug: 05-fonksiyonlar-ve-window
video_slug: 03-neden-window-fonksiyonlarina-ihtiyacimiz-var
video_file: videos/03-neden-window-fonksiyonlarina-ihtiyacimiz-var.mp4
duration_seconds: 198
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:22Z
tags: [transcript, sprint-2]
---

# Neden window fonksiyonlarina ihtiyacimiz var

> Otomatik transkript — kaynak: `videos/03-neden-window-fonksiyonlarina-ihtiyacimiz-var.mp4` (ders: Fonksiyonlar Ve Window). Düzeltmeler için video referans alınmalıdır.

Window fonksiyonları, toplamları, ortalamaları ya da sıralamaları gruplar bazında hesaplamanı sağlar. Ama klasik toplama işlemlerinden farklı olarak orijinal satırları gizlemez. Yani hem detayları hem de özet bilgiyi tek bir sorguda bir arada görebilirsin. Bugün Circle Apparel'da yeni başlayan bir veri analistisin. Depo yöneticin senden ürünlerin model, renk, beden, fiyat ve miktar bilgilerini gösteren ama aynı zamanda her ürün türü için grup bazında toplam stok değerini de içeren bir tablo istiyor. Kısacası tek bir sorguyla hem detay hem özet içgörü sunan bir tablo oluşturacaksın. İlk adımda klasik yaklaşım olan grup buy ile başlayalım. Daha önce sütunları dönüştürmek için fonksiyonlar kullanmayı öğrenmiştin. Şimdi sıra verileri gruplara ayırıp bu gruplar üzerinde özet hesaplamalar yapmaya geldi. Örneğin model adı ve model türüne göre bir tabloyu grupladığında her grubun toplam stok değerini elde edebilirsin. Bu şekilde yazılmış bir sorgu her grup için tek bir satır üretir ve o satırda gruba ait toplam veya ortalama gibi değerler yer alır. Yani model adı ve model type'a göre gruplar oluşturur, her bir grupta stok değerlerini toplar ve sonuçta her grup için tek bir satır döndürür. Bu yöntem bir özet tablo oluşturmak için idealdir. Ancak bunun bir bedeli vardır. Orijinal satır detaylarını kaybedersin. İşte burada iş ihtiyacı değişiyor. Depo yöneticin şöyle diyor. Ben her ürün satırını görmek istiyorum ama aynı satırda o ürünün ait olduğu ürün tipinin toplam stok değerini de görmek istiyorum. Klasik grup buy ile bunu yapmaya çalışırsan birden fazla sorgu, alt sorgular ya da join kullanman gerekir. Sonuç sorgu karmaşıklaşır, okunabilirlik azalır ve hata yapma riski artar. Tam bu noktada window fonksiyonları devreye girer. Bu fonksiyonlar grup buy'ın aha esnek ve şeffaf bir versiyonu gibidir. Gruplar üzerinde toplama veya ortalama işlemleri yapar ama satırları birleştirmez. Yani her satır kendi kimliğini korur ancak yanına ait olduğu grubun özet bilgisi eklenir. Bu sayede hem ürünün kendi detaylarını görebilir hem de o ürünün ait olduğu kategorinin toplam stok değerini aynı tabloda görebilirsin. Kısaca bir benzetme yapalım. Grup buy bir özet makinesi gibidir. Tüm meyveleri karıştırıp smoothie yapmak gibi düşün. Sonuçta lezzetli bir karışım elde edersin ama hangi meyvenin hangisi olduğunu artık göremezsin. Window fonksiyonları ise şeffaf bir skor tahtası gibidir. Her oyuncu yani her satır sahnede kalır ama üzerinde grubun toplam puanı, ortalaması ya da sıralaması görünür. Özetle ihtiyacımız hem detayları hem özet bilgileri aynı anda gösterebilmekti. Grup buy satırları birleştirerek bu detayı kaybettirirken window fonksiyonları her satırı koruyup onun üzerine grup veya genel toplam, ortalama ve sıralama gibi bilgileri ekleyerek daha zengin bir tablo oluşturur.
