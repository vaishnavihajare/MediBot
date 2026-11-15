from fastapi.testclient import TestClient
from app import config
from app.main import app

client = TestClient(app)


def test_empty_question_rejected():
    assert client.post("/ask", json={"question": ""}).status_code == 422


def test_whitespace_question_rejected():
    assert client.post("/ask", json={"question": "      "}).status_code == 422


def test_short_question_rejected():
    assert client.post("/ask", json={"question": "hi"}).status_code == 422


def test_missing_api_key_returns_503(monkeypatch):
    monkeypatch.setattr(config, "GEMINI_API_KEY", "")
    monkeypatch.setattr(config, "GROQ_API_KEY", "")
    r = client.post("/ask", json={"question": "What helps a mild fever at home?"})
    assert r.status_code == 503
