import requests, json
from datetime import datetime

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [INFO] {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'[{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}] [ERROR] {message}', flush=True)
    
    @staticmethod 
    def push_info(title: str, message: str, ntfy: str, topic: str, priority: int):
        requests.post(ntfy,
            data=json.dumps({
                "topic": topic,
                "message": message,
                "title": title,
                "tags": ["info"],
                "priority": priority,
            })
        )

    @staticmethod
    def push_error(title: str, message: str, ntfy: str, topic: str, priority: int):
        requests.post(ntfy,
            data=json.dumps({
                "topic": topic,
                "message": message,
                "title": title,
                "tags": ["error"],
                "priority": priority,
            })
        )