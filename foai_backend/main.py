import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_health import health
from fastapi.middleware.cors import CORSMiddleware

from foai_backend.routes.predict import predict

load_dotenv("./../.env")
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def always_ok():
    return True


app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins if origin],
    allow_credentials=True,
    allow_methods=["GET, POST"],
    allow_headers=["*"],
)


app.add_api_route("/health", health([always_ok]))

app.include_router(predict.router)
