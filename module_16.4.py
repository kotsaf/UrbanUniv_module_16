from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(username: Annotated[str, Path(min_length=3, max_length=12, description='Enter your username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=100, description='Enter yor age')]) -> User:
    user_id = max(users, key=lambda usr: usr.id).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: Annotated[str, Path(min_length=3, max_length=12, description='Enter your username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=100, description='Enter yor age')]):
    try:
        users[user_id - 1] = f'ID: {user_id}, username: {username}, age: {age}'
        return f'User {user_id} is updated'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    try:
        users.pop(user_id - 1)
        return f'User {user_id} is deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
