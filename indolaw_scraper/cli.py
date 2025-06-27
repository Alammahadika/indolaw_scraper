# cli.py

import click
import json
from indolaw_scraper.models.document import LegalDocument

from indolaw_scraper.scraper.mahkamah_agung import get_detail_data as scrape_ma
from indolaw_scraper.scraper.kpu import scrape_kpu_regulation_detail, map_kpu_data_to_legal_document_format
from indolaw_scraper.scraper.bpk import get_detail_data as scrape_bpk
from indolaw_scraper.scraper.kemendikdasmen import get_detail_data as scrape_kemendikdasmen
from indolaw_scraper.scraper.kementan import get_detail_data as scrape_kementan
from indolaw_scraper.scraper.kkp import get_detail_data_kkp



@click.command()
@click.option('--source', help='Sumber dokumen (ma/kpu/kemendikbud/bpk)', required=True)
@click.option('--url', help='URL detail dokumen', required=True)
def main(source, url):
    if source == "ma":
        data = scrape_ma(url)
        print("=== DETAIL DOKUMEN MAHKAMAH AGUNG ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kpu":
        raw = scrape_kpu_regulation_detail(url)
        if raw:
            mapped = map_kpu_data_to_legal_document_format(raw)
            try:
                doc = LegalDocument(**mapped)
                print("=== DETAIL DOKUMEN KPU ===")
                print(json.dumps(doc.to_dict(), indent=2, ensure_ascii=False))
            except Exception as e:
                print(f"Gagal membuat LegalDocument: {e}")
                print(json.dumps(mapped, indent=2, ensure_ascii=False))
        else:
            print("Gagal mengambil data dari KPU.")

    elif source == "kemendikbud":
        data = scrape_kemendikbud(url)
        print("=== DETAIL DOKUMEN KEMENDIKBUD ===")
        for k, v in data.items():
            print(f"{k}: {v}")
            
    elif source == "kementan":
        data = scrape_kementan(url)
        print("=== DETAIL DOKUMEN KEMENTAN ===")
        for k, v in data.items():
        print(f"{k}: {v}")

    elif source == "bpk":
        data = scrape_bpk(url)
        print("=== DETAIL DOKUMEN BPK ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    else:
        print("❌ Sumber dokumen tidak dikenali. Gunakan salah satu dari: ma, kpu, kemendikbud, bpk.")

if __name__ == "__main__":
    main()


