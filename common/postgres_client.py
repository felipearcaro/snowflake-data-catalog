from re import split
import psycopg2
import requests
import os
from dotenv import load_dotenv

load_dotenv()

pg_user = os.getenv('PG_USER')
pg_host = os.getenv('PG_HOST')
pg_password = os.getenv('PG_PASSWORD')
pg_database = os.getenv('PG_DATABASE')

def postgree_client_fetch_all(sql_statement):
    con = psycopg2.connect(
                host = pg_host,
                database=pg_database,
                user = pg_user,
                password = pg_password) 

    cursor = con.cursor()
    cur = con.cursor()
    cur.execute(sql_statement)
    rows = cur.fetchall()
    return rows


def postgree_client(sql_statement):
    con = psycopg2.connect(
                host = pg_host,
                database=pg_database,
                user = pg_user,
                password = pg_password)

    cur = con.cursor()
    cur.execute(sql_statement)
    con.commit()