import mysql.connector
import logging
from packages.config import mysql_config, name

logger = logging.getLogger(name)


def create_cursor():
    mydb = mysql.connector.connect(**mysql_config)
    mycursor = mydb.cursor()
    return mydb, mycursor


def select_data(mycursor, query):
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult


def insert_data(mydb, mycursor, query, values):
    try:
        mycursor.execute(query, values)
        mydb.commit()
        return True
    except Exception as e:
        logger.warning(f"Exception: `{e}`")
    return False
