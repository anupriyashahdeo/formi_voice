from app.utils.tokenizer import chunk_text

# In-memory knowledge base
knowledge_base = []

def add_document(doc_text: str):
    """Break a document into chunks and add to the knowledge base"""
    chunks = chunk_text(doc_text, max_tokens=800)
    for chunk in chunks:
        knowledge_base.append(chunk)

def get_all_documents():
    """Return all stored document chunks"""
    return knowledge_base
