import requests
from bs4 import BeautifulSoup

def get_detail_data(url: str):
    """Scrape metadata dokumen dari halaman JDIH Kemenparekraf."""
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}
    for li in soup.select("ul.course-item li"):
        label = li.select_one(".label")
        value = li.select_one(".value")
        if label and value:
            key = label.get_text(strip=True)
            val = value.get_text(strip=True)
            data[key] = val

    # Ambil link PDF (Full Text)
    pdf_link = soup.select_one("a.edu-btn.btn-small.mt-4.w-100[href*='api-jdih.kemenpar.go.id']")
    if pdf_link and pdf_link.get("href"):
        data["PDF"] = pdf_link["href"]

    return data


# --- BAGIAN INI HANYA AKAN JALAN KETIKA FILE INI DIEKSEKUSI LANGSUNG ---
if __name__ == "__main__":
    url = "https://jdih.kemenpar.go.id/peraturan/1358"
    data = get_detail_data(url)

    print("=== DETAIL DOKUMEN KEMENPAREKRAF ===")
    for k, v in data.items():
        print(f"{k}: {v}")

