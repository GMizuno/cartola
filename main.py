from datetime import date

from cartola_project import GCSStorage

from cartola_2023.constant import ProjectId
from cartola_2023.export.util import filter_by_date

gcs = GCSStorage('cartola.json', ProjectId.GCP_PROD)

r = filter_by_date(
    cloudstorage=gcs,
    league_id='71',
    season_year='2022',
    date_from=date(2022, 4, 10),
    date_to=date(2022, 11, 13),
)
set(r)
