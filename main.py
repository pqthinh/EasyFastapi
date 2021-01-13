from typing import Optional

from fastapi import FastAPI, Query

from pydantic import BaseModel 

app = FastAPI()

# test server
@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

@app.get("/info/{full}/{age}")
async def read_info(full: str, age: int, info: Optional[str]= None): 
    return {"name:": full, "age": age, "info": info}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    # sample data
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/item/")
async def write_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}  #noi id vao doi tuong item

