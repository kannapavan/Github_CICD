# Deep Dive: Flask Application

## File: app/__init__.py (App Factory)
```python
from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
```

## File: app/config.py
```python
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    VERSION = os.getenv("APP_VERSION", "0.1.0")
```

## File: app/routes.py
```python
from flask import Blueprint, jsonify
from app.config import Config

main_bp = Blueprint("main", __name__)

@main_bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@main_bp.route("/version")
def version():
    return jsonify({
        "version": Config.VERSION,
        "environment": Config.ENVIRONMENT
    })

@main_bp.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello {name}!"})
```

## File: tests/conftest.py
```python
import pytest
from app import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()
```

## File: tests/test_routes.py
```python
def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"

def test_version(client):
    resp = client.get("/version")
    assert resp.status_code == 200
    assert "version" in resp.json
    assert "environment" in resp.json

def test_greet(client):
    resp = client.get("/greet/World")
    assert resp.status_code == 200
    assert resp.json["message"] == "Hello World!"
```
