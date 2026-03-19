import time
from typing import Any, Dict

import streamlit as st


def get_settings() -> Dict[str, str]:
    api_key = st.secrets.get("GEMINI_API_KEY", "").strip()
    model = st.secrets.get("GEMINI_MODEL", "").strip() or "gemini-2.5-flash"

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing in .streamlit/secrets.toml")

    return {
        "gemini_api_key": api_key,
        "gemini_model": model,
    }


def is_retryable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    retry_terms = [
        "rate limit",
        "rate-limited",
        "rate_limited",
        "429",
        "resource exhausted",
        "temporarily unavailable",
        "internal error",
        "service unavailable",
        "timeout",
    ]
    return any(term in msg for term in retry_terms)


def generate_with_retry(client: Any, model_name: str, prompt: str, max_retries: int = 3) -> str:
    delay = 2.0
    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            text = getattr(response, "text", None)
            if not text:
                raise ValueError("Model returned an empty response.")
            return text.strip()

        except Exception as exc:
            last_error = exc
            if attempt == max_retries - 1 or not is_retryable_error(exc):
                break
            time.sleep(delay)
            delay *= 2

    raise RuntimeError(f"Gemini request failed after retries: {last_error}")