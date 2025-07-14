# 🇮🇩 IndoLaw Scraper

**Indonesian Government Document Scraper**  
_An open-source Python project for scraping official legal and policy documents from Indonesian government websites._

---

## 🔍 Overview

**IndoLaw Scraper** is an open-source Python project to collect and archive legal and policy documents from official Indonesian government websites, such as:
- [JDIH Mahkamah Agung](https://jdih.mahkamahagung.go.id)
- [JDIH KPU](https://jdih.kpu.go.id)
- [JDIH Kemendikbud](https://jdih.kemendikdasmen.go.id)
- [JDIH BPK](https://peraturan.bpk.go.id)
- [and others...]

This project was inspired by the [FlatGov SAP US Project](https://flatgov.com/), with the goal of creating a **modular**, **open**, and **easy to use** open metadata and legal filing system for:
- Researchers law and socio - politics
- Student and Academicy
- Developers Data

---

## 🎯 Project Objectives

- ✅ Scraping and storing legal documents (UU, Regulations, Decrees, etc.) in metadata format.
- ✅ Provides a command-line interface (CLI) for easy scraping access.
- ✅ Building modular, extensible Python packages for multiple institutions.

---

---
## Getting Started

```bash
   python -m indolaw_scraper.cli --type peraturan --url "https://jdih.mahkamahagung.go.id/legal-product/..."
```
---
## Getting Try

```py
indolaw_scraper/sources/kominfo.py

import requests
from bs4 import BeautifulSoup
import urllib3
from indolaw_scraper.models.document import LegalDocument

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_soup(url):
    res = requests.get(url, verify=False)
    return BeautifulSoup(res.text, 'html.parser')

def get_detail_data(url):
    soup = get_soup(url)
    field_map = {
        "Tipe Dokumen": "Tipe Dokumen",
        "Judul": "Judul",
        "T.E.U. Badan/Pengarang": "T.E.U Badan",
        "Nomor Peraturan": "Nomor Peraturan",
        "Jenis / Bentuk Peraturan": "Jenis/Bentuk Peraturan",
        "Singkatan Jenis/Bentuk Peraturan": "Singkatan Jenis/Bentuk Peraturan",
        "Tempat Penetapan": "Tempat Penetapan",
        "Tanggal-Bulan-Tahun Penetapan/Pengundangan": "Tanggal Ditetapkan / Diundangkan",
        "Sumber": "Sumber",
        "Subjek": "Subjek",
        "Status Peraturan": "Status",
        "Bahasa": "Bahasa",
        "Lokasi": "Lokasi",
        "Bidang Hukum": "Bidang Hukum",
        "Lampiran": "Lampiran"
    }
    
    data = {}
    for row in soup.select("table tr"):
        cols = row.find_all("td")
        if len(cols) >= 2:
            label = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True).replace("\n", " ")
            if label in field_map:
                data[field_map[label]] = value
    return data

def scrape_putusan_detail(url):
    soup = get_soup(url)
    data = get_detail_data(url)
    return LegalDocument(
        title=data.get("Judul"),
        year=data.get("Tanggal Ditetapkan / Diundangkan", "")[:4],
        pdf_url=soup.select_one('a.btn[href*="unduh"]')['href'] if soup.select_one('a.btn[href*="unduh"]') else None,
        metadata=data
    )

def inspect_labels(url):
    soup = get_soup(url)
    for p in soup.select("div.tx-14 p"):
        strong = p.find("strong")
        if strong:
            label = strong.get_text(strip=True).rstrip(':')
            print(f"🔎 Ditemukan label: {label}")

if __name__ == "__main__":
    url = "https://jdih.komdigi.go.id/produk_hukum/view/id/954/t/keputusan+menteri+komunikasi+dan+digital+nomor+44+tahun+2025"
    data = get_detail_data(url)
    print("=== MINISTRY OF COMMUNICATION AND INFORMATION DOCUMENT DETAILS ===")
    for k, v in data.items():
        print(f"{k}: {v}")


```
## Result Scraped

```text
=== MINISTRY OF COMMUNICATION AND INFORMATION DOCUMENT DETAILS ===
Tipe Dokumen                    : 
Judul                          : Keputusan Menteri Komunikasi dan Digital Nomor 44 Tahun 2025 tentang Standar Teknis Transiver Radio Amatir
T.E.U Badan                    : Indonesia. Kementerian Komunikasi dan Informatika
Nomor Peraturan                : 44
Jenis/Bentuk Peraturan         : Keputusan Menteri
Singkatan Jenis/Bentuk Peraturan: KEPMEN
Tempat Penetapan               : Jakarta
Tanggal Ditetapkan / Diundangkan: 18-02-2025 / -
Sumber                         : -
Subjek                         : 
Status                         : Berlaku
Bahasa                         : Indonesia
Lokasi                         : 
Bidang Hukum                   : Hukum Administrasi Negara
Lampiran                       : Unduh Produk Hukum


```
