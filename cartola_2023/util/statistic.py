from datetime import date

from cartola_2023.export import export_statistics_bronze, \
    export_statistics_silver
from cartola_2023.util.util import config_with_date

# TODO: Mover essa parte,
params = [
    config_with_date(
        league_id='71',
        season_year='2022',
        date_from=date(2022, 4, 10),
        date_to=date(2022, 11, 13),
    ),
]
for param in params:
    result = export_statistics_bronze(**param)
    export_statistics_silver(result, param['league_id'], param['season_year'])
