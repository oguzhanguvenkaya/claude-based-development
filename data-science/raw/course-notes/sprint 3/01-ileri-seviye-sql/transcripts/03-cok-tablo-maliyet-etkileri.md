---
sprint: 3
lesson_slug: 01-ileri-seviye-sql
video_slug: 03-cok-tablo-maliyet-etkileri
video_file: videos/03-cok-tablo-maliyet-etkileri.mp4
duration_seconds: 160
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:31Z
tags: [transcript, sprint-3]
---

# Cok tablo maliyet etkileri

> Otomatik transkript — kaynak: `videos/03-cok-tablo-maliyet-etkileri.mp4` (ders: Ileri Seviye Sql). Düzeltmeler için video referans alınmalıdır.

Her ara sorgu sonucunu ayrı bir tablo olarak kaydedip, gereksiz depolama maliyeti oluşturmak yerine sonuçları anlık olarak hesaplayan viewları kullan. Böylece tablo çoğaltmaktan kaçınarak sistemi sadeleştir ve depolama maliyetini azalt. Abonelik tabanlı bir SaaS şirketinde veri analisti olarak çalışıyorum ve BigQuery faturam aniden yükseldi. Neden mi? Çünkü veri hattımın her adımını ayrı bir tablo olarak kaydediyorum. Ham veri, temiz tablo, zenginleştirilmiş tablo, join edilmiş tablo, özetlenmiş tablo. Bugün sana view kullanarak bu süreci nasıl dönüştürebileceğini göstereceğim. Böylece depolama maliyetini azaltabilir, kopya verileri önleyebilir ve veri hattını çok daha sade hale getirebilirsin. Adım 1. Maliyet tuzaklarını fark et. Yöntem. Tipik bir veri akışında şu adımlar olur. Ham tabloyu alırız, temizleriz ve tabloya yazarız. Sonra zenginleştirir, tekrar tabloya yazarız. Böylece birçok ara tablo birikir. Her sorgunun çalıştırılmasının bir maliyeti vardır. Her tabloyu saklamanın da ayrı bir maliyeti. Günlük olarak çalışan bir veri hattında bu maliyetler hızla katlanır. Araştırmalar ve en iyi uygulamalar da aynı şeyi söyler. Gereksiz veri çoğaltmadan kaçınmalı ve mümkün olduğunda anlık hesaplamayı tercih etmelisin. Adım 2. Ara tablolar yerine view kullan. Uygulama. Her adımda yeni tablo oluşturmak yerine SQL sorgunu view olarak kaydetmelisin. BigQuery bir view'u sadece sorguladığında hesaplar. Böylece ek depolama maliyetinden kaçınır, sadece sorgunun maliyetini ödersin. Sonuç daha az tablo, daha düzenli sistem, daha düşük maliyet. Adım 3. Ne zaman tablo oluşturmalı? Uygulama kuralları ve uyarılar. Elbette her şeyi view ile çözmek mümkün değil. Bazı durumlarda tabloya yazmak gerekir. Sık çalıştırılan ve ağır sorgular varsa, geçmişin sabit bir snapshot halini saklamak gerekiyorsa, yavaş değişen boyutlar kaydediliyorsa. Ama ara adımlar için en iyi tercih her zaman view kullanmaktır. Özet. Eski yöntem, sorgu, tablo, sorgu, tablo eşittir, artan işlem artı depolama maliyeti. Daha iyi yöntem, adımları view olarak kaydet, sadece okunduğunda hesapla, yalnızca performans veya yasal gereklilik olduğunda tabloyu oluştur. Sonuç, ara adımlarda view kullanarak depolamayı azalt ve veri hattını sadeleştir. Sadece sık okunan ve snapshot alınması gereken verileri tabloya yaz. Hem maliyetlerin hem de gelecekteki iş yükün sana teşekkür edecek.
