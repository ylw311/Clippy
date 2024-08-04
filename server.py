import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import sys

sys.path.append("..")
from globall import url

app = FastAPI()

# Initialize logger
logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_data")
def get_data():

    logging.info(f"QR code requested: {url}")
    data = {"url": url}
    return JSONResponse(content=data)


# connection to ui
# TODO: add jobs to queue
jobs = asyncio.Queue()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # keep clearing queue
    async def check_queue():
        while True:
            print("Checking queue")
            job = await jobs.get()
            await websocket.send_json(job)
    queue_task = asyncio.create_task(check_queue())

    # keep listening for new jobs
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        queue_task.cancel()
        await websocket.close()
