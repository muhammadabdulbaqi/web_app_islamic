import requests
from datetime import datetime, timedelta

def get_prayer_times_by_address(address: str):
    today = datetime.now().strftime("%d-%m-%Y")
    url = f"https://api.aladhan.com/v1/timingsByAddress/{today}"
    params = {
        "address": address
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()["data"]
    return {
        "date": data["date"]["readable"],
        "timings": data["timings"]
    }

def get_next_prayer_by_address(address: str):
    base_url = "https://api.aladhan.com/v1"
    today = datetime.now().strftime("%d-%m-%Y")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")

    # First, try today's next prayer
    url_today = f"{base_url}/nextPrayerByAddress/{today}?address={address}"
    res = requests.get(url_today)
    data = res.json().get("data", {})

    # If timing found, use it
    timings = data.get("timings", {})
    if timings:
        next_name, next_time = list(timings.items())[0]
        return {
            "name": next_name,
            "time": next_time,
            "date": today
        }

    # Otherwise, fallback to tomorrow's Fajr
    url_fallback = f"{base_url}/timingsByAddress/{tomorrow}?address={address}"
    fallback_res = requests.get(url_fallback)
    fallback_data = fallback_res.json().get("data", {})
    fallback_timings = fallback_data.get("timings", {})
    fajr_time = fallback_timings.get("Fajr", "Unavailable")

    return {
        "name": "Fajr",
        "time": fajr_time,
        "date": tomorrow
    }
