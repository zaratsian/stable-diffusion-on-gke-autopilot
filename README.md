# Deploy Stable Diffusion within Google GKE Autopilot

This repo contains a ML serving framework for deploying AI models, specifically a Stable Diffusion model from [Hugging Face models](https://huggingface.co/models) on Google GKE Autopilot. All code and assets provided in this repo are made available on an as-is basis and the end user is responsible for all of their own security, scaling, and cost control as part of this deployment. 

[GKE Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) is a mode of operation in GKE in which Google manages your cluster configuration, including your nodes, scaling, security, and other preconfigured settings. Autopilot clusters are optimized to run most production workloads, and provision compute resources based on your Kubernetes manifests.

## Deployment Infra

1. Copy the [.infra/terraform.tfvars.sample](./infra/terraform.tfvars.sample) file into a file called terraform.tfvars.

```
cp ./infra/terraform.tfvars.sample ./infra/terraform.tfvars
```

2. Edit the ./infra/terraform.tfvars file with your own values. This step is potentially optional based on your GCP security and networking setting. If the GCP "default" network is being used and your org security policies do not have rules setup to block certain services, then all of this should run without any modifification required to this terraform.tfvars file.

```
# If you want to modify the file, navigate into the infra directory
cd infra
# Then edit the terraform.tfvars file
vi terraform.tfvars
```

3. Deploy the infrastructure

```
cd infra
terraform init
terraform apply
```

## Build and Deploy Models

1. Navigate into the services directory

```
cd ./services
```

2. Copy the .env.sample into a file called .env, then edit the environment variables to match your preferred setup.

```
cd ./services

# Copy the .env.sample
cp .env.sample .env

# Edit the env variables within the file
vi .env

# Apply the env variables
. .env
```

3. Build the ML Serving Container and Deploy to Artifact Registry

```
cd ./services/app
./cloudbuild_trigger.sh
```

4. Deploy the service to GKE

```
cd ./services
./deploy_to_gke.sh
```

5. Wait a few minutes for the service to start up.

```
kubectl get services -n genai-ns
kubectl get pods -n genai-ns
```

6. Test the Endpoint

```
export SERVICE_IP=$(kubectl get svc genai-service -n genai-ns -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# NOTE: You will need to install the Pillow library (pip3 install Pillow)
python3 ./services/app/make_call.py --host $SERVICE_IP --port 80 --text "surfing goat with sunset in the background"
```
