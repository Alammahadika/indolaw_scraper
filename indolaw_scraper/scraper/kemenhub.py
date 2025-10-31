import requests
from bs4 import BeautifulSoup
import urllib3
from pprint import pprint
from indolaw_scraper.models.document import LegalDocument


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://jdih.dephub.go.id"


# =====================================
# 🔹 UTILITY FUNCTION
# =====================================

def get_soup(url):
    """Ambil dan parsing HTML dari sebuah URL"""
    res = requests.get(url, verify=False)
    res.raise_for_status()
    return BeautifulSoup(res.text, "html.parser")


# =====================================
# 🔹 SCRAPE DETAIL DOKUMEN KEMENHUB
# =====================================

def get_kemenhub_detail(url):
    """Ambil metadata detail dari satu halaman dokumen JDIH Kemenhub"""
    soup = get_soup(url)
    table = soup.select_one(".table-peraturan")

    data = {}
    if not table:
        return data

    for row in table.select(".row"):
        label_el = row.select_one(".col-md-4")
        value_el = row.select_one(".col-md-8")
        if label_el and value_el:
            label = label_el.get_text(strip=True)
            value = value_el.get_text(strip=True).replace("\xa0", " ")
            data[label] = value

    # Ambil file PDF
    file_button = table.select_one('button[data-bs-target=".modal-file-peraturan"]')
    file_iframe = table.select_one(".modal-file-peraturan iframe")
    file_url = (
        BASE_URL + file_iframe["src"]
        if file_iframe and file_iframe.get("src")
        else None
    )

    # Tambah ke metadata
    data["File URL"] = file_url

    return data


# =====================================
# 🔹 BUNGKUS DALAM MODEL
# =====================================

def scrape_kemenhub_document(url):
    """Konversi hasil scraping ke model LegalDocument (versi Kemenhub)"""
    meta = get_kemenhub_detail(url)

    doc = LegalDocument(
        # --- Atribut umum ---
        title=meta.get("Judul"),
        tahun=meta.get("Tanggal Penetapan", "").split()[-1] if meta.get("Tanggal Penetapan") else None,
        nomor=meta.get("Nomor Peraturan"),
        jenis=meta.get("Jenis/Bentuk Peraturan"),
        singkatan_jenis=meta.get("Singkatan Jenis/Bentuk Peraturan"),
        tipe_dokumen=meta.get("Tipe Dokumen"),
        bidang_hukum=meta.get("Bidang Hukum"),
        subjek=meta.get("Subjek"),
        status=meta.get("Status"),

        # --- Tanggal & Penetapan ---
        tanggal_ditetapkan=meta.get("Tanggal Penetapan"),
        tanggal_berlaku=meta.get("Tanggal Berlaku Efektif"),
        tempat_penetapan=meta.get("Tempat Penetapan"),

        # --- Identitas lembaga ---
        teu_badan_pengarang=meta.get("Tajuk Entri Utama"),
        lokasi=meta.get("Lokasi"),

        # --- Metadata tambahan ---
        sumber="kemenhub",
        bahasa=meta.get("Bahasa"),

        # --- File dan link ---
        pdf_url=meta.get("File URL"),
        url_file_peraturan_download=meta.get("File URL"),
    )

    # 🔹 Kembalikan sebagai dictionary agar kompatibel dengan CLI
    return doc.to_dict()



# =====================================
# 🔹 TEST MODE
# =====================================
if __name__ == "__main__":
    url = "https://jdih.dephub.go.id/peraturan/detail?data=KC5uy73MJHW5isBas8JH2l4OUvPzRk6Nk8QmJ6W89gLz8Qp5V1vqcu04edIip6X1E28Qjgnzrp9yp8bJrgqhAt644JH7ngOw5C58m8F62MT4TO5qln437PfdrIBdBGF5fJ9w9msDmiz3apMIo4ImzqV0nt"

    print(f"\n🔍 Mengambil metadata dari: {url}\n")
    doc = scrape_kemenhub_document(url)
    pretty_print_document(doc)



