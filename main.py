# main.py
from scraper import scrape_bis_items
from lua_writer import write_lua_file

URL = "https://www.icy-veins.com/wow-classic/mage-dps-pve-gear-best-in-slot?area=p6_mage"
output_path = "data/mage_phase6.lua"
spec_id = "Mage_Frost_Phase6"

if __name__ == "__main__":
    bis_data = scrape_bis_items(URL)
    write_lua_file(spec_id, bis_data, output_path)
