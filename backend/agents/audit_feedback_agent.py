# backend/agents/audit_feedback_agent.py

from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.audit_tools import log_event

audit_agent = Agent(
    role="Audit Logger",
    goal="""
Log the interaction using log_event tool.
Return JSON:
{
  "logged": true
}
""",
    backstory="Responsible for system logging and audit tracking.",
    llm=get_llm(),
    tools=[log_event],
    verbose=True
)
