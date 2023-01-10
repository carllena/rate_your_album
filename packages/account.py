from packages.database_controller import DatabaseController
from datetime import datetime


class Account(DatabaseController):
    def __init__(self, login, name, surname, password_hash) -> None:
        super().__init__()
        self.login = login
        self.name = name
        self.surname = surname
        self.password_hash = password_hash

    # def __init__(self, login, name, surname, password_hash) -> None:

    def create_account(self, client_ip):
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
        return self.insert_data(query, values)

    def check_login_availability(self):
        query = f"SELECT * FROM users WHERE login = '{self.login}' LIMIT 1;"
        if self.select_data(query):
            return False
        else:
            return True

    def authenticate(self):
        query = f"SELECT * FROM users WHERE login = '{self.login}' AND password = '{self.password_hash}' LIMIT 1;"
        if self.select_data(query):
            return True
        else:
            return False
