import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass'
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("Create Database crudecrm")

print("All done")