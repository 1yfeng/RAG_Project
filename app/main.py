from fastapi import FastAPI
from app.question import Question
from app.rag_query import RAGQuery

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/ask")
def ask_question(q: Question):
    return {"answer": f"You asked: {q.question}"}

@app.post("/query")
def ask_query(q: RAGQuery):
    return {"answer": f"You asked: {q.question}"}