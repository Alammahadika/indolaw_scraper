# indolaw_scraper/scraper/kemendesa.py
import requests
from bs4 import BeautifulSoup
from indolaw_scraper.models.document import LegalDocument


def get_detail_data_kemendesa(url: str):
    """Scrape detail dokumen dari JDIH Kemendesa (jdih.kemendesa.go.id)."""
    print(f"🔍 Mengambil metadata dari: {url}")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="table-striped")
    if not table:
        raise ValueError("Tidak menemukan tabel metadata di halaman ini.")

    data = {}
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) >= 3:
            key = tds[0].get_text(strip=True)
            value = tds[2].get_text(strip=True)
            data[key] = value

    # ambil link PDF
    pdf_link = soup.select_one(".download-buttons a[href$='.pdf']")
    pdf_url = pdf_link["href"] if pdf_link else None

    # mapping ke LegalDocument
    doc = LegalDocument(
        title=data.get("Judul"),
        tipe_dokumen=data.get("Tipe Dokumen"),
        nomor=data.get("Nomor Peraturan"),
        tahun=data.get("Tahun"),
        subjek=data.get("Subjek Dokumen"),
        teu_badan_pengarang=data.get("Tajuk Entri Utama"),
        sumber="kemendesa",
        status=data.get("Status"),
        tempat_penetapan=data.get("Tempat Penetapan"),
        tanggal_diundangkan=data.get("Tanggal Pengundangan"),
        tanggal_berlaku=data.get("Tanggal Berlaku Efektif"),
        bahasa=data.get("Bahasa"),
        bidang_hukum=data.get("Bidang Hukum"),
        pdf_url=pdf_url,
        url_file_peraturan_download=pdf_url,
    )

    return doc.to_dict()


# =====================================
# 🔹 TEST MODE
# =====================================
if __name__ == "__main__":
    test_url = "https://jdih.kemendesa.go.id/web/regulations/read/pengelolaan-keuangan-menggunakan-transaksi-pembayaran-nontunai-oleh-bendahara-pengeluaran-di-lingkungan-kementerian-desa-dan-pembangunan-daerah-tertinggal-413-2025"
    print("\n🧪 TEST MODE: Scraping dokumen Kemendesa\n")
    try:
        doc = get_detail_data_kemendesa(test_url)
        print("\n=== DETAIL DOKUMEN KEMENDESA ===")
        for k, v in doc.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
