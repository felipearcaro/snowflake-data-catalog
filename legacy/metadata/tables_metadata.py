from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class TablesMetadata:

    LIST_TABLES_SQL = read_sql_file('tables')

    def __init__(self, database, schema):
        self._tables = None
        self.database = database
        self.schema = schema

    @property
    def tables(self):
        tables = TablesMetadata.LIST_TABLES_SQL.format(database=self.database, schema=self.schema)
        results = SnowflakeClient().fetch_all(tables)
        tables = [{"db_name": result[0],"schema_name": result[1],"table_name": result[2], "table_comment": result[3]} for result in results]
        self._tables = tables
        return self._tables

