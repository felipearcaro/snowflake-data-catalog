from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class SchemasMetadata:

    LIST_SCHEMAS_SQL = read_sql_file('schemas')

    def __init__(self, database):
        self._schemas = None
        self.database = database

    @property
    def schemas(self):
        schemas = SchemasMetadata.LIST_SCHEMAS_SQL.format(database=self.database)
        results = SnowflakeClient().fetch_all(schemas)
        schemas = [{"db_name": result[0],"schema_name": result[1], "schema_comment": result[2]} for result in results]
        self._schemas = schemas
        return self._schemas

