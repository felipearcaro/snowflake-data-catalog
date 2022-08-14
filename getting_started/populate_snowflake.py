from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

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
CreateAccountMetadata().populate_snowflake()





