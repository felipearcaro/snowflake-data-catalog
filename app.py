from flask import Flask, render_template, redirect, request, url_for, flash, session
from common.snowflake_client import *
from metadata.columns_metadata import ColumnsMetadata
from metadata.databases_metadata import DatabasesMetadata
from metadata.schemas_metadata import SchemasMetadata
from metadata.tables_metadata import TablesMetadata
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import or_, func

TODAYS_DATE = str(datetime.today()).split('.')[0]

app = Flask(__name__)

# Postgres Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/data_catalog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database models
class DataCatalogLineage(db.Model):
    __tablename__ = 'data_catalog_lineage'

    id = db.Column(db.Integer, primary_key=True)
    dbms = db.Column(db.String())
    database_name = db.Column(db.String())
    schema_name = db.Column(db.String())
    table_name = db.Column(db.String())
    source_table = db.Column(db.String())
    source_query = db.Column(db.String())

    def __init__(self, dbms, database_name, schema_name, table_name, source_table, source_query):
        self.dbms = dbms
        self.database_name = database_name
        self.schema_name = schema_name
        self.table_name = table_name
        self.source_table = source_table
        self.source_query = source_query

    def __repr__(self):
        return f"<DataCatalogLineage {self.database_name}>"

class DataCatalogAgg(db.Model):
    __tablename__ = 'data_catalog_agg'

    id = db.Column(db.Integer, primary_key=True)
    dbms = db.Column(db.String())
    database_name = db.Column(db.String())
    database_description = db.Column(db.String())
    schema_name = db.Column(db.String())
    schema_description = db.Column(db.String())
    table_name = db.Column(db.String())
    table_description = db.Column(db.String())
    column_name = db.Column(db.String())
    column_description = db.Column(db.String())
    data_type = db.Column(db.String())
    is_nullable = db.Column(db.String())
    character_maximum_length = db.Column(db.String())
    numeric_precision = db.Column(db.String())


    def __init__(self, dbms, database_name, database_description, schema_name, schema_description, table_name, table_description, column_name, column_description, data_type, is_nullable, character_maximum_length, numeric_precision):
        self.dbms = dbms
        self.database_name = database_name
        self.database_description = database_description
        self.schema_name = schema_name
        self.schema_description = schema_description
        self.table_name = table_name
        self.table_description = table_description
        self.column_name = column_name
        self.column_description = column_description
        self.data_type = data_type
        self.is_nullable = is_nullable
        self.character_maximum_length = character_maximum_length
        self.numeric_precision = numeric_precision

    def __repr__(self):
        return f"<DataCatalogAgg {self.database_name}>"


class DataCatalogDataQuality(db.Model):
    __tablename__ = 'data_catalog_data_quality'

    id = db.Column(db.Integer, primary_key=True)
    dbms = db.Column(db.String())
    database_name = db.Column(db.String())
    schema_name = db.Column(db.String())
    table_name = db.Column(db.String())
    di_metric_1 = db.Column(db.Float())
    di_metric_2 = db.Column(db.Float())
    di_metric3 = db.Column(db.Float())


    def __init__(self, dbms, database_name, schema_name, table_name, di_metric_1, di_metric_2, di_metric3):
        self.dbms = dbms
        self.database_name = database_name
        self.schema_name = schema_name
        self.table_name = table_name
        self.di_metric_1 = di_metric_1
        self.di_metric_2 = di_metric_2
        self.di_metric3 = di_metric3

    def __repr__(self):
        return f"<DataCatalogDataQuality {self.database_name}>"


@app.route('/')
def index():
    databases = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.dbms,
                       DataCatalogAgg.database_name, 
                       DataCatalogAgg.database_description)\
        .distinct()

    return render_template('databases.html', databases=databases)

@app.route('/schemas')
def schemas():
    database = request.args.get('database')
    schemas = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.dbms,
                       DataCatalogAgg.schema_name, 
                       DataCatalogAgg.schema_description, 
                       DataCatalogAgg.database_name)\
        .filter_by(database_name=database).distinct()

    return render_template('schemas.html', schemas=schemas, database=database)

@app.route('/tables')
def tables():
    database = request.args.get('database')
    schema = request.args.get('schema')
    tables = DataCatalogAgg.query.with_entities(DataCatalogAgg.dbms,
                                                DataCatalogAgg.table_name, 
                                                DataCatalogAgg.table_description)\
                                                .filter_by(database_name=database, schema_name = schema)\
                                                .distinct()
    
    return render_template('tables.html',tables = tables, database=database, schema=schema)

@app.route('/columns')
def columns():
    database = request.args.get('database')
    schema = request.args.get('schema')
    table = request.args.get('table')
    columns = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.column_name, 
                        DataCatalogAgg.column_description, 
                        DataCatalogAgg.data_type, 
                        DataCatalogAgg.is_nullable,
                        DataCatalogAgg.character_maximum_length,
                        DataCatalogAgg.numeric_precision)\
        .filter_by(database_name=database, schema_name = schema, table_name = table).distinct()
    
    table_lineage = DataCatalogLineage.query\
        .with_entities(DataCatalogLineage.source_table, 
                        DataCatalogLineage.source_query)\
        .filter_by(database_name=database, schema_name = schema, table_name = table).distinct()
    
    for i in table_lineage:
        print(f"test {i}")

    table_description = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.table_description,
                       DataCatalogAgg.dbms)\
        .filter_by(database_name=database, schema_name = schema, table_name = table).first()

    for i in table_description:
        print(f"test {i}")

    return render_template('columns.html', columns=columns, table_description = table_description, table_lineage=table_lineage, database=database, schema=schema, table=table)


@app.route('/search', methods=['POST'])
def search():
    query = f"%{request.form['query']}%"
    print(query)
    table_results = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.dbms,
                        DataCatalogAgg.database_name, 
                        DataCatalogAgg.schema_name, 
                        DataCatalogAgg.table_name)\
        .filter(or_(DataCatalogAgg.table_description.ilike(query), 
        DataCatalogAgg.column_description.ilike(query),
        DataCatalogAgg.table_name.ilike(query))).distinct()


    column_results = DataCatalogAgg.query\
        .with_entities(DataCatalogAgg.dbms,
                        DataCatalogAgg.database_name, 
                        DataCatalogAgg.schema_name, 
                        DataCatalogAgg.table_name,
                        DataCatalogAgg.column_name,
                        DataCatalogAgg.column_description,
                        DataCatalogAgg.data_type)\
        .filter(or_(DataCatalogAgg.table_description.ilike(query), 
        DataCatalogAgg.column_description.ilike(query),
        DataCatalogAgg.table_name.ilike(query))).distinct()

    return render_template('search.html', table_results=table_results, column_results = column_results)
    
if __name__ == "__main__":
    app.run(debug=True)