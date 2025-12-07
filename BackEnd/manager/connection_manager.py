from fastapi import WebSocket
from typing import Dict,List

class ConnectionManager:
    def __init__(self):
        self.active_connections:Dict[str,WebSocket] = {}

        async def connect(self,user_id:str,websocket: WebSocket,):
            await websocket.accept()
            self.active_connections[user_id] = websocket

        def disconnect(self,user_id:str):
            if user_id in self.active_connections:
                del self.active_connections[user_id]

        async def send_message_to_user(self,user_id:str,message:str):
            ws = self.active_connections.get(user_id)
            if ws:
                await ws.send_str(message)

        async def broadcast(self,user_id:str,exclude:str):
            for user_id,ws in self.active_connections:
                if user_id !=exclude:
                    await ws.send_str(user_id)


