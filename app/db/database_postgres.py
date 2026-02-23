import psycopg
from psycopg.rows import dict_row

async def get_connection():
    conn = await psycopg.AsyncConnection.connect(
        host= "localhost",
        dbname = "rag_db",
        user= "postgres",
        password= "postgres",
        row_factory =dict_row
    )
    return conn