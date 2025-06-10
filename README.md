# Part A: Weather API Infrastructure

This repository provisions infrastructure for the Weather API using **Terraform** on **AWS EKS**, and builds/deploys Docker images to **Docker Hub**.

---

## 🔐 Required GitHub Secrets

To enable GitHub Actions to interact with AWS and Docker Hub, configure the following repository secrets:

| Secret Name              | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `AWS_ACCESS_KEY_ID`      | Your AWS access key ID                                                      |
| `AWS_SECRET_ACCESS_KEY`  | Your AWS secret access key                                                  |
| `AWS_REGION`             | AWS region where infrastructure is provisioned (e.g. `us-east-1`)          |
| `EKS_CLUSTER_NAME`       | Name of your EKS cluster                                                    |
| `DOCKERHUB_USERNAME`     | Docker Hub username                                                         |
| `DOCKERHUB_PASSWORD`     | Docker Hub password or personal access token                                |

### How to set them:

1. Fork this GitHub repo: [kabidhasan/part-a-weather-api](https://github.com/kabidhasan/part-a-weather-api)
2. Navigate to **Settings > Secrets and variables > Actions**
3. Click **"New repository secret"**
4. Add each of the above secrets with their corresponding values

---

## 🧑‍💻 Local Development Setup

To run the infrastructure locally, follow these steps:

### 1. Clone your repository

```bash
git clone https://github.com/<your-username>/part-a-weather-api.git
cd part-a-weather-api
````

### 2. Configure AWS CLI

Make sure you have AWS CLI installed and configured:

```bash
aws configure
```

You'll be prompted to enter:

* AWS Access Key ID
* AWS Secret Access Key
* Default region name (e.g., `us-east-1`)
* Default output format (optional: `json`, `table`, or `text`)

### 3. Initialize Terraform in Infrastructure folder

```bash
cd .\infrastructure\
terraform init
```

### 4. Review the infrastructure plan

```bash
terraform plan
```

### 5. Apply the infrastructure changes

```bash
terraform apply
```

Confirm the action when prompted.

---

### 6. Push the code for triggering CI/CD

```bash
git add .
git commit -m"Pushing for deployment"
git push -u origin main
```
The Weather API APP should be deployed AWS EKS.
