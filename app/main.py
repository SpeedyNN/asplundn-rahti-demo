from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "nå mårå nicke här", "v": "0.1" }

@app.get("/api/ip")
async def read_root(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}

@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}