import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('PG_USER')
HOST = os.getenv('PG_HOST')
PASSWORD = os.getenv('PG_PASSWORD')
DATABASE = os.getenv('PG_DATABASE')


class PostgresClient:

    def _connect(self):
        con = psycopg2.connect(
                    host = HOST,
                    database=DATABASE,
                    user = USER,
                    password = PASSWORD) 
        return con 

    def fetch_all(self, sql_statement):
        con = self._connect()
        cur = con.cursor()
        cur.execute(sql_statement)
        rows = cur.fetchall()
        return rows

    def execute(self, sql_statement):
        con = self._connect()
        cur = con.cursor()
        a = cur.execute(sql_statement)
        b= con.commit()