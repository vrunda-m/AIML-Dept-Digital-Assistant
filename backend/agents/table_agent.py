from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.db_tools import run_sql  # ← wrapped by @tool

table_agent = Agent(
    role="Database Schema Expert",
    goal="Understand and expose DB structure and assist with schema context.",
    backstory="Knows tables, columns, and relationships.",
    llm=get_llm(),
    tools=[run_sql],   # ← pass the wrapped tool directly
    memory=True,
    verbose=True
)
