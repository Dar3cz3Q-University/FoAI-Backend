import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def run_server():
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run("foai_backend.main:app", host=host, port=port, reload=is_dev())

def is_dev():
    return os.getenv("APP_ENV", "dev") == "dev"

def dev():
    os.environ["APP_ENV"] = "dev"
    print("[INFO] Running in development mode...")
    run_server()

def prod():
    os.environ["APP_ENV"] = "prod"
    print("[INFO] Running in production mode...")
    run_server()
