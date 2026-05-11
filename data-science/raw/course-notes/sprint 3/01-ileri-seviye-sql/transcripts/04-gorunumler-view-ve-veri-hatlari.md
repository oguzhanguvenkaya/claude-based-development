---
sprint: 3
lesson_slug: 01-ileri-seviye-sql
video_slug: 04-gorunumler-view-ve-veri-hatlari
video_file: videos/04-gorunumler-view-ve-veri-hatlari.mp4
duration_seconds: 182
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:37Z
tags: [transcript, sprint-3]
---

# Gorunumler view ve veri hatlari

> Otomatik transkript — kaynak: `videos/04-gorunumler-view-ve-veri-hatlari.mp4` (ders: Ileri Seviye Sql). Düzeltmeler için video referans alınmalıdır.

Görünümler, SQL'de tekrar kullanılabilir tarif kartları gibidir. Tüm mantığı tek bir yerde tutarlar, neredeyse hiç depolama alanı harcamazlar ve birbirine zincirlenebilirler. Performans veya maliyet gerektirdiğinde bir adımı gerçek bir tabloya veya hız sağlamak için materialized view'e pişirilmiş hale getirebilirsin. Ben bir SaaS şirketinde veri analistiyim. Ürün, pazarlama ve finans ekitlerinin hepsi aynı KPI'yi istiyor. Plan A ve bölgeye göre günlük aktif kullanıcı sayısı. BI aracımızın tek, temiz ve tutarlı bir kaynağa ihtiyacı var. Her adım için yeni tablolar oluşturmak yerine görünüm view kullanacağım ve sadece gerektiğinde materyalize edeceğim. Adım 1. Temel görünümleri oluştur, tekrar kullanılabilir tarif. İlk adım, ham veriyi düzenli ve anlaşılır bir formata getirmek. Olayları temizlemek için bir görünüm, kullanıcı ve plan bilgilerini birleştirmek için başka bir görünüm oluşturuyorum. Artık herkes, temiz event nedir ya da plan bilgisi nasıl hesaplanıyor tek bir yerde bulabiliyor. Adım 2. Görünümleri zincirle ve sadece görünüm bazlı bir hat oluştur. Henüz tablo yok. Sonra bu temel görünümleri birbirine bağlıyorum. Örneğin, önce günlük aktif kullanıcıları hesaplayan bir görünüm, ardından bu sonucu plana ve bölgeye göre ayıran başka bir görünüm oluşturuyorum. BI aracının sadece bu son görünüme bağlanması yeterli. Ek tablo yok, fazladan depolama yok, sadece tek bir doğru kaynak. Adım 3. Sadece gerektiğinde materialize et. Görünüm ve tablo yöntemi. Tabii bazı durumlarda yalnızca görünümler yeterli olmayabilir. Örneğin, sık kullanılan bir dashboard yavaş çalışıyorsa veya aynı sorgu yüzlerce kez çalıştırılıyorsa bu adımı tabloya yazabilirsin. Bu biraz daha fazla depolama alanı gerektirir ama performans kazandırır. Benzetme. View, tarif kartı. İstediğin zaman yeniden kullanabilirsin. Materialize table veya view, önceden pişmiş kek. Sunumu hızlıdır ama dolapta yer kaplar. Zincirlenmiş görünümler, tarif adımlarından oluşan bir üretim hattı. Açık, modüler ve malzemeleri kolayca değiştirebilirsin. Özet. Görünümler satır değil mantık saklar. Tekrar kullanım için harika ve neredeyse sıfır depolama gerektirir. Sadece görünüm bazlı hatlar çeviktir. Performans için sadece yoğun kullanılan adımları materyalize etmelisin. Her iki yaklaşımda geçerli. Kararını verinin tazeliğine, maliyete ve dashboard hızına göre vermelisin. Sonuç. Varsayılan olarak görünümleri tarifi gibi kullan. Hız veya ölçek gerektiğinde seçici bir şekilde materyalize et. Bu şekilde BI hattın hızlı, tutarlı ve kolay yönetilebilir olur.
