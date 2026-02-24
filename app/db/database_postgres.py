import os
import psycopg
from psycopg.rows import dict_row

async def get_connection():
    conn = await psycopg.AsyncConnection.connect(
        host= os.getenv("DB_HOST", "localhost"),
        dbname = os.getenv("DB_NAME", "rag_db"),
        user= os.getenv("DB_USER", "postgres"),
        password= os.getenv("DB_PASSWORD", "postgres"),
        row_factory =dict_row
    )
    return conn