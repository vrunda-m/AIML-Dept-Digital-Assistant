from llm_instance import get_llm

class TableAgent:
    def __init__(self):
        self.llm = get_llm()

    def execute(self, sql_query: str):
        q = sql_query.lower()

        # Results
        if "subject, marks" in q:
            return {"subject": ["AI", "DBMS", "Python"], "marks": [85, 90, 88]}

        # Timetable
        if "day, subject, time" in q:
            return [
                {"day": "Monday", "subject": "AI", "time": "10:00 AM - 11:00 AM"},
                {"day": "Tuesday", "subject": "DBMS", "time": "9:00 AM - 10:00 AM"},
                {"day": "Wednesday", "subject": "DAA", "time": "9:00 AM - 10:00 AM"},
                {"day": "Thursday", "subject": "ML", "time": "9:00 AM - 10:00 AM"},
                {"day": "Friday", "subject": "GEN AI", "time": "9:00 AM - 10:00 AM"}
                
            ]

        # Placements
        if "placements" in q:
            return [
                {"student_usn": "1DS22AI007", "company": "Infosys", "package": "6 LPA"},
                {"student_usn": "1DS22AI019", "company": "TCS", "package": "5 LPA"},
            ]

        # Internships
        if "internships" in q:
            return [
                {"student_usn": "1DS23AI400", "company": "Zoho", "domain": "ML Intern"},
                {"student_usn": "1DS23AI401", "company": "Google", "domain": "ML Intern"},
                {"student_usn": "1DS23AI402", "company": "Paypal", "domain": "CS Intern"},
                {"student_usn": "1DS23AI403", "company": "Zoho", "domain": "AI Intern"},
                {"student_usn": "1DS23AI405", "company": "Zoho", "domain": "ML Intern"}
            ]

        # Projects
        if "projects" in q:
            return [
                {"project_title": "AI Attendance Tracker", "guide": "Dr. Meena", "year": 2024},
            ]

        # Publications
        if "publications" in q:
            return [
                {"title": "AI in Education", "venue": "IEEE", "year": 2024},
                {"title": "AI in Military", "venue": "IEEE", "year": 2022},
                {"title": "AI in Aerospace", "venue": "IEEE", "year": 2022},
                {"title": "AI in Industries", "venue": "IEEE", "year": 2023},
                {"title": "AI in Farming", "venue": "IEEE", "year": 2024},
                {"title": "AI in  Civil", "venue": "IEEE", "year": 2024}
            ]

        # Faculty
        if "faculty" in q:
            return [
                {"name": "Dr. Vindhya P Malagi", "designation": "HOD", "department": "AI & ML"},
                {"name": "Prof. Kavya", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Ramya", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Reshma", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Aruna", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Anupama", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Deepshree", "designation": "Assistant Professor", "department": "AI & ML"},
                {"name": "Prof. Kusumika", "designation": "Assistant Professor", "department": "AI & ML"}
            ]

        return {}






















































