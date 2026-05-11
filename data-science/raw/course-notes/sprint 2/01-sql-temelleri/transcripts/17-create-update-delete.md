---
sprint: 2
lesson_slug: 01-sql-temelleri
video_slug: 17-create-update-delete
video_file: videos/17-create-update-delete.mp4
duration_seconds: 121
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:24:11Z
tags: [transcript, sprint-2]
---

# Create update delete

> Otomatik transkript — kaynak: `videos/17-create-update-delete.mp4` (ders: Sql Temelleri). Düzeltmeler için video referans alınmalıdır.

Şimdiye kadar SQL'de yaptığımız her şey, select, where, order by, sadece veriye bakmaktı. Yani veri tabanının kendisinde hiçbir değişiklik yapılmadı. Ama bazı komutlar var ki bu verileri kalıcı olarak değiştirirler. İşte bunlar create, update ve delete. Şimdi bunları tek tek inceleyelim. Create, yeni bir şey oluşturur. Yeni bir tablo, yeni bir veri tabanı ya da bazen yeni bir sütun. Örneğin, bu komut, üyeliği premium olan müşterileri seçerek premium alt tre customers adında yeni bir tablo oluşturur. Bu komut sistemine gerçekten yeni bir tablo yazdırır. Update, var olan kayıtları değiştirir. Diyelim ki yöneticin şöyle diyor, Boston'daki tüm müşterileri East bölgesine ata. O zaman şöyle yazmalısın. Bu komut, city değeri Boston olan müşterilerin region alanını East olarak günceller. Ama dikkat et, eğer where koşulunu unutursan, tablodaki tüm satırları değiştirirsin. Delete, satırları kalıcı olarak siler. Örneğin, bu komut, city değeri test will olan müşteri kayıtlarını kalıcı olarak siler. Bu durumda, test will şehrine ait kayıtlar tablodan tamamen silinir. Bir benzetmeyle düşünebiliriz. Select, fotoğraf albümüne bakmak gibidir. Update ve delete ise o fotoğrafları düzenlemek gibidir. Bir sayfa eklemek, bir altyazıyı değiştirmek ya da bir fotoğrafı yırtıp çıkarmak gibi. Yani yaptığın değişiklik kalıcı olur. En iyi uygulama, önce etkilenecek satırları görmek için her zaman bir select sorgusuyla test et. Ayrıca, update veya delete çalıştırmadan önce mutlaka yedeğini al. Çünkü eksik bir where ifadesi önemli verileri tamamen silebilir. Özetle, create yeni şeyler oluşturur. Update mevcut verileri değiştirir. Delete ise kalıcı olarak siler.
