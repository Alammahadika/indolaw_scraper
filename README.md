# 🇮🇩 INDONESIAN GOVERNEMNT DOCUMENT SCRAPER

## Project Description
Indonesian Government Document Scraper is an open-source Python project for scraping and archiving legal and policy documents from official Indonesian government websites, such as JDIH.go.id, DPR.go.id, and others. 
Inspired by the FlatGov SAP US Project, this project aims to build an open metadata repository and archive for Indonesian legal documents that is modular, open-source, and easy to use for researchers, students, and the public.

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
├── indolaw_scraper/
│   ├── __init__.py
│   ├── cli.py  # <- interface main
│   ├── models/
│   │   └── document.py  # <- dataclass LegalDocument
│   └── scraper/
│       ├── __init__.py
│       ├── mahkamah_agung.py
│       ├── kpu.py
│       ├── bpk.py
│       ├── kemendikdasmen.py
│       ├── pertanian.py
│       └── kkp.py
│
├── tests/
│   └── test_scraper.py  
│
├── requirements.txt     # <- library using (requests, beautifulsoup4, click, dll)
├── README.md            # <- project description
└── LICENSE              # <- optional (misal: MIT)


```
---
## Getting Started

```bash
   git clone https://github.com/Alammahadika/indolaw_scraper.git
   cd indolaw_scraper
```
