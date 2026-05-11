---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 03-table-aliasing
video_file: videos/03-table-aliasing.mp4
duration_seconds: 180
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:43Z
tags: [transcript, sprint-2]
---

# Table aliasing

> Otomatik transkript — kaynak: `videos/03-table-aliasing.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Table Aliasing, yani tablolara takma ad verme. Join ile tablo birleştirirken her sütün için tablo ismi belirtmiştik. Peki neden? Bunu, karışıklıkları önlemek ve okunabilirlik için yapıyoruz. Diyelim ki, purchases ve product tablolarını birleştirirken satın alımların id sütünlarını da görmek istiyoruz. id sütününü tablo ismi belirtmeden selekt etmek istediğimizde klasik bir hata alırız. Ambiguous kalım hatası. Çünkü id, birleştirdiğimiz iki tabloda da bulunuyor ve SQL bu sütünu hangi tablodan alacağını bilemiyor. Bu yüzden sütünların sadece bir tabloda olduğundan emin bile olsak, sorguları tablo isimleri belirterek yazmalıyız. Bu sayede duplike sütün isimlerinden doğabilecek sorunları elimine etmiş oluruz. Aynı sorgunun tablo isimleriyle yazılmış haline bakalım. Artık sorgu, ambiguous kalım hatası vermez. Ama biraz uzun duruyor. Her sütün için uzun tablo isimlerini tekrar tekrar yazmamız gerekti. Bu şimdilik büyük bir sorun gibi durmayabilir. Ama görmek istediğimiz sütün sayısı arttıkça baş etmesi zor olabilir. İşte tam da bunun için tablo takma adları var. Bu takma adlar sayesinde tabloları kısa isimlerle çağırabiliriz. Table aliasing'i from ve join kısmında tablo adını yazdıktan hemen sonra yaparız. Örneğin, sorgumuzdaki purchases tablosu için perch takma adını tablo isminden hemen sonra belirtip, select içinde bu takma adıyla sütünları çağırabiliriz. Aynısını product tablosu içinde yaptığımızda sorgu biraz daha okunabilir hale geliyor. Burada dikkat! Özellikle bir ekip içinde çalışırken tablolara verdiğimiz takma adların anlamlı, tutarlı ve kafa karıştırıcı olmamasına dikkat etmeliyiz. Mesela products tablosunu p şeklinde kısaltmak anlık bir hız kazandırabilir ama uzun vadede anlamayı zorlaştıracaktır. Burada önemli bir noktaya daha dikkat edelim. Biz table aliasing yaptığımızda aslında sadece SQL'e hangi tablodan veri alacağını söylüyoruz. Ancak sonuç tablosuna baktığımızda bu sütünlar hala sadece ID olarak görünüyor. Yani alias kullanmak sonuç tablosundaki kolon isimlerini otomatik olarak değiştirmez. Eğer sonuç tablosunda bu sütünları da ayırt etmek istersek bu sefer column aliasing kullanmamız gerekir. Column aliasing'i sütünları belirtirken yaparız. Bu şekilde artık sonuç tablosunda sütünlar purchase ID ve product ID olarak net bir şekilde görünür. Özetle sütünları tablo ismiyle çağırmak hangi tablodan veri geldiğini netleştirir. Table aliasing sorguyu yazarken kolaylık sağlar. Column aliasing sonuç tablosunu düzenler ve anlaşılır hale getirir.
