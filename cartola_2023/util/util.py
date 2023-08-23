from datetime import date
from typing import Optional

from decouple import config


def config_without_date(
    league_id: str,
    season_year: str,
    api_host_key: str = "API_HOST_KEY",
    api_secert_key: str = "API_SECERT_KEY",
    storage=None,
    writer=None,
) -> dict:
    return {
        "api_host_key": config(api_host_key),
        "api_secert_key": config(api_secert_key),
        "league_id": league_id,
        "season_year": season_year,
        "storage": storage,
        "writer": writer,
    }


def config_with_date(
    league_id: str,
    season_year: str,
    date_from: Optional[date],
    date_to: Optional[date],
    api_host_key: str = "API_HOST_KEY",
    api_secert_key: str = "API_SECERT_KEY",
    storage=None,
    writer=None,
) -> dict:
    return {
        "api_host_key": config(api_host_key),
        "api_secert_key": config(api_secert_key),
        "league_id": league_id,
        "season_year": season_year,
        "date_from": date_from,
        "date_to": date_to,
        "storage": storage,
        "writer": writer,
    }
