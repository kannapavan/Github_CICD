# Layer 3: Process Flow — Merged

## 1. Developer Workflow Flow
```
[Developer]                   [GitHub]                   [Docker Registry]
     │                           │                            │
     ├── git push feature/* ─────► PR created                  │
     │                           ├── CI triggers               │
     │                           │   ├── ruff lint             │
     │                           │   ├── pytest                │
     │                           │   └── Docker build          │
     │◄──────────────────────────┤   (status check)            │
     │                           │                            │
     ├── PR merged to main ─────► CI runs again               │
     │                           ├── Docker build & push ─────► ghcr.io
     │                           └── CD: Deploy to Test ─────► docker run test
     │                           │                            │
     │◄── Manual: Approve ──────► CD: Deploy to Staging ────► docker run staging
     │                           │                            │
     │◄── Manual: Approve ──────► CD: Deploy to Prod ───────► docker run prod
```

## 2. Application Data Flow
```
Client Request
     │
     ▼
Flask App (port varies by env)
     │
     ├── GET /health  ──► {"status": "ok"}
     ├── GET /version ──► {"version": "1.0.0", "environment": "production"}
     └── GET /greet/<name> ──► {"message": "Hello <name>!"}
```

## 3. CI Pipeline Flow (ci.yml)
```
Trigger: push or PR to any branch
   │
   ├── Step 1: Checkout code
   ├── Step 2: Setup Python 3.11
   ├── Step 3: Install dependencies
   ├── Step 4: Run ruff linting
   ├── Step 5: Run pytest
   ├── Step 6: Build Docker image (test build only)
   └── Step 7: (Optional) Upload test results
```

## 4. CD Pipeline Flow (cd.yml)
```
Trigger: push to main (or workflow_dispatch)
   │
   ├── Step 1: Checkout code
   ├── Step 2: Login to ghcr.io
   ├── Step 3: Build & push Docker image (tag: git-sha, latest)
   ├── Step 4: Deploy to Test
   │   └── docker run -d -p 5001:5000 ... (on local/simulated host)
   │
   ├── Gate: Manual approval required for Staging ⏸
   │   └── On approve → Deploy to Staging
   │       └── docker run -d -p 5002:5000 ...
   │
   └── Gate: Manual approval required for Production ⏸
       └── On approve → Deploy to Production
           └── docker run -d -p 5000:5000 ...
```

## 5. Version & Tag Strategy
```
git tag v1.0.0
  → Docker image: ghcr.io/username/app:v1.0.0
  → Docker image: ghcr.io/username/app:latest
```
