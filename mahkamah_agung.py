# scraper/mahkamah_agung.py

import requests
from bs4 import BeautifulSoup
import urllib3
from indolaw_scraper.models.document import LegalDocument

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_soup(url):
    """Ambil objek BeautifulSoup dari URL"""
    res = requests.get(url, verify=False)
    return BeautifulSoup(res.text, 'html.parser')

def get_detail_value(soup, label_name):
    """Helper untuk mengambil nilai dari label tertentu"""
    el = soup.find(string=label_name)
    if el:
        next_el = el.find_next()
        return next_el.get_text(strip=True) if next_el else "N/A"
    return "N/A"

def get_detail_data(url):
    """Ekstrak semua data detail dari halaman peraturan"""
    soup = get_soup(url)
    labels = [
        "Judul", "Nomor", "Tahun", "Jenis", "Singkatan Jenis",
        "Tanggal Ditetapkan", "Tanggal Diundangkan", "Penandatangan",
        "Pemrakarsa", "Sumber", "T.E.U.", "Tempat Penetapan", "Lokasi",
        "Bahasa", "Bidang Hukum", "Urusan Pemerintah", "Subjek", "Status"
    ]

    data = {}
    for label in labels:
        data[label] = get_detail_value(soup, label)
    return data

def scrape_putusan_detail(url):
    """Scrape detail dokumen putusan (contoh struktur LegalDocument)"""
    soup = get_soup(url)
    return LegalDocument(
        title=soup.find('h1').text.strip(),
        year=get_detail_value(soup, "Tahun"),
        pdf_url=soup.select_one('a[href$=".pdf"]')['href']
    )

def get_putusan_links(base_url="https://jdih.mahkamahagung.go.id"):
    """Ambil semua link putusan dari halaman indeks"""
    soup = get_soup(f"{base_url}/putusan")
    return [a['href'] for a in soup.select('a.putusan-link')]

# --- BAGIAN INI HANYA AKAN JALAN KETIKA FILE INI DIEKSEKUSI LANGSUNG ---
if __name__ == "__main__":
    url = "https://jdih.mahkamahagung.go.id/legal-product/perma-nomor-1-tahun-2025/detail"
    data = get_detail_data(url)
    print("=== DETAIL DOKUMEN ===")
    for k, v in data.items():
        print(f"{k}: {v}")



