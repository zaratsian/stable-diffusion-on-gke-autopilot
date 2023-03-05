
data "google_project" "project" {
}

resource "google_project_service" "project" {
  for_each = toset(var.gcp_project_services)
  service  = each.value

  disable_on_destroy = false
}
