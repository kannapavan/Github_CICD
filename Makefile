.PHONY: install lint test run clean

install:
	uv venv .venv && uv pip install -r requirements.txt

lint:
	.venv/bin/ruff check app/ tests/

test:
	.venv/bin/pytest tests/ -v

run:
	.venv/bin/flask --app app run --host=0.0.0.0 --port=5000 --reload

clean:
	rm -rf __pycache__ .pytest_cache .venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
