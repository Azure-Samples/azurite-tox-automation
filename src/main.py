from fastapi import FastAPI
from src import app as demoapp

app = FastAPI(
    title="Simple Azurite Demo",
    description = ""
)

app.include_router(demoapp.router)

