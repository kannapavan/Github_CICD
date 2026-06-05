# Project Requirements: CI/CD Pipeline Simulation

## Objective
Create a simple Python-based application and simulate a real-world CI/CD pipeline using GitHub Actions, Docker packaging, and multi-environment deployment (Test → Staging → Production).

## Application Requirements
- Simple Python web application (Flask or FastAPI)
- Health check endpoint (`/health`)
- Version endpoint (`/version`)
- At least one business endpoint (e.g., `/greet`)
- Unit tests with pytest
- Proper project structure

## CI/CD Pipeline Requirements
- **Continuous Integration**: Automated testing on every push
- **Continuous Delivery**: Automated build, Docker packaging, and deployment
- **Environment Strategy**: Three environments — Test, Staging, Production
- **Deployment Gates**: Manual approval required between environments
- **Docker**: Containerize the application
- **Versioning**: Semantic versioning via Git tags

## Learning Goals
- Understand GitHub Actions workflow syntax
- Understand Docker multi-stage builds
- Understand environment promotion strategy
- Understand manual approval gates in CD
- Understand repository structure for CI/CD

## Constraints
- No cloud services (simulated local deployment)
- All files must be in a single repository
- Use free GitHub Actions features only
