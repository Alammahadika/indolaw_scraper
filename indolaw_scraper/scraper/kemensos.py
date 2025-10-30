import requests
from bs4 import BeautifulSoup

def get_detail_data(url: str):
    """
    Scrape detailed metadata of legal documents from JDIH Kemensos.
    
    Args:
        url (str): The detail page URL of the legal document.
    
    Returns:
        dict: A dictionary containing structured metadata of the document.
    """
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}

    # --- Extract document title ---
    title_tag = soup.select_one("h4.mb-4.fw-bold.text-capitalize")
    if title_tag:
        data["Judul"] = " ".join(title_tag.get_text(strip=True).split())

    # --- Extract metadata from main table ---
    for row in soup.select("table tbody tr"):
        tds = row.find_all("td")
        if len(tds) == 2:
            key = tds[0].get_text(strip=True)
            val = " ".join(tds[1].get_text(strip=True).split())
            data[key] = val

    # --- Extract status (Berlaku / Dicabut / etc.) ---
    status_tag = soup.select_one(".card.bg-success .card-title")
    if status_tag:
        data["Status Peraturan"] = status_tag.get_text(strip=True)

    # --- Extract PDF download link ---
    pdf_link = soup.select_one("a.df-ui-download[href]")
    if pdf_link and pdf_link.get("href"):
        data["PDF"] = pdf_link["href"]

    # --- Extract related regulations ---
    related = []
    for rel in soup.select(".card.border-success a[href]"):
        related.append(rel.get_text(strip=True))
    if related:
        data["Peraturan Terkait"] = related

    return data


# --- RUN DIRECTLY (for quick testing/debugging) ---
if __name__ == "__main__":
    url = "https://jdih.kemensos.go.id/detail/surat-edaran-nomor-1-tahun-2025-tentang-dukungan-pelaksanaan-61vHlK3zMe"
    data = get_detail_data(url)

    print("=== DETAIL DOKUMEN KEMENSOS ===")
    for k, v in data.items():
        if isinstance(v, list):
            print(f"{k}:")
            for item in v:
                print(f"  - {item}")
        else:
            print(f"{k}: {v}")
