variable "project_id" {
  type    = string
  default = "cartola-360814"
}
variable "region" {
  type    = string
  default = "us-east1"
}
variable "league_id_europe" {type=string}
variable "seasson_year_europe" {type=string}
variable "league_id_brazil" {type=string}
variable "seasson_year_brazil" {type=string}
variable "service_account" {
  type = string
  default = "functions-cartola@cartola-360814.iam.gserviceaccount.com"
}

variable "bucket_trigger_teams" {type=string}
variable "bucket_trigger_players" {type=string}
variable "bucket_trigger_matches" {type=string}
variable "bucket_trigger_statistics" {type=string}

variable "function_name_teams" {
  type = string
}
variable "function_name_players" {
  type = string
}
variable "function_name_matches" {
  type = string
}
variable "function_name_statistics" {
  type = string
}


// Teams Variables
variable "origin_teams" {
  type = string
}
variable "cloud_run_teams_image" {
  type = string
}
variable "teams_cron" {
  type = string
}
variable "cloud_run_teams_name_europe" {
  type = string
}
variable "cloud_run_teams_name_brazil" {
  type = string
}



// Players Variables
variable "origin_players" {
  type = string
}
variable "cloud_run_players_image" {
  type = string
}
variable "players_cron" {
  type = string
}
variable "cloud_run_players_name_europe" {
  type = string
}
variable "cloud_run_players_name_brazil" {
  type = string
}



// Matches Variables
variable "origin_matches" {
  type = string
}
variable "cloud_run_matches_image" {
  type = string
}
variable "macthes_cron" {
  type = string
}
variable "cloud_run_matches_name_europe" {
  type = string
}
variable "cloud_run_matches_name_brazil" {
  type = string
}



// Statistics Variables
variable "origin_statistics" {
  type = string
}
variable "cloud_run_statistics_image" {
  type = string
}
variable "statistics_cron" {
  type = string
}
variable "cloud_run_statistics_name_europe" {
  type = string
}
variable "cloud_run_statistics_name_brazil" {
  type = string
}