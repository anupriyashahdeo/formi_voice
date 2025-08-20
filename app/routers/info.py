import datetime
from fastapi import APIRouter

router = APIRouter()

start_time = datetime.datetime.utcnow()

@router.get("/")
def get_info():
    uptime = datetime.datetime.utcnow() - start_time
    return {
        "service": "Formi Voice API",
        "version": "1.0.0",
        "uptime": str(uptime),
        "status": "running"
    }