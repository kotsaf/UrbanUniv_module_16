from fastapi import FastAPI, HTTPException, status, Body, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory= r'D:\Projects\H\.venv\templates2')

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> User:
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
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
