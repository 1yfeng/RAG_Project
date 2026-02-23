import pytest
from pydantic import ValidationError
from app.schemas.question import Question
from app.schemas.rag_query import RAGQuery
from app.schemas.qa import QuestionCreate


class TestQuestion:
    """测试 Question 模型"""

    def test_valid_question(self):
        q = Question(question="什么是RAG?")
        assert q.question == "什么是RAG?"

    def test_missing_question(self):
        with pytest.raises(ValidationError):
            Question()


class TestRAGQuery:
    """测试 RAGQuery 模型"""

    def test_valid_with_defaults(self):
        q = RAGQuery(question="测试问题")
        assert q.question == "测试问题"
        assert q.top_k == 5
        assert q.history == []

    def test_valid_full_params(self):
        q = RAGQuery(question="测试问题", top_k=3, history=["历史1"])
        assert q.top_k == 3
        assert q.history == ["历史1"]

    def test_top_k_too_large(self):
        with pytest.raises(ValidationError):
            RAGQuery(question="测试问题", top_k=20)

    def test_top_k_too_small(self):
        with pytest.raises(ValidationError):
            RAGQuery(question="测试问题", top_k=0)

    def test_question_too_short(self):
        with pytest.raises(ValidationError):
            RAGQuery(question="a")

    def test_question_too_long(self):
        with pytest.raises(ValidationError):
            RAGQuery(question="a" * 31)


class TestQuestionCreate:
    """测试 QuestionCreate 模型"""

    def test_valid(self):
        q = QuestionCreate(content="这是一个问题")
        assert q.content == "这是一个问题"

    def test_missing_content(self):
        with pytest.raises(ValidationError):
            QuestionCreate()
