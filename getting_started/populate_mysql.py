from common.functions import read_sql_file
from common.mysql_client import mysql_fetch_all
from common.postgres_client import postgree_client

class CreateAccountMetadataPostgresMySQL():

    GET_MYSQL_DATA = read_sql_file('populate_snowflake//get_mysql_data')
    POPULATE_POSTGRES = read_sql_file('populate_snowflake//populate_postgres_mysql')

    def __init__(self):
        pass

    def populate_postgres(self, schemas:list = None):
         self._get_mysql_data()

    
    def _get_mysql_data(self):

        query = CreateAccountMetadataPostgresMySQL.GET_MYSQL_DATA
        results = mysql_fetch_all(query)
        if results:
            new_results = []
            for row in results:
                row = tuple(new_value.replace("'","").replace('"','') if isinstance(new_value,str) else new_value for new_value in row)
                new_results.append(row)
            print(f"Populating Mysqldatabase metadata... \n\n")
            self._populate_postgres(new_results)
    
    def _populate_postgres(self, snowflake_data):
        query = CreateAccountMetadataPostgresMySQL.POPULATE_POSTGRES.format(values=snowflake_data)
        query = query.replace("[","").replace("]","").replace("None","NULL")
        postgree_client(query)
        
CreateAccountMetadataPostgresMySQL().populate_postgres()