from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient
from common.postgres_client import postgree_client

class CreateAccountMetadata:

    LIST_DATABASES_SQL = read_sql_file('populate_snowflake//databases')
    POPULATE_SQL = read_sql_file('populate_snowflake//join_metadata')
    # SCHEMAS_TABLES_COUNT_SQL = read_sql_file('populate_snowflake//db_schemas_tables_count')

    def __init__(self):
        pass

    def populate_snowflake(self):
        databases = self._list_databases()
        results = self._populate_snowflake(databases)

    def _list_databases(self):
        results = SnowflakeClient().fetch_all(CreateAccountMetadata.LIST_DATABASES_SQL)
        databases = [{"db_name": result[1], "db_description": result[6]} for result in results]
        return databases

    def _populate_snowflake(self, databases):
        for database in databases:
            query = CreateAccountMetadata.POPULATE_SQL.format(db_name=database.get('db_name'), db_description=database.get('db_description'))
            results = SnowflakeClient().execute(query)


#Run file to populate Snowflake with tables metadata
# CreateAccountMetadata().populate_snowflake()

class CreateAccountMetadataPostgres():

    LIST_SNOWFLAKE_DATABASES = read_sql_file('populate_snowflake//databases')
    GET_SNOWFLAKE_DATA = read_sql_file('populate_snowflake//get_snowflake_data')
    POPULATE_POSTGRES = read_sql_file('populate_snowflake//populate_postgres')

    def __init__(self):
        pass

    def populate_postgres(self, databases:list = None):
        if databases is None:
            databases = self._list_snowflake_databases()
        results = self._get_snowflake_data(databases)

    def _list_snowflake_databases(self):
        results = SnowflakeClient().fetch_all(CreateAccountMetadataPostgres.LIST_SNOWFLAKE_DATABASES)
        databases = [{"db_name": result[1], "db_description": result[6]} for result in results]
        return databases
    
    def _get_snowflake_data(self, databases):
        for database in databases:
            query = CreateAccountMetadataPostgres.GET_SNOWFLAKE_DATA.format(db_name=database.get('db_name'), db_description=database.get('db_description'))
            results = SnowflakeClient().fetch_all(query)
            if results:
                print(f"Populating {database.get('db_name')} database metadata... \n\n")
                self._populate_postgres(results)
    
    def _populate_postgres(self, snowflake_data):
        query = CreateAccountMetadataPostgres.POPULATE_POSTGRES.format(values=snowflake_data)
        query = query.replace("[","").replace("]","").replace("None","NULL")
        postgree_client(query)
        
databases = [
    {"db_name": "SUBSCRIBER_TABLES",
    "db_description":"This is FIVETRAN database"
    }
]

CreateAccountMetadataPostgres().populate_postgres(databases)