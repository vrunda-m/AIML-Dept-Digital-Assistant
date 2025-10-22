# BACKEND/llm_instance.py
"""
Shared singleton LLM instance for all agents.
In Phase-1, this is a dummy generator. Replace with real API later.
"""

class DummyLLM:
    def __init__(self):
        self.name = "DummyLLM-Phase1"

    def generate(self, prompt: str, **kwargs) -> str:
        return f"[{self.name}] Generated response for prompt: {prompt}"

_llm_instance = None

def get_llm():
    """Returns a single shared LLM instance."""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = DummyLLM()
    return _llm_instance





















