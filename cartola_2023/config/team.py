from decouple import config

from cartola_2023.export import export_team_bronze, export_team_silver


def config_team_dict(league_id: str,
                     season_year: str,
                     api_host_key: str = 'API_HOST_KEY',
                     api_secert_key: str = 'API_SECERT_KEY', ) -> dict:
    return {
        'api_host_key': config(api_host_key),
        'api_secert_key': config(api_secert_key),
        'league_id': league_id,
        'season_year': season_year,
    }

# TODO: Mover essa parte, 
params = [
    config_team_dict('71', '2022'),
]
for param in params:
    file = export_team_bronze(**param)
    export_team_silver(file, param['league_id'], param['season_year'])
