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
from indolaw_scraper.scraper.kemenkeu import get_detail_data as scrape_kemenkeu
from indolaw_scraper.scraper.kominfo import get_detail_data as scrape_kominfo
from indolaw_scraper.scraper.marves import get_detail_data_marves as scrape_marves
from indolaw_scraper.scraper.kemendag import get_kemendag_data
from indolaw_scraper.scraper.kemenpora import scrape_kemenpora_detail
from indolaw_scraper.scraper.pu import scrape_pu_detail



@click.command()
@click.option('--source', help='Sumber dokumen (ma/kpu/kemendikbud/kementan/kkp/bpk/kemenkeu/kominfo)', required=True)
@click.option('--url', help='URL detail dokumen', required=True)
def main(source, url):
    if source == "ma":
        data = ma.scrape_ma(url)
        print("=== DETAIL DOKUMEN MAHKAMAH AGUNG ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kpu":
        raw = kpu.scrape_kpu_regulation_detail(url)
        if raw:
            mapped = kpu.map_kpu_data_to_legal_document_format(raw)
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
        data = kemendikbud.scrape_kemendikbud(url)
        print("=== DETAIL DOKUMEN KEMENDIKBUD ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kementan":
        data = kementan.scrape_kementan(url)
        print("=== DETAIL DOKUMEN KEMENTAN ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kkp":
        data = kkp.scrape_kementan(url)  
        print("=== DETAIL DOKUMEN KKP ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "bpk":
        data = bpk.scrape_bpk(url)
        print("=== DETAIL DOKUMEN BPK ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kemenkeu":
        data = kemenkeu.get_detail_data(url)
        print("=== DETAIL DOKUMEN KEMENKEU ===")
        for k, v in data.items():
            print(f"{k}: {v}")

    elif source == "kominfo":
        doc = kominfo.scrape_putusan_detail(url)
        print("=== DETAIL DOKUMEN KOMINFO ===")
        print(json.dumps(doc.to_dict(), indent=2, ensure_ascii=False))
    
    elif source == "marves":
         from indolaw_scraper.sources import marves
         data = marves.get_detail_data_marves(url)
         print("=== DETAIL DOKUMEN MARVES ===")
         for k, v in data.items():
         print(f"{k}: {v}")
    
     elif source == "pu":
          result = scrape_pu_detail(url)
          print(json.dumps(result.__dict__, indent=2, ensure_ascii=False))
 
    
    
    elif type == "kemenpora":
        data = scrape_kemenpora_detail(url)
        print("=== DETAIL DOKUMEN KEMENPORA ===")
        for k, v in data.items():
        print(f"{k}: {v}")

    else:
        print("❌ Sumber dokumen tidak dikenali. Gunakan salah satu dari: ma, kpu, kemendikbud, kementan, kkp, bpk, kemenkeu, kominfo.")

if __name__ == "__main__":
    main()



