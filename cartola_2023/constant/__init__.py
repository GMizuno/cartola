from cartola_2023.constant.bucket import Bucket
from cartola_2023.constant.storagefolder import StorageFolder
from cartola_2023.constant.project_id import ProjectId


BUCKET = "cartola_mizuno"
FILE_NAME_JSON = "{FOLDER}/{BUCKET}/league={LEAGUE_ID}/season={SEASON_YEAR}/{DATE}.json"
FILE_NAME_PARQUET = (
    "{FOLDER}/{BUCKET}/league={LEAGUE_ID}/season={SEASON_YEAR}/{DATE}.parquet"
)

DATASET_ID = "cartola"

__ALL_ = [
    "Bucket",
    "StorageFolder",
    "ProjectId",
    "BUCKET",
    "FILE_NAME_JSON",
    "FILE_NAME_PARQUET",
]
