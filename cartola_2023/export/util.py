from datetime import date

import pandas as pd
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cartola_project.storage import CloudStorage


def get_all_ids(
    cloudstorage: "CloudStorage", league_id: str, season_year: str, reader
) -> list:
    d = reader(
        cloudstorage,
        f"matches/silver/league={league_id}/season={season_year}/",
    ).read_all_files()

    return list(
        set(
            d.id_team_home.drop_duplicates().to_list()
            + d.id_team_away.drop_duplicates().to_list()
        )
    )


def filter_by_date(
    cloudstorage: "CloudStorage",
    league_id: str,
    season_year: str,
    date_from: date,
    date_to: date,
    reader,
):
    file_folder = f"matches/silver/league={league_id}/season={season_year}/"
    print(file_folder)
    dataframe = reader(
        cloudstorage,
        file_folder,
    ).read_all_files()

    dataframe["reference_date"] = pd.to_datetime(
        dataframe["reference_date"], format="%d-%m-%Y"
    ).dt.date

    result = set(
        dataframe.loc[
            (dataframe["reference_date"] >= date_from)
            & (dataframe["reference_date"] <= date_to)
        ].match_id.to_list()
    )
    return list(result)
