from cartola_2023.export.matches import export_matches_bronze, export_matches_silver
from cartola_2023.leagues.brasileirao import (
    gcs,
    json_writer,
    parquet_writer,
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
)


result = export_matches_bronze(
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
    gcs,
    json_writer,
)

export_matches_silver(
    result,
    league_id,
    season_year,
    gcs,
    parquet_writer,
)
