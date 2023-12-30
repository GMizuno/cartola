from cartola_2023.export.team import export_team_bronze, export_team_silver
from cartola_2023.leagues.premier_league import (
    gcs,
    json_writer,
    parquet_writer,
    parquet_reader,
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
)


result = export_team_bronze(
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
    gcs,
    json_writer,
    parquet_reader,
)

export_team_silver(
    result,
    league_id,
    season_year,
    gcs,
    parquet_writer,
)
