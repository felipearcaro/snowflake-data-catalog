# Snowflake Data Catalog

##  How to get started

### Backend Setup

- Run `python3 -m venv venv` to create the virtual environment `venv` where Python packages will be installed
- If you're a Windows user, you need to run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` on an elevated command prompt
- To activate your virtual environment, run `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Mac
- To install all Python packages, run `pip install -r requirements.txt`
- To install common module, run `pip -e install .`


Download Postgres and PgAdmin:
- Postgres v10.22 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
  - Choose password `root`
- PgAdmin https://www.pgadmin.org/download/pgadmin-4-windows
  - host: `localhost`
  - database: `data_catalog`
  - user: `postgres`
  - password: `root` 
- Add the following directories to PATH variable (sometimes not necessary)
  - C:\Program Files\PostgreSQL\10\bin 
  - C:\Program Files\PostgreSQL\10\lib

Create tables on Postgres:
- Open PgAdmin and create a database called `data_catalog`
- Run the following commands on terminal
  - Initialize database and enable migrations `flask db init`
  - Initiate migration `flask db migrate`
  - Upgrade tables `flask db upgrade`


Create `.env` file on root directory
