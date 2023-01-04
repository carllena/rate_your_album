from packages.rest import process_GET_request, process_POST_request
from requests import get
from packages.logger import Logger
import logging
import socket
import json
import os
from time import sleep
from threading import Thread
import packages.config as c
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from packages.database_controller import create_cursor, select_data, insert_data

# ścieżka dla pliku z logami w przypadku stosowania LOGGING_FILE
LOGFILE = "log/app.log"
# ile plików ma trzymać wstecz (pliki są tworzone co dobę)
LOGFILE_COUNT = 7
# envy do handlerów
LOGGING_FILE = True if os.getenv("LOGGING_FILE", "false").lower() == "true" else False
LOGGING_STD = True if os.getenv("LOGGING_STD", "true").lower() == "true" else False

# level logowania (globalny niezależnie od wybranego handlera)
LOGGING_LEVEL = (
    logging.DEBUG
    if os.getenv("LOGGING_LEVEL", "info").lower() == "debug"
    else logging.INFO
)

# MAIN
# -------------------------------------------------------------------------


logger = (
    Logger()
    .Init(
        loggerType="std",
        loggerInit=LOGGING_STD,
        level=LOGGING_LEVEL,
        formatterName="formater",
    )
    .Init(
        loggerType="file",
        loggerInit=LOGGING_FILE,
        logFile=LOGFILE,
        logFileCount=LOGFILE_COUNT,
    )
    .Get()
)

# mydb, mycursor = create_cursor()


class MyHandler(BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler.protocol_version = "HTTP/1.1"
    def log_message(self, format, *args):
        return

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS, POST")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        return

    def do_GET(self):
        method_name = "get"
        http_status, response = process_GET_request(str(self.path))
        response_json = {
            "results": {
                "method": method_name,
                "action": str(self.path)[1:],
                "data": "",
                "response": response,
            },
            "status_code": http_status,
        }
        self.send_response(http_status)
        self.send_header("Content-type", "text/html")
        # print(self.client_address[0])
        # self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        response_json = json.dumps(response_json)
        self.wfile.write(
            bytes(
                response_json,
                "utf-8",
            )
        )
        return

    def do_POST(self):
        logger.debug(f"Got POST request with path: `{self.path}`")
        method_name = "post"
        if self.headers["Content-Length"]:
            self.data_string = self.rfile.read(int(self.headers["Content-Length"]))
            # logger.info(self.data_string)
            payload = json.loads(self.data_string)
            data = json.dumps(payload)
        else:
            payload = None
        logger.info(payload)
        logger.debug(f"Payload: `{payload}`")
        path = str(self.path)

        http_status, response = process_POST_request(
            payload, path, self.client_address[0]
        )
        response_json = {
            "results": {
                "method": method_name,
                "action": str(self.path)[1:],
                "data": data,
                "response": response,
            },
            "status_code": http_status,
        }
        self.send_response(http_status)
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.send_header("Accept-Encoding", "gzip, deflate")
        # self.send_header("Content-length", self.headers["Content-Length"])
        self.end_headers()
        response_json = json.dumps(response_json)
        self.wfile.write(
            bytes(
                response_json,
                "utf-8",
            )
        )
        logger.debug(f"Status code: `{http_status}`")
        logger.debug(f"Response: {response[:254]}")
        return


def serve_http(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ("", c.http_port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()


def update_rejectlist():
    # select do bazy
    while True:
        result = ["1.168.1.2", "192.168.0.227"]
        c.registration_reject_list = result
        logger.info(f"rejectlist updadet: {c.registration_reject_list}")
        sleep(10)


def main():
    local_ip = socket.gethostbyname(socket.gethostname())
    print(c.registration_reject_list)
    http_serve = Thread(target=serve_http)
    http_serve.start()
    logger.info(f"http server listening on `{local_ip}:{c.http_port}`")
    rejectlist_updater = Thread(target=update_rejectlist)
    rejectlist_updater.start()
    while True:
        print(c.registration_reject_list)
        sleep(10)

    # query = "INSERT INTO users (login, name, surname, password) VALUES (%s, %s, %s, %s)"
    # values = ("john123", "John", "Johnson", "johny12")
    # insert_data(mydb, mycursor, query, values)
    # res = select_data(mycursor, "SELECT * FROM users;")
    # logger.info(res)


if __name__ == "__main__":
    main()
