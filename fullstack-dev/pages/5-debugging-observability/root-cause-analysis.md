---
title: "Root Cause Analysis"
domain: fullstack-dev
category: 5-debugging-observability
type: playbook
level: foundation
created: 2026-04-13
updated: 2026-04-13
sources: []
tags:
  - debugging
  - root-cause
  - analysis
  - incident
---

# Root Cause Analysis (RCA)

> One-line summary: Bir bug'ı düzeltmek değil, **neden olduğunu** anlamak için sistematik yaklaşım. Symptom fix yerine root cause fix, aynı sorunun tekrar çıkmasını engeller.

## Why It Matters (Senior Perspective)

Junior bug'ı fix eder. Senior **neden olduğunu** anlar ve **aynı class'ın** bug'larının da önünü keser. Fark devasadır: junior aynı pattern'i 5 kez fix eder, senior 1 kez root cause'u çözer.

> "Fix" ≠ "fixed". Kod çalışıyor olmak bug'ın nedeninin anlaşıldığı anlamına gelmez. Senior refleksi: "Bug ortadan kalktı ama **neden** olduğunu biliyor muyum?"

AI "hızlı fix" üretmede usta, root cause analysis'te zayıf. Bu yüzden AI-assisted debug'ta RCA senin işin.

## Core Concept

Root cause = bir problemin **nihai nedeni**, ara sonuç değil. Örnek:
- **Symptom:** Kullanıcı ödeme yapamıyor
- **Proximate cause:** Payment API 500 dönüyor  
- **Intermediate cause:** DB connection pool dolu
- **Root cause:** Bir analytics query N+1 pattern ile idle connection tüketiyor

İlk iki katmanda fix yapsan (API restart, payment retry) problem 3 gün sonra geri gelir. Root cause fix edildikten sonra geri gelmez.

## The 5 Whys

En basit ama en güçlü RCA tekniği. "Neden?" sorusunu **5 kez** üst üste sor — her cevabın nedenini araştır.

### Örnek: "Website yavaş"
1. **Neden yavaş?** → Database query'leri uzun sürüyor
2. **Neden uzun sürüyor?** → Index kullanılmıyor
3. **Neden kullanılmıyor?** → Son migration'da index drop edildi
4. **Neden drop edildi?** → Migration'u yazan kişi eski index'i bilmiyordu
5. **Neden bilmiyordu?** → Index'ler dökümante değil

**Root cause:** Index'lerin dökümante edilmemesi. Fix: index katalogu ekle + PR review checklist'e index kontrolü.

Not: Her zaman tam 5 değil. Bazen 3, bazen 7. Ama "hemen fix yap"'a kaçma, cevabın cevabını sor.

## The Decision Framework — Investigation Order

Bir bug geldiğinde sırayla:

1. **Reproduce:** Bug'ı güvenilir şekilde tetikleyebiliyor musun? Edemiyorsan RCA imkansız.
2. **Isolate:** Hangi koşulda var, hangi koşulda yok? Minimal reproducible example bul.
3. **Hypothesize:** Neden olabilir? 2-3 hipotez kur.
4. **Test:** Her hipotezi doğrulanabilir şekilde test et.
5. **Confirm:** Root cause'u **kanıtla**, tahmin etme.
6. **Fix:** Root cause'u fix et, symptom'u değil.
7. **Prevent:** Aynı class'ın bug'larını nasıl önlersin? Tests, monitoring, documentation.

## Patterns (Do This)

### 1. Reproduce First, Fix Later
Bug'ı reproduce edemiyorsan fix'i de doğrulayamazsın. İlk 15 dakikan reproduction'a git.

### 2. Minimal Reproducible Example
Complex case'i giderek daralt. En küçük "hala bozuk" versiyonunu bul. Bu, root cause'u görünür yapar.

### 3. Bisect in Time
"Dün çalışıyordu, bugün bozuk" → git bisect ile hangi commit kırdı. Commit count'u log(n), root cause hızlı bulunur.

### 4. Changelog Check
Üretilen değişiklikleri incele — code, config, data, infra. Değişiklik penceresi dar ise bunlardan biri.

### 5. Hypothesis-Driven Debug
"Sanırım X yüzünden" — kanıtla veya çürüt. Rastgele değişiklik yapma, test-driven debug.

### 6. Write Down What You Know
Investigation sırasında notlar al. Bug report'una yaz, slack'e yaz — self-reference için bile olsun. İnsan hafızası yanıltır.

### 7. Post-Mortem After Fix
Incident kapandı → "ne olmuştu, nasıl olmuştu, gelecekte nasıl önleyeceğiz?" dokümanı. Blame-free.

## Anti-Patterns (Don't Do This)

### Fix the Symptom
Error handler ekle, log'la, swallow et → bug görünmez olur ama var olmaya devam eder.

### First Hypothesis Trust
"İlk kafama gelen muhtemelen budur" → rastgele fix → bazen işe yarıyor → confirmation bias.

### Random Changes
"Bunu değiştireyim bakalım ne olacak" → çözdü gibi olur ama **neden** bilmiyorsun. Geri gelir.

### Stop at Proximate Cause
"API 500 dönüyordu, restart ettik" → arka planda DB bozuk. 3 saat sonra yine 500.

### Skip Reproduction
"Tek seferlik olmuş olabilir" → aynı şey 100 kullanıcıda var ama log yok. Production incident'a gider.

### Blame-Driven RCA
"X kişisi yaptı" → insan odaklı değil, sistem odaklı analiz yap. Aynı insan aynı sistemdeyken aynı hatayı yapacak.

### No Post-Mortem
Fix'ten sonra dosyayı kapat, lesson yok → aynı bug'ı farklı yerde yaparsın.

## The Fishbone Diagram (Ishikawa)

Complex sistemde 5 Whys yetmez. Root cause kategorileri:

```
                  SYMPTOM
                     │
     ┌───────┬───────┼───────┬───────┐
     │       │       │       │       │
   CODE    DATA   CONFIG   INFRA   PROCESS
     │       │       │       │       │
  Logic   Schema  Env var  Network  Review
  bug   migration  missing  blip   failure
  Race   Corrupt   Wrong    DB     No test
  cond.   record   value   slow   coverage
```

Her kategoride birkaç hipotez türet. Eleme yöntemiyle root cause'a in.

## Gotchas

- **Flaky reproduction:** Bug bazen var bazen yok → race condition veya environment-dependent
- **Heisenbug:** Debug eklediğinde bug kaybolur → timing-sensitive
- **Correlation ≠ causation:** İki şey aynı anda olmuş ama biri diğerinin sebebi değil
- **Hidden dependency:** Bug'ın sebebi code'da değil, config'de veya external dep'te
- **Data-specific:** Bug belirli bir data shape ile var, diğer data'yla yok
- **Time-based:** Bug belirli bir tarihte/saatte var (timezone, DST, quota reset)
- **Concurrent triggers:** İki neden aynı symptom → tek birini fix, yarısı çözülüyor

## Connections

- Related: [[Structured Logging]], [[What Could Go Wrong]], [[Edge Case Thinking]]
- Leads to: [[Debugging Playbook]], [[Incident Response]], [[Testing Strategy]]
- Used by: [[Adding a New Feature]] (bug fix workflow)
- Contrast with: Symptom-treating (quick fix)

## Real Examples (From My Projects)

- **MarketPulse:** "Bazı ürünlerin fiyatı yanlış" bildirimi geldi. İlk hipotez: scraping bug. Reproduce ettik, 5 Whys: scraping doğru → parser doğru → DB yazımı doğru → ama frontend yanlış gösteriyor → frontend'te currency conversion hard-coded "USD to TRY" → ama bazı ürünler EUR'du. Root cause: currency metadata'sı scrape edilmiyordu. Fix tüm conversion logic'i yeniledi.
- **menzernaturkiye:** Random "500 internal error" geliyordu, reproduce edemiyorduk. Log'larda pattern aradık, belirli bir endpoint'te daha sık olduğunu gördük. Minimal repro: o endpoint + belirli bir product ID. Root cause: product description'da emoji vardı, DB encoding utf8 değil utf8mb4'tü. Fix: DB charset migration.
- **prompt_generator:** "Prompts kayboluyor" bildirimi. İlk reaction: "data loss, kritik!". Reproduce ettiğimizde görüldü ki kaybolmuyor — filter aktifti ve search term'e uymuyordu. Root cause: UX problem, empty state'i yanıltıcı. Symptom fix (search clear button) + root cause fix (empty state message "filter aktif, X sonuç gizli").

## My Notes
- Buraya kendi gözlemlerini ekle
