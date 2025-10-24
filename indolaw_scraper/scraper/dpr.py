import requests
from bs4 import BeautifulSoup
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_dpr_detail(url):
    """
    Mengambil metadata dari halaman detail dokumen di jdih.dpr.go.id
    Contoh: https://jdih.dpr.go.id/setjen/detail-dokumen/tipe/peraturan_dpr/id/65
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Referer": "https://jdih.dpr.go.id/",
        "Connection": "keep-alive",
    }

    res = requests.get(url, headers=headers, verify=False, timeout=15)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    # Ambil judul
    title_el = soup.find("h1")
    title = title_el.get_text(strip=True) if title_el else "Tidak ada judul"

    # Ambil seluruh baris metadata
    rows = soup.select("div.card-body table tr")
    metadata = {"Judul": title}

    for row in rows:
        th = row.find("th")
        td = row.find("td")
        if not th or not td:
            continue
        key = th.get_text(strip=True)
        value = td.get_text(" ", strip=True)

        # ambil link jika ada
        link = td.find("a", href=True)
        if link:
            href = link["href"]
            if "abs" in href:
                metadata["Link Abstrak"] = href
            elif "peraturan_dpr" in href or "berkas" in href:
                metadata["Link PDF"] = href

        metadata[key] = value

    # Bersihkan spasi ekstra
    for k, v in metadata.items():
        if isinstance(v, str):
            metadata[k] = v.strip()

    return metadata


# --- TEST ---
if __name__ == "__main__":
    test_url = "https://jdih.dpr.go.id/setjen/detail-dokumen/tipe/peraturan_dpr/id/53"
    data = scrape_dpr_detail(test_url)
    print("=== DETAIL DOKUMEN DPR ===")
    for k, v in data.items():
        print(f"{k}: {v}")

