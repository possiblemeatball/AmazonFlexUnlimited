import requests, json
from datetime import datetime
from time import gmtime

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'[{datetime.now().strftime("%D %T")}] [INFO] {message}', flush=True)
    
    @staticmethod 
    def warn(message: str):
        print(f'[{datetime.now().strftime("%D %T")}] [WARN] {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'[{datetime.now().strftime("%D %T")}] [ERROR] {message}', flush=True)

    @staticmethod 
    def success(message: str):
        print(f'[{datetime.now().strftime("%D %T")}] [SUCCESS] {message}', flush=True)