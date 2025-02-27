from fastapi import WebSocket

class ConnectionRepo:
    def __init__(self):
        self.active_connections = []

    async def add_connection(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def remove_connection(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    def get_active_connections(self):
        return self.active_connections