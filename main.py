"""FASTAPI MAIN"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """
    root page
    """
    return {"message": "welcome to my api!"}
