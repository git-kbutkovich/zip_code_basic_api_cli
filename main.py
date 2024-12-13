from fastapi import FastAPI

import zip_codes

app = FastAPI()
app.include_router(zip_codes.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
