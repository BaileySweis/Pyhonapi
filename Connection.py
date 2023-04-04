# import pyodbc, an open source python package that makes accessing ODBC databases simple
import pyodbc as db

# Connection through Windows Authentication, defining how to connect to database
connection = db.connect(
    "Driver= {ODBC Driver 17 for SQL Server};"
    "Server=ML-RefVm-526995;"
    "Database=GVV2;"
    "Trusted_Connection=yes;")
cursor = connection.cursor()

# From here you can do things such as 'Select all from Products'
cursor.execute("Select * From Products")
rows = cursor.fetchall()

for row in rows:
    print(row)

#Use indexing to show us only product name 
cursor.execute("Select * From Products")
rows = cursor.fetchall()

for row in rows:
    print(row[1])
