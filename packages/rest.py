# coding: utf-8
#!/usr/bin/python3

import logging, json
import packages.config as c
from datetime import datetime as dt
from http import HTTPStatus
from packages.utils import hide_the_pass
from packages.account import Account
from packages.album import Album

logger = logging.getLogger(c.name)


def process_GET_request(path):
    logger.debug("-- processing GET request: start")
    path = str(path)[1:]
    if path == "health":
        response = json.dumps(
            {
                "name": c.name,
                "version": c.version,
                "uptime": f"{dt.now() - c.start_time}",
            }
        )
        logger.info(f"do_GET method: {response}")
    else:
        http_status = HTTPStatus.NOT_FOUND
        response = "notfound"
    if response != "notfound":
        http_status = HTTPStatus.OK
    logger.debug("-- processing GET request: end")
    return http_status, response


def process_POST_request(payload, path, client_ip):
    logger.debug("-- processing POST request: start")
    if str(path) == "/create_account":
        payload["password"] = hide_the_pass(payload["password"], payload["login"])
        if client_ip in c.registration_reject_list:
            return HTTPStatus.BAD_REQUEST, "Account not created"
        if "name" in payload:
            new_account = Account(
                payload["login"],
                payload["name"],
                payload["surname"],
                payload["password"],
            )
            if new_account.create_account(client_ip):
                response = f"Account created correctly"
                http_status = HTTPStatus.OK
            else:
                response = f"Account not created"
                http_status = HTTPStatus.BAD_REQUEST
        else:
            response = f"bad payload: {payload.keys()}"

    elif str(path) == "/free_login":
        new_account = Account(
            payload["login"],
            None,
            None,
            None,
        )
        if new_account.check_login_availability():
            response = f"Login is available"
            http_status = HTTPStatus.OK
        else:
            response = f"Login is not available"
            http_status = HTTPStatus.BAD_REQUEST
    elif str(path) == "/auth":
        payload["password"] = hide_the_pass(payload["password"], payload["login"])
        new_account = Account(
            payload["login"],
            None,
            None,
            payload["password"],
        )
        if new_account.authenticate():
            response = "Authorized"
            http_status = HTTPStatus.OK
        else:
            response = "Bad Login or Password"
            http_status = HTTPStatus.BAD_REQUEST
    elif str(path) == "/add_album":
        new_album = Album(
            payload["album_title"], payload["band"], payload["release_date"]
        )
        if new_album.add_album():
            http_status = HTTPStatus.CREATED
            response = "Album correctly inserted to database"
        else:
            http_status = HTTPStatus.BAD_REQUEST
            response = "Album cannot be inserted to database"
    logger.debug("-- processing POST request: end")
    return http_status, response
