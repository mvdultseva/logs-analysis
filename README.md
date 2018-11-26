# Logs Analysis
An internal reporting tool that uses information from the database to discover what kind of articles the site's readers like.

The application unconditionally outputs three types of information:
- The most popular article authors of all time
- The most popular three articles of all time
- Day list when more than 1% of requests led to errors

## Requirements
In order to run application you have to create Python virtual environment and install all packages 
from the `requirements.txt`:
1. Create virtual environment: `python3 -m venv log_analysis_venv`
2. Activate virtual environment: `source log_analysis_venv/bin/activate`
3. Install all dependencies: `pip install -r requirements.txt`

LogAnalysis application connects to the database `news`. Before any use of the application the database server must exist, 
server must have the database named `news`, and database must contain the data. 

>Further instructions assume, that you already have a running Postgres DB server 
on the local host (or in the virtual machine). If you don't have access to the running Postgres DB server, 
please consult with official Postgres documentation [tutorial](https://www.postgresql.org/docs/11/tutorial.html).

Please follow these steps to create the database and import the database data:
1. [Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
2. You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`.
3. Create `news` database with the command:

    `psql -c 'create database news;'`
 
4. Create all necessary tables and load the site's data into your local database with the command:
 
    `psql -d news -f newsdata.sql`
  

LogAnalysis application uses PostgresViews, so you have to create them before first application run 
(you can find views definitions in `all_requests_view.sql` and `err_requests_view.sql` files). 
In order to create views, please run these two commands with installed `psql` CLI client tool:
1. `psql -d news -f all_requests_view.sql`
2. `psql -d news -f err_requests_view.sql`

This will create two PostgresViews and grant access to `vagrant` user.

## Application usage
After you have installed all dependencies and created PostgresView, you may run application 
and get statistical information from the database.

In order to run your application you have to activate virtual environment (if it is not activated yet), 
and execute this command: 

`python log_analysis.py` 

Results will be printed to the console and include information about most popular authors, articles 
and days with high (more than 1%) error rate. You can find output example in the `example_output.txt` file. 
