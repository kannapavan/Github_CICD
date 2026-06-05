# Merged Architecture — Layer 2

## Final Architecture Decisions

### Application Structure
A1's clean separation (routes/services/config) provides better learning value for real-world practices. A2's single-file approach is simpler but less instructive.

**Decision:** Middle ground — separate `routes.py` for endpoints but keep a simple `app.py` as the entry point.

### Repository Structure (Final)
```
Github_CICD/
├── .github/workflows/
│   ├── ci.yml                    # CI: lint, test, build
│   └── cd.yml                    # CD: deploy to envs
├── app/
│   ├── __init__.py               # Flask app factory
│   ├── routes.py                 # API endpoints
│   └── config.py                 # Configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # Shared fixtures
│   └── test_routes.py            # Route tests
├── scripts/
│   ├── deploy.sh                 # Deployment script
│   └── test_docker_local.sh      # Local Docker test
├── Dockerfile                    # Multi-stage build
├── docker-compose.yml            # Local dev + environment sim
├── requirements.txt
├── Makefile                      # Common commands
├── .gitignore
└── README.md
```

### Pipeline Flow (Final)
```
 Developer Push/PR
       │
       ▼
   ┌────── CI ──────┐
   │ 1. Run ruff     │
   │ 2. Run pytest   │
   │ 3. Build Docker │
   └──────┬─────────┘
          │ (on main / tag)
          ▼
   ┌── CD: Deploy ──┐
   │ → Test env     │ ← Auto on push to main
   │ → Staging env  │ ← Manual approval gate
   │ → Production   │ ← Manual approval gate
   └────────────────┘
```

### Environment Ports
- **Test**: `localhost:5001` — auto-deployed
- **Staging**: `localhost:5002` — manual gate
- **Production**: `localhost:5000` — manual gate
