from datetime import datetime as dt
from http import HTTPStatus
from os import getenv
from setenvs import set
import socket

start_time = dt.now()
name = "RateYourAlbumAPI"
version = "1.0.0"
server_IP = socket.gethostbyname(socket.gethostname())
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

IP_reject_list = ["192.168.1.2", "192.168.0.220"]

error_responses = {
    "create_account": ["Account not created", HTTPStatus.BAD_REQUEST],
    "free_login": ["Login is not available", HTTPStatus.BAD_REQUEST],
    "auth": ["Bad Login or Password", HTTPStatus.BAD_REQUEST],
    "add_album": ["Album cannot be added to the database", HTTPStatus.BAD_REQUEST],
    "rate_album": ["Album rating update failed", HTTPStatus.BAD_REQUEST],
    "default": ["Not Found", HTTPStatus.NOT_FOUND],
}
positive_responses = {
    "create_account": ["Account created correctly", HTTPStatus.OK],
    "free_login": ["Login is available", HTTPStatus.OK],
    "auth": ["Authorized", HTTPStatus.OK],
    "add_album": ["Album correctly inserted to database", HTTPStatus.CREATED],
    "rate_album": ["Album rating updated correctly", HTTPStatus.OK],
}
