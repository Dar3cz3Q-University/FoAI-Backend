FROM python:3.12-slim AS builder

ENV POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY foai_backend ./foai_backend
COPY scripts ./scripts

RUN poetry install --only main --no-root

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

WORKDIR /app

CMD ["poetry", "run", "prod"]
