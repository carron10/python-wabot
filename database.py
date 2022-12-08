import psycopg2
import os
from urlparse import urlparse # for python 3+ use: from urllib.parse import urlparse
class database:
    def __init__(self):
        
        
        result = urlparse("postgres://microservices_user:P0yvBbwCPkDutmCq22o9LvOJyuidt8xe@dpg-ce7ikr1a6gdnvfth6m7g-a/microservices")
        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        port = result.port
        self.conn = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
        )
        cur=self.conn.cursor()
        cur.execute(''''create table if not exists my_data(
              id SERIAL,
              users text,
              msgs text,
              products text
        )''')
        cur.close()
    def get_connection(self):
        return self.conn
