---
sprint: 3
lesson_slug: 01-ileri-seviye-sql
video_slug: 09-fiyatlandirma-modelleri
video_file: videos/09-fiyatlandirma-modelleri.mp4
duration_seconds: 197
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:25:51Z
tags: [transcript, sprint-3]
---

# Fiyatlandirma modelleri

> Otomatik transkript — kaynak: `videos/09-fiyatlandirma-modelleri.mp4` (ders: Ileri Seviye Sql). Düzeltmeler için video referans alınmalıdır.

Büyüyen bir SaaS şirketinde veri analisti olarak çalışıyorsun. Finans ekibi sana şunu soruyor: Analitik platformumuzu on-demand fiyatlandırmaya mı geçirelim yoksa sabit ücretli flat bir plan mı kullanalım? Senin görevin her iki seçeneği de modelleyip depolama ve işlem açısından en uygun olanı önermek. Yöntem: Adım 1: Kullanım profilini çıkar. Adım 2: İki maliyet modeli oluştur: on-demand ve flat. Adım 3: Toplam maliyetleri, değişkenliği ve birim maliyetlerini karşılaştır. Adım 4: Bir karar kuralı oluştur ve hibrit seçeneği de göz önünde bulundur. Adım 1: Problem: Son altı aydaki kullanım düzeyiniz. Bazı aylarda 50 GB depoluyorsun ve küçük işlemler yapıyorsun, ürün lansmanı döneminde ise kullanım dört katına çıkıyor. Yanlış fiyatlandırma modeli seçmek on-demand'de yüksek fatura şoku yaratabilir ya da flat modelde kaynak israfına neden olabilir. Adım 2: Analiz: Kullanım profilini belirliyorsun. Ortalama, tepe değerleri ve dalgalanma oranını ölçüyorsun. Adım 3: Karar: İki maliyet modelini yan yana karşılaştırıyorsun. Talep tabanlı model esnek ama değişken, sabit model öngörülebilir ama bazen gereğinden pahalı. Genellikle çözüm hibrittir: Temel kullanım için flat, ani artışlar için on-demand. Adım 4: Karar kuralı: Depolama ve işlem göz önünde bulundurularak. On-demand'ı seç: Kullanım dalgalı veya mevsimselse, deneme aşamasındaysan veya başlangıç sürecindeysen, öngörülebilirlikten çok esnekliği önemsiyorsan. Flat'i seç: Kullanımın sabitse ve kaynaklarını sürekli yüksek verimle kullanabiliyorsan, aylık harcamalarının önceden belirlenmesini istiyorsan. Hibriti düşün: Öngörülebilir temel tüketim için flat, ani artışlar için on-demand. Birçok ekip maliyet ve riski dengelemek için bu yaklaşımı tercih ediyor. Benzetme: On-demand taksimetre gibi; ne kadar yol gidersen o kadar ödersin. Flat açık büfe gibi; ne kadar tüketirsen tüket, tek bir fiyat ödersin. Uygulamada dikkat edilecekler: En az 3-6 aylık kullanım verisini analiz et. Zirve dönemleri dahil olsun. Bütçe uyarıları ve harcama limitleri belirle. Aylık olarak kullanımı izle. Sözleşme detaylarını iyi incele. Ek ücret, kısıtlama ve veri çıkış ücretleri tabloyu değiştirebilir. Mevsimselliği göz ardı etme; kampanyalar, lansmanlar ve tatiller maliyetleri etkileyebilir. Depolama ile işlem davranışlarını aynı varsayma; her birini ayrı değerlendirmelisin. Özet: On-demand sadece kullandığın kadar ödersin; değişken veya deneme amaçlı senaryolar için idealdir. Flat her dönem aynı ücreti ödersin; sabit ve yüksek kullanım için uygundur. Her iki modelde depolama ve işlem için geçerli, hibrit model genelde maliyeti ve kontrolü dengelemek için en iyi yaklaşımdır. Sonuç: Kullanımın dalgalanıyorsa, on-demand ile başla ve ölçüm yap. Kullanımın sabit ve yüksekse, flat modeli değerlendir. Ya da ikisini karıştır: Temel için flat, ani artışlar için on-demand. Kullanım desenine göre modeli şekillendir, böylece hem maliyeti hem de esnekliği kontrol edebilirsin.
