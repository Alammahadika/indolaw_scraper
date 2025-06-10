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

~/Projects/indolaw_scraper/
│
├── __init__.py                # Penanda package Python
├── jdih.go.id.py              # Scraper JDIH Nasional
├── dpr.go.id.py               # Scraper Dokumen DPR
├── mpr.go.id.py               # Scraper Dokumen MPR
├── peraturanbpk.go.id.py       # Scraper Dokumen BPK
├── kementerian.go.id.py         # Scraper Dokumen Kementerian
├── putusan3.mahkamaagung.go.id.py  # Scrape Dokumen Mahkama Agung
├── mkri.go.id.py               # Scrape Dokumen Mahkama Konstitusi
├── bphn.go.id.py                # Scrape Badan Pembina Hukum Nasional
├── setkab.go.id.py               #Scraper Sekretariat Kabinet
├── jdih.kpu.go.id.py         # Scraper Dokumen Komisi Pemilihan Umum
├── jdih.bawaslu.go.id.py     # Scraper Dokumen Badan Penngawas Pemilu
├── jdih.kpk.go.id.py         # Scraper Dokumen Komisi Pemberantas Korupsi
├── jdih.ojk.go.id.py          # Scraper Dokumen Otoritas Jasa Keuangan
├── jdih.bps.go.id.py         # Scraper Dokumen Badan Pusat Statistik
├── jdih.menpan.go.id.py     # Scraper Dokumen Kementerian Pendayagunaan Aparatur Negara dan Reformasi Birokrasi
├── jdih.bi.go.id.py          # Scraper Dokumen Bank Indonesia
├── peraturan.go.id.py        # Scraper regulasi sektoral
    └── daerah/
        ├── dki_jakarta.py
        ├── jawa_barat.py
        ├── jawa_timur.py
        ├── jawa_tengah.py
        ├── aceh.py
        ├── bali.py
        ├── banten.py
        ├── bengkulu.py
        ├── di_yogyakarta.py
        ├── gorontalo.py
        ├── jambi.py
        ├── kalimantan_barat.py
        ├── kalimantan_selatan.py
        ├── kalimantan_timur.py
        ├── kalimantan_tengah.py
        ├── kalimantan_utara.py
        ├── kepualian_bangka_belitung.py
        ├── kepulauan_riau.py
        ├── lampung.py
        ├── maluku.py
        ├── maluku_utara.py
        ├── nusa_tenggara_barat.py
        ├── nusa_tenggara_timur.py
        ├── papua.py
        ├── papuabarat.py
        ├── papua_pegunungan.py
        ├── papua_selatan.py
        ├── papua_tengah.py
        ├── riau.py
        ├── sulawesi_tengah.py
        ├── sulawesi_barat.py
        ├── sulawesi_selatan.py
        ├── sulawesi_tenggara.py
        ├── sulawesi_utara.py
        ├── sumatera_barat.py
        ├── sumatera_utara.py
        ├── sumatera_selatan.py
        
├── utils.py                   # Fungsi bantu: parsing tanggal, normalisasi judul, dll
├── config.py                  # Konfigurasi URL, headers, keyword
│
├── archive/                   # Folder arsip PDF yang disimpan
│   ├── uu/                    # Undang-undang
│   ├── ruu/                   # RUU
│   └── perpres/               # Peraturan Presiden
│   └── perda/               # Peraturan daerah
│
├── metadata/                  # Metadata YAML atau JSON per dokumen
│   ├── uu.yaml
│   └── perpres.yaml
│   └── perda.yaml
└── presidents.yaml            # Informasi presiden (opsional, seperti FlatGov)

tests/
└── test_jdih.py               # Unit test untuk scraper jdih



```
