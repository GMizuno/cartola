from .bucket import Bucket
from .storagefolder import StorageFolder
from .project_id import ProjectId


BUCKET = "cartola_mizuno"
FILE_NAME_JSON = "{FOLDER}/{BUCKET}/league={LEAGUE_ID}/season={SEASON_YEAR}/{DATE}.json"
FILE_NAME_PARQUET = "{FOLDER}/{BUCKET}/league={LEAGUE_ID}/season={SEASON_YEAR}/{DATE}.parquet"
DATASET_ID = "cartola"

__ALL_ = [
    "Bucket",
    "StorageFolder",
    "ProjectId",
]
