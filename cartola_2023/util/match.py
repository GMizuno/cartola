from cartola_2023.constant import ProjectId, BUCKET
from cartola_2023.export.matches import export_matches_bronze, export_matches_silver
from cartola_2023.util.util import config_without_date
from cartola_project import factory_writer, factory_storage

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")


params = [
    config_without_date(
        league_id="71", season_year="2023", storage=gcs, writer=json_writer
    ),
]


for param in params:
    result = export_matches_bronze(**param)
    export_matches_silver(
        result, param["league_id"], param["season_year"], gcs, parquet_writer
    )
