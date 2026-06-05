# Layer 1: Technical Stack — Architect 1 (Scalability & Clean Architecture)

## 1. Language & Framework
- **Python 3.12** — latest stable, better error messages, performance improvements
- **FastAPI** — async-first, auto OpenAPI docs, Pydantic validation, production-grade
  - Better scalability than Flask for future API growth
  - Built-in validation reduces boilerplate
  - Self-documenting via Swagger UI

## 2. Testing
- **pytest** 8.x — fixtures, parameterization, plugins
- **httpx** — async HTTP client for FastAPI test client
- **coverage** 7.x — threshold enforcement (80%+)
- **pytest-mock** — built-in mocking

## 3. Code Quality
- **ruff** — unified linter + formatter (replaces flake8 + isort + black)
- **mypy** — strict mode for type safety
- **pre-commit hooks** — gate quality before CI

## 4. Containerization
- **Multi-stage Docker build**:
  - Stage 1: Build/dependencies
  - Stage 2: Runtime (slim image)
- **docker-compose** for local dev + test orchestration
- **Non-root user** in container (security best practice)

## 5. CI/CD
- **GitHub Actions** — two workflow files:
  - `ci.yml`: On push/PR — lint, type-check, test, build Docker
  - `cd.yml`: On tag/release — build, push, deploy with environment gates

## 6. Environments
- **GitHub Environments** — `test`, `staging`, `production`
- **Manual approval** required between stages
- **Environment-specific variables** via GitHub secrets

## 7. Version Control
- **Feature branch workflow** — branches per feature, PRs to main
- **Semantic versioning** — `v{major}.{minor}.{patch}` tags
- **Protected main branch** — PR required, status checks pass

## 8. Artifacts
- **GitHub Container Registry (ghcr.io)** — tight GitHub integration, no extra login

## 9. Dependencies
- **pip + requirements.txt** — simple, universal, no extra tooling
- **Virtual environment** with `.venv` (gitignored)

## 10. Dev Tooling
- **Makefile** — `make lint`, `make test`, `make build`, `make run`
- **Logging** — structlog for structured logging
- **Health checks** — `/health` and `/ready` endpoints
