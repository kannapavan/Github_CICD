# Layer 2: Architecture Layers — Architect 2 (Pragmatic Simplicity)

## 1. Application Architecture

Minimal — Flask app as a single module with a few routes. No services layer needed for a simple demo.

```
app.py          ← Routes + logic together
config.py       ← Settings
tests/          ← Test files
```

One file to read, one file to change. Zero over-engineering.

## 2. Repository Structure
```
cicd-pipeline-demo/
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
├── app/
│   ├── __init__.py
│   └── app.py                  # Single file app
├── tests/
│   ├── conftest.py
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
└── README.md
```

## 3. Pipeline Architecture

One push-based flow with manual deploy steps:
```
Push → [CI] Lint + Test → Build Docker → Push to Registry
                                            ↓
                              workflow_dispatch to deploy
                              (choose environment)
```

## 4. Environment Architecture

Same binary deployed to all — only config changes:
```
Dev (docker-compose up)  →  Test (via CI)  →  Staging (manual)  →  Prod (manual)
    Port 5000                 Port 5001          Port 5002              Port 5000
    Hot reload                Latest tag         Release tag            Release tag
```
