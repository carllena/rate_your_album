from packages.rest import process_GET_request
import logging
import socket
import json
from threading import Thread
import packages.config as c
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from packages.database_controller import create_cursor, select_data, insert_data

logger = logging.getLogger("logger")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        method_name = "get"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        http_status, response = process_GET_request(str(self.path))
        self.wfile.write(bytes(response, "utf-8"))
        return


def serve_http(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ("", c.http_port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()


def main():
    local_ip = socket.gethostbyname(socket.gethostname())
    http_serve = Thread(target=serve_http)
    http_serve.start()
    print(f"http server listening on `{local_ip}:{c.http_port}`")
    mydb, mycursor = create_cursor()
    # query = "INSERT INTO users (login, name, surname, password) VALUES (%s, %s, %s, %s)"
    # values = ("john123", "John", "Johnson", "johny12")
    # insert_data(mydb, mycursor, query, values)
    res = select_data(mycursor, "SELECT * FROM users;")
    print(res)


if __name__ == "__main__":
    main()
