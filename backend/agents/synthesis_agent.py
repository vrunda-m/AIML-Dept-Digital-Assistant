# backend/agents/synthesis_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm

synthesis_agent = Agent(
    role="Response Synthesizer",
    goal="Combine retriever output into a final, user-friendly message. For results: show courses and grades; for timetable: show slots; for others: summarize clearly in markdown.",
    backstory="Writes polished final answers for students and faculty.",
    llm=get_llm(),
    memory=True,
    verbose=True
)
