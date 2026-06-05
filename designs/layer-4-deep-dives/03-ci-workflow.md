# Deep Dive: CI Workflow (.github/workflows/ci.yml)

```yaml
name: CI Pipeline

on:
  push:
    branches: [ "**" ]     # All branches
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: ruff check app/ tests/

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t app-test --target builder .
      - run: echo "Build successful"
```

Key notes:
- Separate jobs for lint, test, build (parallel where possible)
- `needs` creates dependency chain
- Build step uses `--target builder` for fast validation
