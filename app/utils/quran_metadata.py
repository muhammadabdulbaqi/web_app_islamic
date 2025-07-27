import xml.etree.ElementTree as ET
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # This points to the `app/` directory
QURAN_METADATA_PATH = os.path.join(BASE_DIR, "data", "quran-data.xml")

def parse_quran_metadata(xml_path=QURAN_METADATA_PATH):
    """
    Parses Quran metadata from the provided XML file.

    Returns:
        list: List of surah metadata dictionaries.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    metadata_list = []

    for sura in root.findall(".//sura"):
        metadata_list.append({
            "index": int(sura.get("index")),
            "arabic_name": sura.get("name"),
            "english_name": sura.get("tname"),
            "transliteration": sura.get("ename"),
            "type": sura.get("type"),
            "ayah_count": int(sura.get("ayas")),
            "rukus": int(sura.get("rukus")),
            "revelation_order": int(sura.get("order")),
            "start_ayah": int(sura.get("start")) + 1,
        })

    return metadata_list
