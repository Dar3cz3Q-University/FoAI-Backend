from fastapi import FastAPI
from fastapi_health import health
from fastapi.middleware.cors import CORSMiddleware

from foai_backend.routes.predict import predict

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


app.include_router(predict.router)
app.add_api_route("/health", health([always_ok]))
