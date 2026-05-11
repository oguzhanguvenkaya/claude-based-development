---
sprint: 2
lesson_slug: 03-tablolari-birlestirmek-ve-test-etmek
video_slug: 04-join-turleri
video_file: videos/04-join-turleri.mp4
duration_seconds: 205
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:46Z
tags: [transcript, sprint-2]
---

# Join turleri

> Otomatik transkript — kaynak: `videos/04-join-turleri.mp4` (ders: Tablolari Birlestirmek Ve Test Etmek). Düzeltmeler için video referans alınmalıdır.

Şimdiye kadar tabloları nasıl birleştireceğimizi gördük. Ancak her join aynı şekilde çalışmaz. Kullanacağımız join türü, iki tablo arasındaki verilerin nasıl eşleşeceğini ve sonuçta hangi kayıtların listeleneceğini belirler. Inner, left, right ve full outer join gibi farklı türler sayesinde ihtiyacımıza göre yalnızca eşleşen verileri ya da eşleşmeyenleri de dahil edebiliriz. İlk olarak inner join ile başlayalım. Inner join sadece iki tabloda da eşleşen kayıtları getirir. Yani bir satın alımın product id değeri, products tablosunda gerçekten varsa o kayıt sonuçta görünür. Ama satın alım tablosunda olup products tablosunda karşılığı olmayan bir kayıt varsa inner join bunu göstermez. Şimdi left join'a bakalım. Left join sol taraftaki tabloyu tamamen korur. Yani join sorgusundaki ana tabloyu. Bizim sorgumuzda ana tablo purchases'sa, purchases tablosundaki tüm kayıtlar sonuçta yer alır. Eğer products tablosunda eşleşen bir ürün varsa ürün bilgileri de gelir. Ama eşleşme yoksa ürün tarafındaki sütunlar null olur. Yani left join için mantık şu. Soldaki her şeyi getir, eşleşme varsa sağ tarafı da ekle. Sol taraftaki tablonun tamamını aldığı için inner join'e kıyasla daha fazla satır döndürebilir. Join türü seçerken şu ipucunu kullanabiliriz. Hangi tablodaki hiçbir satırı kaybetmek istemiyorsan o tabloyu sol tarafa koy. Yani ana tablon o olsun. Üçüncü tür right join. Çalışma mantığı left join'e benzer. Ancak right join ana tablodaki değil birleştirilen tablodaki tüm satırları tutar. Sol tablodaki eşleşmeyen sütunlarsa null gözükür. Eğer amacımız siparişi olan veya olmayan tüm ürün satırlarını listelemekse right join kullanırken products tablosunu sağ tarafa, purchases tablosunu da sol tarafa koyabiliriz. Unutmayın, left join ve right join aslında birbirinin ayna görüntüsüdür. Left join soldaki tabloyu, right join ise sağdaki tabloyu korur. Bu yüzden çoğu durumda right join kullanmak zorunda değilsiniz. Aynı sonucu tabloların yerini değiştirip left join kullanarak da elde edebilirsiniz. Son olarak full outer join var. Bu join türü iki tablodaki tüm kayıtları getirir. Eşleşen kayıtlar birleştirilir, eşleşmeyen kayıtlarda atılmaz. Sadece karşı taraftaki alanlar null olur. Yani full outer join bize şunu söyler. İki tabloda ne varsa getir, eşleşiyorsa birleştir, eşleşmiyorsa da yine göster. Bu yüzden en kapsayıcı join türüdür. En fazla satır bu tür bir joinden gelir. Özetle, inner join sadece eşleşen kayıtlar. Left join soldaki tüm kayıtlar, eşleşme varsa sağ taraf. Right join sağdaki tüm kayıtlar, eşleşmeyen sol taraf. Full outer join iki tablodaki tüm kayıtlar. Yani aslında join türlerini ayıran temel soru şu. Sadece eşleşenleri mi görmek istiyoruz, yoksa eşleşmeyenleri de sonuçta tutmak istiyor muyuz? Kararımızı buna göre veririz.
