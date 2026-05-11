---
sprint: 2
lesson_slug: 04-subquery-ve-with-as
video_slug: 03-join-vs-nested-subquery
video_file: videos/03-join-vs-nested-subquery.mp4
duration_seconds: 166
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:06Z
tags: [transcript, sprint-2]
---

# Join vs nested subquery

> Otomatik transkript — kaynak: `videos/03-join-vs-nested-subquery.mp4` (ders: Subquery Ve With As). Düzeltmeler için video referans alınmalıdır.

Birden fazla ilişkili sütunu tek bir işlemle almak için join kullanmak, nested subqueries'e kıyasla çok daha hızlı ve anlaşılırdır. Bir e-ticaret şirketinde veri analisti olduğunu düşünelim. Görevin, sales tablosundan ciro ve marj, orders tablosundan ise sipariş kodu ve taşıyıcıyı gösteren bir satış raporu oluşturmak. Eskiden yazılmış bir sorgu çalışıyor. Ama her yenileme dakikalar alıyor. Hadi bunu düzeltelim. İlk olarak sorunu anlayalım. Ne yanlış gidiyor? Elindeki sorgu, her ek sütunu almak için iç içe alt sorgular kullanıyor. Çalışıyor. Ama okuması zor. Ve çok yavaş. Çünkü veri tabanı her sütun için aynı tabloya tekrar tekrar gidiyor. Sales tablosundaki her satır için veri tabanı orders tablosunu iki kez sorguluyor. Önce cold için, sonra da transporter için. Yani her satış satırı için aynı tabloya iki kez erişiyor. Sonra bu sonuçları birleştiriyor. Mantık büyüdükçe ya da satırlar arttıkça bu yöntem tam bir bakım kabusuna dönüşür. Peki aynı sorguyu joinle yazarsak ne değişir? Hadi inceleyelim. Join, her sütunu tek tek çekmek yerine, sorgu başladığında ilk satır için sales tablosundaki tüm satırları orders tablosuyla bir kere birleştirir. Devam eden satırlara geçildiğinde, hali hazırda birleştirilmiş olan tablo üzerinden sütunlara erişeceği için tekrar birleştirmeye gerek kalmaz. Böylece her satırda orders'a iki kez gitmek yerine hepsi bir seferde çözülmüş olur. Bu yaklaşımın sağladığı şeyleri özetlemek gerekirse, performans. Tek bir join işlemi, orders satırını bir defa da getirir ve tüm sütunlara erişir. Daha az sorgu turu olmasını sağlar. Okunabilirlik. İlişki açıkça ortada. Sales ve order tabloları order id üzerinden birleşiyor. Son olarak bakım kolaylığı. Yeni bir order sütunu mu eklemek istiyorsun? Sadece select'e eklemen yeterli. Ekstra alt sorgulara gerek yok. Peki nested subquerileri ne zaman kullanmalıyız? Alt sorgular, yani subqueriler çoğu zaman joinden önce veriyi hazırlamak için kullanılır. Örneğin, önce veriyi özetlemek isteyebilirsiniz. Buna pre-aggregation denir. Bir başka kullanım ise veriyi temizlemek veya yeniden şekillendirmektir. Özetlemek gerekirse, join bir kamyon, paketleri tek seferde topluca getirir. Nested subqueriy ise her paket için ayrı kurye tutmak gibidir. Toplamda daha fazla yol, daha fazla zaman alır.
