from cartola_project import factory_writer, factory_storage, factory_reader
from decouple import config

from cartola_2023.constant import ProjectId

api_host_key = config("API_HOST_KEY")
api_secert_key = config("API_SECERT_KEY")
league_id_list = config("LEAGUE_ID")
leagues_id = list(
    map(
        lambda x: x.strip(),
        league_id_list.split("_"),
    )
)
season_year = config("SEASON_YEAR")

storage = factory_storage.get_storage("GCP")

gcs_matches_json = storage(None, ProjectId.GCP_PROD, "matches_json")
gcs_matches_parquet = storage(None, ProjectId.GCP_PROD, "matches_parquet")

gcs_teams_json = storage(None, ProjectId.GCP_PROD, "teams_json")
gcs_teams_parquet = storage(None, ProjectId.GCP_PROD, "teams_parquet")

gcs_players_json = storage(None, ProjectId.GCP_PROD, "players_json")
gcs_players_parquet = storage(None, ProjectId.GCP_PROD, "players_parquet")

gcs_statistics_json = storage(None, ProjectId.GCP_PROD, "statistics_json")
gcs_statistics_parquet = storage(None, ProjectId.GCP_PROD, "statistics_parquet")

json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")
