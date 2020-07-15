import psycopg2
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set up variable to use for connecting to Postgres Database
PGHOST = 'your_host_name'
PGDATABASE = 'your_database_name'
PGUSER = 'your_username'
PGPASSWORD = 'your_password'

# Set up connection to the Postgres Server [local server + local database]
conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + PGDATABASE + " user=" + PGUSER + " password=" \
              + PGPASSWORD
conn = psycopg2.connect(conn_string)
print("Connection is successfully established to " + PGDATABASE)

# Testing SQL Query through Python
DataFrame = pd.read_sql('SELECT * FROM "table_name" ORDER BY column1, column2 ASC', conn)
print(DataFrame.head(10))  # Print the first 10 rows

# Building plot using data from Postgres Table
fig_line = px.line(DataFrame,
                   x='column1',
                   y='column2',
                   color='column3')
fig_line.update_xaxes(showgrid=True,
                       ticks="outside",            # OPTIONAL
                       tickson="boundaries",       
                       ticklen=20)                 
fig_line.show()
