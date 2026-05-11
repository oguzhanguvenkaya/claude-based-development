---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 02-tablolar-anahtarlar
video_file: videos/02-tablolar-anahtarlar.mp4
duration_seconds: 136
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:45Z
tags: [transcript, sprint-2]
---

# Tablolar anahtarlar

> Otomatik transkript — kaynak: `videos/02-tablolar-anahtarlar.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi, verilerin veri tabanlarında nasıl saklandığını ve birbirine nasıl bağlandığını inceleyelim. Bir veri tabanı nasıl yapılandırılmıştır? Bunun için bazı temel yapıları anlamamız gerekir. Tablolar, tables, satırlar, rows, sütunlar, columns, primary keyler ve foreign keyler. Ve elbette bu yapılarla çalışırken kullandığımız dil SQL'dir. Önce tablolardan başlayalım. Bir veri tabanındaki her şey tablolarla başlar. Basitçe söylemek gerekirse, bir tablo satırlardan ve sütunlardan oluşur. Ama burada kurallar biraz daha katıdır. Her sütun tek bir veri türü tutar. Metin, sayı ya da tarih gibi. Her satır ise tek bir kaydı temsil eder. Örneğin bir müşteri ya da bir işlem. İkinci olarak primary key, yani birincil anahtar. Bu, tablodaki her kayıt için benzersiz bir tanımlayıcıdır. Pasaport numarası gibi düşünebilirsin. İki kişinin adı aynı olabilir ama dünyanın hiçbir yerinde iki kişiye aynı pasaport numarası verilmez. Örneğin bir buyers tablosunda customer id, first name ve last name sütunlarını saklayabilirsin. Burada customer id sütunu pasaport numarası gibi çalışır. Otomatik artar ve her alıcının benzersiz bir kimliğe sahip olmasını sağlar. Üçüncü olarak foreign key. Bu, bir tablodaki bir alanın başka bir tablodaki primary key ile bağlanmasıdır ve böylece bir ilişki kurar. Bunu şöyle düşün, havaalanındaki bir free shoptan alışveriş yaptığında sistem senin ad ve soyadını doğrudan satın alma tablosuna kaydetmez. Bunun yerine pasaport numaranı kaydeder. O numara satın alma kaydını doğru müşteri kaydıyla ilişkilendirir. İşte bu bir foreign key'dir. Veri tabanları bu sayede gereksiz tekrarları önler. Yarın soyadın değişse bile her bir satın alma kaydını tek tek güncellemen gerekmez. Çünkü tüm satın almalar senin benzersiz kimliğin üzerinden bağlanmıştır, bu bağlantı temiz ve doğru kalır. Özetle tablolar verileri düzenler, primary key her kaydı benzersiz şekilde tanımlar, foreign key ise tablolar arasındaki kayıtları tekrar etmeden birbirine bağlar.
