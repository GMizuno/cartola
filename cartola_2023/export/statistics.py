from datetime import date
from typing import Optional

import pendulum
from cartola_project import Matches, GCSStorage, JsonWriter, ParquetWriter
from cartola_project.transformations import MatchTransformer

from cartola_2023.constant import StorageFolder, Bucket, ProjectId, BUCKET
from cartola_2023.export.util import filter_by_date


def export_statistics_bronze(api_host_key: str,
                             api_secert_key: str,
                             league_id: str,
                             season_year: str,
                             date_from: date,
                             date_to: date,
                             matches_id: Optional[list] = None,
                             ) -> list:
    statistics = Matches(api_host_key, api_secert_key)
    gcs = GCSStorage('cartola.json', ProjectId.GCP_PROD)

    if matches_id is None:
        matches_id = filter_by_date(gcs, league_id, season_year, date_from,
                                    date_to)

    data = statistics.get_data(match_id=matches_id)

    date = pendulum.now().strftime('%Y-%d-%m_%H:%M:%S')
    file_name = f'{StorageFolder.STATISTICS}/{Bucket.BRONZE}/league={league_id}/season={season_year}/{date}.json'
    JsonWriter(gcs, BUCKET, file_name, data).write()

    return data


def export_statistics_silver(file: dict | list[dict], league_id: str,
                             season_year: str) -> None:
    data = MatchTransformer(file)._get_transformation()

    gcs = GCSStorage('cartola.json', ProjectId.GCP_PROD)
    date = pendulum.now().strftime('%Y-%d-%m_%H:%M:%S')
    file_name = f'{StorageFolder.STATISTICS}/{Bucket.SILVER}/league={league_id}/season={season_year}/{date}.parquet'
    ParquetWriter(gcs, BUCKET, file_name, data).write()
