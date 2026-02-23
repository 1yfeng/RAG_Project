from pydantic import BaseModel

class QuestionCreate(BaseModel):
    content: str
    