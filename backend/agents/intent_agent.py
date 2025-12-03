# backend/agents/intent_agent.py
from crewai import Agent
from core.llm_config import get_llm

intent_agent = Agent(
    role="Intent Classifier",
    goal="Identify what the user is asking — {result, timetable, notice, faculty, unknown} — and extract any useful entities like USN, year, or semester. Output strict JSON.",
    backstory="You are the department's query router. You decide which downstream agents need to handle the request.",
    llm=get_llm(),
    memory=True,
    allow_delegation=False,
    verbose=True
)
