# BACKEND/backend_test.py
"""
Simple test script to verify each agent can call the shared LLM and return dummy outputs.
Run from project root:
    python BACKEND/backend_test.py
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from intent_agent import IntentAgent
from query_generator_agent import QueryGeneratorAgent
from sql_validator_agent import SQLValidatorAgent
from table_agent import TableAgent
from retriever_agent import RetrieverAgent
from synthesis_agent import SynthesisAgent
from audit_feedback_agent import AuditFeedbackAgent

def test_example_queries():
    queries = [
        "Show my 3rd sem results",
        "Show my timetable",
        "Give me placements from batch 2020",
        "List internships",
        "Show student publications",
        "Show faculty list",
        "Show curriculum scheme & syllabus",
        "List hackathons",
    ]

    intent_agent = IntentAgent()
    query_gen = QueryGeneratorAgent()
    validator = SQLValidatorAgent()
    table = TableAgent()
    retriever = RetrieverAgent()
    synth = SynthesisAgent()
    audit = AuditFeedbackAgent()

    for q in queries:
        print("\n" + "="*60)
        print("QUERY:", q)
        intent = intent_agent.identify_intent(q)
        print("-> Intent:", intent)

        sql = query_gen.generate_sql(intent, q)
        print("-> SQL (templated):", sql)

        validated_sql = validator.validate(sql)
        print("-> Validated SQL:", validated_sql)

        data = table.execute(validated_sql)
        print("-> Data fetched:", data)

        context = retriever.get_context(intent)
        print("-> Context:", context)

        response = synth.create_response(data, context)
        print("\n---- Chatbot Response ----\n")
        print(response)

        audit.log_interaction(q, response)

if __name__ == "__main__":
    test_example_queries()
