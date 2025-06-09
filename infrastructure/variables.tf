variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "weather-api-cluster"
  type        = string
  default     = "weather-api-cluster"
}
