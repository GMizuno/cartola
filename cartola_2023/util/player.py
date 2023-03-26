from datetime import date

from cartola_project import GCSStorage

from cartola_2023.constant import ProjectId
from cartola_2023.export import export_player_bronze, export_player_silver
from cartola_2023.export.util import filter_by_date
from cartola_2023.util.util import config_with_date

# TODO: Mover essa parte,
params = [
    config_with_date(
        league_id='71',
        season_year='2022',
    ),
]

gcs = GCSStorage('cartola.json', ProjectId.GCP_PROD)
match_id = filter_by_date(
    cloudstorage=gcs,
    league_id='71',
    season_year='2022',
    date_from=date(2022, 4, 10),
    date_to=date(2022, 11, 13),
)

# match_id[:100]
# match_id[100:200]
# match_id[200:300]
# match_id[300:]


for param in params:
    result = export_player_bronze(**param, matches_id=match_id[:100])
    export_player_silver(result, param['league_id'], param['season_year'])
