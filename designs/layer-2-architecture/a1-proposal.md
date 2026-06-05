# Layer 2: Architecture Layers — Architect 1 (Clean Architecture)

## 1. Application Architecture
```
┌─────────────────────────────┐
│         Flask App            │
│  ┌───────────────────────┐  │
│  │   Routes / Controllers │  │
│  │   - /health            │  │
│  │   - /version           │  │
│  │   - /greet/<name>      │  │
│  └───────────┬───────────┘  │
│              │               │
│  ┌───────────▼───────────┐  │
│  │     Services Layer     │  │  ← Business logic
│  └───────────┬───────────┘  │
│              │               │
│  ┌───────────▼───────────┐  │
│  │    Configuration       │  │  ← Settings, env vars
│  └───────────────────────┘  │
└─────────────────────────────┘
```

## 2. Repository Structure
```
cicd-pipeline-demo/
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI pipeline
│       └── cd.yml              # CD pipeline
├── app/
│   ├── __init__.py
│   ├── routes.py               # API endpoints
│   ├── services.py             # Business logic
│   └── config.py               # Configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # pytest fixtures
│   └── test_routes.py          # Route tests
├── Dockerfile                  # Multi-stage build
├── docker-compose.yml          # Local orchestration
├── requirements.txt            # Dependencies
├── Makefile                    # Command shortcuts
├── .github/CODEOWNERS          # Review assignments
└── README.md
```

## 3. Pipeline Architecture
```
Source Code → CI (lint, test, build) → CD (deploy test → staging → prod)
     ↑                                          ↓
  GitHub                                  Manual Approval
  Push/PR                                  Gates at each stage
```

## 4. Environment Architecture
```
test ──(approve)──> staging ──(approve)──> production
  │                      │                      │
  ├ Port 5001            ├ Port 5002            ├ Port 5000
  ├ Latest build         ├ Staged release       ├ Stable release
  └ Ephemeral data       └ Persistent data      └ Persistent data
```
