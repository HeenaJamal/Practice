from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''@app.get("/")
async def root():
    return{"message": "Hello"}'''

'''@app.get("/{name}")
async def root(name: str):
    return{"message":"Hello " + name}'''

'''@app.get("/")
async def root(name: str):
    return {"message": "Hello "+name}'''

db = {}

class Item(BaseModel):
    name: str
    desc: str

@app.post("/")
def create(item:Item):
    db[item.name] = item.desc
    return{"item": item}

@app.get("/")
def get_all_data():
    return db

@app.delete("/")
def delete_data(name: str):
    del db[name]
    return db

@app.put("/")
def update_data(item:Item):
    db[item.name] = item.desc
    return db