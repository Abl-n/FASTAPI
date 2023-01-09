"""FASTAPI MAIN"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my api!"}
