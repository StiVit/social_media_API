from datetime import datetime
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse

    class Config:
        orm_mode = True
 

class PostResponseWithVotes(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class VoteBase(BaseModel):
    post_id: int
    dir: conint(le=1)


class VoteCreate(VoteBase):
    pass