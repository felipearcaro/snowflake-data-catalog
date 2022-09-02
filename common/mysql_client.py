import mysql.connector as connection
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT = os.getenv('MYSQL_ACCOUNT')
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSOWRD')

def fetch_pandas_mysql(sql: str):
    try:
        mydb = connection.connect(host=ACCOUNT,user=USER, passwd=PASSWORD,use_pure=True)
        query = sql
        df = pd.read_sql(query,mydb)
        mydb.close() 
    except Exception as e:
        mydb.close()
        print(str(e))
        df = None
    finally:
        return df

def mysql_fetch_all(sql: str):
    try:
        mydb = connection.connect(host=ACCOUNT,user=USER, passwd=PASSWORD,use_pure=True)
        query = sql
        cursor = mydb.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        mydb.close() 
    except Exception as e:
        mydb.close()
        print(str(e))
        results = None
    finally:
        return results