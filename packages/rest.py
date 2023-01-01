# coding: utf-8
#!/usr/bin/python3

import logging, json
import packages.config as c
from datetime import datetime as dt
from http import HTTPStatus
from urllib.parse import parse_qs, urlsplit
from packages.account import Account
from packages.database_controller import create_cursor, select_data, insert_data

logger = logging.getLogger(c.name)


def __qparser(path):
    logger.debug("Parsing PATH")
    params = parse_qs(urlsplit(path).query)
    logger.debug(f"Path:: {path}")
    logger.debug(f"Parsed params:: {params}")
    return params


def process_GET_request(path):
    path = str(path)[1:]
    if path == "health":
        response = json.dumps(
            {
                "name": c.name,
                "version": c.version,
                "uptime": f"{dt.now() - c.start_time}",
            }
        )
        print(f"do_GET method: {response}")
    else:
        http_status = HTTPStatus.NOT_FOUND
        response = "notfound"
    if response != "notfound":
        http_status = HTTPStatus.OK
    return http_status, response


def process_POST_request(payload, path):
    print("-- processing GET request: start")
    mydb, mycursor = create_cursor()
    parsed_params = __qparser(path)
    print(f"Params: {parsed_params}")
    print(f"Payload: {payload}")
    if str(path) == "/create_account":
        if "name" in payload:
            print(payload)
            new_account = Account(
                payload["login"],
                payload["name"],
                payload["surname"],
                payload["password"],
                None,
            )
            if new_account.create_account(mydb, mycursor):
                response = f"ok: Account {payload['login']} created correctly"
            else:
                response = f"Account {payload['login']} not created"
        else:
            response = f"bad payload: {payload.keys()}"
        http_status = HTTPStatus.OK
    return http_status, response
