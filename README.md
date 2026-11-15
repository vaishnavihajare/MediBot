# MediBot — Multi-Agent Healthcare Assistant

FastAPI + Agno (3 collaborating agents, `TeamMode.coordinate`) + Gemini/Groq, with a clinical-style web UI.
Assignment deliverables included: **Dockerfile, docker-compose.yml, Kubernetes manifests, CI/CD pipeline, tests.**

> Educational project. MediBot gives general health information only. It is not a doctor and does not diagnose or prescribe.

## Architecture
```
User question -> Agno Team ( 1. Query Analyzer -> 2. Research Agent (search_library tool)
                             -> 3. Answer Reviewer ) -> Final answer + sources + disclaimer
```

## Project layout
```
MediBot/
├── app/
│   ├── main.py            # FastAPI: GET /, POST /ask, GET /health
│   ├── config.py          # reads .env (API keys)
│   ├── schemas.py         # request/response models
│   ├── agents/team.py     # the three agents + Team
│   ├── agents/tools.py    # search_library tool
│   ├── data/sample_documents.py   # healthcare knowledge library
│   └── static/            # index.html, style.css, app.js (the website)
├── tests/                 # 12 pytest tests
├── k8s/                   # Kubernetes manifests
├── .github/workflows/ci.yml
├── Dockerfile, docker-compose.yml
├── requirements.txt, requirements-dev.txt
└── .env.example
```

## Step 0 — get a free API key (2 minutes)
1. Open https://aistudio.google.com/apikey, sign in with Google, click **Create API key**, copy it.
2. In this folder, copy `.env.example` to a new file named `.env`
   - Windows PowerShell: `copy .env.example .env`   |   Mac/Linux: `cp .env.example .env`
3. Open `.env` in Notepad, replace `your_gemini_api_key_here` with your key, save.

## Option A — Run with Python
Install Python 3.11+ (https://www.python.org/downloads/, tick **Add Python to PATH** on Windows). In a terminal inside this folder:

Windows (PowerShell)
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
Mac / Linux
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
Open http://127.0.0.1:8000. Stop with `Ctrl + C`.

## Option B — Run with Docker
1. Install and start **Docker Desktop**.
2. `docker compose up --build`
3. Open http://localhost:8000. Stop: `Ctrl + C`, then `docker compose down`.

Handy: `docker compose ps` (should say *healthy*), `docker compose logs -f`, `docker images`.

## Tests
```
pip install -r requirements-dev.txt
pytest -v
```

## Kubernetes (local with minikube)
```
minikube start
docker build -t medibot:latest .
minikube image load medibot:latest
# put your key in k8s/secret.yaml first
kubectl apply -f k8s/
kubectl get pods
minikube service medibot --url
```

## CI/CD
`.github/workflows/ci.yml` runs tests on every push, builds the image, and pushes it to GitHub Container Registry on `main`.
Create a GitHub repo, push this folder (`.env` is git-ignored), then open the **Actions** tab.

## API
`GET /` UI · `GET /health` · `POST /ask` with `{"question": "..."}` · `GET /docs` (Swagger)
