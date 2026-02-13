# backend/agents/synthesis_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

synthesis_agent = Agent(
    role="Academic Response Generator",
    goal="""
You generate the FINAL answer for the user.

Rules:
- If SQL returned rows, respond like this:

Student: <name>
CGPA: <cgpa>

- If no rows returned:
Student not found.

- Do NOT return JSON.
- Do NOT repeat instructions.
- Do NOT explain steps.
- Output only the final human-readable answer.
""",
    backstory="Transforms structured database results into final clean academic responses.",
    llm=get_llm(),
    verbose=True
)
