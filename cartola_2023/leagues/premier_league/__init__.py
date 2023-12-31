from cartola_project import factory_writer, factory_storage, factory_reader

from cartola_2023.constant import ProjectId, BUCKET
from cartola_2023.leagues.secret import get_secret

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")


api_host_key = get_secret("API_HOST_KEY")
api_secert_key = get_secret("API_SECERT_KEY")
league_id = "39"
season_year = "2023"
