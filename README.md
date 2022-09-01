# Snowflake Data Catalog

##  How to get started

### Backend Setup

- Run `python3 -m venv venv` to create the virtual environment `venv` where Python packages will be installed
- If you're a Windows user, you need to run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` on an elevated command prompt
- To activate your virtual environment, run `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Mac
- To install all Python packages, run `pip install -r requirements.txt`
- Install PostgreSQL locally:
    - host: `localhost`
    - database: `data_catalog`
    - user: `postgres`
    - password: `root` 
    - I recommend using pgAdmin 4 for database management


$ flask db init
$ flask db migrate
$ flask db upgrade
We start by initializing the database and enabling migrations. The generated migrations are just scripts that define the operations to be undertaken on our database. Since this is the first time, the script will just generate the cars table with columns as specified in our model.