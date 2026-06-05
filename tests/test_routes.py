def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json == {"status": "ok"}

def test_version(client):
    resp = client.get("/version")
    assert resp.status_code == 200
    assert "version" in resp.json
    assert "environment" in resp.json

def test_greet(client):
    resp = client.get("/greet/World")
    assert resp.status_code == 200
    assert resp.json == {"message": "Hello World!"}

def test_greet_with_name(client):
    resp = client.get("/greet/Pavan")
    assert resp.status_code == 200
    assert resp.json == {"message": "Hello Pavan!"}
