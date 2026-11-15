from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint_reports_three_agents():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "healthy"
    assert body["agents"] == ["Query Analyzer", "Research Agent", "Answer Reviewer"]


def test_health_does_not_leak_keys():
    text = client.get("/health").text
    assert "gsk_" not in text and "AIza" not in text


def test_homepage_served():
    r = client.get("/")
    assert r.status_code == 200
    assert "MediBot" in r.text
