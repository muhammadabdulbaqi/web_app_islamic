from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.prayer_calc import get_prayer_times

router = APIRouter()

@router.get("/api/prayer-times")
def prayer_times():
    data = get_prayer_times()
    return JSONResponse(data)
