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
## Getting Try

```py
indolaw_scraper/sources/kemendag.py

import requests
from bs4 import BeautifulSoup
import json
from indolaw_scraper.models.document import LegalDocument

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_kemendag_data(url):
    """Scrape metadata dokumen dari JDIH Kemendag."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error saat mengambil data: {e}")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.select("table.table tbody tr")
    data = {}

    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            label = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True)
            data[label] = value

    return data

if __name__ == "__main__":
    test_url = "https://jdih.kemendag.go.id/peraturan/keputusan-menteri-perdagangan-nomor-1484-tahun-2025-tentang-harga-referensi-crude-palm-oil-yang-dikenakan-bea-keluar-dan-tarif-layanan-badan-layanan-umum-badan-pengelola-dana-perkebunan-kelapa-sawit"
    result = get_kemendag_data(test_url)
    print("=== DETAIL DOKUMEN KEMENDAG ===")
    for k, v in result.items():
        print(f"{k}: {v}")


```
---
## Result Scraped

```text

=== DETAIL DOKUMEN KEMENDAG ===
Tipe Dokumen: Peraturan Perundang-undangan
Judul: Keputusan Menteri Perdagangan Nomor 1484 Tahun 2025 tentang Harga Referensi Crude Palm Oil yang Dikenakan Bea Keluar dan Tarif Layanan Badan Layanan Umum Badan Pengelola Dana Perkebunan Kelapa Sawit
T.E.U. Badan/Pengarang: Indonesia.Kementerian Perdagangan
Nomor Peraturan: 1484
Jenis / Bentuk Peraturan: Keputusan Menteri
Singkatan Jenis / Bentuk Peraturan: Kepmendag
Tempat Penetapan: Jakarta
Tanggal Penetapan / Pengundangan: 28 Mei 2025 / -
Sumber: -
Subjek: CPO, Harga, Bea Keluar, Kelapa Sawit
Status Peraturan: Berlaku
Bahasa: Indonesia
Lokasi: Jakarta
Bidang Hukum: -
Tematik: Kelapa Sawit

```
---
## CLI Command to Scrape Document 

```bash

python -m indolaw_scraper.cli --source bpk --url "https://peraturan.bpk.go.id/Details/227490/peraturan-kpk-no-5-tahun-2018"

```
---

## Resut Scraped

```text

=== DETAIL DOKUMEN BPK ===
Judul: Peraturan KPK No. 5 Tahun 2018  
Nomor: 5  
Tahun: 2018  
T.E.U. Badan / Pengarang: N/A  
Tipe Dokumen: Peraturan Perundang-undangan  
Bentuk: Peraturan Komisi Pemberantasan Korupsi  
Singkatan Bentuk: N/A  
Tempat Penetapan: Jakarta  
Tanggal Penetapan: 21 Mei 2018  
Tanggal Pengundangan: 24 Mei 2018  
Tanggal Berlaku: 24 Mei 2018  
Sumber: BN. 2018 No. 692, www.peraturan.go.id  
Subjek: KEPEGAWAIAN, APARATUR NEGARA  
Status: Tidak Berlaku  
Bahasa: Bahasa Indonesia  
Bidang Hukum: N/A  

```
