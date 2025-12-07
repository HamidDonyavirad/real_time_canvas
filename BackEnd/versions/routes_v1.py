from fastapi import FastAPI,WebSocket
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "FrontEnd", "index.html")

connections = []
@app.get("/")
async def get():
    with open(HTML_PATH,encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in connections:
                if connection != websocket:
                    await connection.send_text(data)
    except:
        connections.remove(websocket)
