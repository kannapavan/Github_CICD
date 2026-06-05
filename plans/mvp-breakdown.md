# MVP Breakdown Plan

## Overview
4 MVPs, each building on the previous. Every MVP is independently testable.

## MVP 1: Core Application
**Goal:** Working Flask app with tests, runnable locally

**Files to create:**
- `app/__init__.py` — Flask app factory
- `app/routes.py` — API endpoints (/health, /version, /greet/<name>)
- `app/config.py` — Configuration from environment variables
- `tests/__init__.py` — Empty
- `tests/conftest.py` — pytest fixtures
- `tests/test_routes.py` — Route tests
- `requirements.txt` — Dependencies (flask, pytest, pytest-flask, ruff, gunicorn)
- `.gitignore` — Python standard
- `Makefile` — install, lint, test, run, clean targets

**Verification:** `make install && make lint && make test && make run`

---

## MVP 2: Docker & Local Dev Setup
**Goal:** Application runs in Docker; can simulate environments locally

**Files to create:**
- `Dockerfile` — Multi-stage build
- `docker-compose.yml` — All 4 services (dev, test, staging, prod)
- `scripts/deploy.sh` — Environment deployment script
- `scripts/test_docker_local.sh` — Local Docker smoke test

**Verification:** `docker-compose up app-dev` and hit endpoints

---

## MVP 3: CI/CD Pipeline (GitHub Actions)
**Goal:** Automated CI on push, CD with environment promotion + approval gates

**Files to create:**
- `.github/workflows/ci.yml` — Lint → Test → Build
- `.github/workflows/cd.yml` — Build & Push → Deploy Test → (gate) → Deploy Staging → (gate) → Deploy Production

**Verification:** Push to GitHub; watch Actions run; approve deployments

---

## MVP 4: Documentation & Polish
**Goal:** Complete README with instructions, architecture diagram, learning notes

**Files to create/modify:**
- `README.md` — Full project documentation
- `.gitignore` updates if needed
- Any final cleanup

**Verification:** README accurately describes how to run everything

## Dependencies
```
MVP 1 ← MVP 2 ← MVP 3 ← MVP 4
```
Each MVP depends on the previous one.
