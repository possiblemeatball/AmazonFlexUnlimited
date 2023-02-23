import requests, json

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'INFO: {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'ERROR: {message}', flush=True)
    
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
        Log.info(message)

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
        Log.error(message)