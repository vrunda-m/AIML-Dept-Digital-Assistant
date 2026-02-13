# backend/agents/intent_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm


intent_agent = Agent(
    role="Intent Classifier",
    goal="You ONLY have one table named 'students' with columns: id, name, usn, cgpa. You never invent other tables.",
    backstory="You are the department's query router. You decide which downstream agents need to handle the request.",
    llm=get_llm(),
    memory=True,
    allow_delegation=False,
    verbose=True
)
