# backend/agents/retriever_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.db_tools import run_sql
from backend.tools.rag_tools import rag_query

retriever_agent = Agent(
    role="Retriever",
    goal="Execute validated SQL queries via run_sql and optionally perform RAG lookups for unstructured academic documents.",
    backstory="Bridges structured (SQL) and unstructured (vector DB) data for the department assistant.",
    llm=get_llm(),
    tools=[run_sql, rag_query],
    memory=False,
    verbose=True
)
