from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
load_dotenv()
db_connection_string = os.environ.get('SECRET_KEY')
engine = create_engine(
    db_connection_string,
    connect_args={
        'ssl': {
            'ssl_ca': '"/etc/ssl/cert.pem"'
        }
    })
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Jobs"))
        jobs = []
        for row in result.all():
            d = row._mapping
            jobs.append(d)
        return jobs

def jobDetails(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Jobs WHERE id = :val").bindparams(val=id))
        row = result.all()
        if not row:
            return 'Job not found'
        else:
            return row[0]._mapping

def add_application(job_id,application):
    with engine.connect() as conn:
        query = conn.execute(text("INSERT INTO applications (Job_Id, Full_Name, Email, Work_Experience, LinkedIn,Education,Resume_URL)"
                     " VALUES ((:Job_Id, :Full_Name, :Email, :Work_Experience,:LinkedIn,:Education,:Resume_URL)").bindparams(
            Job_Id=application['Job_Id'], Full_Name=application['Full_Name'], Email=application['Email'],
            Work_Experience=application['Work_Experience'], LinkedIn=application['LinkedIn'],
            Education=application['Education'], Resume_URL=application['Resume_URL']))
