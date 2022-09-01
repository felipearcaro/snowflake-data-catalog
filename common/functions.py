import os

def read_transformation_file(file_name):
    sql_file = f"{os.getcwd()}//transformation_sample//sql//{file_name}"
    with open(sql_file, "r") as f:
        query = f.read()
    return query

def read_sql_file(file_name):
    sql_file = f"{os.getcwd()}//metadata//sql//{file_name}.sql"
    with open(sql_file, "r") as f:
        query = f.read()
    return query