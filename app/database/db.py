import sqlite3

schema_file = "~/user_app/app/database/schema.sql"

conn = sqlite3.connect('user_app.db', check_same_thread=False)

with open(schema_file,'r') as f:
    schema = f.read().decode('utf8')

conn.execute(schema)
conn.commit()
conn.close()