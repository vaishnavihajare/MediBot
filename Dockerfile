# ---------- MediBot image ----------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 1) Install dependencies first so Docker can cache this layer
COPY requirements.txt .
RUN pip install -r requirements.txt

# 2) Copy the application code
COPY app ./app

# 3) Run as a non-root user (good security practice)
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 8000

# Container is "healthy" only when /health answers (python is used because slim has no curl)
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=4).status==200 else 1)"

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
