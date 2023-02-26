import requests, json
from datetime import datetime
from time import gmtime

class Log:
    
    @staticmethod 
    def info(message: str):
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{now}] [INFO] {message}', flush=True)
    
    @staticmethod 
    def warn(message: str):
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{now}] [WARN] {message}', flush=True)

    @staticmethod
    def error(message: str):
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{now}] [ERROR] {message}', flush=True)

    @staticmethod 
    def success(message: str):
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{now}] [SUCCESS] {message}', flush=True)