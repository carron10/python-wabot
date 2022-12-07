class database:

    def __init__(self,db,user,pswd):
        self.conn = psycopg2.connect(
        host=os.getenv("postgres_host"),
        database=os.getenv("postgres_db"),
        user=os.getenv("postgres_user"),
        password=os.getenv("postgres_pswd"),
        port=os.getenv("postgres_port")
        )
    def get_connection(self):
        return self.conn
