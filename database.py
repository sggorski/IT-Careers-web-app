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
    
def load_job(id):
  print("got:", id, "nothing")
  with engine.connect() as conn:
    cmd = f"select * from jobs where id={id}"
    result = conn.execute(text(cmd))
    data = result.mappings().all()
    if len(data) == 0: 
      return None
    else:
      return dict(data[0])
    
