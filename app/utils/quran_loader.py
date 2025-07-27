import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
QURAN_TEXT_PATH = os.path.join(BASE_DIR, "data", "quran-simple.txt")
ENGLISH_TEXT_PATH = os.path.join(BASE_DIR, "data", "en.ahmedali.txt")

BISMILLAH_AR = "بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ"
BISMILLAH_EN = "IN THE NAME OF ALLAH, THE MERCIFUL, THE COMPASSIONATE"
BISMILLAH_EN_ALT = "In the name of Allah, the Merciful, the Compassionate"  # some versions are capitalized differently

def load_quran(arabic_path=QURAN_TEXT_PATH, english_path=ENGLISH_TEXT_PATH):
    """
    Loads Quran Arabic and English text, pairing each ayah line-by-line.
    Returns a list of dictionaries with surah, ayah, arabic, and english text.
    Strips Bismillah from all surahs except Surah 1 (Al-Fatiha).
    """
    def clean_lines(path):
        with open(path, encoding="utf-8") as f:
            return [
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith("#")
            ]

    arabic_lines = clean_lines(arabic_path)
    english_lines = clean_lines(english_path)

    if len(arabic_lines) != len(english_lines):
        raise ValueError(f"Mismatch in line counts: Arabic={len(arabic_lines)}, English={len(english_lines)}")

    quran = []

    for ar_line, en_line in zip(arabic_lines, english_lines):
        try:
            surah_num, ayah_num, ar_text = ar_line.split("|", 2)
            _, _, en_text = en_line.split("|", 2)

            surah_num = int(surah_num)
            ayah_num = int(ayah_num)

            # === Remove Bismillah if it's NOT Surah 1 and it's the first verse
            if surah_num != 1 and ayah_num == 1:
                if ar_text.startswith(BISMILLAH_AR):
                    ar_text = ar_text.replace(BISMILLAH_AR, "").strip()
                if en_text.upper().startswith(BISMILLAH_EN.upper()):
                    en_text = en_text[len(BISMILLAH_EN):].strip()
                elif en_text.startswith(BISMILLAH_EN_ALT):
                    en_text = en_text[len(BISMILLAH_EN_ALT):].strip()

            quran.append({
                "surah": surah_num,
                "ayah": ayah_num,
                "arabic": ar_text,
                "english": en_text,
            })

        except ValueError:
            print("⚠️ Skipping malformed line:", ar_line, "||", en_line)

    return quran
