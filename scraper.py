# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_bis_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    bis_data = []
    gear_sections = soup.select('div.gear-best-in-slot div.gear-table')

    for section in gear_sections:
        slot_header = section.select_one('h3')
        slot = slot_header.get_text(strip=True) if slot_header else "Unknown"

        item_row = section.select_one('a[href*="wowhead.com/item"]')
        if item_row:
            name = item_row.get_text(strip=True)
            link = item_row['href']
            item_id = extract_item_id_from_url(link)
            source = "Icy Veins"  # Placeholder
            bis_data.append({
                "slot": slot,
                "name": name,
                "source": source,
                "id": item_id
            })

    return bis_data

def extract_item_id_from_url(url):
    try:
        return url.split("/item=")[-1].split("&")[0]
    except Exception:
        return ""
