# backend/agents/intent_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

intent_agent = Agent(
    role="Intent Classifier",
    goal="""
You are an academic department assistant.

Classify the user query into ONE of the following intents:

1. student_cgpa_lookup
2. student_search
3. department_info
4. magazine_query

Rules:
- If query contains a USN and asks for CGPA → student_cgpa_lookup
- If query asks about department info → department_info
- If query asks about magazine or achievements → magazine_query
- Never invent new intents.
- Output STRICT JSON only:
{
  "intent": "<intent_name>",
  "entities": {
      "usn": "...",
      "name": "..."
  }
}
""",
    backstory="Specialist in understanding structured academic queries.",
    llm=get_llm(),
    verbose=True
)
