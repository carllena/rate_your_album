import mysql.connector
from packages.config import mysql_config


def create_cursor():
    mydb = mysql.connector.connect(**mysql_config)
    mycursor = mydb.cursor()
    return mydb, mycursor


def select_data(mycursor, query):
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
