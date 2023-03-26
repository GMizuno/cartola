from datetime import date
from typing import Optional

import pendulum
from cartola_project import Players, GCSStorage, JsonWriter, ParquetWriter
from cartola_project.transformations import PlayerTransformer

from cartola_2023.constant import StorageFolder, Bucket, ProjectId, BUCKET
from cartola_2023.export.util import filter_by_date


def export_player_bronze(api_host_key: str,
                         api_secert_key: str,
                         league_id: str,
                         season_year: str,
                         date_from: Optional[date],
                         date_to: Optional[date],
                         matches_id: Optional[list] = None,
                         ) -> list:
    partidas = Players(api_host_key, api_secert_key)
    gcs = GCSStorage('cartola.json', ProjectId.GCP_PROD)
    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")

    if matches_id is None and date_from is not None and date_to is not None:
        matches_id = filter_by_date(gcs, league_id, season_year, date_from,
                                    date_to)
        
    elif date_from is None or date_to is None:
        raise ValueError(f"date_from e date_to nao podem ser nulos") 

    data = partidas.get_data(match_id=matches_id)

    file_name = f"{StorageFolder.PLAYERS}/{Bucket.BRONZE}/league={league_id}/season={season_year}/{date}.json"
    JsonWriter(gcs, BUCKET, file_name, data).write()

    return data


def export_player_silver(
        file: dict | list[dict], league_id: str, season_year: str
) -> None:
    data = PlayerTransformer(file)._get_transformation()

    gcs = GCSStorage("cartola.json", "cartola-360814")
    date = pendulum.now().strftime("%Y-%d-%m_%H:%M:%S")
    file_name = f"{StorageFolder.PLAYERS}/{Bucket.SILVER}/league={league_id}/season={season_year}/{date}.parquet"
    print(file_name)
    ParquetWriter(gcs, BUCKET, file_name, data).write()
