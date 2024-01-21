from cartola_2023.export.matches import export_matches_bronze, export_matches_silver

from cartola_2023.export.team import export_team_bronze, export_team_silver
from cartola_2023.leagues import (
    gcs,
    json_writer,
    parquet_writer,
    parquet_reader,
    api_host_key,
    api_secert_key,
    league_id_list,
    season_year,
)

leagues_id = list(
    map(
        lambda x: x.strip(),
        league_id_list.split("_"),
    )
)

for league_id in leagues_id:
    result_matches = export_matches_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        gcs,
        json_writer,
    )

    export_matches_silver(
        result_matches,
        league_id,
        season_year,
        gcs,
        parquet_writer,
    )

    result_teams = export_team_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        gcs,
        json_writer,
        parquet_reader,
    )

    export_team_silver(
        result_teams,
        league_id,
        season_year,
        gcs,
        parquet_writer,
    )
