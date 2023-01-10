from datetime import datetime as dt
from os import getenv
from setenvs import set

start_time = dt.now()
name = "RateYourAlbumAPI"
version = "1.0.0"
http_port = int(getenv("HTTPPORT", "5123"))

rates = [str(i) for i in range(1, 11)]

set()
mysql_config = {
    "user": getenv("DB_USER", ""),
    "password": getenv("DB_PASSWORD", ""),
    "host": getenv("DB_HOST", ""),
    "database": getenv("DB_DATABASE", ""),
    "port": 3306,
}

registration_reject_list = ["192.168.1.2", "192.168.0.220"]
