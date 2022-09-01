merge into target_db.target_schema.target_table using source_db.source_schema.source_table
    on target_table.id = source_table.id
    when matched then 
        update set target_table.description = source_table.description
    when not matched then 
        insert (id, description) values (source_table.id, source_table.description);