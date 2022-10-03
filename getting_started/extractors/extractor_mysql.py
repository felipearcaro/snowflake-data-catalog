from common.functions import read_sql_file
from common.mysql_client import MySQLClient
from common.postgres_client import PostgresClient
import os

class MySQLPopulatesPostgres():

    FILE_PATH = f"{os.getcwd()}//getting_started///extractors//sql"
    GET_MYSQL_DATA = read_sql_file(FILE_PATH, 'get_mysql_data')
    POPULATE_POSTGRES = read_sql_file(FILE_PATH,'populate_postgres_mysql')

    def __init__(self):
        pass

    def populate_postgres(self, schemas:list = None):
         self._get_mysql_data()
    
    def _get_mysql_data(self):
        query = MySQLPopulatesPostgres.GET_MYSQL_DATA
        results = MySQLClient().fetch_all(query)
        if results:
            print(f"Fetching data from MySQL... \n")
            new_results = []
            for row in results:
                row = tuple(new_value.replace("'","").replace('"','') if isinstance(new_value,str) else new_value for new_value in row)
                new_results.append(row)
            self._populate_postgres(new_results)
    
    def _populate_postgres(self, snowflake_data):
        print(f"Populating Postgres... \n")
        query = MySQLPopulatesPostgres.POPULATE_POSTGRES.format(values=snowflake_data)
        query = query.replace("[","").replace("]","").replace("None","NULL")
        results = PostgresClient().execute(query)
        print(results)

# Currently just extracting subscriberb shard        
MySQLPopulatesPostgres().populate_postgres()