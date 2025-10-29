import requests
import fitz
import pandas as pd

def extract_pdf_text(pdf_url):
    """Ambil sebagian teks dari PDF (misal 1000 karakter pertama)."""
    try:
        resp = requests.get(pdf_url, timeout=20)
        resp.raise_for_status()
        with fitz.open(stream=resp.content, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text("text")
                if len(text) > 1000:
                    break
        return text.strip()[:1000]
    except Exception as e:
        return f"[Error extract_pdf_text: {e}]"

def get_tni_data(page: int = 15):
    """Ambil daftar Peraturan Panglima TNI dari API JDIH TNI."""
    url = f"https://jdih.tni.mil.id/api/produk-uud/{page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; indolaw_scraper/1.0; +https://github.com/indolaw)",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://jdih.tni.mil.id/peraturan-panglima-tni",
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data_json = resp.json()

    data = []
    for item in data_json:
        pdf_url = item.get("url_view")
        deskripsi = extract_pdf_text(pdf_url) if pdf_url else None

        data.append({
            "judul": item.get("title"),
            "kategori": item.get("category"),
            "status": item.get("status"),
            "tanggal": item.get("date"),
            "url_pdf": pdf_url,
            "deskripsi": deskripsi
        })

    return data


# Jalankan fungsi untuk ambil data
data = get_tni_data()

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Tampilkan hasilnya
pd.set_option("display.max_colwidth", 200)
print(df.head(3))

