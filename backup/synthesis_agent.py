from typing import Any
from llm_instance import get_llm

class SynthesisAgent:
    def __init__(self):
        self.llm = get_llm()

    def create_response(self, data: Any, context: str) -> str:
        # 🎓 Results
        if isinstance(data, dict) and "marks" in data:
            subjects = data["subject"]
            marks = data["marks"]
            avg = sum(marks) / len(marks) if marks else 0
            lines = ["🎓 Semester Results\n"]
            for s, m in zip(subjects, marks):
                lines.append(f"• {s}: {m}")
            lines.append(f"\n📊 Average: {avg:.2f}")
            return "\n".join(lines)

        # 📅 Timetable
        if isinstance(data, list) and data and "day" in data[0]:
            lines = ["📅 Weekly Timetable\n"]
            for e in data:
                lines.append(f"{e['day']}: {e['subject']} ({e['time']})")
            return "\n".join(lines)

        # 🏢 Placements
        if isinstance(data, list) and data and "package" in data[0]:
            lines = ["🏢 Placements\n"]
            for e in data:
                lines.append(f"{e['student_usn']} → {e['company']} ({e['package']})")
            return "\n".join(lines)

        # 💼 Internships
        if isinstance(data, list) and data and "domain" in data[0]:
            lines = ["💼 Internships\n"]
            for e in data:
                lines.append(f"{e['student_usn']} → {e['company']} ({e['domain']})")
            return "\n".join(lines)

        # 📚 Projects / Publications / Faculty fallback
        if isinstance(data, list):
            lines = []
            for item in data:
                lines.append(" | ".join(f"{k}: {v}" for k, v in item.items()))
            return "\n".join(lines)

        # 🧠 Fallback
        prompt = f"Summarize: {context} - {data}"
        return self.llm.generate(prompt)

































