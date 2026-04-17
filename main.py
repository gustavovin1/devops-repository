from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}
@app.get("/random-int")
async def funcaoteste():
    return {"teste": True, "random_int": random.randint(1, 10)}