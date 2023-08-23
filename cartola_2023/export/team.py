import pendulum

from cartola_project import Teams, factory_reader, factory_writer, factory_storage
from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    ProjectId,
    BUCKET,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)
from cartola_project.transformations import TeamsTransformer
from cartola_2023.export.util import get_all_ids


def export_team_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    storage,
    writer,
    reader,
) -> list[dict]:
    times = Teams(api_host_key, api_secert_key)

    ids = get_all_ids(storage, league_id, season_year, reader)
    data = times.get_data(team_id=ids)

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
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
    data = TeamsTransformer(file)._get_transformation()

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.TEAMS,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    writer(storage, file_name, data).write()
