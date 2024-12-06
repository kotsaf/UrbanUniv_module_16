from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, Возраст: 18'}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=12, description='Enter your username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=100, description='Enter yor age')]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: Annotated[str, Path(min_length=3, max_length=12, description='Enter your username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=100, description='Enter yor age')]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    users.pop(user_id)
    return f'User {user_id} is deleted'
