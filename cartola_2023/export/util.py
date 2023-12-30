from datetime import date

import pandas as pd
from typing import TYPE_CHECKING
from pandas import DataFrame

if TYPE_CHECKING:
    from cartola_project.storage import CloudStorage


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
    elif data.win_home == "home_win" and data.home is True:
        return "win"
    else:
        return "lose"


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
    dataframe = reader(
        cloudstorage,
        f"matches/silver/league={league_id}/season={season_year}/",
    ).read_all_files()

    dataframe["reference_date"] = pd.to_datetime(
        dataframe["date"], format="mixed"
    ).dt.date

    result = set(
        dataframe.loc[
            (dataframe["reference_date"] >= date_from)
            & (dataframe["reference_date"] <= date_to)
        ].partida_id.to_list()
    )
    return list(result)


def create_obt_matches(cloudstorage: "CloudStorage", reader) -> pd.DataFrame:
    dataframe1 = reader(cloudstorage, "matches/silver/").read_all_files()

    dataframe2 = reader(cloudstorage, "statistics/silver/").read_all_files()

    dataframe3 = reader(cloudstorage, "teams/silver/").read_all_files()

    dataframe2 = dataframe2.astype({"fixture": "int64"})
    dataframe3 = dataframe3.astype({"team_id": "int64"})

    result = dataframe1.merge(
        dataframe2, how="inner", right_on="fixture", left_on="match_id"
    )
    result = result.merge(dataframe3, how="inner", on=["team_id"])

    result = result.assign(home=result.id_team_home == result.team_id)

    return result.drop_duplicates()


def create_obt_players(cloudstorage: "CloudStorage", reader) -> pd.DataFrame:
    dataframe1 = reader(cloudstorage, "players/silver/").read_all_files()

    dataframe2 = reader(cloudstorage, "matches/silver/").read_all_files()

    dataframe1 = dataframe1.astype({"fixture": "int64"})
    dataframe2 = dataframe2.astype({"match_id": "int64"})

    result = dataframe1.merge(
        dataframe2, how="inner", right_on="match_id", left_on="fixture"
    )

    return result.drop_duplicates()
