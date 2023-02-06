from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/item/{item_id}')
def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.post("/items")
def update_item(item: Item):
    return {"item_name": item.name, "twice price": item.price * 2}

@app.post('/json_post')
def update_item(item: Item):
    return {"item_name": item.name, "twice price": item.price * 2}