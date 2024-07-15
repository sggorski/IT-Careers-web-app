from sqlalchemy import create_engine, text
import os
engine = create_engine(os.environ['DB_STR'])

def get_data():
  with engine.connect() as conn:
     result = conn.execute(text("select * from jobs"))
     data = []
     for row in result.mappings().all():
       data.append(dict(row))
  return data
    
print(get_data())       