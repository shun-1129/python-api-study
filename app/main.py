from wsgiref.util import request_uri
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/item/{item_id}')
def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.post('/items')
def update_item(item: Item):
    return {'item_name': item.name, 'item_age': item.age}