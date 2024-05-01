import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate")
async def root():
    time.sleep(5)
    return {"message": "It's all right"}