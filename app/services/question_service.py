from app.db.database_postgres import get_connection

async def save_question(context: str):
    conn = await get_connection()

    async with conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO questions (content) VALUES (%s) RETURNING id;", 
                   (context,)
                   )
            result = await cur.fetchone()
            await conn.commit()
            return result["id"]