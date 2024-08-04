from fastapi import FastAPI
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
    data = {
        "url": url
    }
    return JSONResponse(content=data)

