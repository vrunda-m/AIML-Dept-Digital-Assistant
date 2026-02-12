from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.db_tools import run_sql
from backend.tools.rag_tools import rag_query

retriever_agent = Agent(
    role="Retriever",
    goal="Execute validated SQL and perform document retrieval via RAG.",
    backstory="Bridges structured SQL with unstructured department docs.",
    llm=get_llm(),
    tools=[run_sql, rag_query],
    memory=False,
    verbose=True
)
