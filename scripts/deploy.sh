#!/bin/bash
set -euo pipefail

ENV=$1
TAG=${2:-latest}
IMAGE="ghcr.io/${GITHUB_REPOSITORY:-your-org/your-app}:${TAG}"

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
    echo "Usage: $0 {test|staging|production} [tag]"
    exit 1
    ;;
esac

echo "Deploying ${IMAGE} to ${ENV_NAME} on port ${PORT}"

docker stop "app-${ENV_NAME}" 2>/dev/null || true
docker rm "app-${ENV_NAME}" 2>/dev/null || true

docker run -d \
  --name "app-${ENV_NAME}" \
  -p "${PORT}:5000" \
  -e "ENVIRONMENT=${ENV_NAME}" \
  -e "APP_VERSION=${TAG}" \
  "${IMAGE}"

echo "Deployed to ${ENV_NAME} at http://localhost:${PORT}"
