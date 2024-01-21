from cartola_project import factory_writer, factory_storage, factory_reader
from decouple import config

from cartola_2023.constant import ProjectId, BUCKET

api_host_key = config("API_HOST_KEY")
api_secert_key = config("API_SECERT_KEY")
league_id_list = config("LEAGUE_ID")
season_year = config("SEASON_YEAR")

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")
