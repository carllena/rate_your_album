from packages.rest import process_GET_request, process_POST_request
from packages.utils import check_fingerprint
from requests import get
from packages.logger import Logger
from datetime import datetime
import logging
import json
import os
from time import sleep
from threading import Thread
import packages.config as c
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

# from packages.database_controller import create_cursor, select_data, insert_data


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
        def should_be_rejected(ip_addr):
            if ip_addr in c.IP_reject_list:
                return True
            return False

        logger.debug(f"Got POST request with path: `{self.path}`")
        date_time = datetime.now()
        timestamp = datetime.timestamp(date_time)
        log_date = date_time.strftime("%Y-%m-%d")

        reject_ip_flag = False
        authorized_origin = True
        method_name = "post"
        print(self.headers)
        user_agent = self.headers.get("User-Agent")
        if self.headers["Content-Length"]:
            self.data_string = self.rfile.read(int(self.headers["Content-Length"]))
            # logger.info(self.data_string)
            payload = json.loads(self.data_string)
            data = json.dumps(payload)
        else:
            payload = None
        logger.info(f"Client IP: `{self.client_address[0]}`, Payload: `{payload}`")
        path = str(self.path)
        try:
            if not check_fingerprint(
                payload["login"],
                user_agent,
                payload["timestamp"],
                payload["fingerprint"],
            ):
                authorized_origin = False
        except Exception as e:
            logger.warning(f"Exception in origin checking: `{e}`")
            authorized_origin = False
        if should_be_rejected(self.client_address[0]):
            reject_ip_flag = True
            correct_request = False
        else:
            correct_request = process_POST_request(
                payload, path, self.client_address[0], user_agent
            )
        if correct_request:
            response = c.positive_responses[path[1:]][0]
            http_status = c.positive_responses[path[1:]][1]
        else:
            response = c.error_responses[path[1:]][0]
            http_status = c.error_responses[path[1:]][1]
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
        login = payload["login"]
        password = payload["password"][:10]
        firstname = payload["name"]
        lastname = payload["surname"]
        result = "PASS" if correct_request else "FAIL"
        print(
            f"LogDate: `{log_date}`, DateTime: `{date_time}`, Timestamp: `{timestamp}` Event: `{str(path)[1:]}`, ServerIP: `{c.server_IP}`, Port: `{c.http_port}`, ClientIP: `{self.client_address[0]}`, ClientPort: `{self.client_address[1]}`, Login: `{login}`, Password: `{password}`, FirstName: `{firstname}`, LastName: `{lastname}`, Result: `{result}`, RejectIP: `{reject_ip_flag}, AuthorizedOrigin: `{authorized_origin}`, UserAgent: `{user_agent}`"
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
        c.IP_reject_list = result
        logger.info(f"rejectlist updadet: {c.IP_reject_list}")
        sleep(10000)


def main():
    print(c.IP_reject_list)
    http_serve = Thread(target=serve_http)
    http_serve.start()
    logger.info(f"http server listening on `{c.server_IP}:{c.http_port}`")
    rejectlist_updater = Thread(target=update_rejectlist)
    rejectlist_updater.start()
    # while True:
    #     print(c.registration_reject_list)
    #     sleep(10)

    # query = "INSERT INTO users (login, name, surname, password) VALUES (%s, %s, %s, %s)"
    # values = ("john123", "John", "Johnson", "johny12")
    # insert_data(mydb, mycursor, query, values)
    # res = select_data(mycursor, "SELECT * FROM users;")
    # logger.info(res)


if __name__ == "__main__":
    main()
