import os
from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONNECTION_STRING']
#connection_string = "mysql+pymysql://ihhraicn2uvqzd2naaqw:pscale_pw_5x1USgGzrg1GnbR1IkdIDSE0UCi76Dsg3DY69KZGMZV@ap-south.connect.psdb.cloud/freshersportaldb?charset=utf8mb4"
print(db_conn_string)
print(type(db_conn_string))
ssl_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem" }}


engine = create_engine(db_conn_string,
                       connect_args=ssl_args)
