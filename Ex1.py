from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    age: int


users = []
users.append(User(name="Dmitriy", surname="Solenkov", age=26))
users.append(User(name="Alex", surname="Ivanov", age=34))
users.append(User(name="Max", surname="Stepanov", age=28))
users.append(User(name="Alice", surname="Kuznetsova", age=24))
users.append(User(name="Maria", surname="Makova", age=27))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/")
async def print_users():
    print("Printed all users")
    return users


@app.get("/users/{id}")
async def print_user(id: int):
    print(f"Printed user #{id}")
    return users[id]


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    print("Added new user")


@app.put("/users/{id}")
async def edit_user(id: int, user: User):
    users[id] = user
    print(f"Edited user #{id}")


@app.delete("/users/{id}")
async def delete_user(id: int):
    users.pop(id)
    print(f"Deleted user #{id}")
