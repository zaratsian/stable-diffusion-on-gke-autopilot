
provider "google" {
  project = var.gcp_project_id
}

data "google_client_config" "provider" {}
