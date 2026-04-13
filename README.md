# 🚀 AI Personal Knowledge Assistant (Chat with Your Data)

An AI-powered application that allows users to query their own data using natural language. The system retrieves relevant information from local documents and generates intelligent responses using a Large Language Model (LLM).

---

## 📌 Overview

This project implements a simplified **Retrieval-Augmented Generation (RAG)** pipeline:

* 📄 Load custom data (text files)
* 🔍 Retrieve relevant context
* 🤖 Generate AI-based responses
* 🌐 Expose functionality via FastAPI

---

## 🎯 Key Features

* ✅ Ask questions based on your own data
* ✅ Context-aware AI responses
* ✅ Lightweight RAG implementation (no heavy dependencies)
* ✅ FastAPI backend with interactive Swagger UI
* ✅ Modular architecture (loader, retriever, AI engine)

---

## 🧱 Project Structure

```
ai_knowledge_assistant/
│── main.py            # FastAPI entry point
│── ai_engine.py       # Handles AI response generation
│── retriever.py       # Retrieves relevant chunks
│── loader.py          # Loads data from file
│── data.txt           # Knowledge base
│── requirements.txt   # Dependencies
```

---

## ⚙️ How It Works (Step-by-Step)

### 1. Data Loading

The system reads data from a text file:

```python
text_data = load_docs("data.txt")
```

---

### 2. Chunking (Preprocessing)

The text is split into smaller chunks:

```python
chunks = split_text(text_data)
```

👉 Why?

* LLMs work better with smaller context
* Improves retrieval accuracy

---

### 3. Retrieval

When a query is received:

```python
relevant_chunks = retrieve_chunks(chunks, query)
```

👉 This step:

* Matches keywords from query
* Selects most relevant parts of data

---

### 4. Context Building

```python
context = "\n".join(relevant_chunks)
```

👉 Combines retrieved chunks into usable input

---

### 5. AI Response Generation

```python
answer = generate_answer(query, context)
```

👉 The LLM:

* Reads context
* Understands the question
* Generates a meaningful response

---

### 🔁 Full Flow

```
User Query → Retrieval → Context → LLM → Answer
```

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Set API Key (by using OpenAI)

```bash
$env:OPENAI_API_KEY="your_api_key_here"
```

---

### 3. Start Server

```bash
uvicorn main:app --reload
```

---

### 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

### 5. Test API

Use endpoint:

```
GET /ask
```

Example query:

```
What is Artificial Intelligence?
```

---

## 🧪 Sample Input & Output

### Input:

```text
Query: What is AI?
```

### Output:

```json
{
  "query": "What is AI?",
  "answer": "Artificial Intelligence is the simulation of human intelligence..."
}
```

---

## 🧠 What’s Happening Behind the Scenes

| Step | Component       | Description          |
| ---- | --------------- | -------------------- |
| 1    | Loader          | Reads data from file |
| 2    | Retriever       | Finds relevant text  |
| 3    | Context Builder | Combines chunks      |
| 4    | AI Engine       | Generates response   |

---

## 🚨 Current Limitations

* Uses keyword-based retrieval (not embeddings)
* Works best with small datasets
* Requires API key (if using OpenAI)

---

## 🚀 Future Improvements

* 🔍 Vector embeddings (FAISS)
* 📄 PDF & DOCX support
* 💬 Chat UI (Streamlit)
* 🧠 Conversation memory
* 🤖 Multi-agent workflows

---

## 🎯 Use Cases

* Personal knowledge assistant
* Study helper
* Documentation search tool
* AI-powered notes system

---

## 🧠 Skills Demonstrated

* Python backend development
* FastAPI API design
* AI/LLM integration
* Retrieval-Augmented Generation (RAG)
* System design thinking



