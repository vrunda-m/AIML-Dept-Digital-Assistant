from ..llm_instance import LLMInstance

class IntentAgent:
    def __init__(self):
        self.llm = LLMInstance.get_instance()

    def detect_intent(self, query: str):
        if "timetable" in query.lower():
            return "timetable_query"
        elif "result" in query.lower() or "marks" in query.lower():
            return "result_query"
        else:
            return "general_query"
