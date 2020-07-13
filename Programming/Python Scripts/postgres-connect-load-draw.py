import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Set up display options of Pandas library
pd.set_option('display.max_column', None)     # This line force Pandas to display any number of columns
pd.set_option('display.width, 200)            # This line tells Pandas to to display output on Python console up to 200 characters

# Set up variable to use for connecting to Postgres Database
PGHOST = 'your_host_name'
PGDATABASE = 'your_database_name'
PGUSER = 'your_postgres_id'
PGPASSWORD = 'your_postgres_password'

# Set up a connection to the Postgres server.
# port number 5432 is the default postgres port number
conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + PGDATABASE + " user=" + PGUSER + " password=" \
              + PGPASSWORD
conn = psycopg2.connect(conn_string)
print("Connection is successfully established to " + PGDATABASE)

# Testing SQL Query through Python
data = pd.read_sql('SELECT * FROM "table_name" ORDER BY column1, column2 ASC', conn)
print(data.head(10))  # Print the first 10 rows

# Building plot using data from Postgres Table
fig = plt.figure(figsize=(8, 4))

# 1. Plot column1 as X-axis and column2 as Y-axis
plt.bar(data['column1'], data['column2'])
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('PLOT TITLE')
plt.xticks(rotation=45)  # Rotate the value of X-axis points into 45 degree
plt.tick_params(axis='x', which='major', labelsize=8)  # Increase the size of points label on X-axis
plt.rc('grid', linestyle="-", color='lightblue')
plt.grid(True)
plt.show()
