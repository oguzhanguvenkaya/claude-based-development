---
sprint: 1
lesson_slug: 01-google-sheets-ile-analizin-temelleri
video_slug: 03-veri-kesfi-ve-temizlenmesi
video_file: videos/03-veri-kesfi-ve-temizlenmesi.mp4
duration_seconds: 196
model: gpt-4o-transcribe
language: tr
transcribed_at: 2026-05-10T18:22:27Z
tags: [transcript, sprint-1]
---

# Veri kesfi ve temizlenmesi

> Otomatik transkript — kaynak: `videos/03-veri-kesfi-ve-temizlenmesi.mp4` (ders: Google Sheets Ile Analizin Temelleri). Düzeltmeler için video referans alınmalıdır.

Adım 2: Google Sheets'te Verileri Keşfet ve Temizle

Bir analist olarak müşteri kayıt verilerini az önce içe aktardım ama bir sorun var. Tarihler gerçek tarih formatında değil, metin olarak geliyor. Bazı hücrelerin sonunda UTC yazısı var. Bir sütunda da ad ve soyadı tek bir tam isim olarak birleştirmem gerekiyor. İşim, verileri adım adım temizleyip analiz için hazır hale getirmek.

Adım 1: Metni Temizle

İlk olarak, Bul ve Değiştir'i kullanarak birkaç satırdaki UTC yazısını manuel olarak kaldırıyorum. İşe yarıyor ama yeni satırlar gelmeye devam ederse çok yavaş kalır. Bu yüzden SUBSTITUTE fonksiyonuna geçiyorum. Tek bir formülle tüm UTC kısımları kayboluyor. Çok daha hızlı.

SUBSTITUTE, bir dikiş makinesi gibi çalışır. Her hatayı elle düzeltmek yerine, tüm satırları otomatik olarak düzeltir.

Sonra başka bir sütunda ad ve soyadı birleştirmem gerekiyor. Burada CONCATENATE fonksiyonunu, boşluk sembolünü kullanarak tam isim haline getiriyorum.

CONCATENATE, Lego bloklarını birleştirmek gibidir ve istediğiniz kadar elementi birleştirebilirsiniz.

Adım 2: Hücre Formatını Düzelt

Şimdi, Sheets'in tarihlerimi gerçek tarih olarak görmesini sağlamalıyım. Sorun şu ki, bunlar metin olarak saklanıyor ve Sheets bunları gerçek tarih olarak algılamıyor. Temizlenmiş metni DATEVALUE fonksiyonuna sarıyorum. Aniden, Sheets bunları düzgün bir şekilde tanıyor, böylece hesaplamalarda kullanabiliyorum.

Metin olarak saklanan sayılar için aynısını VALUE fonksiyonuyla yapabilirim. Örneğin, "123" metni, 123 sayısına dönüşür.

Eğer sözdizimini unutursam, E-A'ya soruyorum: "Metni sayıya çeviren formül nedir?" Çok basit bir örnek ekle. Ezberlemeye çalışmaktan daha hızlı.

Adım 3: Tarihlerle Çalış

Tarihlerim temizlendikten sonra, bunlarla hesaplama yapabilirim. DATEDIF'i kullanarak her kayıttan bu yana kaç gün geçtiğini buluyorum. Ona bir başlangıç tarihi, bir bitiş tarihi ve birim veriyorum. Günler için "D", aylar için "M", yıllar için "Y" gibi. İki tarih arasındaki farkı hesaplıyor.

Tarihin parçalarını da çıkarabilirim. Yılı çıkarmak için "YEAR(date)". Ayı çıkarmak için "MONTH(date)". Günü çıkarmak için "DAY(date)". Yıl içindeki hafta numarası için "WEEKNUM(date)". Parçalardan tarih oluşturmak için "DATE(year, month, day)" kullanılır.

Özet olarak, analizden önce temizle ve formatla. Fonksiyonlar, dağınık ham verileri tutarlı ve analize hazır verilere dönüştürür.
