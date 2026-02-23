from pydantic import BaseModel, Field
from typing import Optional, List

class RAGQuery(BaseModel):
    question: str = Field(..., min_length=2, max_length=30, description="this is the customer's question")

    top_k: int = Field(default = 5 , ge= 1, le = 10, description="the number of retrieved documents to return")

    history: List[str] = []
