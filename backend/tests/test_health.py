from fastapi.testclient import TestClient

from app import main
from app.main import app

client = TestClient(app)


def test_health_db_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "ok"}


def test_health_db_down(monkeypatch):
    monkeypatch.setattr(main, "check_db", lambda: False)

    response = client.get("/health")

    assert response.status_code == 503
    assert response.json() == {"status": "unhealthy", "db": "error"}
