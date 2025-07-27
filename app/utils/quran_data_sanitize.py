import os
import xml.etree.ElementTree as ET

# === Paths ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Points to /app/
DATA_DIR = os.path.join(BASE_DIR, "data")

ARABIC_PATH = os.path.join(DATA_DIR, "quran-simple.txt")
ENGLISH_PATH = os.path.join(DATA_DIR, "en.ahmedali.txt")
XML_PATH = os.path.join(DATA_DIR, "quran-data.xml")

CLEAN_ARABIC_OUT = os.path.join(DATA_DIR, "quran-simple-cleaned.txt")
CLEAN_ENGLISH_OUT = os.path.join(DATA_DIR, "en.ahmedali-cleaned.txt")


# === Load and Clean ===
def clean_lines(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]


def parse_metadata():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
    return [
        {
            "index": int(s.get("index")),
            "start": int(s.get("start")),
            "ayas": int(s.get("ayas"))
        }
        for s in root.find("suras").findall("sura")
    ]


def sanitize_quran():
    arabic = clean_lines(ARABIC_PATH)
    english = clean_lines(ENGLISH_PATH)
    metadata = parse_metadata()

    clean_arabic = []
    clean_english = []

    for surah in metadata:
        start = surah["start"]
        end = start + surah["ayas"]
        surah_num = surah["index"]

        ar_verses = arabic[start:end]
        en_verses = english[start:end]

        if surah_num != 1 and ar_verses[0].split("|", 2)[2].startswith("بِسْمِ اللَّهِ"):
            ar_verses = ar_verses[1:]
            en_verses = en_verses[1:]

        clean_arabic.extend(ar_verses)
        clean_english.extend(en_verses)

    if len(clean_arabic) != len(clean_english):
        raise ValueError(f"Post-cleaning mismatch: Arabic={len(clean_arabic)}, English={len(clean_english)}")

    with open(CLEAN_ARABIC_OUT, "w", encoding="utf-8") as f_ar:
        f_ar.write("\n".join(clean_arabic))

    with open(CLEAN_ENGLISH_OUT, "w", encoding="utf-8") as f_en:
        f_en.write("\n".join(clean_english))

    print(f"✅ Cleaned files written: \n- {CLEAN_ARABIC_OUT}\n- {CLEAN_ENGLISH_OUT}")


if __name__ == "__main__":
    sanitize_quran()
