---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 04-entity-iliski-diyagramlari-erd
video_file: videos/04-entity-iliski-diyagramlari-erd.mp4
duration_seconds: 160
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:23:52Z
tags: [transcript, sprint-2]
---

# Entity iliski diyagramlari erd

> Otomatik transkript — kaynak: `videos/04-entity-iliski-diyagramlari-erd.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdi, bu tabloların birbiriyle nasıl ilişkili olduğunu görselleştirelim. Veri tabanlarını anlamak için en önemli araçlardan biri Entity Relationship Diagrams ya da kısaca ERD. Şöyle düşün, veri tabanın bir şehir gibi. Her tablo bir bina. Binanın her katı bir sütun, o katta yaşayan her kişiyse bir satır. Her binanın tepesinde bir kimlik kartı gibi bir Primary Key vardır. O binada kimin yaşadığını kesin olarak gösterir. İnsanlar binalar arasında dolaşırken yolları kullanır. Bu yollar Foreign Key'lerdir. Binaları birbirine bağlar ve verinin şehir içinde nasıl aktığını gösterir. İşte ERD bu şehrin haritasıdır. Hangi binaların var olduğunu ve aralarındaki yolları görmeni sağlar. Gerçek bir örnekle somutlaştıralım. Diyelim iki tablomuz var. Customers ve Orders. Customers tablosunda her satırın Customer ID adında bir Primary Key var. Orders tablosunda ise müşterinin adını her siparişte tekrar yazmak yerine Customer ID'yi Foreign Key olarak kullanırız. Bu sayede, mesela Nathan üç alışveriş yaptığında, her sipariş satırı Customers tablosundaki tek kaydına bağlanır. Bu bir One-to-Many ilişkidir. Bir müşteri birçok sipariş verebilir ama her sipariş sadece bir müşteriye aittir. Başka ilişki türleri de var. One-to-One ilişki örneği bir müşteri ile pasaport bilgisi olabilir. Her biri doğrudan tek bir kayıtla bağlıdır. Many-to-Many biraz daha karmaşıktır. Öğrenciler ve dersler gibi. Bir öğrenci birçok derse katılabilir, her dersinde birçok öğrencisi olabilir. Gerçekte bu ilişkiyi kurmak için her iki id'yi içeren bir Linking Table yani bir Junction Table kullanırız. Burada önemli olan şu, ERD görünmeyen ilişkileri görünür hale getirir. Tahmin yürütmeyi ortadan kaldırır. Bir ilişki One-to-Many olduğunda bir Join işleminde birden fazla satır beklemen gerektiğini bilirsin. Eğer One-to-One ise sadece tek bir satır döneceğini beklersin. Many-to-Many ise iki tablo arasında ek bir tabloya ihtiyaç duyduğunu fark edersin. Bir eğitmen olarak özellikle vurgulamak isterim. Bu ilişki türlerini anlamak doğru SQL sorguları yazmanın en temel becerilerinden biridir. Ana fikir, ERD planlama aracıdır, tabloları ve ilişkileri gösterir. SQL ise bu harita üzerinde yürüdüğün dildir. Tabloları oluşturur, anahtarları tanımlar ve aralarında sorgular yazmanı sağlar.
