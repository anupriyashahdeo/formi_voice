def chunk_text(text: str, max_tokens: int = 800):
    words = text.split()
    chunks, current_chunk = [], []

    for word in words:
        if len(" ".join(current_chunk + [word])) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
        else:
            current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
