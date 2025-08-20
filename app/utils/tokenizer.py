# app/utils/tokenizer.py
import tiktoken

# Use OpenAI GPT-3.5/4 tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    return len(encoding.encode(text))

def chunk_text(text: str, max_tokens: int = 800) -> list[str]:
    tokens = encoding.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i+max_tokens]
        chunks.append(encoding.decode(chunk))
    return chunks
