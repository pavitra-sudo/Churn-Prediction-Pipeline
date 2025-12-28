from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()  # loads .env into environment

DB_PATH = os.getenv("SQLITE_DB_PATH")

if not DB_PATH:
    raise RuntimeError("❌ SQLITE_DB_PATH not set in .env")

def get_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # dict-like rows
    return conn
