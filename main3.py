from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: str):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: str):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
    return f'User {user_id} is deleted'