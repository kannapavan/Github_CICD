# Layer 1: Technical Stack — Architect 2 (Developer Experience & Pragmatism)

## 1. Language & Framework
- **Python 3.11+** — whatever is available, no strict version pinning
- **Flask** — dead simple, minimal learning curve, perfect for a sample app
  - Everyone knows Flask; less cognitive overhead
  - Fewer concepts to learn (no async, no Pydantic required)
  - Fast to prototype and iterate

## 2. Testing
- **pytest** — bare minimum, no plugins needed at first
- **pytest-flask** — lightweight Flask test helpers
- Simple `test_*.py` files, no coverage threshold initially

## 3. Code Quality
- **flake8** — one config, catches obvious issues
- No type checking (reduces complexity)
- No pre-commit hooks (keep it simple to start)

## 4. Containerization
- **Single-stage Dockerfile** — simple, debuggable
- **docker-compose** for local dev with volume mount (hot reload)
- Root user is fine for learning/development

## 5. CI/CD
- **GitHub Actions** — single workflow file
  - On push to main: run tests → build Docker → deploy to Test
  - Manual workflow_dispatch for Staging/Prod deployments

## 6. Environments
- **Branches as environments** — `test` branch, `staging` branch, `main` as prod
- **Simple shell scripts** for deployment instead of GitHub Environments UX
- **Manual triggers** via workflow_dispatch with `environment` input

## 7. Version Control
- **Trunk-based** — push directly to main, keep it simple
- **Git tags** for versions — `v1.0.0`, `v1.1.0`
- No branch protection to keep friction low

## 8. Artifacts
- **Docker Hub** — free, well-known, easy to understand
- Tag format: `username/app:latest`, `username/app:1.0.0`

## 9. Dependencies
- **requirements.txt** — plain list, no pip-tools
- Global install or venv, no strict pinning

## 10. Dev Tooling
- **Hot-reload** via Flask debug mode + volume mount
- **Simple print/logging** — no logging framework
- **README.md** with 3 commands to get running
