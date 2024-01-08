import pendulum

from cartola_project import Fixtures
from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)
from cartola_project.transformations import MatchTransformer


def export_matches_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    storage,
    writer,
) -> list[dict]:
    partidas = Fixtures(api_host_key, api_secert_key)
    data = partidas.get_data(league_id=league_id, season_year=season_year)

    file_name = FILE_NAME_JSON.format(
        FOLDER=StorageFolder.MATCHES,
        BUCKET=Bucket.BRONZE,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=pendulum.now().strftime("%Y"),
    )
    writer(storage, file_name, data).write()

    return data


def export_matches_silver(
    file: dict | list[dict],
    league_id: str,
    season_year: str,
    storage,
    writer,
) -> None:
    data = MatchTransformer(file).transformation()

    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.MATCHES,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=pendulum.now().strftime("%Y"),
    )
    writer(storage, file_name, data).write()
