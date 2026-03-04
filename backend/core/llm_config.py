# backend/core/llm_config.py

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

_MODEL = None
_TOKENIZER = None


class LocalHFLLM:
    def __init__(self, model_name="google/flan-t5-base"):
        global _MODEL, _TOKENIZER

        if _MODEL is None:
            print(f"[DEBUG] Loading HuggingFace model → {model_name}")
            _TOKENIZER = AutoTokenizer.from_pretrained(model_name)
            _MODEL = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        self.model = _MODEL
        self.tokenizer = _TOKENIZER

    def generate(self, prompt, **kwargs):
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.0
            )

        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"text": text}


_LLM_INSTANCE = None


def get_llm():
    global _LLM_INSTANCE

    if _LLM_INSTANCE is None:
        _LLM_INSTANCE = LocalHFLLM()

    return _LLM_INSTANCE