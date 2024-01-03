from datetime import date, timedelta

from cartola_2023.export.players import export_player_bronze, export_player_silver
from cartola_2023.export.statistics import (
    export_statistics_bronze,
    export_statistics_silver,
)
from cartola_2023.export.util import filter_by_date
from cartola_2023.leagues import (
    gcs,
    parquet_reader,
    parquet_writer,
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
)

date_to = date.today()
date_from = date_to - timedelta(days=7)

matches_id = filter_by_date(
    gcs, league_id, season_year, date_from, date_to, parquet_reader
)


if matches_id:
    result_player = export_player_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        matches_id,
        gcs,
        parquet_writer,
    )

    export_player_silver(
        result_player,
        league_id,
        season_year,
        gcs,
        parquet_writer,
    )

    result_statistics = export_statistics_bronze(
        api_host_key,
        api_secert_key,
        league_id,
        season_year,
        matches_id,
        gcs,
        parquet_writer,
    )

    export_statistics_silver(
        result_statistics,
        league_id,
        season_year,
        gcs,
        parquet_writer,
    )
else:
    print("No matches found")
