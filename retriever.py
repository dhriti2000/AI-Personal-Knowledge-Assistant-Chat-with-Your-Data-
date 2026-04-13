def split_text(text, chunk_size=200):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def retrieve_chunks(chunks, query):
    # simple keyword match (no FAISS dependency)
    results = []
    for chunk in chunks:
        if any(word.lower() in chunk.lower() for word in query.split()):
            results.append(chunk)

    return results[:2] if results else chunks[:1]