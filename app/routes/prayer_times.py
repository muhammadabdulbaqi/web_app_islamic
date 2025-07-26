from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.utils.prayer_calc import get_prayer_times_by_address, get_next_prayer_by_address

router = APIRouter()

@router.get("/api/prayer-times")
def prayer_times(address: str = Query(...)):
    data = get_prayer_times_by_address(address)
    return JSONResponse(data)

@router.get("/api/next-prayer")
def next_prayer(address: str = Query(...)):
    data = get_next_prayer_by_address(address)
    return JSONResponse(data)
