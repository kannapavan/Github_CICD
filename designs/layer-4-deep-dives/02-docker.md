# Deep Dive: Docker Configuration

## Dockerfile (Multi-stage)
```dockerfile
# Stage 1: Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dirs -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=app
ENV PYTHONUNBUFFERED=1

# Non-root user
RUN addgroup --system app && adduser --system --group app
USER app

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
```

## docker-compose.yml (Local Development)
```yaml
version: "3.8"
services:
  app-dev:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENVIRONMENT=development
      - APP_VERSION=0.1.0
    volumes:
      - .:/app          # Hot reload
    command: flask run --host=0.0.0.0 --reload
  
  app-test:
    build: .
    ports:
      - "5001:5000"
    environment:
      - ENVIRONMENT=test
      - APP_VERSION=latest
    command: gunicorn --bind 0.0.0.0:5000 "app:create_app()"

  app-staging:
    build: .
    ports:
      - "5002:5000"
    environment:
      - ENVIRONMENT=staging
      - APP_VERSION=latest
    command: gunicorn --bind 0.0.0.0:5000 "app:create_app()"

  app-prod:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENVIRONMENT=production
      - APP_VERSION=latest
    command: gunicorn --bind 0.0.0.0:5000 "app:create_app()"
```
