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
    Build explicit sequential task list.
    IMPORTANT:
    - Audit runs BEFORE synthesis
    - Synthesis is LAST so Crew returns human-readable answer
    """

    tasks = []

    # 1️⃣ Intent
    tasks.append(
        Task(
            description="Intent classification: determine intent and extract entities from the user query.",
            expected_output="{'intent': <str>, 'entities': {...}}",
            agent=intent_agent
        )
    )

    # 2️⃣ Schema
    tasks.append(
        Task(
            description="Schema/table agent: expose DB schema or confirm which tables to query.",
            expected_output="{'table': 'students', 'columns': [...]}",
            agent=table_agent
        )
    )

    # 3️⃣ SQL Generation
    tasks.append(
        Task(
            description="Query generator: translate intent+entities into a SQL query.",
            expected_output="{'sql': 'SELECT ...'}",
            agent=query_gen_agent
        )
    )

    # 4️⃣ SQL Validation
    tasks.append(
        Task(
            description="SQL validator: verify SQL safety and correctness.",
            expected_output="{'sql_valid': True, 'safe_sql': '...'}",
            agent=sql_validator_agent
        )
    )

    # 5️⃣ Retrieval
    tasks.append(
        Task(
            description="Retriever: execute SQL or perform RAG retrieval if needed.",
            expected_output="{'rows': [...], 'passages': [...]}",
            agent=retriever_agent
        )
    )

    # 6️⃣ Audit (moved BEFORE synthesis)
    tasks.append(
        Task(
            description="Audit & Feedback: log the interaction.",
            expected_output="{'logged': True}",
            agent=audit_agent
        )
    )

    # 7️⃣ Synthesis (FINAL TASK → returned to user)
    tasks.append(
    Task(
        description="Synthesis: produce final answer for the user.",
        agent=synthesis_agent
         )
    )


    return tasks


def build_pipeline():
    """
    Build sequential multi-agent crew.
    """

    tasks = build_pipeline_tasks()

    crew = Crew(
        agents=[
            intent_agent,
            table_agent,
            query_gen_agent,
            sql_validator_agent,
            retriever_agent,
            audit_agent,        # audit still included
            synthesis_agent     # synthesis last
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def run_pipeline(query: str):
    """
    Executes a single query through the crew.
    Returns final synthesis output.
    """

    crew = build_pipeline()

    result = crew.kickoff(inputs={"query": query})

    return result
