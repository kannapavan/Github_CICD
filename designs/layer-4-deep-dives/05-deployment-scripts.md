# Deep Dive: Deployment Scripts

## scripts/deploy.sh
```bash
#!/bin/bash
# Usage: ./scripts/deploy.sh <environment> <image_tag>
# Example: ./scripts/deploy.sh test v1.0.0

set -euo pipefail

ENV=$1
TAG=${2:-latest}
IMAGE="ghcr.io/your-org/your-app:${TAG}"

case $ENV in
  test)
    PORT=5001
    ENV_NAME=test
    ;;
  staging)
    PORT=5002
    ENV_NAME=staging
    ;;
  production)
    PORT=5000
    ENV_NAME=production
    ;;
  *)
    echo "Unknown environment: $ENV"
    exit 1
    ;;
esac

echo "Deploying ${IMAGE} to ${ENV_NAME} on port ${PORT}"

# Stop existing container if running
docker stop "app-${ENV_NAME}" 2>/dev/null || true
docker rm "app-${ENV_NAME}" 2>/dev/null || true

# Run new container
docker run -d \
  --name "app-${ENV_NAME}" \
  -p "${PORT}:5000" \
  -e "ENVIRONMENT=${ENV_NAME}" \
  -e "APP_VERSION=${TAG}" \
  "${IMAGE}"

echo "✅ Deployed to ${ENV_NAME} at http://localhost:${PORT}"
```

## scripts/test_docker_local.sh
```bash
#!/bin/bash
# Build and test Docker image locally
set -euo pipefail

docker build -t cicd-app:latest .
docker run -d --name cicd-test -p 5001:5000 -e ENVIRONMENT=test cicd-app:latest

echo "Waiting for app to start..."
sleep 2

curl -s http://localhost:5001/health
echo ""
curl -s http://localhost:5001/version
echo ""
curl -s http://localhost:5001/greet/World
echo ""

docker stop cicd-test
docker rm cicd-test
echo "✅ Local test passed"
```
