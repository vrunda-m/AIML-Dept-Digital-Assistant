from llm_instance import get_llm

class RetrieverAgent:
    def __init__(self):
        self.llm = get_llm()

    def get_context(self, intent: str) -> str:
        mapping = {
            "Result": "Context: semester marks and grading scale.",
            "Timetable": "Context: weekly class schedule.",
            "Placements": "Context: placement records for department.",
            "Internships": "Context: internship records and details.",
            "Projects": "Context: student project information.",
            "Publications": "Context: student or faculty publication data.",
            "Faculty": "Context: faculty list and designations.",
        }
        return mapping.get(intent, "Context: general academic information.")



















