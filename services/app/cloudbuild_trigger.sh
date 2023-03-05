gcloud builds submit \
--substitutions=_GCP_PROJECT_ID="$GCP_PROJECT_ID",_ARTIFACT_REPO_REGION="$ARTIFACT_REPO_REGION",_ARTIFACT_REPO_NAME="$ARTIFACT_REPO_NAME",_IMAGE_NAME="genai" \
--region=us-central1 \
--config cloudbuild.yaml
