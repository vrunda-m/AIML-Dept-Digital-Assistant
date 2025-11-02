from llm_instance import get_llm

class QueryGeneratorAgent:
    def __init__(self):
        self.llm = get_llm()

    def generate_sql(self, intent: str, query: str) -> str:
        if intent == "Result":
            return "SELECT subject, marks FROM marks WHERE semester = 3;"
        if intent == "Timetable":
            return "SELECT day, subject, time FROM timetable WHERE semester = 3;"
        if intent == "Placements":
            return "SELECT student_usn, company, package FROM placements WHERE batch = 2020;"
        if intent == "Internships":
            return "SELECT student_usn, company, domain FROM internships;"
        if intent == "Projects":
            return "SELECT project_title, guide, year FROM projects;"
        if intent == "Publications":
            return "SELECT title, venue, year FROM publications;"
        if intent == "Faculty":
            return "SELECT name, designation, department FROM faculty;"
        return "-- NO_SQL_FOR_INTENT"

    def call_llm_for_sql(self, intent: str, query: str) -> str:
        prompt = f"Generate SQL for intent: {intent}, query: {query}"
        return self.llm.generate(prompt)



















