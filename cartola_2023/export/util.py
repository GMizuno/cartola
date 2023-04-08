from datetime import date

import pandas as pd
from cartola_project import ParquetReader
from cartola_project.connector import CloudStorage
from pandas import DataFrame

from cartola_2023.constant import Bucket


def win_home(data: DataFrame):
    if data.goals_home == data.goals_away:
        return "home_draw"
    elif data.goals_home > data.goals_away:
        return "home_win"
    else:
        return "home_lose"


def win(data: DataFrame):
    if data.win_home == "home_draw":
        return "draw"
    elif data.win_home == "home_win" and data.home == True:
        return "win"
    else:
        return "lose"


def get_all_ids(cloudstorage: CloudStorage, league_id: str,
                season_year: str) -> list:
    d = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        f"matches/silver/league={league_id}/season={season_year}/",
    ).read_all_files()
    return list(
        set(
            d.id_team_home.drop_duplicates().to_list()
            + d.id_team_away.drop_duplicates().to_list()
        )
    )


def filter_by_date(
        cloudstorage: CloudStorage,
        league_id: str,
        season_year: str,
        date_from: date,
        date_to: date,
):
    dataframe = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        f"matches/silver/league={league_id}/season={season_year}/",
    ).read_all_files()

    dataframe["reference_date"] = pd.to_datetime(dataframe['date']).dt.date
    result = dataframe.loc[
        (dataframe['reference_date'] >= date_from) &
        (dataframe['reference_date'] <= date_to)]. \
        match_id.to_list()
    return result


def create_obt_matches(cloudstorage: CloudStorage) -> pd.DataFrame:
    dataframe1 = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        "matches/silver/"
    ).read_all_files()

    dataframe2 = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        "statistics/silver/"
    ).read_all_files()

    dataframe3 = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        "teams/silver/"
    ).read_all_files()

    dataframe2 = dataframe2.astype({"fixture": "int64"})
    dataframe3 = dataframe3.astype({"team_id": "int64"})

    result = dataframe1.merge(dataframe2, how="inner", right_on="fixture",
                              left_on="match_id")
    result = result.merge(dataframe3, how="inner", on=["team_id"])

    result = result.assign(home=result.id_team_home == result.team_id)

    return result.drop_duplicates()


def create_obt_players(cloudstorage: CloudStorage) -> pd.DataFrame:
    dataframe1 = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        "players/silver/"
    ).read_all_files()

    dataframe2 = ParquetReader(
        cloudstorage,
        Bucket.MAIN,
        f"matches/silver/"
    ).read_all_files()

    dataframe1 = dataframe1.astype({"fixture": "int64"})
    dataframe2 = dataframe2.astype({"match_id": "int64"})

    result = dataframe1.merge(dataframe2, how="inner", right_on="match_id",
                              left_on="fixture")

    return result.drop_duplicates()
