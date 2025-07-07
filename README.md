# 🇮🇩 IndoLaw Scraper

**Indonesian Government Document Scraper**  
_An open-source Python project for scraping official legal and policy documents from Indonesian government websites._

---

## 🔍 Overview

**IndoLaw Scraper** adalah proyek Python sumber terbuka untuk mengumpulkan dan mengarsipkan dokumen hukum dan kebijakan dari situs web resmi pemerintah Indonesia, seperti:
- [JDIH Mahkamah Agung](https://jdih.mahkamahagung.go.id)
- [JDIH KPU](https://jdih.kpu.go.id)
- [JDIH Kemendikbud](https://jdih.kemendikdasmen.go.id)
- [JDIH BPK](https://peraturan.bpk.go.id)
- [dan lainnya...]

Proyek ini terinspirasi oleh [FlatGov SAP US Project](https://flatgov.com/), dengan tujuan membuat metadata terbuka dan sistem arsip legal yang **modular**, **terbuka**, dan **mudah digunakan** untuk:
- Peneliti hukum dan sosial-politik
- Mahasiswa dan akademisi
- Jurnalis data
- Pengembang aplikasi hukum

---

## 🎯 Project Objectives

- ✅ Scraping dan menyimpan dokumen hukum (UU, Peraturan, SK, dsb.) dalam format PDF dan metadata.
- ✅ Menyediakan interface command-line (CLI) untuk akses mudah scraping.
- ✅ Membangun package Python modular yang bisa diperluas untuk berbagai lembaga.

---

---
## Getting Started

```bash
   python -m indolaw_scraper.cli --type peraturan --url "https://jdih.mahkamahagung.go.id/legal-product/..."
```
