FROM python:3.11-buster

RUN pip install poetry==1.5.1

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root

COPY cartola_2023 ./cartola_2023
RUN poetry install --without dev

EXPOSE 8080
ENTRYPOINT ["ls"]


