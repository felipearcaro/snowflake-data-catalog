merge into SUBSCRIBER_TABLES.SUBSCRIBER_DATABASE_TABLES.APPROVALACCTJOURNAL using source_db.source_schema.test_2
    on target_table.id = source_table.id
    when matched then 
        update set target_table.description = source_table.description
    when not matched then 
        insert (id, description) values (source_table.id, source_table.description);