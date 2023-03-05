# Project Variables

variable "gcp_project_id" {
  type        = string
  description = "GCP Project Name"
}

variable "gcp_project_services" {
  type        = list(any)
  description = "GCP Service APIs to enable for this project"
  default     = []
}

# VPC Variables

variable "vpc_name" {
  type        = string
  description = "VPC Name"
}

# GKE Variables

variable "gke_clusters" {
  type        = map(any)
  description = "GKE Cluster configs"
}

