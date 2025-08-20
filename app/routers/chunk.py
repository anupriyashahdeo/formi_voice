from fastapi import APIRouter
from app.db.knowledge_base import get_all_documents
from app.utils.chunker import chunk_text

router = APIRouter()

@router.get("/chunks")
def get_chunks():
    docs = get_all_documents()
    all_chunks = []
    for doc in docs:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)
    return {"chunks": all_chunks}
