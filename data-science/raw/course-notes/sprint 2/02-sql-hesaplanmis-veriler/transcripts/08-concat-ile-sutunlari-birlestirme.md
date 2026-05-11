---
sprint: 2
lesson_slug: 02-sql-hesaplanmis-veriler
video_slug: 08-concat-ile-sutunlari-birlestirme
video_file: videos/08-concat-ile-sutunlari-birlestirme.mp4
duration_seconds: 142
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:26Z
tags: [transcript, sprint-2]
---

# Concat ile sutunlari birlestirme

> Otomatik transkript — kaynak: `videos/08-concat-ile-sutunlari-birlestirme.mp4` (ders: Sql Hesaplanmis Veriler). Düzeltmeler için video referans alınmalıdır.

Concat, SQL içindeki Lego blokları gibidir. Birden fazla sütunu bir araya getirerek okunabilir bir metin oluşturmanı sağlar. Tarih stringleri, kullanıcı dostu kimlikler, tam isimler ya da kullanıcı adları üretmek için idealdir. Senaryo: Ben Brightkart adlı bir perakende şirketinde veri analistiyim. Ürün yöneticim şöyle diyor: Satın alma kayıtları çok göz yorucu. Okunabilir bir sipariş etiketi gösterebilir miyiz? Ad ve soyadı birleştirebilir miyiz? Ayrıca yeni hesaplar için basit bir kullanıcı adı oluşturabilir miyiz? Concat burada devreye girer. Yöntem, adım adım. Adım 1: Ne oluşturmak istediğini belirle. Okunabilir etiketler. Birkaç alanı net ayraçlarla birleştir. Örneğin tarih, alt tire, ürün. Benzersiz anahtarlar. Çakışmayı önlemek için yeterli alan ekle. Örneğin saat, mağaza veya order number. Sunum alanları. Raporlar ve e-postalar için first name artı boşluk, last name şeklinde birleştir. Adım 2: Sağlam konkat ifadeleri yaz. Ayırıcılar eklemeyi unutma ki sınırlar net olsun. Alt tire veya eksi genellikle uygundur. Null değerlerine karşı koaleys kullan. Metnin bozulmasını önler. Adım 3: Örnek sorgular. 1. İsimleri tek bir string olarak göster. Bu sorgu ad ve soyadı birleştirerek full name üretir. 2. Okunabilir bir tarih stringi oluştur. Yıl, ay, gün. Yyy, mm, d formatında. Bu sorgu tarih bileşenlerini biçimlendirip sıfır doldurarak okunabilir bir tarih dizisi üretir. 3. Ayırıcılarla daha okunabilir bir satın alma etiketi oluştur. Bu sorgu tarih ve ürün isimlerini birleştirerek daha okunabilir etiketler oluşturur. 4. Etiketin benzersizliğini artır. Bu sorgu tarih, ürün, mağaza kodu ve sipariş numarasını birleştirerek etiketi benzersiz hale getirir. 5. Basit kullanıcı adları üret. Bu sorgu adın ilk harfi, çalışan numarası ve soyadını birleştirerek basit bir kullanıcı adı oluşturur. Ana fikir, concat sütunları birleştirip okunabilir, anlamlı metinler üretmeni sağlar.
