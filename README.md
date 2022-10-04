# Buildium Data Catalog

##  How to get started

### Step 1:
Download Python, Postgres and PgAdmin:
- [Python](https://www.python.org/downloads/)
- [Postgres v10.22](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
  - Choose password `root`
- [PgAdmin](https://www.pgadmin.org/download/pgadmin-4-windows)
  - host: `localhost`
  - database: `data_catalog`
  - user: `postgres`
  - password: `root` 
- Add the following directories to PATH variable 
  - C:\Program Files\PostgreSQL\10\bin 
  - C:\Program Files\PostgreSQL\10\lib


### Step 2:
Set up development environment: 
- Clone [data-catalog project](https://github.com/buildium/pweek-1029-data-catalog) 
- Open the terminal on the project root and run `python3 -m venv env-data-catalog` to create the virtual environment `env-data-catalog` where Python packages will be installed
   - If you're a Windows user, you need to run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` on an elevated command prompt
- To activate your virtual environment, run `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Mac
- To install all Python packages, run `pip install -r requirements.txt`
- To install the common package, run `pip -e install .`
- Create a `.env` file:
```
PG_HOST=localhost
PG_USER=postgres
PG_DATABASE=data_catalog
PG_PASSWORD=root

SF_ACCOUNT=<snowflake_account>
SF_USER=<snowflake_user>
SF_PASSWORD=<snowflake_pw>

MYSQL_ACCOUNT=<mysql_account>
MYSQL_USER=<mysql_user>
MYSQL_PASSOWRD=<mysql_passowrd>
```

### Step 3:
Create tables on Postgres:
- Open PgAdmin and create a database called `data_catalog`
- Run the following commands on the terminal from the project root
  - Initialize database and enable migrations `flask db init`
  - Initiate migration `flask db migrate`
  - Upgrade tables `flask db upgrade`


### Step 4:
Run data extractors on `getting_started` folder:
- Run the following files:
  - `getting_started\extractors\extractor_mysql.py`
  - `getting_started\extractors\extractor_snowflake.py`
  - `getting_started\data_lineage\merge_into_table_regex.py`


### Step 5:
Start application:
- Run `app.py` file