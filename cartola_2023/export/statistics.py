from datetime import date
from typing import Optional

import pendulum
from cartola_project import Matches
from cartola_project.transformations import MatchTransformer

from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)
from cartola_2023.export.util import filter_by_date


def export_statistics_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    date_from: date,
    date_to: date,
    matches_id: Optional[list] = None,
    storage=None,
    writer=None,
    reader=None,
) -> list:
    statistics = Matches(api_host_key, api_secert_key)

    if matches_id is None:
        matches_id = filter_by_date(
            storage, league_id, season_year, date_from, date_to, reader
        )

    data = statistics.get_data(match_id=matches_id)

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = FILE_NAME_JSON.format(
        FOLDER=StorageFolder.STATISTICS,
        BUCKET=Bucket.BRONZE,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )
    writer(storage, file_name, data).write()

    return data


def export_statistics_silver(
    file: dict | list[dict],
    league_id: str,
    season_year: str,
    storage,
    writer,
) -> None:
    data = MatchTransformer(file)._get_transformation()

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.STATISTICS,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )

    writer(storage, file_name, data).write()
