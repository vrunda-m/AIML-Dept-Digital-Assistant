# backend/agents/query_generator_agent.py
from crewai import Agent
from core.llm_config import get_llm

query_gen_agent = Agent(
    role="Query Generator",
    goal="Convert natural language user requests into SQL SELECT statements, using schema context from the Table Agent and intent JSON from the Intent Agent.",
    backstory="Transforms natural language into SQL queries for structured data retrieval.",
    llm=get_llm(),
    memory=False,
    verbose=True
)
