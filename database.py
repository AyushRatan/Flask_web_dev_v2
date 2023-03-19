import os
from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONNECTION_STRING']
#connection_string = "mysql+pymysql://ihhraicn2uvqzd2naaqw:pscale_pw_5x1USgGzrg1GnbR1IkdIDSE0UCi76Dsg3DY69KZGMZV@ap-south.connect.psdb.cloud/freshersportaldb?charset=utf8mb4"
print(db_conn_string)
print(type(db_conn_string))
ssl_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

engine = create_engine(db_conn_string, connect_args=ssl_args)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val "),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
