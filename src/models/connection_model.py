from fastapi import WebSocket


class ConnectionModel:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket