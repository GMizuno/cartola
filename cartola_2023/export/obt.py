import pendulum

from cartola_project import factory_writer, factory_storage
from cartola_2023.constant import StorageFolder, ProjectId, BUCKET
from cartola_2023.export.util import create_obt_matches, create_obt_players


# def export_obt() -> None:
#     gcs = GCSStorage("cartola.json", ProjectId.GCP_PROD)
#     data_matches = create_obt_matches(gcs)
#     data_players = create_obt_players(gcs)
#
#     date = pendulum.now().strftime("%Y-%d-%m")
#     file_name = (
#         f"{StorageFolder.OBT}/{StorageFolder.OBT_MATCHES}/matches_{date}.parquet"
#     )
#     ParquetWriter(gcs, BUCKET, file_name, data_matches).write()
#
#     file_name = f"{StorageFolder.OBT}/{StorageFolder.OBT_PLAYERS}/players{date}.parquet"
#     ParquetWriter(gcs, BUCKET, file_name, data_players).write()
