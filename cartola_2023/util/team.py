from cartola_2023.export import export_team_bronze, export_team_silver
from cartola_2023.util.util import config_without_date

# TODO: Mover essa parte,
params = [
    config_without_date('71', '2022'),
]
for param in params:
    file = export_team_bronze(**param)
    export_team_silver(file, param['league_id'], param['season_year'])
