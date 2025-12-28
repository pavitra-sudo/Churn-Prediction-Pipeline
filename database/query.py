from database.connect import get_connection
def fetch(query: str, params: tuple = ()):
    with get_connection() as conn:
        cursor = conn.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
