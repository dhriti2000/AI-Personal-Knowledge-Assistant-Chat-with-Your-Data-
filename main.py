from fastapi import FastAPI
from loader import load_docs
from retriever import split_text, retrieve_chunks
from ai_engine import generate_answer

app = FastAPI()

text_data = load_docs("data.txt")
chunks = split_text(text_data)

@app.get("/ask")
def ask(query: str):
    relevant_chunks = retrieve_chunks(chunks, query)
    context = "\n".join(relevant_chunks)

    answer = generate_answer(query, context)

    return {
        "query": query,
        "answer": answer
    }
@app.get("/")
def home():
    return {"message": "AI Knowledge Assistant is running 🚀"}