# Deep Dive: Makefile

```makefile
.PHONY: install lint test run docker-build docker-run docker-stop clean

install:
	pip install -r requirements.txt

lint:
	ruff check app/ tests/

test:
	pytest tests/ -v --cov=app

run:
	flask run --host=0.0.0.0 --port=5000 --reload

docker-build:
	docker build -t cicd-app:latest .

docker-run:
	docker run -d --name cicd-app -p 5000:5000 cicd-app:latest

docker-stop:
	docker stop cicd-app 2>/dev/null || true
	docker rm cicd-app 2>/dev/null || true

deploy:
	./scripts/deploy.sh $(env) $(tag)

clean:
	rm -rf __pycache__ .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
```
