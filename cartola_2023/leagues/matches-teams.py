from cartola_2023.export.matches import export_matches_bronze, export_matches_silver

from cartola_2023.export.team import export_team_bronze, export_team_silver
from cartola_2023.export.util import get_all_ids
from cartola_2023.leagues import (
    gcs_matches_json,
    gcs_matches_parquet,
    gcs_teams_json,
    gcs_teams_parquet,
    json_writer,
    parquet_writer,
    parquet_reader,
    api_host_key,
    api_secert_key,
    leagues_id,
    season_year,
)


for league_id in leagues_id:
    print(f"Getting Match information to League {league_id}")
    result_matches = export_matches_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        gcs_matches_json,
        json_writer,
    )

    print(f"Transformer Matches to Parquet league_id={league_id}")
    export_matches_silver(
        result_matches,
        league_id,
        season_year,
        gcs_matches_parquet,
        parquet_writer,
    )

    print(f"Getting Team information to League {league_id}")
    ids = get_all_ids(gcs_matches_parquet, league_id, season_year, parquet_reader)
    result_teams = export_team_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        ids,
        gcs_teams_json,
        json_writer,
    )

    print(f"Transformer Team to Parquet league_id={league_id}")
    export_team_silver(
        result_teams,
        league_id,
        season_year,
        gcs_teams_parquet,
        parquet_writer,
    )
