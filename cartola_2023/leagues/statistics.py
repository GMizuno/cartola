from datetime import date

from cartola_2023.export.statistics import (
    export_statistics_bronze,
    export_statistics_silver,
)
from cartola_2023.export.util import filter_by_date
from cartola_2023.leagues import (
    gcs,
    parquet_writer,
    parquet_reader,
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
)

date_from = date(2023, 4, 1)
date_to = date(2023, 4, 10)

matches_id = filter_by_date(
    gcs, league_id, season_year, date_from, date_to, parquet_reader
)

result = export_statistics_bronze(
    api_host_key,
    api_secert_key,
    league_id,
    season_year,
    matches_id,
    gcs,
    parquet_writer,
)

export_statistics_silver(
    result,
    league_id,
    season_year,
    gcs,
    parquet_writer,
)
