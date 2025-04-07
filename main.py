from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

connections = []

# Almacenamos los últimos 4 mensajes
messages = ["", "", "", ""]

@app.post("/send-message/")
async def send_message(request: Request):
    data = await request.json()
    quadrant = data.get("quadrant")
    message = data.get("message", "")

    if quadrant is not None and 0 <= quadrant <= 3:
        messages[quadrant] = message

        # Enviar la actualización a todos los clientes conectados
        for connection in connections:
            await connection.send_json({"quadrant": quadrant, "message": message})

    return {"status": "Message sent"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        connections.remove(websocket)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)