import os
from dotenv import load_dotenv
import psycopg
load_dotenv()
with open(r'D:\Enterprise GPT\database\schema.sql', 'r') as f:
    schema_sql = f.read()
conn = psycopg.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()
cur.execute(schema_sql)
conn.commit()
cur.execute("SELECT COUNT(*) FROM orders;")
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
