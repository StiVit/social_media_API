from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()


# The schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "post1", "content": "content of post1", "id": 1}, 
{"title": "post2", "content": "content of post2", "id": 2}]


# Functions
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# Endpoints
@app.get('/')
async def root():
    return {"message": "Welcome to my API"}


@app.get('/posts')
def get_posts():
    return {"data": my_posts}


@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id {id} was not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    return {"data": post}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {'data': post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')

    my_posts.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)