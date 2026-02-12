from crewai import Agent
from backend.core.llm_config import get_llm
from backend.tools.audit_tools import log_event

audit_agent = Agent(
    role="Audit & Feedback Agent",
    goal="Log queries, intents, SQL, and final outcomes for QA and improvement.",
    backstory="Ensures transparency and telemetry.",
    llm=get_llm(),
    tools=[log_event],
    memory=False,
    verbose=True
)
