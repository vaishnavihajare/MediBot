"""Configuration management for MediBot.

Supports Google Gemini (free tier, recommended) and Groq. Secrets come from the .env file,
never from the source code.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file if present (local runs). In Docker/Kubernetes, variables are injected instead.
load_dotenv(BASE_DIR / ".env", override=True)

GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "").strip()

# Provider: "google" or "groq" (defaults to google when a Gemini key exists)
default_provider = "google" if GEMINI_API_KEY else "groq"
MODEL_PROVIDER: str = os.getenv("MODEL_PROVIDER", default_provider).strip().lower()

GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-3.6-flash").strip()
GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()

HOST: str = os.getenv("HOST", "127.0.0.1").strip()
PORT: int = int(os.getenv("PORT", "8000").strip())
REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "90").strip())

APP_NAME: str = "MediBot — Multi-Agent Healthcare Assistant"

MEDICAL_DISCLAIMER: str = (
    "Disclaimer: MediBot provides general educational health information only. It is not a doctor, "
    "does not diagnose conditions or prescribe treatment, and does not replace professional medical advice. "
    "Consult a qualified doctor for your own health concerns. In an emergency call 112 immediately."
)

_DUMMY_KEYS = {"", "your_groq_api_key_here", "your_gemini_api_key_here", "placeholder"}


def is_provider_configured() -> bool:
    """True if the active provider has a real-looking API key."""
    if MODEL_PROVIDER == "google":
        return GEMINI_API_KEY not in _DUMMY_KEYS
    return GROQ_API_KEY not in _DUMMY_KEYS


def is_groq_configured() -> bool:
    """Backward-compatible name used by the /health endpoint."""
    return is_provider_configured()


def get_active_model_name() -> str:
    if MODEL_PROVIDER == "google":
        return f"Google ({GEMINI_MODEL})"
    return f"Groq ({GROQ_MODEL})"
