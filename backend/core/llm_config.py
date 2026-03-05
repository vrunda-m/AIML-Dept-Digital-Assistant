# backend/core/llm_config.py

import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

_LLM_INSTANCE = None


def get_llm():
    global _LLM_INSTANCE

    if _LLM_INSTANCE is not None:
        return _LLM_INSTANCE

    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")

    if not model:
        raise ValueError("LLM_MODEL missing in .env")

    print(f"[DEBUG] Using model → {model}")

    _LLM_INSTANCE = LLM(
        model=model,
        base_url=base_url,
        api_key=api_key,
        temperature=0
    )

    return _LLM_INSTANCE