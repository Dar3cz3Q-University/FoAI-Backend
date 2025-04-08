FROM python:3.12-slim AS builder

ENV POETRY_NO_INTERACTION=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.2 python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry export --without-hashes -f requirements.txt -o requirements.txt

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_HOST=0.0.0.0
ENV APP_PORT=8080

CMD ["sh", "-c", "uvicorn foai_backend.main:app --host $APP_HOST --port $APP_PORT"]
