# Cloud Native GitOps Platform

A production-oriented cloud-native application demonstrating a complete DevOps and GitOps workflow, from application development to containerization, continuous integration, Kubernetes deployment, GitOps delivery, infrastructure as code, and observability.

## 🚀 Project Overview

The goal of this project is to build and operate a small cloud-native application using modern DevOps practices.

The project progressively implements:

- Application development with Python and FastAPI
- PostgreSQL database
- Automated testing
- Docker containerization
- Docker Compose for local development
- CI/CD with GitHub Actions
- Container image management with GitHub Container Registry (GHCR)
- Kubernetes deployment
- Helm charts
- GitOps with Argo CD
- Infrastructure as Code with Terraform
- Monitoring with Prometheus and Grafana
- Security and container best practices

## 🏗️ Architecture

The final architecture will follow this workflow:

```text
Developer
    │
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Tests
    ├── Lint
    ├── Security Scan
    └── Docker Build
            │
            ▼
           GHCR
            │
            ▼
       GitOps Repository
            │
            ▼
          Argo CD
            │
            ▼
       Kubernetes Cluster
            │
       ┌────┴─────┐
       ▼          ▼
    FastAPI   PostgreSQL
       │
       ▼
 Prometheus
       │
       ▼
   Grafana