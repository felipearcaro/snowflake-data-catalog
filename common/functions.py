def read_sql_file(file_path, file_name):
    sql_file = f"{file_path}//{file_name}.sql"
    with open(sql_file, "r") as f:
        query = f.read()
    return query