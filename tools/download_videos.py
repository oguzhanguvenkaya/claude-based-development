"""Batch Vimeo video downloader for WorkInTech course videos.

Reads VIDEOS list (clip_id, lesson_folder, video_filename) and downloads
each via yt-dlp at 720p with Turkish audio, into the lesson's videos/ subfolder.

Skips already-existing files. Logs failures to download_videos.log.
"""

from __future__ import annotations
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

CONCURRENCY = 4
_log_lock = Lock()

BASE = Path(r"c:\Users\oguzhan\Desktop\claude-based-development\data-science\raw\course-notes")
REFERER = "https://nextgen.workintech.com.tr/"
LOG = Path(__file__).parent / "download_videos.log"

# (clip_id, lesson_folder_relative_to_BASE, output_filename_without_ext)
VIDEOS: list[tuple[str, str, str]] = [
    # === SPRINT 1 / DERS 1 — Google Sheets ile Analizin Temelleri ===
    ("1172437995", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "01-veri-analizinin-asamalari"),
    ("1172438203", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "02-google-sheetse-import-etmek"),
    ("1172438434", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "03-veri-kesfi-ve-temizlenmesi"),
    # 04-lookup-fonksiyonlari and 05-pivot-tablo already downloaded
    ("1172439275", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "06-veriyi-filter-ile-filtrelemek"),
    ("1172439480", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "07-veriyi-query-ile-filtrelemek"),
    ("1172554166", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "08-veriyi-unique-ile-filtrelemek"),
    ("1172439834", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "09-lookup-kullanarak-veri-temizleme"),
    ("1172440077", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "10-index-match-ile-analiz"),
    ("1172440399", r"sprint 1\01-google-sheets-ile-analizin-temelleri", "11-veriyi-gorsellestirme"),

    # === SPRINT 1 / DERS 2 — KPI'ın Temelleri ===
    ("1128611314", r"sprint 1\02-kpi-temelleri", "01-adim-1-sorular-sor"),
    ("1128611480", r"sprint 1\02-kpi-temelleri", "02-adim-2-veri-ihtiyaclarini-belirle"),
    ("1128611538", r"sprint 1\02-kpi-temelleri", "03-adim-3-analiz-turunu-sec"),
    ("1128611627", r"sprint 1\02-kpi-temelleri", "04-adim-4-veriyi-kesfet"),
    ("1128611689", r"sprint 1\02-kpi-temelleri", "05-adim-5-verileri-temizle"),
    ("1128611745", r"sprint 1\02-kpi-temelleri", "06-adim-6-icgorulerini-ozetle"),
    ("1128611795", r"sprint 1\02-kpi-temelleri", "07-adim-7-sonuclari-gorsellestir"),
    ("1128611836", r"sprint 1\02-kpi-temelleri", "08-sonuc-ve-yinelemenin-onemi"),
    ("1128611901", r"sprint 1\02-kpi-temelleri", "09-kpi-nedir"),
    ("1128611932", r"sprint 1\02-kpi-temelleri", "10-kpi-metrik-farki"),
    ("1128612029", r"sprint 1\02-kpi-temelleri", "11-finans-kpilari"),
    ("1128612138", r"sprint 1\02-kpi-temelleri", "12-envanter-kpilari"),
    ("1128612244", r"sprint 1\02-kpi-temelleri", "13-kalite-kpilari"),

    # === SPRINT 1 / DERS 3 — İleri Seviye KPI'lar ===
    ("1185573273", r"sprint 1\03-ileri-seviye-kpi", "01-farkli-sirketler-farkli-kpilar"),
    ("1185573731", r"sprint 1\03-ileri-seviye-kpi", "02-is-modeli-ve-kpi"),
    ("1185574268", r"sprint 1\03-ileri-seviye-kpi", "03-ticari-model-ve-olgunluk-seviyesi"),
    ("1128599318", r"sprint 1\03-ileri-seviye-kpi", "04-farkli-takimlar-farkli-kpilar"),
    ("1128686083", r"sprint 1\03-ileri-seviye-kpi", "05-kpi-seciminde-kacinilmasi-gerekenler"),
    # NOTE: 1128686083 also listed for 06-musteri-kazanim-hunisi (DUPLICATE in master file).
    # Skipping the second occurrence; user should provide correct clip_id later.
    ("1129167558", r"sprint 1\03-ileri-seviye-kpi", "07-musteri-kazanim-kanallari"),
    ("1128989750", r"sprint 1\03-ileri-seviye-kpi", "08-genisleme-hunisi"),
    ("1178482590", r"sprint 1\03-ileri-seviye-kpi", "09-segmentasyon-nedir"),
    ("1178483144", r"sprint 1\03-ileri-seviye-kpi", "10-segmentasyon-rfm-yontemi"),
    ("1129027935", r"sprint 1\03-ileri-seviye-kpi", "11-cohort-analizi"),

    # === SPRINT 1 / DERS 4 — Data Analiz Ekosistemi ===
    ("1128606101", r"sprint 1\04-data-analiz-ekosistemi", "01-veri-uzmanlarinin-rolu"),
    ("1128606684", r"sprint 1\04-data-analiz-ekosistemi", "02-is-ve-veri-ekipleri-arasindaki-isbirligi"),
    ("1128607796", r"sprint 1\04-data-analiz-ekosistemi", "03-muze-vaka-analizi"),
    ("1128608654", r"sprint 1\04-data-analiz-ekosistemi", "04-nestle-musteri-verisi-stratejisi"),
    ("1128616067", r"sprint 1\04-data-analiz-ekosistemi", "05-vodafone-yapay-zeka-botlari"),
    ("1128616112", r"sprint 1\04-data-analiz-ekosistemi", "06-veri-yasam-dongusu"),
    ("1180718143", r"sprint 1\04-data-analiz-ekosistemi", "07-veri-rolleri-i"),
    ("1180718497", r"sprint 1\04-data-analiz-ekosistemi", "08-veri-rolleri-ii"),
    ("1180718749", r"sprint 1\04-data-analiz-ekosistemi", "09-veri-rolleri-iii"),
    ("1128610049", r"sprint 1\04-data-analiz-ekosistemi", "10-olgunluk-duzeyine-gore-veri-ekip-yapisi"),
    ("1128616160", r"sprint 1\04-data-analiz-ekosistemi", "11-magaza-ici-satislarin-artirilmasi"),

    # === SPRINT 2 / DERS 1 — SQL'in Temelleri ===
    ("1129833737", r"sprint 2\01-sql-temelleri", "01-tanitim-ve-amaci"),
    ("1129833909", r"sprint 2\01-sql-temelleri", "02-tablolar-anahtarlar"),
    ("1129834118", r"sprint 2\01-sql-temelleri", "03-oltp-ve-olap-sistemleri"),
    ("1129834282", r"sprint 2\01-sql-temelleri", "04-entity-iliski-diyagramlari-erd"),
    ("1129894332", r"sprint 2\01-sql-temelleri", "05-select"),
    ("1129895029", r"sprint 2\01-sql-temelleri", "06-distinct"),
    ("1129893091", r"sprint 2\01-sql-temelleri", "07-verileri-filtreleme-where"),
    ("1129891158", r"sprint 2\01-sql-temelleri", "08-diger-anahtar-kelimelerle-filtreleme"),
    ("1129970141", r"sprint 2\01-sql-temelleri", "09-desen-eslestirme-pattern-matching"),
    ("1129970317", r"sprint 2\01-sql-temelleri", "10-in-ve-not-in-kullanimi"),
    ("1129970476", r"sprint 2\01-sql-temelleri", "11-takma-adlar-aliasing"),
    ("1129970587", r"sprint 2\01-sql-temelleri", "12-order-by-ile-siralama"),
    ("1129970746", r"sprint 2\01-sql-temelleri", "13-kosullu-sutunlar"),
    ("1129970911", r"sprint 2\01-sql-temelleri", "14-null-degerleri"),
    ("1130018738", r"sprint 2\01-sql-temelleri", "15-veri-turleri"),
    ("1130018911", r"sprint 2\01-sql-temelleri", "16-veri-turu-donusturme-casting"),
    ("1130019126", r"sprint 2\01-sql-temelleri", "17-create-update-delete"),

    # === SPRINT 2 / DERS 2 — SQL'de Hesaplanmış Veriler ===
    ("1130327289", r"sprint 2\02-sql-hesaplanmis-veriler", "01-aggregate-fonksiyonu-nedir"),
    ("1130838499", r"sprint 2\02-sql-hesaplanmis-veriler", "02-count-countif"),
    ("1130334512", r"sprint 2\02-sql-hesaplanmis-veriler", "03-sum-avg-min-max"),
    ("1130336927", r"sprint 2\02-sql-hesaplanmis-veriler", "04-safe-divide-fonksiyonu"),
    ("1130333959", r"sprint 2\02-sql-hesaplanmis-veriler", "05-group-by"),
    ("1130327800", r"sprint 2\02-sql-hesaplanmis-veriler", "06-where-ve-having-ile-filtreleme"),
    ("1130721509", r"sprint 2\02-sql-hesaplanmis-veriler", "07-sayisal-fonksiyonlar-round"),
    ("1130723097", r"sprint 2\02-sql-hesaplanmis-veriler", "08-concat-ile-sutunlari-birlestirme"),
    ("1130723507", r"sprint 2\02-sql-hesaplanmis-veriler", "09-sutunlardaki-metinleri-degistirme"),
    ("1130723949", r"sprint 2\02-sql-hesaplanmis-veriler", "10-buyuk-kucuk-harf-bicimi"),
    ("1130740971", r"sprint 2\02-sql-hesaplanmis-veriler", "11-date-sub-ile-zaman-araligi-cikarma"),

    # === SPRINT 2 / DERS 3 — Tabloları Birleştirmek ve Test Etmek ===
    ("1129684576", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "01-joine-giris"),
    ("1130015133", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "02-join-kullanimi"),
    ("1130036630", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "03-table-aliasing"),
    ("1130343562", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "04-join-turleri"),
    ("1130365688", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "05-coklu-join-islemleri"),
    ("1130645025", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "06-join-ve-group-by"),
    ("1130728117", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "07-join-dikkat-edilmesi-gerekenler"),
    ("1130813309", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "08-neden-test-ediyoruz"),
    ("1130827811", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "09-primary-key-testi"),
    ("1131049729", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "10-column-testi"),
    ("1131078551", r"sprint 2\03-tablolari-birlestirmek-ve-test-etmek", "11-deger-korunumu-testi"),

    # === SPRINT 2 / DERS 4 — Subquery ve With As ===
    ("1132015635", r"sprint 2\04-subquery-ve-with-as", "01-with-as-ile-query-tanimlama"),
    ("1132016572", r"sprint 2\04-subquery-ve-with-as", "02-ic-ice-query-nested-query"),
    ("1132041087", r"sprint 2\04-subquery-ve-with-as", "03-join-vs-nested-subquery"),
    ("1132063367", r"sprint 2\04-subquery-ve-with-as", "04-union"),
    ("1130983735", r"sprint 2\04-subquery-ve-with-as", "05-bigquery-insert-ve-cast-islemleri"),
    ("1130984932", r"sprint 2\04-subquery-ve-with-as", "06-temiz-kodun-onemi"),

    # === SPRINT 2 / DERS 5 — UDF + Window ===
    ("1131298344", r"sprint 2\05-fonksiyonlar-ve-window", "01-fonksiyonlari-ve-yerlesik-ornekleri-anlamak"),
    ("1131462458", r"sprint 2\05-fonksiyonlar-ve-window", "02-sqlde-fonksiyon-tanimlama-ve-cagirma"),
    ("1131859916", r"sprint 2\05-fonksiyonlar-ve-window", "03-neden-window-fonksiyonlarina-ihtiyacimiz-var"),
    ("1131862001", r"sprint 2\05-fonksiyonlar-ve-window", "04-partition-by-ve-over-kullanimi"),
    ("1132262848", r"sprint 2\05-fonksiyonlar-ve-window", "05-window-ile-farkli-detay-seviyelerinde-join"),

    # === SPRINT 3 / DERS 1 — İleri Seviye SQL ===
    ("1132044893", r"sprint 3\01-ileri-seviye-sql", "01-veri-hatti-genel-bakis"),
    ("1132045026", r"sprint 3\01-ileri-seviye-sql", "02-donusum-asamalari-ve-veri-modelleme"),
    ("1132058187", r"sprint 3\01-ileri-seviye-sql", "03-cok-tablo-maliyet-etkileri"),
    ("1132059064", r"sprint 3\01-ileri-seviye-sql", "04-gorunumler-view-ve-veri-hatlari"),
    ("1132059508", r"sprint 3\01-ileri-seviye-sql", "05-gorunumler-ve-tablolar-arti-eksi"),
    ("1132060158", r"sprint 3\01-ileri-seviye-sql", "06-karma-tablo-ve-gorunum-yaklasimi"),
    ("1132072924", r"sprint 3\01-ileri-seviye-sql", "07-veri-platformu-genel-bakisi"),
    ("1132073068", r"sprint 3\01-ileri-seviye-sql", "08-depolama-ve-isleme-ucretleri"),
    ("1132073171", r"sprint 3\01-ileri-seviye-sql", "09-fiyatlandirma-modelleri"),
    ("1132073268", r"sprint 3\01-ileri-seviye-sql", "10-modern-veri-ambarlarinin-karsilastirilmasi"),
    ("1132073419", r"sprint 3\01-ileri-seviye-sql", "11-bigquery-sorgu-maliyetleri"),
    ("1132073552", r"sprint 3\01-ileri-seviye-sql", "12-sutun-ve-satir-bazli-maliyetler"),
    ("1132073672", r"sprint 3\01-ileri-seviye-sql", "13-veri-bolumlendirme-partitioning"),
]


def log(msg: str) -> None:
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    with _log_lock:
        print(line, flush=True)
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def download_one(cid: str, out_dir: Path, name: str) -> tuple[bool, str]:
    out_file = out_dir / f"{name}.mp4"
    if out_file.exists() and out_file.stat().st_size > 100_000:
        return True, "exists"

    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--referer", REFERER,
        "-f", "bv*[height=720]+ba/b[height=720]/bv*+ba/b",
        "--merge-output-format", "mp4",
        "--no-warnings",
        "--quiet",
        "--no-progress",
        "-o", str(out_dir / f"{name}.%(ext)s"),
        f"https://player.vimeo.com/video/{cid}",
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if res.returncode == 0 and out_file.exists():
        return True, "downloaded"
    return False, (res.stderr or res.stdout or "unknown error").strip()[-300:]


def process(idx: int, total: int, cid: str, folder: str, name: str) -> tuple[str, str, str]:
    """Returns (status, target, info) where status in {ok, skip, fail}."""
    target = f"{folder}/videos/{name}.mp4"
    out_dir = BASE / folder / "videos"
    success, info = download_one(cid, out_dir, name)
    if success and info == "exists":
        log(f"[{idx}/{total}] SKIP (exists): {target}")
        return "skip", target, info
    if success:
        size = (out_dir / f"{name}.mp4").stat().st_size / (1024 * 1024)
        log(f"[{idx}/{total}] OK ({size:.1f} MB): {target}")
        return "ok", target, info
    log(f"[{idx}/{total}] FAIL: {target} :: {info}")
    return "fail", target, info


def main() -> int:
    LOG.write_text("", encoding="utf-8")
    log(f"Starting batch download: {len(VIDEOS)} videos (concurrency={CONCURRENCY})")
    ok = skip = fail = 0
    failures: list[tuple[str, str, str]] = []
    seen_cids: dict[str, str] = {}

    tasks: list[tuple[int, str, str, str]] = []
    for i, (cid, folder, name) in enumerate(VIDEOS, 1):
        target = f"{folder}/videos/{name}.mp4"
        if cid in seen_cids:
            log(f"[{i}/{len(VIDEOS)}] DUPLICATE clip_id {cid} → {target} (already used for {seen_cids[cid]}). SKIP.")
            failures.append((cid, target, f"duplicate of {seen_cids[cid]}"))
            fail += 1
            continue
        seen_cids[cid] = target
        tasks.append((i, cid, folder, name))

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = {ex.submit(process, i, len(VIDEOS), cid, folder, name): (cid, folder, name)
                   for i, cid, folder, name in tasks}
        for fut in as_completed(futures):
            cid, folder, name = futures[fut]
            try:
                status, target, info = fut.result()
            except Exception as e:
                log(f"EXCEPTION: {cid} → {folder}/videos/{name}.mp4 :: {e}")
                failures.append((cid, f"{folder}/videos/{name}.mp4", f"exception: {e}"))
                fail += 1
                continue
            if status == "ok":
                ok += 1
            elif status == "skip":
                skip += 1
            else:
                fail += 1
                failures.append((cid, target, info))

    log("=" * 60)
    log(f"DONE: ok={ok} skip={skip} fail={fail} total={len(VIDEOS)}")
    if failures:
        log("Failures:")
        for cid, target, err in failures:
            log(f"  - {cid} → {target} :: {err}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
