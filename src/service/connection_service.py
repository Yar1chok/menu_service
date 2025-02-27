

from fastapi import WebSocket
from src.repository.connection_repo import ConnectionRepo


class ConnectionService:
    def __init__(self, repository: ConnectionRepo):
        self.repository = repository

    async def connect(self, websocket: WebSocket):
        await self.repository.add_connection(websocket)

    def disconnect(self, websocket: WebSocket):
        self.repository.remove_connection(websocket)

    async def broadcast(self, message):
        disconnected = []
        for connection in self.repository.get_active_connections():
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                disconnected.append(connection)
        # Удаляем неактивные соединения
        for connection in disconnected:
            self.disconnect(connection)
        