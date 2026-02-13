# backend/agents/query_generator_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm

query_gen_agent = Agent(
    role="Query Generator",
    goal="Generate ONLY valid SQLite SQL queries using the 'students' table. Available columns: id, name, usn, cgpa.Do not invent tables. Do not invent columns.",
    backstory="Transforms natural language into SQL queries for structured data retrieval.",
    llm=get_llm(),
    memory=False,
    verbose=True
)
