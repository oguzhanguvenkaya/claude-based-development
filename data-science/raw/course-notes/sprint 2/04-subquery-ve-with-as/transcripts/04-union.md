---
sprint: 2
lesson_slug: 04-subquery-ve-with-as
video_slug: 04-union
video_file: videos/04-union.mp4
duration_seconds: 126
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:05Z
tags: [transcript, sprint-2]
---

# Union

> Otomatik transkript — kaynak: `videos/04-union.mp4` (ders: Subquery Ve With As). Düzeltmeler için video referans alınmalıdır.

Bir perakende pazaryerinde veri analisti olarak siparişlerin tek bir görünümüne elde etmem gerekiyor. Bazı siparişler eski sistem olan Orders1 tablosunda, bazılarıysa yeni sistem Orders2 tablosunda tutuluyor. Peki bunları en hızlı şekilde nasıl birleştiririm? Cevap, Union. Yapmak istediğimiz şey şu. Adım adım şunları yapacağız. Önce sütunları hizalayacağız. Doğru birleştirme için bu iki tablonun sütunlarının aynı sayıda, aynı sırada ve uyumlu veri tiplerine sahip olduğunu kontrol etmeliyiz. Daha sonra satırları üst üste ekleyeceğiz. Eğer tüm satırları almak istiyorsak Union All, sadece benzersiz satırları almak istiyorsak Union Distinct ya da Union kullanacağız. Adım 1. Tabloları incele. Orders1 tablosunda şu sütunlar var. Date Purchase, Orders ID, Turnover ve Ship Fee. Orders2'de ise Date Purchase, Orders ID ve Turnover. Bize yalnızca üç uyumlu sütun yeterli. Date Purchase, bir sipariş kimliği yani ID ve Turnover. Adım 2. Sütunları hizala ve Union All ile birleştir. Aynı sütunları aynı sırayla seçiyoruz. Bu sorgu her Orders1 ve Orders2 tablolarından kolonları seçip tekrarlı satırları dahil ederek birleştirir. Sonuç, iki tablodaki tüm satırlar üst üste yığılmış, içlerinde tekrar eden satırlarda bulunuyor. Adım 3. Tekrarlardan kurtulmak. Her satırın sadece bir kez görünmesini istiyorsak Union Distinct veya sadece Union kullanmalıyız. Anolojiyi hatırla. Union, kağıtları üst üste koymak gibidir. Union All, her şeyi olduğu gibi üst üste yığmak. Union Distinct ise kağıtları yığdıktan sonra tekrar süzgecinden geçirmek. Dikkat etmen gereken bir konu, Join ve Union farklı işlere yarar. Join işlemi, sütunları yan yana koyar. Sanki iki sayfayı yan yana bantlamışsın gibi. Union ise sayfaları üst üste yığar.
