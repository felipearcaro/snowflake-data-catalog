import snowflake.connector
import os 
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('SF_USER')
PASSWORD = os.getenv('SF_PASSWORD')
ACCOUNT = os.getenv('SF_ACCOUNT')
print(USER,PASSWORD,ACCOUNT)


snowflake_client = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    session_parameters={
        'QUERY_TAG': 'Data_Catalog_MVP',
    }
)

cs = snowflake_client.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
snowflake_client.close()
