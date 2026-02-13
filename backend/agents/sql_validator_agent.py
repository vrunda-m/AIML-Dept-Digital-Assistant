# backend/agents/sql_validator_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm

sql_validator_agent = Agent(
    role="SQL Validator",
    goal="""
Validate SQL for safety.

Rules:
- Only SELECT statements allowed.
- No DROP, DELETE, UPDATE.
- Must reference students table only.
- Return JSON:

{
  "sql_valid": true,
  "safe_sql": "<query>"
}
""",
    backstory="Ensures SQL safety and correctness.",
    llm=get_llm(),
    verbose=True
)
