from llm_instance import LLMInstance


class IntentAgent:
def __init__(self):
self.llm = LLMInstance()


def detect_intent(self, query):
prompt = f"Identify intent of this academic query: {query}"
return self.llm.generate(prompt)
