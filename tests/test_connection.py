import os
from dotenv import load_dotenv
import psycopg
load_dotenv()
conn = psycopg.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()
row = cur.execute("SELECT version();").fetchall()
cur.close()
conn.close()
