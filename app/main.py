from fastapi import FastAPI
from app.db.knowledge_base import add_document
from app.utils.retriever import build_embeddings

from app.routers import info, retrieve, validate, meta, route, log, retell, twilio,chunk

app = FastAPI(
    title="Formi Voice API",
    description="Backend service for Formi Voice assignment",
    version="1.0.0"
)
app.include_router(chunk.router, prefix="/api", tags=["Chunking"])
app.include_router(retrieve.router, prefix="/api", tags=["Retrieval"])
@app.on_event("startup")
def load_data():
    # Example doc (replace with real docs later)
    add_document("Apple, Banana, and Mango are three fruits.")
    add_document("FastAPI is a modern web framework for building APIs with Python.")
    add_document("Twilio provides APIs for messaging, voice, and video applications.")
    add_document("Google Sheets API allows programmatic access to spreadsheets.")

    build_embeddings()
# Include routers
app.include_router(info.router, prefix="/info", tags=["Info"])
app.include_router(validate.router, prefix="/validate", tags=["Validate"])
app.include_router(meta.router, prefix="/meta", tags=["Metadata"])
app.include_router(route.router, prefix="/route", tags=["Routing"])
app.include_router(log.router, prefix="/log", tags=["Logging"])
app.include_router(retell.router, prefix="/retell", tags=["Function Calling"])
app.include_router(chunk.router, prefix="/api", tags=["Chunking"])
# app.include_router(twilio.router, prefix="/twilio", tags=["Twilio"])

# Root health check
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Formi Voice API is running 🚀"}

