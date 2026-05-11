---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 09-primary-key-testi
video_file: videos/09-primary-key-testi.mp4
duration_seconds: 153
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:54Z
tags: [transcript, sprint-2]
---

# Primary key testi

> Otomatik transkript — kaynak: `videos/09-primary-key-testi.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

SQL test türlerinden biri olan Primary Key testiyle her zaman birincil anahtarın her kaydı benzersiz şekilde tanımladığını kontrol ederiz. Bunu anahtara göre grup bay yapıp Count ile olası tekrarları kontrol ederek doğrularız. Böylece join işlemleri güvenilir olur ve veri bütünlüğü korunur. Data analisti olarak kampanyalara göre bir gelir raporu hazırlaman gerekiyor. Purchases tablosunu Promotions tablosuyla birleştirip raporu hazırlayabilirsin. Ama bunu yapmadan önce Purchases.id değerlerinin benzersiz olduğunu doğrulaman gerekir. Satın alma tablosunu havaalanına gelen yolcuların kuyruğu gibi düşün. Her yolcunun benzersiz bir pasaport numarası olmalı. Tablodaki Purchases.id gibi. Görevin kimse yinelenmeden bir sonraki terminale yani Promotions tablosuyla joine geçmelerini sağlamaktır. Eğer bu anahtar benzersiz değilse her join işlemi satırları çoğaltır. Bu da toplamları şişirir ve metrikleri bozar. Adım 1. Varsayımı belirle. Siparişler tablosu için varsayım Purchases.id'nin benzersiz olması. Yani her satın alma yalnızca bir kez görünmelidir. Adım 2. id'ye göre grupla ve say. Bunu kontrol etmek için şu sorguyu çalıştır. Bu sorgu her id için kaç satır bulunduğunu listeler ve birden fazla olanları gösterir. Eğer hiçbir satır dönmüyorsa anahtar benzersizdir. Eğer sonuçta satırlar varsa bunlar tekrar eden değerlerdir. Nedeni araştırmalısın. Adım 3. Count yıldız kullanın. Count kolon değil. Count yıldız her satırı sayar, null değer içerenleri de. Count kolon ise null içeren satırları atlar ve bu da tekrarları gizleyebilir. Bu yüzden benzersizliği test ederken her zaman count yıldız kullanmalısın. Adım 4. Anahtar olmayan sütunu karşılaştır. Örneğin buyer sütunu birden fazla satırda tekrarlanabilir. Bu normaldir. Tekrarlanan buyer değerleri sorun değildir. Ama tekrarlanan id asla olmamalı. Özetlemek gerekirse, join işlemlerine başlamadan önce birincil anahtarı mutlaka kontrol et. Bir id bir satır demektir. Temiz anahtarlar temiz joinler ve doğru toplamlar sağlar. Benzersiz bir primary key güvenilir veri bütünlüğünün temelidir.
