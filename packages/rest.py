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


def process_POST_request(payload, path, client_ip, user_agent):

    correct_request = False
    logger.debug("-- processing POST request: start")
    if str(path) == "/create_account":
        payload["password"] = hide_the_pass(payload["password"], payload["login"])
        if "name" in payload:
            new_account = Account(
                payload["login"],
                payload["name"],
                payload["surname"],
                payload["password"],
            )
            if new_account.create_account(client_ip):
                correct_request = True
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
            correct_request = True

    elif str(path) == "/auth":
        payload["password"] = hide_the_pass(payload["password"], payload["login"])
        new_account = Account(
            payload["login"],
            None,
            None,
            payload["password"],
        )
        if new_account.authenticate():
            correct_request = True
    elif str(path) == "/add_album":
        new_album = Album(
            payload["album_title"], payload["band"], payload["release_date"]
        )
        if new_album.add_album():
            correct_request = True
    elif str(path) == "/rate_album":
        album = Album(payload["album_title"], payload["band"], payload["release_date"])
        if album.rate_the_album(payload["login"], payload["rate"]):
            correct_request = True
    # logger.info(f"Status code: `{http_status}`, Response: `{response}`")
    logger.debug("-- processing POST request: end")
    return correct_request
