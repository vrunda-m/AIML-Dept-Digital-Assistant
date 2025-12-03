import datetime
from llm_instance import get_llm

class AuditFeedbackAgent:
    def __init__(self):
        self.llm = get_llm()
        self.logfile = "backend_audit.log"

    def log_interaction(self, query: str, response: str):
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        entry = f"{ts} | QUERY: {query} | RESPONSE: {response[:200]}\n"
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(entry)















