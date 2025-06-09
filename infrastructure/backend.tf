terraform {
  backend "s3" {
    bucket         = "weather-api-state"
    key            = "eks/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
