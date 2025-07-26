from datetime import datetime

def get_prayer_times():
    # Temporary mock data for now
    now = datetime.now().strftime("%Y-%m-%d")
    return {
        "date": now,
        "Fajr": "04:45 AM",
        "Dhuhr": "12:15 PM",
        "Asr": "03:45 PM",
        "Maghrib": "06:30 PM",
        "Isha": "08:00 PM"
    }
