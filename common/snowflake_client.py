import snowflake.connector
import os 
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('SF_USER')
PASSWORD = os.getenv('SF_PASSWORD')
ACCOUNT = os.getenv('SF_ACCOUNT')

class SnowflakeClient:

    def _connect(self):
        snowflake_client = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT)
        return snowflake_client.cursor()

    def execute(self, sql: str):
        cursor = self._connect()
        cursor.execute("USE WAREHOUSE LOAD_WH;")
        with cursor.execute(sql) as execute_query:
            print(f"Executing query: {sql[:100]}")
 
    def fetch_one(self, sql: str):
        cursor = self._connect()
        cursor.execute("USE WAREHOUSE LOAD_WH;")
        with cursor.execute(sql) as execute_query:
            print(f"Executing query: {sql[:100]}")
            result = execute_query.fetchone()
        return result 
     
    def fetch_all(self, sql: str):
        cursor = self._connect()
        cursor.execute("USE WAREHOUSE LOAD_WH;")
        with cursor.execute(sql) as execute_query:
            print(f"Executing query: {sql}")
            result = execute_query.fetchall()
        return result 

    def fetch_pandas_dataframe(self, sql: str):
        cursor = self._connect()
        cursor.execute("USE WAREHOUSE LOAD_WH;")
        with cursor.execute(sql) as execute_query:
            print(f"Executing query: {sql}")
            result = execute_query.fetch_pandas_all()
        return result