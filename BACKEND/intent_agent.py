from llm_instance import get_llm

class IntentAgent:
    def __init__(self):
        self.llm = get_llm()

    def identify_intent(self, query: str) -> str:
        q = query.lower()
        if "result" in q or "marks" in q:
            return "Result"
        if "timetable" in q or "schedule" in q or "class" in q:
            return "Timetable"
        if "placement" in q:
            return "Placements"
        if "internship" in q:
            return "Internships"
        if "project" in q:
            return "Projects"
        if "publication" in q:
            return "Publications"
        if "faculty" in q:
            return "Faculty"
        return "Unknown"

 
 
 
 
 

 
 
 
 
 
 




















