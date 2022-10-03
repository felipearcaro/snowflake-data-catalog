select 'mysql', 'My_SQL', sc.schema_name, tb.table_name, tb.table_comment, co.column_name, co.column_comment, co.data_type, co.is_nullable, co.CHARACTER_MAXIMUM_LENGTH, co.numeric_precision
FROM information_schema.schemata sc
INNER join information_schema.tables tb on sc.schema_name = tb.table_schema
INNER join information_schema.columns co on tb.table_name = co.table_name
WHERE sc.schema_name NOT IN ('PUBLIC','INFORMATION_SCHEMA') AND tb.table_schema NOT IN ('PUBLIC','INFORMATION_SCHEMA') and co.table_schema NOT IN ('PUBLIC','INFORMATION_SCHEMA')
AND sc.schema_name = 'subscriberb';