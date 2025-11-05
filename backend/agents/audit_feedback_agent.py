# backend/agents/audit_feedback_agent.py
from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.audit_tools import log_event

audit_agent = Agent(
    role="Audit & Feedback Agent",
    goal="Record user queries, detected intent, executed SQL, and generated responses for transparency and feedback tracking.",
    backstory="Maintains logs for all interactions to improve future accuracy and accountability.",
    llm=get_llm(),
    tools=[log_event],
    memory=False,
    verbose=True
)
