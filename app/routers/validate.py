# app/routers/validate.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserRequest(BaseModel):
    name: str
    age: int
    email: str

@router.post("/")
def validate_request(data: UserRequest):
    if data.age < 18:
        raise HTTPException(status_code=400, detail="User must be 18+")
    return {"valid": True, "message": "User data is valid ✅"}
