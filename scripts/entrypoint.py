import os
import uvicorn
from dotenv import load_dotenv

load_dotenv("./../.env")


def dev():
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", 8080))
    uvicorn.run("foai_backend.main:app", host=host, port=port, reload=True)
