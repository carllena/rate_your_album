from packages.database_controller import DatabaseController
from datetime import datetime


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
        album_id = f"SELECT album_id FROM albums WHERE album={self.album_title} AND band={self.band} AND release_date={self.release_date}"
        query = "INSERT INTO user_album (album_id, login, rate) VALUES (%s, %s, %s)"
        values = (album_id, login, rate)
        return self.insert_data(query, values)
