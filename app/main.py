from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return { "msg": "nå mårå nicke här", "v": "0.1" }

@app.get("/api/ip")
async def read_root(request: Request):
    client_ip = request.client.host
    return {"ip": client_ip}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"id": item_id, "q": q}