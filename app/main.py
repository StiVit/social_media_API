from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()


# The schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = '150205', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('Connected to the database')
except Exception as e:
    print('Connection to database failed')
    print(f'Error: {e}')


# Endpoints
@app.get('/')
async def root():
    return {"message": "Welcome to my API"}


@app.get('/posts')
def get_posts():
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    return {"data": posts}


@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    cursor.execute('SELECT * FROM posts WHERE id = %s', (id,))
    post = cursor.fetchone()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id {id} was not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    return {"data": post}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute('INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *', (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data': new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute('DELETE FROM posts WHERE id = %s RETURNING *', (id,))
    post = cursor.fetchone()
    conn.commit()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute('UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *', (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    return {"data": updated_post}