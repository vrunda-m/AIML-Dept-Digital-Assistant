# backend/agents/intent_agent.py

def get_intent(query: str):
    query = query.lower()

    if "student" in query or "usn" in query or "batch" in query:
        return "students"

    elif "mark" in query or "score" in query:
        return "marks"

    elif "subject" in query or "semester" in query:
        return "subjects"

    else:
        return "unknown"
