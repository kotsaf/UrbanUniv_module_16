from fastapi import FastAPI, HTTPException, status, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: str) -> User:
    user_id = len(users) + 1
    user = f'ID: {user_id}, username: {username}, age: {age}'
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: str):
    try:
        users[user_id - 1] = f'ID: {user_id}, username: {username}, age: {age}'
        return f'User {user_id} is updated'
    except IndexError:
        raise HTTPException(status_code= 404, detail= 'User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        users.pop(user_id - 1)
        return f'User {user_id} is deleted'
    except IndexError:
        raise HTTPException(status_code= 404, detail= 'User was not found')
