# app/routers/log.py
from fastapi import APIRouter
from pydantic import BaseModel
import datetime

router = APIRouter()

logs = []  # in-memory log list (can be DB later)

class LogEntry(BaseModel):
    event: str
    level: str = "INFO"

@router.post("/")
def add_log(entry: LogEntry):
    log_item = {"event": entry.event, "level": entry.level, "timestamp": datetime.datetime.utcnow().isoformat()}
    logs.append(log_item)
    return {"message": "Log added", "log": log_item}

@router.get("/")
def get_logs():
    return {"logs": logs}
