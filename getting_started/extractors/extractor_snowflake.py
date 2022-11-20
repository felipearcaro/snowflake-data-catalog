from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient
from common.postgres_client import PostgresClient
import os

class SnowflakePopulatesPostgres():

    # LIST_SNOWFLAKE_DATABASES = read_sql_file('populate_snowflake//databases')
    FILE_PATH = f"{os.getcwd()}/getting_started///extractors//sql"
    GET_SNOWFLAKE_DATA = read_sql_file(FILE_PATH, 'get_snowflake_data')
    POPULATE_POSTGRES = read_sql_file(FILE_PATH,'populate_postgres_snowflake')

    def __init__(self):
        pass

    # def _list_snowflake_databases(self):
    #     results = SnowflakeClient().fetch_all(SnowflakePopulatesPostgres.LIST_SNOWFLAKE_DATABASES)
    #     databases = [{"db_name": result[1], "db_description": result[6]} for result in results]
    #     return databases

    def populate_postgres(self, databases:list = None):
        if databases is None:
            databases = self._list_snowflake_databases()
        results = self._get_snowflake_data(databases)

    
    def _get_snowflake_data(self, databases):
        for database in databases:
            query = SnowflakePopulatesPostgres.GET_SNOWFLAKE_DATA.format(db_name=database.get('db_name'), db_description=database.get('db_description'))
            results = SnowflakeClient().fetch_all(query)
            if results:
                print(f"Populating {database.get('db_name')} database metadata... \n\n")
                self._populate_postgres(results)
    
    def _populate_postgres(self, snowflake_data):
        query = SnowflakePopulatesPostgres.POPULATE_POSTGRES.format(values=snowflake_data)
        query = query.replace("[","").replace("]","").replace("None","NULL")
        PostgresClient().execute(query)
        
databases = [
    {"db_name": "SUBSCRIBER_TABLES",
    "db_description":"Subscriber databases"
    }
]

# Currently only extracting SUBSCRIBER_TABLES database   
SnowflakePopulatesPostgres().populate_postgres(databases)