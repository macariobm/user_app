import psycopg2
import os

#fix the path to schema.sql, make it not hardcoded 
schema_file = f"{HOME}/user_app/app/database/schema.sql"

conn = psycopg2.connect(host='localhost',
                       database='user_app',
                       user=os.environ['POSTGRES_USER'],
                       password=os.environ['POSTGRES_PASSWORD'])
cursor = conn.cursor()

with open(schema_file,'r') as f:
    schema = f.read()

cursor.execute(schema)
conn.commit()
