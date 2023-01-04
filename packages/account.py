from packages.database_controller import insert_data, select_data
from datetime import datetime


class Account:
    def __init__(self, login, name, surname, password_hash) -> None:
        self.login = login
        self.name = name
        self.surname = surname
        self.password_hash = password_hash

    def create_account(self, mydb, mycursor, client_ip):
        query = "INSERT INTO users (login, name, surname, password, registration_ip, registration_date, modify_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = (
            self.login,
            self.name,
            self.surname,
            self.password_hash,
            client_ip,
            registration_date,
            registration_date,  # modify_date
        )
        print(values)
        return insert_data(mydb, mycursor, query, values)

    def check_login_availability(self, mycursor):
        query = f"SELECT * FROM users WHERE login = '{self.login}' LIMIT 1;"
        result = select_data(mycursor, query)
        if result:
            return False
        else:
            return True

    def authenticate(self, mycursor):
        query = f"SELECT * FROM users WHERE login = '{self.login}' AND password = '{self.password_hash}' LIMIT 1;"
        result = select_data(mycursor, query)
        print(result)
        if result:
            return True
        else:
            return False
