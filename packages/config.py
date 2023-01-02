from datetime import datetime as dt
from os import getenv
from setenvs import set

start_time = dt.now()
name = "RateYourAlbumAPI"
version = "1.0.0"
http_port = int(getenv("HTTPPORT", "5123"))

set()
mysql_config = {
    "user": getenv("DB_USER", ""),
    "password": getenv("DB_PASSWORD", ""),
    "host": getenv("DB_HOST", ""),
    "database": getenv("DB_DATABASE", ""),
    "port": 3306,
}
