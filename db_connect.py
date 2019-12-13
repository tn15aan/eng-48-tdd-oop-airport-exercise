import pyodbc

# These are our variables to connect
server = 'localhost,1433'
database = 'AirportEx'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_AirportEx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making a cursor
cursor = docker_AirportEx.cursor()

# Executing some SQL commands
cursor.execute("SELECT * FROM Flight")

# row = cursor.fetchone()
# print(row)