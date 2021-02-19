import mysql.connector
from mysql.connector import Error
import os 

# Get environment variables
USER = os.getenv('')
PASSWORD = os.environ.get('')
HOST = os.environ.get('')
PORT = os.environ.get('')
DATABASE = os.environ.get('')

if USER is None:
    USER = "user"
if PASSWORD is None:
    PASSWORD = "password"
if HOST is None:
    HOST = "host"
if DATABASE is None:
    DATABASE = "database"         
if PORT is None:
    PORT = "3306"

try:
    connection = mysql.connector.connect(host=HOST,
                                         database=DATABASE,
                                         user=USER,
                                         password=PASSWORD,
                                         port = PORT)

    mySql_Create_Table_Query = """SELECT VERSION();"""

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
    print("Version queried successfully ")

except mysql.connector.Error as error:
    print("Failed to query version in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

