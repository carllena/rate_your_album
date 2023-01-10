import mysql.connector
import logging
from packages.config import mysql_config, name

logger = logging.getLogger(name)


class DatabaseController:
    def __init__(self) -> None:
        self.database = mysql.connector.connect(**mysql_config)
        self.cursor = self.database.cursor()
        pass

    def select_data(self, query):
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        return myresult

    def insert_data(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.database.commit()
            return True
        except Exception as e:
            logger.warning(f"Exception: `{e}`")
        return False

    def update_data(self, query, values):
        pass
