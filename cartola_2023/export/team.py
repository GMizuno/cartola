import pendulum

from cartola_project import Teams
from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)
from cartola_project.transformations import TeamTransformer


def export_team_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    teams_id: list,
    storage,
    writer,
) -> list[dict]:
    times = Teams(api_host_key, api_secert_key)
    data = times.get_data(team_id=teams_id)

    date = pendulum.now().strftime("%Y")
    file_name = FILE_NAME_JSON.format(
        FOLDER=StorageFolder.TEAMS,
        BUCKET=Bucket.BRONZE,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    writer(storage, file_name, data).write()

    return data


def export_team_silver(
    file: dict | list[dict],
    league_id: str,
    season_year: str,
    storage,
    writer,
) -> None:
    data = TeamTransformer(file).transformation()

    date = pendulum.now().strftime("%Y")
    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.TEAMS,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    writer(storage, file_name, data).write()
