# backend/agents/retriever_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.db_tools import run_sql
from backend.tools.rag_tools import rag_query

retriever_agent = Agent(
    role="Data Retriever",
    goal="""
Execute SQL using run_sql tool.
If intent is magazine_query, use rag_query.

Return JSON:
{
  "rows": [...],
  "passages": [...]
}
""",
    backstory="Fetches structured and unstructured academic data.",
    llm=get_llm(),
    tools=[run_sql, rag_query],
    verbose=True
)
