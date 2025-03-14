FROM python:3.11-buster

RUN pip install poetry==1.5.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN touch README.md

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY cartola_2023 ./cartola_2023

RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "cartola_2023.leagues.statistics"]
