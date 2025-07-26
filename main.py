from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static assets under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve "/" -> index.html
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Serve *.html files dynamically from static/
@app.get("/{page_name}.html")
async def html_page(page_name: str):
    filepath = f"static/{page_name}.html"
    if os.path.exists(filepath):
        return FileResponse(filepath)
    return {"detail": "Not Found"}
