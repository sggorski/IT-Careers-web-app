from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
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
  with engine.connect() as conn:
    cmd = f"select * from jobs where id={id}"
    result = conn.execute(text(cmd))
    data = result.mappings().all()
    if len(data) == 0: 
      return None
    else:
      return dict(data[0])
    
def save_application(id, data):
  try:
      with engine.connect() as conn:
          cmd = text("""
              INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
              VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
          """)
          conn.execute(cmd, {
              'job_id': id,
              'full_name': data['full_name'],
              'email': data['email'],
              'linkedin_url': data['li_url'],
              'education': data['education'],
              'work_experience': data['work_experience'],
              'resume_url': data['cv_url']
          })
          conn.commit()
          print("Dane zostały zapisane pomyślnie")
  except SQLAlchemyError as e:
      print(f"Wystąpił błąd: {e}")