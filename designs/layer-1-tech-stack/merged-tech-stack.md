# Merged Tech Stack — Layer 1

After reconciling both architect perspectives:

## Final Decisions

| Area | Choice | Rationale |
|------|--------|-----------|
| **Framework** | **Flask** | A1 wanted FastAPI, A2 wanted Flask. For a **learning exercise**, Flask wins — fewer concepts, wider familiarity, the focus is CI/CD not the web framework |
| **Python** | 3.11+ | No strict pin; use system Python |
| **Testing** | pytest + pytest-flask | Simple, effective |
| **Linting** | **ruff** | Compromise: A1 wanted ruff, A2 wanted flake8. Ruff is faster, modern, and replaces multiple tools (flake8 + isort + black). Best of both worlds |
| **Type Check** | **Skip for now** | Adds complexity without proportional learning value for CI/CD focus |
| **Docker** | **Multi-stage build** | A1's suggestion — teaches best practices without extra complexity |
| **Docker Compose** | Yes | For local dev with volume mount + hot reload |
| **CI/CD** | **2 workflows** (ci.yml + cd.yml) | A1's structure wins — separation of concerns mirrors real-world |
| **Environments** | **GitHub Environments** with manual approval gates | Teaches real GitHub feature |
| **Registry** | **GitHub Container Registry (ghcr.io)** | Tighter integration, no extra accounts |
| **Branching** | **Feature branches** with PRs to main | Real-world practice |
| **Dependencies** | requirements.txt | Simple, universal |
| **Dev Tooling** | Makefile + hot-reload | Compromise — both wanted this |

## Why These Choices
- **Learning-first**: Every choice prioritizes learning CI/CD concepts over production optimization
- **Real-world patterns**: Multi-stage builds, environment gates, PR workflows are industry standards
- **Minimal overhead**: Remove type checking, heavy lint configs — keep focus on the pipeline
