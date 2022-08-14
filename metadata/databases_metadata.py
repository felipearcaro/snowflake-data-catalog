from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class DatabasesMetadata:

    LIST_DATABASES_SQL = read_sql_file('databases')

    def __init__(self):
        self._databases = None

    @property
    def databases(self):
        results = SnowflakeClient().fetch_all(DatabasesMetadata.LIST_DATABASES_SQL)
        databases = [{"db_name": result[0], "db_comment": result[1]} for result in results]
        self._databases = databases
        return self._databases

