from common.functions import read_sql_file
from common.snowflake_client import SnowflakeClient

class ColumnsMetadata:

    LIST_COLUMNS_SQL = read_sql_file('columns')

    def __init__(self, database, schema, table):
        self._tables = None
        self.database = database
        self.schema = schema
        self.table = table

    @property
    def columns(self):
        columns = ColumnsMetadata.LIST_COLUMNS_SQL.format(database=self.database, schema=self.schema, table=self.table)
        results = SnowflakeClient().fetch_all(columns)
        columns = [{"db_name": result[0],"schema_name": result[1],"table_name": result[2], "column_name": result[3],"column_comment": result[4],"data_type": result[5], "is_nullable": result[6], "char_max_len": result[7],"num_precision": result[8]} for result in results]
        self._columns = columns
        return self._columns

