import requests
from bs4 import BeautifulSoup
import json
from indolaw_scraper.models.document import LegalDocument

def scrape_kpu_regulation_detail(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    data = {}

    # Ambil judul
    title_tag = soup.find('div', class_='card-body')
    if title_tag and title_tag.find('strong'):
        data['title'] = title_tag.find('strong').get_text(strip=True)

    # Ambil data dari tabel
    table = soup.find('table', class_='table table-hover')
    if table:
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 3:
                key = cols[0].get_text(strip=True)
                value = cols[2].get_text(strip=True)
                
                # Mapping key ke field yang sesuai
                if 'Tipe Dokumen' in key:
                    data['tipe_dokumen'] = value
                elif 'Jenis Dokumen' in key:
                    data['jenis'] = value
                elif 'Singkatan Jenis' in key:
                    data['singkatan_jenis'] = value
                elif 'Nomor' in key:
                    data['nomor'] = value
                elif 'Tahun Terbit' in key:
                    data['tahun'] = value  # Gunakan 'tahun' bukan 'tahun_terbit'
                elif 'T.E.U Badan / Pengarang' in key:
                    data['teu_badan_pengarang'] = value
                elif 'Tanggal Penetapan' in key:
                    data['tanggal_ditetapkan'] = value
                elif 'Tanggal Pengundangan' in key:
                    data['tanggal_diundangkan'] = value
                elif 'Tempat Penetapan' in key:
                    data['tempat_penetapan'] = value
                elif 'Penandatangan' in key:
                    data['penandatangan'] = value
                elif 'Sumber' in key:
                    data['sumber'] = value
                elif 'Subjek' in key:
                    data['subjek'] = value
                elif 'Bidang Hukum' in key:
                    data['bidang_hukum'] = value
                elif 'Bahasa' in key:
                    data['bahasa'] = value
                elif 'Keterangan Status' in key:
                    data['detail_status'] = value
                    if 'mencabut' in value.lower():
                        data['status'] = 'Berlaku'
                    elif 'dicabut' in value.lower():
                        data['status'] = 'Dicabut'

    # Ambil status dari status box
    status_box_value = soup.find('div', class_='status__box__value')
    if status_box_value:
        data['status'] = status_box_value.get_text(strip=True)

    # Ambil link PDF
    def extract_file_urls(header_text):
        file_data = {}
        all_mt4_divs = soup.find_all('div', class_='mt-4')
        for div in all_mt4_divs:
            if header_text in div.get_text():
                links_div = div.find_next_sibling('div', class_='mt-2')
                if links_div:
                    preview_link = links_div.find('a', class_='link_preview')
                    if preview_link and 'data-src' in preview_link.attrs:
                        file_data['preview'] = preview_link['data-src']
                    download_link = links_div.find('a', href=True, target='_blank')
                    if download_link and ('download' in download_link['href']):
                        file_data['download'] = download_link['href']
                break
        return file_data

    # Ambil link file peraturan (PDF)
    peraturan_files = extract_file_urls('File Peraturan')
    if 'download' in peraturan_files:
        data['pdf_url'] = peraturan_files['download']
    elif 'preview' in peraturan_files:
        data['pdf_url'] = peraturan_files['preview']

    return data

def map_kpu_data_to_legal_document_format(scraped_data: dict) -> dict:
    """Map KPU data to LegalDocument format"""
    # Buat mapping yang sesuai dengan struktur LegalDocument
    mapping = {
        'title': scraped_data.get('title'),
        'tahun': scraped_data.get('tahun'),  # Pastikan namanya 'tahun' bukan 'tahun_terbit'
        'nomor': scraped_data.get('nomor'),
        'jenis': scraped_data.get('jenis'),
        'singkatan_jenis': scraped_data.get('singkatan_jenis'),
        'tipe_dokumen': scraped_data.get('tipe_dokumen'),
        'tanggal_ditetapkan': scraped_data.get('tanggal_ditetapkan'),
        'tanggal_diundangkan': scraped_data.get('tanggal_diundangkan'),
        'tempat_penetapan': scraped_data.get('tempat_penetapan'),
        'penandatangan': scraped_data.get('penandatangan'),
        'teu_badan_pengarang': scraped_data.get('teu_badan_pengarang'),
        'bahasa': scraped_data.get('bahasa'),
        'bidang_hukum': scraped_data.get('bidang_hukum'),
        'subjek': scraped_data.get('subjek'),
        'status': scraped_data.get('status'),
        'detail_status': scraped_data.get('detail_status'),
        'pdf_url': scraped_data.get('pdf_url')
    }
    
    # Hapus key yang None
    return {k: v for k, v in mapping.items() if v is not None}

if __name__ == "__main__":
    url_to_scrape = "https://jdih.kpu.go.id/peraturan-kpu/detail/IOKYlOq4mz7DF-uJxUUm8UJRNnBVclk2MDBIWnlwVmdKUkhJRVE9PQ"
    
    print("🔍 Memulai scraping...")
    scraped_data = scrape_kpu_regulation_detail(url_to_scrape)
    
    print("\n📊 Data yang berhasil di-scrape:")
    print(json.dumps(scraped_data, indent=2, ensure_ascii=False))
    
    if scraped_data:
        mapped_data_for_legal_doc = map_kpu_data_to_legal_document_format(scraped_data)
        
        print("\n🔄 Data setelah mapping:")
        print(json.dumps(mapped_data_for_legal_doc, indent=2, ensure_ascii=False))

        try:
            legal_document_instance = LegalDocument(**mapped_data_for_legal_doc)
            print("\n✅ Objek LegalDocument berhasil dibuat dan dipetakan:")
            if hasattr(legal_document_instance, 'to_dict'):
                print(json.dumps(legal_document_instance.to_dict(), indent=2, ensure_ascii=False))
            else:
                print(json.dumps(legal_document_instance.__dict__, indent=2, ensure_ascii=False))
        except TypeError as e:
            print(f"\n❌ Gagal membuat objek LegalDocument: {e}")
            print("Data yang dipetakan:")
            print(json.dumps(mapped_data_for_legal_doc, indent=2, ensure_ascii=False))
    else:
        print("Gagal mengambil atau mem-parse data dari URL.")

