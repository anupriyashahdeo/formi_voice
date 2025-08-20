from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_info():
    return {"twillio": "twilio endpoint working"}
