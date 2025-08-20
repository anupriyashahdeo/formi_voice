# app/routers/retell.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/repeat/{text}")
def repeat_text(text: str):
    return {"original": text, "retell": text[::-1]}  # just reverses text for demo
