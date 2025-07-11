import requests
from bs4 import BeautifulSoup
import urllib3
from indolaw_scraper.models.document import LegalDocument

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_soup(url):
    """Ambil dan parsing HTML dari sebuah URL"""
    res = requests.get(url, verify=False)
    return BeautifulSoup(res.text, 'html.parser')


def get_all_kemenkeu_links():
    """Ambil semua link dokumen dari halaman pertama situs Kemenkeu"""
    base_url = "https://jdih.kemenkeu.go.id"
    index_url = f"{base_url}/search?order=desc"
    soup = get_soup(index_url)
    links = []
    for a in soup.select('a[href^="/dok/"]'):
        href = a.get('href')
        if href:
            full_url = base_url + href
            if full_url not in links:
                links.append(full_url)
    return links


def get_detail_data(url):
    """Ambil detail metadata dari halaman dokumen Kemenkeu"""
    soup = get_soup(url)
    
    field_map = {
        "Kode": "Nomor Peraturan",
        "Judul/Tentang": "Judul",
        "Nomor": "Nomor",
        "Tahun": "Tahun",
        "Jenis": "Jenis/Bentuk Peraturan",
        "Tajuk Entri Utama": "T.E.U Badan",
        "Bidang": "Bidang Hukum",
        "Subyek": "Subjek",
        "Penetapan": "Tanggal Ditetapkan",
        "Pengundangan": "Tanggal Diundangkan",
        "Tgl. Berlaku": "Tanggal Berlaku",
        "Tempat Terbit": "Tempat Penetapan",
        "Sumber": "Sumber",
        "Lokasi": "Lokasi"
    }

    data = {}
    for row in soup.select('.row.dok-item'):
        label_el = row.select_one('.col-4')
        value_el = row.select_one('.col-8')
        if label_el and value_el:
            label = label_el.get_text(strip=True)
            value = value_el.get_text(strip=True).replace('\n', ' ').strip()
            if label in field_map:
                data[field_map[label]] = value
    return data


def scrape_putusan_detail(url):
    """Buat instance LegalDocument dari halaman dokumen Kemenkeu"""
    soup = get_soup(url)
    detail_data = get_detail_data(url)
    pdf_link = soup.select_one('a[href$=".pdf"]')
    return LegalDocument(
        title=detail_data.get("Judul"),
        year=detail_data.get("Tahun"),
        pdf_url=pdf_link['href'] if pdf_link else None
    )


# === MAIN LOOP ===
if __name__ == "__main__":
    print("🔎 Mengambil semua link peraturan dari Kementerian Keuangan ...")
    links = get_all_kemenkeu_links()
    print(f"✅ Ditemukan {len(links)} dokumen (dari halaman pertama)")

    for i, link in enumerate(links[:10], 1):  # Batas 5 dokumen dulu
        print(f"\n📄 [{i}] {link}")
        try:
            data = get_detail_data(link)
            for k, v in data.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"❌ Gagal scrape {link}: {e}")

