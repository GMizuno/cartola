from datetime import date

from cartola_2023.export import export_statistics_bronze, \
    export_statistics_silver
from cartola_2023.util.util import config_with_date

# TODO: Mover essa parte,
params = [
    config_with_date('71', '2022', date(2022, 10, 1), date(2022, 10, 12)),
]
for param in params:
    result = export_statistics_bronze(**param)
    export_statistics_silver(result, param['league_id'], param['season_year'])
