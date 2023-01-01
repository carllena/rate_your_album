from packages.database_controller import insert_data


class Account:
    def __init__(self, login, name, surname, password, password_hash) -> None:
        self.login = login
        self.name = name
        self.surname = surname
        self.password = password
        self.password_hash = password_hash

    def create_account(self, mydb, mycursor):
        query = (
            "INSERT INTO users (login, name, surname, password) VALUES (%s, %s, %s, %s)"
        )
        values = (self.login, self.name, self.surname, self.password)
        return insert_data(mydb, mycursor, query, values)
