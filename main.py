from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    surname: str
    description: str
    price: float

@app.get("/hello")
def hello_world():
    return { "message": "Hello World" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/str/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}

@app.post("/items")
async def create_item(item: Item):
    print(item.name, item.surname, item.price)
    return { "request body": item }

@app.put("/items/{item_id}")
async def edit_item(item_id: int, item: Item):
    return { "id": item_id, "request body": item }

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return { "message": f"Item {item_id}  deleted" }