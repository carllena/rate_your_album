from packages.database_controller import DatabaseController
from packages.config import rates
from datetime import datetime
from mysql.connector.errors import IntegrityError, ProgrammingError


class Album(DatabaseController):
    def __init__(self, album_title, band, release_date) -> None:
        super().__init__()
        self.album_title = album_title
        self.band = band
        self.release_date = release_date

    def add_album(self):
        query = "INSERT INTO albums (album, band, release_date) VALUES (%s, %s, %s)"
        values = (self.album_title, self.band, self.release_date)
        return self.insert_data(query, values)

    def rate_the_album(self, login, rate):
        if rate not in rates:
            return False
        album_id_query = f"SELECT album_id FROM albums WHERE album='{self.album_title}' AND band='{self.band}' AND release_date='{self.release_date}';"
        album_id = self.select_data(album_id_query)[0][0]
        query = "INSERT INTO user_album (album_id, login, rate) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE rate=%s"
        values = (album_id, login, rate, rate)
        return self.insert_data(query, values)
