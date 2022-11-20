from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class DatabaseMetadata:

    LIST_SCHEMAS_SQL = read_sql_file('database//schemas')
    NUM_TABLES_SQL = read_sql_file('database//num_tables')

    def __init__(self, database):
        self._schemas = None
        self.database = database

    @property
    def schemas(self):
        schemas = DatabaseMetadata.LIST_SCHEMAS_SQL.format(database=self.database)
        results = SnowflakeClient().fetch_all(schemas)
        schemas = [{"db_name": result[0], "schema_name": result[1], "schema_comment": result[2]} for result in results]
        self._schemas = self.num_tables(schemas)
        return self._schemas

    def num_tables(self, schemas: dict):
        schemas_metadata = []
        for schema in schemas:
            num_tables = DatabaseMetadata.NUM_TABLES_SQL.format(database=schema.get('db_name'), schema=schema.get('schema_name'))
            results = SnowflakeClient().fetch_all(num_tables)
            schema.update({"num_tables":results[0][0]})
            schemas_metadata.append(schema)
        
        return schemas_metadata


# felipe = DatabaseMetadata('DATA_CATALOG')
# print(felipe.schemas)


