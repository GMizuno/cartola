from datetime import date, timedelta

from cartola_2023.export.players import export_player_bronze, export_player_silver

from cartola_2023.export.util import filter_by_date
from cartola_2023.leagues import (
    gcs_matches_parquet,
    gcs_players_json,
    gcs_players_parquet,
    parquet_reader,
    parquet_writer,
    api_host_key,
    api_secert_key,
    leagues_id,
    season_year,
)

date_to = date.today()
date_from = date_to - timedelta(days=7)


for league_id in leagues_id:
    matches_id = filter_by_date(
        gcs_matches_parquet, league_id, season_year, date_from, date_to, parquet_reader
    )

    if matches_id:
        result_player = export_player_bronze(
            api_host_key,
            api_secert_key,
            league_id,
            season_year,
            matches_id,
            gcs_players_json,
            parquet_writer,
        )

        export_player_silver(
            result_player,
            league_id,
            season_year,
            gcs_players_parquet,
            parquet_writer,
        )
    else:
        print("No matches found")
