from fastapi import FastAPI
from fastapi_health import health

from foai_backend.routes.predict import predict

app = FastAPI()


def always_ok():
    return True


app.include_router(predict.router)
app.add_api_route("/health", health([always_ok]))
