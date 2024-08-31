from datetime import date

from cartola_2023.export.statistics import (
    export_statistics_bronze,
    export_statistics_silver,
)
from cartola_2023.export.util import filter_by_date
from cartola_2023.leagues import (
    gcs_matches_parquet,
    gcs_statistics_json,
    gcs_statistics_parquet,
    parquet_reader,
    parquet_writer,
    api_host_key,
    api_secert_key,
    leagues_id,
    season_year,
)

date_to = date.fromisoformat("2024-08-30")
date_from = date.fromisoformat("2024-01-01")

matches_id = filter_by_date(
    gcs_matches_parquet, leagues_id[0], season_year, date_from, date_to, parquet_reader
)

# matches_id = _matches_id[:100]
# matches_id = _matches_id[100:200]
# matches_id = _matches_id[200:239]

for league_id in leagues_id:
    if matches_id:
        result_statistics = export_statistics_bronze(
            api_host_key,
            api_secert_key,
            league_id,
            season_year,
            matches_id,
            gcs_statistics_json,
            parquet_writer,
        )

        export_statistics_silver(
            result_statistics,
            league_id,
            season_year,
            gcs_statistics_parquet,
            parquet_writer,
        )
    else:
        print("No matches found")
