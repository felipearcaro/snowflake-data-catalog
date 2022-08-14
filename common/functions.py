import os

def read_sql_file(file_name):
    sql_file = f"{os.getcwd()}//metadata//sql//{file_name}.sql"
    with open(sql_file, "r") as f:
        query = f.read()
    return query
