FROM python:3.11-buster

RUN pip install poetry==1.5.1

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-root

COPY cartola_2023 ./cartola_2023
RUN poetry install

EXPOSE 8080
ENTRYPOINT ["poetry", "run", "python", "-m", "cartola_2023.leagues.brasileirao.match.py"]


