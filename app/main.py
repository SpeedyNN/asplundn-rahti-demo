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

rooms = [
    {"room_id": 1, "room_number": "1", "type": "1 Bed", "price": 1000, "occupied": False},
    {"room_id": 2, "room_number": "2", "type": "1 Bed", "price": 1000, "occupied": False},
    {"room_id": 3, "room_number": "3", "type": "2 Beds", "price": 2000, "occupied": False},
    {"room_id": 4, "room_number": "4", "type": "2 Beds", "price": 2000, "occupied": False},
    {"room_id": 5, "room_number": "5", "type": "Crazy shit", "price": 5000, "occupied": False},
    {"room_id": 6, "room_number": "6", "type": "Crazy shit", "price": 10000, "occupied": False},
    {"room_id": 7, "room_number": "7", "type": "not haunted room", "price": 1, "occupied": False}
]

@app.get("/api/rooms")
def read_rooms():
    return {"rooms": rooms}