from fastapi import FastAPI

import q_4

app = FastAPI()

app.include_router(q_4.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}
