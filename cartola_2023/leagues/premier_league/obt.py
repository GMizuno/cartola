from cartola_2023.export.obt import export_obt

from cartola_2023.constant import ProjectId, BUCKET
from cartola_project import factory_writer, factory_storage, factory_reader

storage = factory_storage.get_storage("GCP")
gcs = storage(None, ProjectId.GCP_PROD, BUCKET)
parquet_writer = factory_writer.get_storage("Parquet")
parquet_reader = factory_reader.get_storage("Parquet")

export_obt(gcs, parquet_writer, parquet_reader)
