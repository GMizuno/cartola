from cartola_2023.export.team import export_team_bronze, export_team_silver
from cartola_2023.leagues.brasileirao import (
    gcs,
    json_writer,
    parquet_writer,
    parquet_reader,
    api_host_key,
    api_secert_key,
)


result = export_team_bronze(
    api_host_key,
    api_secert_key,
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
