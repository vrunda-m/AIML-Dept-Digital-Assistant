# backend/agents/table_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.db_tools import run_sql

table_agent = Agent(
    role="Database Schema Expert",
    goal="Understand and expose the structure of the academic database (tables: students, courses, results, timetables). Provide schema summaries and help others craft valid SQL queries.",
    backstory="Knows every table, column, and relationship in the departmental database.",
    llm=get_llm(),
    tools=[run_sql],
    memory=True,
    verbose=True
)
