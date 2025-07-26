from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from app.routes import prayer_times  

app = FastAPI()

# Serve static assets (CSS, JS, partials)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve "/" as index.html
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Serve any static *.html page like /prayer_times.html
@app.get("/{page_name}.html")
async def html_page(page_name: str):
    filepath = f"static/{page_name}.html"
    if os.path.exists(filepath):
        return FileResponse(filepath)
    return {"detail": "Not Found"}

# Include the prayer times router
app.include_router(prayer_times.router)
