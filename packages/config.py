from datetime import datetime as dt
import os

start_time = dt.now()
name = "rya_api"
version = "1.0.0"
http_port = int(os.getenv("HTTPPORT", "5123"))
