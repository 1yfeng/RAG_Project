import pytest
from unittest.mock import AsyncMock, patch, MagicMock


@pytest.mark.asyncio
@patch("app.services.question_service.get_connection")
async def test_save_question(mock_get_conn):
    """测试 save_question 函数（mock 数据库）"""
    # 模拟游标和连接
    mock_cursor = AsyncMock()
    mock_cursor.__aenter__.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {"id": 1}

    mock_conn = AsyncMock()
    mock_conn.__aenter__.return_value = mock_conn
    mock_conn.cursor = MagicMock(return_value=mock_cursor)

    mock_get_conn.return_value = mock_conn

    from app.services.question_service import save_question
    result = await save_question("测试问题")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO questions (content) VALUES (%s) RETURNING id;",
        ("测试问题",)
    )
    mock_conn.commit.assert_called_once()
