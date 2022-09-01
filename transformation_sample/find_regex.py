import re
from common.functions import read_sql_file, read_transformation_file
from common.snowflake_client import *
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
        insert into data_catalog.public.data_catalog_lineage (DB_NAME, SCHEMA_NAME, TABLE_NAME, SOURCE_TABLE, QUERY)
        VALUES (
        'DATA_CATALOG',
        'DATA_CATALOG_SAMPLE',
        'SALES',
        '{source_table}',
        '{sql_query}')
        """

        SnowflakeClient().execute(query)
 

    