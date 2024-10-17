from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data = []

class Book(BaseModel):
    title: str                        #"title": "Harry Potter",
    author: str                       #"author": "Heena",
    publisher: str                    #"publisher": "Jamal pvt ltd"

   
@app.post("/book")
def createbook(book:Book):
    data.append(book.dict())

    return data

@app.get("/{id}")
def readbook(id:int):
    return data[id]

@app.put("/book/{id}")
def updatebook(id:int, book:Book):
    data[id] = book
    return book

@app.delete("/book/{id}")
def deletebook(id:int):
    data.pop(id)
    return data