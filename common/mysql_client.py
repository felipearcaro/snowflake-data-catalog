import mysql.connector as connection
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT = os.getenv('MYSQL_ACCOUNT')
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSOWRD')

class MySQLClient:

    def _connect(self):
        mysql_client = connection.connect(host=ACCOUNT,user=USER, passwd=PASSWORD,use_pure=True)
        return mysql_client

    def fetch_pandas_dataframe(self, sql: str):
        mysql_client = self._connect()
        try:
            query = sql
            df = pd.read_sql(query, mysql_client)
            mysql_client.close() 
        except Exception as e:
            mysql_client.close()
            print(str(e))
            df = None
        finally:
            return df

    def fetch_all(self, sql: str):
        mysql_client = self._connect()
        try:
            cursor = mysql_client.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            mysql_client.close() 
        except Exception as e:
            results = None
            mysql_client.close()
            print(str(e))
        finally:
            return results