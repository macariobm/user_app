import psycopg2
from psycopg2.extras import DictCursor
import os

#fix the path to schema.sql, make it not hardcoded 
schema_file = f"$HOME/user_app/app/database/schema.sql"

conn = psycopg2.connect(host='localhost',
                       database='user_app',
                       user=os.environ['POSTGRES_USER'],
                       password=os.environ['POSTGRES_PASSWORD'])
cursor = conn.cursor(cursor_factory=DictCursor)

with open(schema_file,'r') as f:
    schema = f.read()

cursor.execute(schema)
conn.commit()
