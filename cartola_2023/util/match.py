from cartola_2023.constant import ProjectId, BUCKET
from cartola_2023.export.matches import export_matches_bronze, export_matches_silver
from decouple import config
from cartola_project import factory_writer, factory_storage

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
json_writer = factory_writer.get_storage("JSON")
parquet_writer = factory_writer.get_storage("Parquet")


result = export_matches_bronze(
    config("API_HOST_KEY"),
    config("API_SECERT_KEY"),
    "71",
    "2023",
    gcs,
    json_writer,
)

export_matches_silver(
    result,
    "71",
    "2023",
    gcs,
    parquet_writer,
)
