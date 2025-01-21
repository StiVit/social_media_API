from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

# The schema
class Post(BaseModel):
    title: str
    content: str

@app.get('/')
async def root():
    return {"message": "Welcome to my API"}

@app.get('/posts')
def get_posts():
    return {"data": "This is your posts"}

@app.post('/createposts')
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}