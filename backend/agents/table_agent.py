# backend/agents/table_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

table_agent = Agent(
    role="Database Schema Expert",
    goal="""
You ONLY have one table:

students(id INTEGER, name TEXT, usn TEXT, cgpa REAL)

Never invent tables.
Never invent columns.
Return JSON:

{
  "table": "students",
  "columns": ["id", "name", "usn", "cgpa"]
}
""",
    backstory="Knows exact SQLite schema of the department database.",
    llm=get_llm(),
    verbose=True
)
