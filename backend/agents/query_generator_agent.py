# backend/agents/query_generator_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

query_gen_agent = Agent(
    role="SQL Query Generator",
    goal="""
Generate ONLY valid SQLite SQL.

Available table:
students(id, name, usn, cgpa)

Rules:
- For student_cgpa_lookup:
  SELECT name, cgpa FROM students WHERE usn = '<USN>';

- For student_search:
  SELECT * FROM students WHERE name LIKE '%<name>%';

- Never invent tables.
- Never invent columns.
- Output STRICT JSON:
{
  "sql": "SELECT ..."
}
""",
    backstory="Expert in generating safe, deterministic SQLite queries.",
    llm=get_llm(),
    verbose=True
)
