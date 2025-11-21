# 🇮🇩 IndoLaw Scraper

**Indonesian Government Document Scraper**  
_An open-source Python project to scrape official legal and policy documents from Indonesian government websites._

---

## 🔍 Overview

**IndoLaw Scraper** collects and archives legal and policy documents from official Indonesian government websites, such as:

| Institution | Website |
|------------|---------|
| Mahkamah Agung (MA) | [jdih.mahkamahagung.go.id](https://jdih.mahkamahagung.go.id) |
| KPU | [jdih.kpu.go.id](https://jdih.kpu.go.id) |
| Kemendikbud | [jdih.kemendikdasmen.go.id](https://jdih.kemendikdasmen.go.id) |
| BPK | [peraturan.bpk.go.id](https://peraturan.bpk.go.id) |
| And others | - |

Inspired by the [FlatGov SAP US Project](https://flatgov.com/), this project aims to create a **modular**, **open**, and **easy-to-use** metadata and legal filing system for:

- Researchers in law and socio-politics  
- Students and academics  
- Developers and data enthusiasts  

---

## 🎯 Project Objectives

- ✅ Scraping and storing legal documents (UU, Regulations, Decrees, etc.) in metadata format  
- ✅ Provides a **command-line interface (CLI)** for easy scraping access  
- ✅ Building **modular, extensible Python packages** for multiple institutions  

---

## 💻 Installation

Install the package via PyPI:

```bash
pip install indolaw-scraper
```

## Run 
```bash
scrape_bpk "https://peraturan.bpk.go.id/Details/227490/peraturan-kpk-no-5-tahun-2018"
```

## Result
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
