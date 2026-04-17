from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "random_int": random.randint(1, 10)}