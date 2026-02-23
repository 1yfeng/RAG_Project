import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_root(client: AsyncClient):
    """测试根路径 GET /"""
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_read_item(client: AsyncClient):
    """测试 GET /items/{item_id}"""
    response = await client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "test"}


@pytest.mark.asyncio
async def test_read_item_no_query(client: AsyncClient):
    """测试 GET /items/{item_id} 不传 q 参数"""
    response = await client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


@pytest.mark.asyncio
async def test_read_item_invalid_id(client: AsyncClient):
    """测试 GET /items/{item_id} 传入非整数"""
    response = await client.get("/items/abc")
    assert response.status_code == 422  # 校验失败


@pytest.mark.asyncio
async def test_ask_question(client: AsyncClient):
    """测试 POST /ask"""
    response = await client.post("/ask", json={"question": "什么是RAG?"})
    assert response.status_code == 200
    assert response.json() == {"answer": "You asked: 什么是RAG?"}


@pytest.mark.asyncio
async def test_ask_question_missing_field(client: AsyncClient):
    """测试 POST /ask 缺少必填字段"""
    response = await client.post("/ask", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_ask_query(client: AsyncClient):
    """测试 POST /query"""
    response = await client.post("/query", json={"question": "什么是向量数据库?"})
    assert response.status_code == 200
    assert response.json() == {"answer": "You asked: 什么是向量数据库?"}


@pytest.mark.asyncio
async def test_ask_query_with_params(client: AsyncClient):
    """测试 POST /query 带完整参数"""
    response = await client.post("/query", json={
        "question": "RAG是什么?",
        "top_k": 3,
        "history": ["之前的问题"]
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_ask_query_invalid_top_k(client: AsyncClient):
    """测试 POST /query top_k 超出范围"""
    response = await client.post("/query", json={
        "question": "测试问题",
        "top_k": 20  # 超过 le=10
    })
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_ask_query_question_too_short(client: AsyncClient):
    """测试 POST /query question 太短"""
    response = await client.post("/query", json={
        "question": "a"  # 小于 min_length=2
    })
    assert response.status_code == 422
