FROM python:3.12-alpine

WORKDIR /usr/news-ktk/src

RUN pip install poetry==2.0.1 --no-cache-dir --root-user-action=ignore

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-cache

COPY . .