from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apicultura.v1.main import app as v1_app

app = FastAPI(title="APIcultura API")

app.mount("/v1", v1_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
