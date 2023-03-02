gcloud container clusters get-credentials $GKE_CLUSTER_NAME --region us-central1 --project $GCP_PROJECT_ID

envsubst < kubernetes.yaml | kubectl apply -f -
