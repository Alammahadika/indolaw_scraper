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
