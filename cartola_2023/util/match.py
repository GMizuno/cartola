from cartola_2023.export import export_matches_bronze, export_matches_silver
from cartola_2023.util.util import config_without_date

params = [
    config_without_date(
        league_id='71',
        season_year='2022'
    ),
]
for param in params:
    result = export_matches_bronze(**param)
    export_matches_silver(result, param['league_id'], param['season_year'])
