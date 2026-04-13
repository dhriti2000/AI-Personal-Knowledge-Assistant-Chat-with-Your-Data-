from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return db