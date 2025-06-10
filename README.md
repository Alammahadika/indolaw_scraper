# 🇮🇩 INDONESIAN GOVERNEMNT DOCUMENT SCRAPER

## Project Description
Indonesian Legislative Document Scraper is an open-source Python project for scraping and archiving legal and policy documents from official Indonesian government websites, such as JDIH.go.id, DPR.go.id, and others. 
The project is inspired by the FlatGov SAP US Project and aims to build an open metadata repository and archive of Indonesian legislative documents.

## Project Objectives
Obtain and store legal documents (UU, RUU, Perpres, etc.) in PDF format and metadata.
Make it easier for researchers, students, and the public to access legal documents.
Develop a modular Python package that can be used to scrape various official Indonesian sources.

## Project Structures

```
indolaw_scraper/
├── 📁 scrapers/                # Semua scraper terorganisir
│   ├── 📁 national/           # Lembaga nasional
│   │   ├── 🐍 dpr.py         # DPR.go.id
│   │   ├── 🐍 mkri.py        # Mahkamah Konstitusi
│   │   └── ...
│   │
│   ├── 📁 regional/          # Peraturan daerah
│   │   ├── 🐍 dki_jakarta.py
│   │   └── ...
│   │
│   └── 📁 ministries/        # ministry
│       ├── 🐍 kemendagri.py
│       └── ...
│
├── 📁 core/                  # Modul inti
│   ├── 🐍 downloader.py      # Unduh dokumen
│   ├── 🐍 parser.py         # Ekstrak teks
│   └── 🐍 storage.py        # Simpan ke database
│
├── 📄 README.md              # Dokumentasi utama (lihat template di bawah)
└── 📄 requirements.txt       # Dependensi


```
