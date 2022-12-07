class database:
    def __init__(self):
        
        self.conn = psycopg2.connect(
        host=os.getenv("postgres_host"),
        database=os.getenv("postgres_db"),
        user=os.getenv("postgres_user"),
        password=os.getenv("postgres_pswd"),
        port=os.getenv("postgres_port")
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
