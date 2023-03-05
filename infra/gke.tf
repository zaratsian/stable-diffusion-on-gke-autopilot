resource "google_container_cluster" "unified-data-cluster" {
  for_each = var.gke_clusters

  name     = each.key
  location = each.value.region

  network    = var.vpc_name

  # See issue: https://github.com/hashicorp/terraform-provider-google/issues/10782
  ip_allocation_policy {}

  # Enabling Autopilot for this cluster
  enable_autopilot = true

  depends_on = [google_project_service.project]
}

resource "google_service_account" "gke-sa" {
  account_id   = "gke-sa"
  display_name = "GKE Service Account for UDP"
}
