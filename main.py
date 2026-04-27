import random
from fastapi import FastAPI

app = FastAPI()


def get_hello_message():
    return {"message": "Hello World"}


def generate_random_number():
    return random.randint(1, 10)


@app.get("/hello")
async def root():
    return get_hello_message()


@app.get("/random-int")
async def random_int():
    return {"teste": True, "random_int": generate_random_number()}
