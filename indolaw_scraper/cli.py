import click
import json
from indolaw_scraper.models.document import LegalDocument
from indolaw_scraper.scraper.mahkamah_agung import get_detail_data as scrape_ma
from indolaw_scraper.scraper.kpu import (
    scrape_kpu_regulation_detail,
    map_kpu_data_to_legal_document_format,
)
from indolaw_scraper.scraper.bpk import get_detail_data as scrape_bpk
from indolaw_scraper.scraper.kemendikdasmen import get_detail_data as scrape_kemendikdasmen
from indolaw_scraper.scraper.kementan import get_detail_data as scrape_kementan
from indolaw_scraper.scraper.kkp import get_detail_data_kkp as scrape_kkp
from indolaw_scraper.scraper.kemenkeu import (
    get_detail_data as scrape_kemenkeu
)
from indolaw_scraper.scraper.marves import get_detail_data_marves as scrape_marves
from indolaw_scraper.scraper.kemendag import get_kemendag_data as scrape_kemendag
from indolaw_scraper.scraper.kemenpora import scrape_kemenpora_detail
from indolaw_scraper.scraper.pu import scrape_pu_detail
from indolaw_scraper.scraper.kehutanan import scrape_forestry_document as scrape_kehutanan
from indolaw_scraper.scraper.itb import scrape_itb_detail
from indolaw_scraper.scraper.dpr import scrape_dpr_detail


@click.command()
@click.option(
    '--source',
    required=True,
    help='Sumber dokumen: ma, kpu, kemendikbud, kementan, kkp, bpk, kemenkeu, kominfo, marves, pu, kemenpora, kehutanan, itb, dpr'
)
@click.option('--url', help='URL detail dokumen yang ingin di-scrape (mode tunggal)')
@click.option('--bulk', is_flag=True, help='Aktifkan mode scrape banyak dokumen (khusus kemenkeu)')
@click.option('--pages', default=1, type=int, help='Jumlah halaman yang ingin diambil saat mode bulk')
@click.option('--output', default=None, help='Nama file JSON untuk menyimpan hasil (opsional)')
def main(source, url, bulk, pages, output):
    """Command Line Interface for IndoLaw Scraper"""
    try:
        # ======================
        # MODE KHUSUS KEMENKEU - COMMENT DULU KARENA ADA FUNGSI YANG TIDAK ADA
        # ======================
        if source == "kemenkeu":
            # Hapus bagian bulk untuk sementara karena scrape_kemenkeu_bulk tidak ada
            if not url:
                raise click.BadParameter("Harus menyertakan --url untuk mode tunggal.")
            data = scrape_kemenkeu(url)
            click.secho(f"\n=== DETAIL DOKUMEN KEMENKEU ===", fg="green", bold=True)
            print(json.dumps(data, indent=2, ensure_ascii=False))
            return

        # ======================
        # SUMBER LAIN
        # ======================
        if source == "ma":
            data = scrape_ma(url)

        elif source == "kpu":
            raw = scrape_kpu_regulation_detail(url)
            if raw:
                mapped = map_kpu_data_to_legal_document_format(raw)
                data = LegalDocument(**mapped).to_dict()
            else:
                raise ValueError("Gagal mengambil data dari KPU.")

        elif source == "kemendikbud":
            data = scrape_kemendikdasmen(url)

        elif source == "kementan":
            data = scrape_kementan(url)

        elif source == "kkp":
            data = scrape_kkp(url)

        elif source == "bpk":
            data = scrape_bpk(url)
            
        elif source == "dpr":
            data = scrape_dpr_detail(url)

        elif source == "marves":
            data = scrape_marves(url)

        elif source == "pu":
            data = scrape_pu_detail(url)

        elif source == "kemenpora":
            data = scrape_kemenpora_detail(url)

        elif source == "kehutanan":
            data = scrape_kehutanan(url)

        elif source == "itb":
            data = scrape_itb_detail(url)

        else:
            raise ValueError("Sumber dokumen tidak dikenali.")

        click.secho(f"\n=== DETAIL DOKUMEN {source.upper()} ===", fg="green", bold=True)
        for k, v in data.items():
            print(f"{k}: {v}")

        # Simpan ke file jika ada parameter output
        if output:
            with open(output, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            click.secho(f"\n📁 Data disimpan ke: {output}", fg="cyan")

    except Exception as e:
        click.secho(f"❌ Terjadi kesalahan: {e}", fg="red")


if __name__ == "__main__":
    main()

