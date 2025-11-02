from llm_instance import LLMInstance

class SynthesisAgent:
    def __init__(self):
        self.llm = LLMInstance()

    def format_response(self, data):
        prompt = f"Generate a readable result summary:\n{data}"
        return self.llm.generate(prompt)
