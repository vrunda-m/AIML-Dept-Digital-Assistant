from ..llm_instance import LLMInstance

class QueryGeneratorAgent:
    def __init__(self):
        self.llm = LLMInstance.get_instance()

    def generate_sql(self, intent, query):
        if intent == "result_query":
            return "SELECT * FROM marks WHERE student_id = ?"
        elif intent == "timetable_query":
            return "SELECT * FROM timetable WHERE semester = ?"
        else:
            return None
