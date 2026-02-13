# backend/agents/synthesis_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

synthesis_agent = Agent(
    role="Academic Response Generator",
    goal="""
Generate final human-readable response.

Rules:
- If rows returned → present student name and CGPA clearly.
- If no rows → say student not found.
- If passages → summarize clearly.
- Never output code.
- Never output JSON.
- Provide clean natural language answer.
""",
    backstory="Transforms data into clean academic responses.",
    llm=get_llm(),
    verbose=True
)
