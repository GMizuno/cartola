module "gcs_functions" {
 source       = "./modules/storage-bucket"
}

module "cloud_functions_matches" {
 source = "./modules/cloudfunction"
 bucket_name =  module.gcs_functions.gcs-name.name
 project_id = var.project_id
 region = var.region
 service_account = var.service_account
 function_name = var.function_name_matches
 origin = var.origin_matches
 bucket_trigger = var.bucket_trigger_matches
}

module "cloud_functions_teams" {
 source = "./modules/cloudfunction"
 bucket_name =  module.gcs_functions.gcs-name.name
 project_id = var.project_id
 region = var.region
 service_account = var.service_account
 function_name = var.function_name_teams
 origin = var.origin_teams
 bucket_trigger = var.bucket_trigger_teams
}

module "cloud_functions_statistics" {
 source = "./modules/cloudfunction"
 bucket_name =  module.gcs_functions.gcs-name.name
 project_id = var.project_id
 region = var.region
 service_account = var.service_account
 function_name = var.function_name_statistics
 origin = var.origin_players
 bucket_trigger = var.bucket_trigger_statistics
}

module "cloud_functions_players" {
 source = "./modules/cloudfunction"
 bucket_name =  module.gcs_functions.gcs-name.name
 project_id = var.project_id
 region = var.region
 service_account = var.service_account
 function_name = var.function_name_players
 origin = var.origin_players
 bucket_trigger = var.bucket_trigger_players
}

// BR
module "cloud_run_job_matches_br" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_matches_name_brazil
 image_name = var.cloud_run_matches_image
 cron = var.macthes_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_teams_br" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_teams_name_brazil
 image_name = var.cloud_run_teams_image
 cron = var.teams_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_statistics_br" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_statistics_name_brazil
 image_name = var.cloud_run_statistics_image
 cron = var.statistics_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_players_br" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_players_name_brazil
 image_name = var.cloud_run_players_image
 cron = var.players_cron
 league_id = var.league_id
 season_year = var.seasson_year
}


// EUROPE
module "cloud_run_job_matches_europe" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_matches_name_europe
 image_name = var.cloud_run_matches_image
 cron = var.macthes_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_teams_europe" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_teams_name_europe
 image_name = var.cloud_run_teams_image
 cron = var.teams_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_statistics_europe" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_statistics_name_europe
 image_name = var.cloud_run_statistics_image
 cron = var.statistics_cron
 league_id = var.league_id
 season_year = var.seasson_year
}

module "cloud_run_job_players_europe" {
 source = "./modules/cloudrun"
 region = var.region
 project = var.project_id
 cloud_run_name = var.cloud_run_players_name_europe
 image_name = var.cloud_run_players_image
 cron = var.players_cron
 league_id = var.league_id
 season_year = var.seasson_year
}
