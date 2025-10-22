# llm_instance.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMInstance:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
            model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b-instruct", device_map="auto")
            cls._instance = super(LLMInstance, cls).__new__(cls)
            cls._instance.tokenizer = tokenizer
            cls._instance.model = model
        return cls._instance

    def generate(self, prompt, max_tokens=128):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
