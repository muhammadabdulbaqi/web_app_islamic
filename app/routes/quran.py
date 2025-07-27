from fastapi import APIRouter
from app.utils.quran_loader import load_quran
from app.utils.quran_metadata import parse_quran_metadata

router = APIRouter()

@router.get("/api/quran")
def get_quran():
    quran_data = load_quran()
    return {"quran": quran_data}

@router.get("/api/quran/metadata")
def get_quran_metadata():
    metadata = parse_quran_metadata()
    return {"metadata": metadata}
