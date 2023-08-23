from cartola_2023.export.team import export_team_bronze, export_team_silver
from decouple import config

from cartola_2023.constant import ProjectId, BUCKET
from cartola_project import factory_writer, factory_storage, factory_reader

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")


result = export_team_bronze(
    config("API_HOST_KEY"),
    config("API_SECERT_KEY"),
    "71",
    "2023",
    gcs,
    json_writer,
    parquet_reader,
)

export_team_silver(
    result,
    "71",
    "2023",
    gcs,
    parquet_writer,
)
