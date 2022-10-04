import re
from common.functions import read_sql_file
from common.postgres_client import PostgresClient
import os

FILE_PATH = f"{os.getcwd()}//getting_started///data_lineage//sql"
transformation_files = [x[2] for x in os.walk(f"{os.getcwd()}//getting_started//data_lineage//sql")]

for file in transformation_files[0]:

    sql_query = read_sql_file(FILE_PATH, file.split(".")[0])
    regexp = r"(merge into|MERGE INTO)"
    if re.search(regexp, sql_query):

        # Getting table that's being populated
        regexp = r"(merge into|MERGE INTO)(\s+|\n+)([^\s]+)"
        result = re.search(regexp, sql_query)

        target_full_table = result.group(0).split(" ")[-1]
        target_database = target_full_table.split(".")[0]
        target_schema = target_full_table.split(".")[1]
        target_table = target_full_table.split(".")[2]
        print(f"Here's the table that's being populated: {target_full_table.upper()}")

        # Getting table that's being used to populate new table
        regexp = r"(using|USING)(\s+|\n+)([^\s]+)"
        result = re.search(regexp, sql_query)

        source_table= result.group(0).split(" ")[-1]
        print(f"Here's the table that's being used: {source_table.upper()}")

        query = f"""
        insert into data_catalog_lineage (dbms, database_name, schema_name, table_name, source_table, source_query)
        VALUES (
        'snowflake', 
        '{target_database}',
        '{target_schema}',
        '{target_table}',
        '{source_table}',
        '{sql_query}')
        """

        PostgresClient().execute(query)