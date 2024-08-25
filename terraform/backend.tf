terraform {
  backend "gcs" {
    bucket = "gcp-cartola-terraform"
    prefix = "function"
  }
}