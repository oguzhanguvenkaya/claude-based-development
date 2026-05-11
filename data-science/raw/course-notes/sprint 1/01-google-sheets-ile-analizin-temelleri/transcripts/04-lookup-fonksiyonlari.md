---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 04-lookup-fonksiyonlari
video_file: videos/04-lookup-fonksiyonlari.mp4
duration_seconds: 180
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:27Z
tags: [transcript, sprint-1]
---

# Lookup fonksiyonlari

> Otomatik transkript — kaynak: `videos/04-lookup-fonksiyonlari.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

XLookup'ı modern bir arama aracı gibi düşün. Analiz. Bir analist olarak sıradaki görevim, iki farklı tablodaki verileri birbirine bağlamak. Bu, analistlerin sıklıkla yaptığı bir iştir. Durum şöyle, bir sayfada müşteri kayıt listem var ve her müşteriye ait Node ID'ler bulunuyor. Diğer sayfada ise bu Node ID'lerle ilgili ek bilgiler var. Örneğin müşterinin Facebook, Google Ads gibi hangi platformdan geldiği. Görevim, bu tabloları eşleştirip kayıtların hangi kaynaktan geldiğini analiz edebilmek. Adım 1. Sorunu anlamak. Eğer tabloları elle eşleştirmeye çalışırsam, sign-up tablosundaki Node ID 454 ile kaynak tablosundaki Node ID 454'ün gerçekten aynı olduğunu garantileyemem. Özellikle de listeler sıralı değilse karışıklık çıkar. Adım 2. VLOOKUP kullanmak. Bu noktada VLOOKUP fonksiyonunu kullanmalıyım. Formül şöyle görünüyor. Eşittir. VLOOKUP 454 A1D1002 FALSE. Bu formülle size diyorum ki, bu Node ID'yi kaynak tablosunda dikey olarak bul. Bulduğunda ikinci sütünündeki değeri getir. Böylece ana tablomdaki her kaydı ilgili platform bilgisiyle bağlamış oluyorum. VLOOKUP'ı bir telefon rehberinde isim bulup yanındaki numarayı almak gibi düşünebilirsin. Adım 3. Hatalardan kaçınmak. Son argümanı FALSE olarak ayarladım. Böylece sadece tam eşleşme olduğunda değer getiriyor. Eğer ID yoksa hashtag NA döner. Yanlış bilgi gelmesindense hata görmeyi tercih ederim. Adım 4. Diğer lookup seçenekleri. Bir de daha gelişmiş bir seçenek var. XLOOKUP. Formül şöyle. Eşittir. XLOOKUP 454 AAA NOT FOUND 0. Bu fonksiyonun avantajları arama yapılan sütünün ilk sütün olması gerekmiyor. Veriyi bulamazsa ne döndüreceğini belirtebilirim. Söz dizimi daha basit ve esnek. XLOOKUP'ı modern bir arama aracı gibi düşün. Tablo nasıl yapılandırılmış olursa olsun doğru eşleşmeyi bulur. Sonuç. Artık kayıt ve kaynak tabloların birbirine bağlı. Her platformdan kaç müşterinin geldiğini net olarak görebiliyorum. Kısa özet. VLOOKUP dikey arama. Yani bir telefon rehberinde ismi bulup yanındaki numarayı almak gibi. XLOOKUP ise evrensel arama. Telefonda bir arkadaşının adını yazdığında nerede kayıtta olursa olsun onu bulması gibi. Dikey veya yatay çalışır. Daha esnektir. Bulunamazsa ne olacağını sen belirlersin.
