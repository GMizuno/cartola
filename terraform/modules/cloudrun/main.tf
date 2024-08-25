locals {
  date_tag = formatdate("YYYYMMDD", timestamp())
#   date_tag = "20240818"
}

resource "google_cloud_run_v2_job" "cloud_run_players" {
  name     = var.cloud_run_name
  location = var.region
  project = var.project

  template {
    template {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project}/cartola-project/${var.image_name}:${local.date_tag}"
        env {
          name  = "LEAGUE_ID"
          value = var.league_id
        }
        env {
          name  = "SEASON_YEAR"
          value = var.season_year
        }
        env {
          name = "API_SECERT_KEY"
          value_source {
            secret_key_ref {
              secret  = "projects/1077543354314/secrets/Rapid_Api_API_SECERT_KEY"
              version = "1"
            }
          }
        }
        env {
          name = "API_HOST_KEY"
          value_source {
            secret_key_ref {
              secret  = "projects/1077543354314/secrets/Rapid_Api_API_SHOST_KEY"
              version = "1"
            }
          }
        }
        resources {
          limits = {
            cpu    = "1"
            memory = "1024Mi"
          }
        }
      }
      service_account = "cartola-projeto-python@cartola-360814.iam.gserviceaccount.com"
    }
  }

  lifecycle {
    ignore_changes = [
      launch_stage,
    ]
  }
}


resource "google_cloud_scheduler_job" "scheduler_job_players" {
  name     = "${google_cloud_run_v2_job.cloud_run_players.name}-agendador"
  project  = google_cloud_run_v2_job.cloud_run_players.project
  region   = google_cloud_run_v2_job.cloud_run_players.location
  schedule = var.cron

  http_target {
    http_method = "POST"
    uri         = "https://${google_cloud_run_v2_job.cloud_run_players.location}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${google_cloud_run_v2_job.cloud_run_players.project}/jobs/${google_cloud_run_v2_job.cloud_run_players.name}:run"

    oauth_token {
      service_account_email = "cartola-projeto-python@cartola-360814.iam.gserviceaccount.com"
    }
  }
}
