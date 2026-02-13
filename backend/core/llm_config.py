# backend/core/llm_config.py

import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------------
# SINGLETON LLM INSTANCE
# --------------------------------------------------------
_LLM_INSTANCE = None


def get_llm():
    """
    Returns ONE shared LLM instance for all agents.
    Works with:
    - OpenAI API (gpt-4o-mini)
    - Ollama (tinyllama, phi3:mini)
    Deterministic output via temperature=0.
    """

    global _LLM_INSTANCE

    if _LLM_INSTANCE is not None:
        return _LLM_INSTANCE

    # -------------------------------------------
    # Optional dummy mode (for testing)
    # -------------------------------------------
    USE_DUMMY = os.getenv("USE_DUMMY_LLM", "0") == "1"
    if USE_DUMMY:
        class DummyLLM:
            def generate(self, prompt, **kwargs):
                return {"text": "DUMMY OUTPUT — LLM disabled."}

        print("[DEBUG] Using Dummy LLM")
        _LLM_INSTANCE = DummyLLM()
        return _LLM_INSTANCE

    # -------------------------------------------
    # Real LLM (OpenAI or Ollama)
    # -------------------------------------------
    from crewai import LLM

    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")

    if not model or not base_url or not api_key:
        raise ValueError("LLM configuration missing in .env file.")

    print(f"[DEBUG] Creating SINGLE shared LLM instance → {model}")

    _LLM_INSTANCE = LLM(
        model=model,
        base_url=base_url,
        api_key=api_key,
        temperature=0  # deterministic behavior
    )

    return _LLM_INSTANCE
