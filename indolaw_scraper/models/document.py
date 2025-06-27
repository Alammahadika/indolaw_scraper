# indolaw_scraper/indolaw_scraper/models/document.py
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class LegalDocument:
    # --- Atribut Umum ---
    title: str
    tahun: Optional[str] = None
    nomor: Optional[str] = None
    jenis: Optional[str] = None
    singkatan_jenis: Optional[str] = None
    tipe_dokumen: Optional[str] = None
    bentuk: Optional[str] = None
    singkatan_bentuk: Optional[str] = None

    # --- Tanggal & Penetapan ---
    tanggal_ditetapkan: Optional[str] = None
    tanggal_diundangkan: Optional[str] = None
    tanggal_berlaku: Optional[str] = None
    tempat_penetapan: Optional[str] = None
    penandatangan: Optional[str] = None

    # --- Identitas Lembaga & Pengarang ---
    pemrakarsa: Optional[str] = None
    teu_badan_pengarang: Optional[str] = None
    lokasi: Optional[str] = None

    # --- Metadata Tambahan ---
    sumber: Optional[str] = None
    nomor_sumber: Optional[str] = None
    bahasa: Optional[str] = None
    bidang_hukum: Optional[str] = None
    urusan_pemerintah: Optional[str] = None
    subjek: Optional[str] = None
    status: Optional[str] = None
    detail_status: Optional[str] = None

    # --- File atau Link ---
    pdf_url: Optional[str] = None
    url_abstrak_preview: Optional[str] = None
    url_abstrak_download: Optional[str] = None
    url_file_peraturan_preview: Optional[str] = None
    url_file_peraturan_download: Optional[str] = None
    url_peraturan_dicabut: Optional[str] = None

    # --- Metode untuk bantu konversi ke dict ---
    def to_dict(self):
        return asdict(self)
