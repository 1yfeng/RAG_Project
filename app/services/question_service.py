from app.db.database_postgres import get_connection

def save_question(context: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO questions (content) VALUES (%s) RETURNING id;", 
                   (context,)
                   )
    
    question_id = cursor.fetchone()['id']
    conn.commit()
    cursor.close()
    conn.close()

    return question_id