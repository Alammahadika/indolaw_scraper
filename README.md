# 🇮🇩 INDONESIAN GOVERNEMNT DOCUMENT SCRAPER

## Project Description
Indonesian Government Document Scraper is an open-source Python project for scraping and archiving legal and policy documents from official Indonesian government websites, such as JDIH.go.id, DPR.go.id, and others. 
Inspired by the [FlatGov SAP US Project](https://flatgov.com), this project aims to build an open metadata repository and archive for Indonesian legal documents that is modular, open-source, and easy to use for researchers, students, and the public.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---


## Project Objectives
Obtain and store legal documents (UU, RUU, Perpres, etc.) in PDF format and metadata.
Make it easier for researchers, students, and the public to access legal documents.
Develop a modular Python package that can be used to scrape various official Indonesian sources.

---

## Project Structures

```
indolaw_scraper/
│
├── scrapers/ # Semua scraper terorganisir
│ ├── national/ # Lembaga nasional
│ │ ├── dpr.py # DPR.go.id
│ │ ├── mkri.py # Mahkamah Konstitusi
│ │ └── ...
│ │
│ ├── regional/ # Peraturan daerah
│ │ └── dki_jakarta.py # DKI Jakarta
│ │ └── ...
│ │
│ └── ministries/ # Kementerian
│ └── kemendagri.py
│ └── ...
│
├── core/ # Modul inti
│ ├── downloader.py # Unduh dokumen
│ ├── parser.py # Ekstrak teks
│ └── storage.py # Simpan ke database
│
├── archive/ # Folder arsip dokumen PDF
│ ├── uu/ # Undang-undang
│ ├── ruu/ # RUU
│ ├── perpres/ # Peraturan Presiden
│ └── perda/ # Peraturan Daerah
│
├── metadata/ # Metadata YAML atau JSON per dokumen
│ ├── uu.yaml
│ ├── perpres.yaml
│ └── perda.yaml
│
├── tests/ # Unit tests
│ └── test_jdih.py
│
├── utils.py # Fungsi bantu
├── config.py # Konfigurasi URL, headers, keyword
├── presidents.yaml # Data Presiden (opsional)
├── requirements.txt # Dependensi Python
├── setup.py # Setup installasi package
└── README.md # Dokumentasi proyek


```
