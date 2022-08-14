from flask import Flask, render_template, redirect, request, url_for, flash, session
from common.snowflake_client import *
from metadata.columns_metadata import ColumnsMetadata
from metadata.databases_metadata import DatabasesMetadata
from metadata.schemas_metadata import SchemasMetadata
from metadata.tables_metadata import TablesMetadata
from datetime import datetime

TODAYS_DATE = str(datetime.today()).split('.')[0]

app = Flask(__name__)


@app.route('/')
def index():
    results = DatabasesMetadata().databases
    return render_template('databases.html', results=results)

@app.route('/schemas')
def schemas():
    database = request.args.get('database')
    results = SchemasMetadata(database).schemas 
    return render_template('schemas.html', results=results, database=database)

@app.route('/tables')
def tables():
    database = request.args.get('database')
    schema = request.args.get('schema')
    results = TablesMetadata(database, schema).tables 
    return render_template('tables.html', results=results, database=database, schema=schema)

@app.route('/columns')
def columns():
    database = request.args.get('database')
    schema = request.args.get('schema')
    table = request.args.get('table')
    results = ColumnsMetadata(database, schema, table).columns 
    print(results)
    return render_template('columns.html', results=results, database=database, schema=schema, table=table)
    
if __name__ == "__main__":
    app.run(debug=True)

