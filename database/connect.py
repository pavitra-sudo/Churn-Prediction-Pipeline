from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()  # loads .env into environment

DB_PATH = os.getenv("SQLITE_DB_PATH")

if not DB_PATH:
    raise RuntimeError("❌ SQLITE_DB_PATH not set in .env")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
