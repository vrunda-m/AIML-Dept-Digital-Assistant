# backend/agents/sql_validator_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm

sql_validator_agent = Agent(
    role="SQL Validator",
    goal="Check if the SQL query is safe (SELECT-only, no DROP/INSERT/DELETE) and valid for the given schema. Return JSON: {ok: bool, reason: str, sql: str}.",
    backstory="Protects the database from unsafe or malformed SQL queries.",
    llm=get_llm(),
    memory=False,
    verbose=True
)
