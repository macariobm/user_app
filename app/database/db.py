import sqlite3
import os

#fix the path to schema.sql, make it not hardcoded 
schema_file = f"{HOME}/user_app/app/database/schema.sql"

conn = sqlite3.connect('user_app.db', check_same_thread=False)
cursor = conn.cursor()

with open(schema_file,'r') as f:
    schema = f.read()

cursor.execute(schema)
conn.commit()
