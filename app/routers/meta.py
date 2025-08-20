# app/routers/meta.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_metadata():
    return {
        "api": "Formi Voice",
        "description": "Assignment API for handling validation, logging, routing, and function calls",
        "author": "Your Name",
        "framework": "FastAPI"
    }
