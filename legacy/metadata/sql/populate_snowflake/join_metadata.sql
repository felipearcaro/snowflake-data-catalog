INSERT INTO DATA_CATALOG.PUBLIC.DATA_CATALOG_AGG(
	DB_NAME,
	DB_DESCRIPTION,
	SCHEMA_NAME,
	SCHEMA_DESCRIPTION,
	TABLE_NAME,
	TABLE_DESCRIPTION,
	COLUMN_NAME,
	COLUMN_DESCRIPTION,
	DATA_TYPE,
	IS_NULLABLE,
	CHARACTER_MAXIMUM_LENGTH,
	NUMERIC_PRECISION
)
select db.database_name, db.comment, sc.schema_name, sc.comment, tb.table_name, tb.comment, co.column_name, co.comment, co.data_type, co.is_nullable, co.CHARACTER_MAXIMUM_LENGTH, co.numeric_precision from data_catalog.information_schema.databases db 
INNER join {db_name}.information_schema.schemata sc on db.database_name = sc.catalog_name
INNER join {db_name}.information_schema.tables tb on sc.schema_name = tb.table_schema
INNER join {db_name}.information_schema.columns co on tb.table_name = co.table_name
where database_name = '{db_name}' 
and sc.schema_name NOT IN ('PUBLIC','INFORMATION_SCHEMA') AND tb.table_schema NOT IN ('PUBLIC','INFORMATION_SCHEMA') and co.table_schema NOT IN ('PUBLIC','INFORMATION_SCHEMA');