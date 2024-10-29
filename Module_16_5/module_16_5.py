from fastapi import FastAPI, HTTPException,Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates=Jinja2Templates(directory='templates')


app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/",response_class=HTMLResponse)
async def get_list(request:Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int) -> User:
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")
