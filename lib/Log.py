import requests, json
from datetime import datetime

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [INFO] {message}', flush=True)
    
    @staticmethod 
    def warn(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [WARN] {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [ERROR] {message}', flush=True)

    @staticmethod 
    def success(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [SUCCESS] {message}', flush=True)