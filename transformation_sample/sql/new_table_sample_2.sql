merge into data_quality.felipe.new_table using source_db.source_schema.source_table2
    on target_table.id = source_table.id
    when matched then 
        update set target_table.description = source_table.description
    when not matched then 
        insert (id, description) values (source_table.id, source_table.description);