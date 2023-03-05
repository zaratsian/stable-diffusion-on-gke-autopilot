resource "google_artifact_registry_repository" "my-repo" {
  location      = "us-central1"
  repository_id = "genai-repo"
  description   = "Docker repo for GenAI Models"
  format        = "DOCKER"
}
