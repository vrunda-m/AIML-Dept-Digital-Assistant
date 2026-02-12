# backend/core/crew_router.py
from crewai import Crew, Process, Task
from backend.agents.intent_agent import intent_agent
from backend.agents.table_agent import table_agent
from backend.agents.query_generator_agent import query_gen_agent
from backend.agents.sql_validator_agent import sql_validator_agent
from backend.agents.retriever_agent import retriever_agent
from backend.agents.synthesis_agent import synthesis_agent
from backend.agents.audit_feedback_agent import audit_agent


def build_pipeline_tasks():
    """
    Build an explicit sequential task list: each Task is assigned to one agent.
    Crew in Process.sequential will run these in order.
    """
    tasks = []

    tasks.append(
        Task(
            description="Intent classification: determine intent and extract entities from the user query.",
            expected_output="{'intent': <str>, 'entities': {...}}",
            agent=intent_agent
        )
    )

    tasks.append(
        Task(
            description="Schema/table agent: expose DB schema or confirm which tables to query.",
            expected_output="{'tables': [...], 'schema_hint': '...'}",
            agent=table_agent
        )
    )

    tasks.append(
        Task(
            description="Query generator: translate intent+entities into a SQL query or DB action.",
            expected_output="{'sql': 'SELECT ...'}",
            agent=query_gen_agent
        )
    )

    tasks.append(
        Task(
            description="SQL validator: verify SQL safety and correctness.",
            expected_output="{'sql_valid': True, 'safe_sql': '...'}",
            agent=sql_validator_agent
        )
    )

    tasks.append(
        Task(
            description="Retriever: run the validated SQL and/or perform RAG retrieval for documents.",
            expected_output="{'rows': [...], 'passages': [...]}",
            agent=retriever_agent
        )
    )

    tasks.append(
        Task(
            description="Synthesis: create the final human-readable response using structured + retrieved context.",
            expected_output="{'response_text': '...'}",
            agent=synthesis_agent
        )
    )

    tasks.append(
        Task(
            description="Audit & Feedback: log the full interaction and collect feedback if available.",
            expected_output="{'logged': True}",
            agent=audit_agent
        )
    )

    return tasks

def build_pipeline():
    """Build the full sequential multi-agent crew with explicit tasks."""
    tasks = build_pipeline_tasks()

    crew = Crew(
        agents=[
            intent_agent,
            table_agent,
            query_gen_agent,
            sql_validator_agent,
            retriever_agent,
            synthesis_agent,
            audit_agent
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    return crew

def run_pipeline(query: str):
    """
    Executes a single query through the crew.
    Provide the user's query as the kickoff input; each Task will see the inputs and previous outputs.
    """
    crew = build_pipeline()
    # kickoff expects a mapping of input variables; we pass the original query
    result = crew.kickoff(inputs={"query": query})
    return result
