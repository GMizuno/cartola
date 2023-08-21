from datetime import date
from typing import Optional

import pendulum
from cartola_project import Players
from cartola_project.transformations import PlayerTransformer

from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)
from cartola_2023.export.util import filter_by_date


def export_player_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    date_from: Optional[date],
    date_to: Optional[date],
    matches_id: Optional[list] = None,
    storage=None,
    writer=None,
    reader=None,
) -> list:
    partidas = Players(api_host_key, api_secert_key)
    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")

    if matches_id is None and date_from is not None and date_to is not None:
        matches_id = filter_by_date(
            storage, league_id, season_year, date_from, date_to, reader
        )

    elif date_from is None or date_to is None:
        raise ValueError(f"date_from e date_to nao podem ser nulos")

    data = partidas.get_data(match_id=matches_id)

    file_name = FILE_NAME_JSON.format(
        FOLDER=StorageFolder.PLAYERS,
        BUCKET=Bucket.BRONZE,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    writer(storage, file_name, data).write()

    return data


def export_player_silver(
    file: dict | list[dict],
    league_id: str,
    season_year: str,
    storage=None,
    writer=None,
) -> None:
    data = PlayerTransformer(file)._get_transformation()
    data = data.astype(str)

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.PLAYERS,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    print(file_name)
    writer(storage, file_name, data).write()
