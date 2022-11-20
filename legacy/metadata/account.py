from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class AccountMetadata:

    LIST_DATABASES_SQL = read_sql_file('account//databases')
    SCHEMAS_N_TABLES_SQL = read_sql_file('account//schemas_n_tables')

    def __init__(self):
        self._databases = None

    @property
    def databases(self):
        results = SnowflakeClient().fetch_all(AccountMetadata.LIST_DATABASES_SQL)
        databases = [{"db_name": result[1], "db_comment": result[6]} for result in results]
        self._databases = self.schemas_n_tables(databases)
        return self._databases

    def schemas_n_tables(self, databases: dict):
        databases_metadata = []
        for database in databases:
            schema_n_tables = AccountMetadata.SCHEMAS_N_TABLES_SQL.format(database=database.get('db_name'))
            results = SnowflakeClient().fetch_all(schema_n_tables)
            database.update({"num_schemas":results[0][0],"num_tables":results[0][1]})
            databases_metadata.append(database)
        
        return databases_metadata



