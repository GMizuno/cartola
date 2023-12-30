from typing import Optional

import pendulum
from cartola_project import Matches
from cartola_project.transformations import StatisticsTransformer

from cartola_2023.constant import (
    StorageFolder,
    Bucket,
    FILE_NAME_JSON,
    FILE_NAME_PARQUET,
)


def export_statistics_bronze(
    api_host_key: str,
    api_secert_key: str,
    league_id: str,
    season_year: str,
    matches_id: Optional[list] = None,
    storage=None,
    writer=None,
) -> list:
    statistics = Matches(api_host_key, api_secert_key)
    data = statistics.get_data(match_id=matches_id)

    file_name = FILE_NAME_JSON.format(
        FOLDER=StorageFolder.STATISTICS,
        BUCKET=Bucket.BRONZE,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=pendulum.now().strftime("%Y-%d-%m_%H:%M:%S"),
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
    data = StatisticsTransformer(file).transformation()

    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = FILE_NAME_PARQUET.format(
        FOLDER=StorageFolder.STATISTICS,
        BUCKET=Bucket.SILVER,
        LEAGUE_ID=league_id,
        SEASON_YEAR=season_year,
        DATE=date,
    )

    writer(storage, file_name, data).write()
