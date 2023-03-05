# Deploy AI Models on Google GKE Autopilot

This repo contains a ML serving framework for deploying AI models specifically from [Hugging Face models](https://huggingface.co/models) on Google GKE Autopilot. 

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






