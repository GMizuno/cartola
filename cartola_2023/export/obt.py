import pendulum

from cartola_2023.constant import StorageFolder
from cartola_2023.export.util import create_obt_matches, create_obt_players


def export_obt(storage, writer, reader) -> None:
    data_matches = create_obt_matches(storage, reader)
    data_players = create_obt_players(storage, reader)

    date = pendulum.now().strftime("%Y-%d-%m")
    file_name = (
        f"{StorageFolder.OBT}/{StorageFolder.OBT_MATCHES}/matches_{date}.parquet"
    )
    writer(storage, file_name, data_matches).write()

    file_name = f"{StorageFolder.OBT}/{StorageFolder.OBT_PLAYERS}/players{date}.parquet"
    writer(storage, file_name, data_players).write()
