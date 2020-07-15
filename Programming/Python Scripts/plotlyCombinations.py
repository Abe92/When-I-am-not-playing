import psycopg2
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set up variable to use for connecting to Postgres Database
PGHOST = 'localhost'
PGDATABASE = 'UN_Volunteers'
PGUSER = 'postgres'
PGPASSWORD = 'admin123'

# Set up connection to the Postgres Server [local server + local database]
conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + PGDATABASE + " user=" + PGUSER + " password=" \
              + PGPASSWORD
conn = psycopg2.connect(conn_string)
print("Connection is successfully established to " + PGDATABASE)

# Testing SQL Query through Python
UN_Data = pd.read_sql('SELECT * FROM "govt_respond_tracker" ORDER BY datec, countryname ASC', conn)
print(UN_Data.head(10))  # Print the first 10 rows

# Building plot using data from Postgres Table
fig_line = px.line(UN_Data,
                   x='countryname',
                   y='confirmedcases',
                   color='countrycode')
# fig_line.update_xaxes(showgrid=True,
#                       ticks="outside",            # It looks horrendous with this alteration
#                       tickson="boundaries",       # These lines function;
#                       ticklen=20)                 # Placing ticks and gridlines between categories
fig_line.show()
