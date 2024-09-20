// Functions
bucket_trigger_teams = "teams_parquet"
bucket_trigger_players = "players_parquet"
bucket_trigger_matches = "matches_parquet"
bucket_trigger_statistics = "statistics_parquet"


// Teams
teams_cron            = "0 9 * * 4"
origin_teams          = "teams"
cloud_run_teams_image = "cartola-python-teams"
function_name_teams   = "teams"
league_id_europe             = 71
league_id_brazil             = 39
seasson_year_europe          = 2024
seasson_year_brazil          = 2024

// Teams - EUROPE
cloud_run_teams_name_europe = "teams-europe"

// Teams - BR
cloud_run_teams_name_brazil = "teams-br"

// Players
cloud_run_players_image = "cartola-python-players"
players_cron            = "0 10 * * 1,3,5"
origin_players          = "players"
function_name_players   = "players"

// Matches
cloud_run_matches_image = "cartola-python-matchs"
macthes_cron            = "30 8 * * 2,4"
origin_matches          = "matches"
function_name_matches   = "matches"


// Matches - EUROPE
cloud_run_matches_name_europe = "matches-europe"

// Matches - BR
cloud_run_matches_name_brazil = "matches-br"


// Players - EUROPE
cloud_run_players_name_europe = "players-europe"

// Players - BR
cloud_run_players_name_brazil = "players-br"

// Statitics
cloud_run_statistics_image = "cartola-python-statistics"
statistics_cron            = "0 10 * * 1,3,5"
origin_statistics          = "statistics"
function_name_statistics   = "statistics"

// Statitics - EUROPE
cloud_run_statistics_name_europe = "statistics-europe"

// Statitics - BR
cloud_run_statistics_name_brazil = "statistics-br"
