# backend/core/llm_config.py

import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------------
# SINGLETON LLM INSTANCE  (CRITICAL FOR LOW-RAM MACHINES)
# --------------------------------------------------------
_LLM_INSTANCE = None


def get_llm():
    """
    Returns ONE shared LLM instance for all agents.
    Prevents multiple model loads → stops out-of-memory errors.
    Deterministic output (temperature=0) for SQL reliability.
    """
    global _LLM_INSTANCE

    if _LLM_INSTANCE is not None:
        return _LLM_INSTANCE

    # -------------------------------------------
    # OPTIONAL: dummy mode for safe debugging
    # -------------------------------------------
    USE_DUMMY = os.getenv("USE_DUMMY_LLM", "0") == "1"
    if USE_DUMMY:
        class DummyLLM:
            def generate(self, prompt, **kwargs):
                return {"text": "DUMMY OUTPUT — LLM disabled for testing."}

        print("[DEBUG] Using Dummy LLM")
        _LLM_INSTANCE = DummyLLM()
        return _LLM_INSTANCE

    # -------------------------------------------
    # REAL LOCAL OLLAMA MODEL
    # -------------------------------------------
    from crewai import LLM

    model = os.getenv("LLM_MODEL", "tinyllama")
    base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
    api_key = os.getenv("LLM_API_KEY", "ollama")

    print(f"[DEBUG] Creating SINGLE shared LLM instance → {model}")

    _LLM_INSTANCE = LLM(
        model=model,
        base_url=base_url,
        api_key=api_key,
        temperature=0   # 🔒 Deterministic output
    )

    return _LLM_INSTANCE
