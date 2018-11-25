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
