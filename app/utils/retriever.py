from sentence_transformers import SentenceTransformer, util
from app.utils.chunker import chunk_text
from app.db.knowledge_base import get_all_documents

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Cache for chunk embeddings
embeddings_cache = {}

def build_embeddings():
    """Build embeddings for all chunks in the knowledge base"""
    docs = get_all_documents()
    idx = 0
    for doc in docs:
        chunks = chunk_text(doc)  # Break doc into <800 token chunks
        for chunk in chunks:
            embeddings_cache[idx] = {
                "text": chunk,
                "embedding": model.encode(chunk, convert_to_tensor=True)
            }
            idx += 1

def retrieve_relevant_chunks(query: str, top_k: int = 3, threshold: float = 0.3):
    """Retrieve most relevant chunks instead of whole docs"""
    if not embeddings_cache:
        return [{"text": "Knowledge base is empty. Please add documents first.", "score": 0.0}]

    query_embedding = model.encode(query, convert_to_tensor=True)
    
    results = []
    for idx, entry in embeddings_cache.items():
        score = util.pytorch_cos_sim(query_embedding, entry["embedding"])[0].item()
        if score >= threshold:
            results.append({"text": entry["text"], "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results[:top_k] if results else [{"text": "Sorry, I don’t know the answer to that.", "score": 0.0}]
