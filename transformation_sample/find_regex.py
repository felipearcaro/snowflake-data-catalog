import re
from common.functions import read_sql_file, read_transformation_file
from common.snowflake_client import *
from common.postgres_client import *
import os

transformation_files = [x[2] for x in os.walk(f"{os.getcwd()}//transformation_sample//sql")]

for file in transformation_files[0]:


    sql_query = read_transformation_file(file)
    regexp = r"(merge into|MERGE INTO)"
    if re.search(regexp, sql_query):

        ## Getting table that's being populated
        regexp = r"(merge into|MERGE INTO)(\s+|\n+)([^\s]+)"
        result = re.search(regexp, sql_query)

        target_table= result.group(0).split(" ")[-1]
        print(f"Here's the table that's being populated: {target_table.upper()}")


        ## Getting table that's being used to populate new table
        regexp = r"(using|USING)(\s+|\n+)([^\s]+)"
        result = re.search(regexp, sql_query)

        source_table= result.group(0).split(" ")[-1]
        print(f"Here's the table that's being used: {source_table.upper()}")

        query = f"""
        insert into data_catalog_lineage (database_name, schema_name, table_name, source_table, source_query)
        VALUES (
        'DATA_QUALITY',
        'FELIPE',
        'NEW_TABLE',
        '{source_table}',
        '{sql_query}')
        """

        postgree_client(query)
 

    