from datetime import date
from decouple import config

from cartola_2023.constant import ProjectId, BUCKET
from cartola_2023.export.players import export_player_bronze, export_player_silver
from cartola_project import factory_writer, factory_storage, factory_reader

from cartola_2023.export.util import filter_by_date

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")

api_host_key = config("API_HOST_KEY")
api_secert_key = config("API_SECERT_KEY")
league_id = "71"
season_year = "2023"
date_from = date(2023, 4, 1)
date_to = date(2023, 4, 10)

matches_id = filter_by_date(
    gcs, league_id, season_year, date_from, date_to, parquet_reader
)

result = export_player_bronze(
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
    matches_id,
    gcs,
    parquet_writer,
)

export_player_silver(
    result,
    league_id,
    season_year,
    gcs,
    parquet_writer,
)
