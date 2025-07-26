# Islamic Web App

* Prayer Times: Display accurate daily prayer times based on user location.

## Next Steps: Enhancing the Islamic Web App

We plan to continue building on this foundation with the following features:

### Core Features to Add

* Qur'an Viewer: Let users read the Qur'an in Arabic and English, with bookmarking and navigation.
* Hadith of the Day: Show a rotating daily hadith from authentic collections.

### Frontend Enhancements

* Build a responsive frontend using modern tools (e.g., TailwindCSS, React, or just enhanced HTML/CSS).
* Improve the user experience with layout, navigation, and accessibility improvements.

### Dynamic Content Storage

* Store Qur'an and Hadith content dynamically (e.g., from APIs or a structured local database).
* Add caching and performance optimization.

---

## What We've Built So Far

* Modular folder structure with clear separation between frontend (HTML, CSS, JS) and backend (FastAPI routes and utils)
* Reusable `header.html` and `footer.html` dynamically loaded into each page via `include.js`
* `prayer_times.html` page that fetches mock prayer times from `/api/prayer-times`
* Clean API logic separated in `routes/prayer_times.py` and `utils/prayer_calc.py`

---

## How to Run It Locally

1. Navigate to the project root:

   ```bash
   cd path/to/web_app_islamic
   ```

2. Run the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Open your browser and visit:

   * `http://localhost:8000/` for the home page
   * `http://localhost:8000/prayer_times.html` for the prayer times view

---

## What’s Next

* Replace mock prayer times with real data from the [AlAdhan API](https://aladhan.com/prayer-times-api)
* Add JS-based location support (get user’s location via browser and pass to API)
* Begin work on Qur’an and Hadith views (static content first, dynamic later)
* Possibly start introducing component-based structure if we shift to a JS frontend

---
