# Deep Dive: CD Workflow (.github/workflows/cd.yml)

```yaml
name: CD Pipeline

on:
  push:
    branches: [ main ]
  workflow_dispatch:
    inputs:
      environment:
        description: "Target environment"
        type: choice
        options: [test, staging, production]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    outputs:
      image: ${{ steps.push.outputs.image }}
    
    steps:
      - uses: actions/checkout@v4
      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        id: push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest

  deploy-test:
    needs: build-and-push
    environment: test
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Deploying ${{ needs.build-and-push.outputs.image }} to Test"
          echo "docker run -d -p 5001:5000 ..."

  deploy-staging:
    needs: deploy-test
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Deploying to Staging"
          echo "docker run -d -p 5002:5000 ..."

  deploy-production:
    needs: deploy-staging
    environment: production
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Deploying to Production"
          echo "docker run -d -p 5000:5000 ..."
```

Key notes:
- `environment:` creates manual approval gates in GitHub
- `needs:` creates deployment pipeline chain
- Build once, promote across environments
- Uses `GITHUB_TOKEN` for registry auth (auto-injected)
