from fastapi import FastAPI
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id" : 1},{"title": "Fav food", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p ["id"] == id:
            return p

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

'''@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post )
    return{"data": "new post"}'''

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000)
    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/posts/{id}")
def get_posts(id):
    print(id)
    post = find_post(int(id))
    print(post)
    return {"post_detail": post}




    