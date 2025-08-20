from fastapi import APIRouter, Query
from app.utils.retriever import retrieve_relevant_chunks

router = APIRouter()

@router.get("/retrieve")
def retrieve(query: str = Query(..., description="User query text")):
    results = retrieve_relevant_chunks(query)
    return {"query": query, "results": results}
