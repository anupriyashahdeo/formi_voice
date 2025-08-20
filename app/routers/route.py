# app/routers/route.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/{destination}")
def route_call(destination: str):
    routes = {
        "sales": "+91-111-222-333",
        "support": "+91-444-555-666",
        "billing": "+91-777-888-999"
    }
    return {"destination": destination, "number": routes.get(destination, "Unknown")}
