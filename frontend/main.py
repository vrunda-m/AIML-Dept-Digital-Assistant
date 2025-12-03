import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BACKEND')))

from intent_agent import IntentAgent
from query_generator_agent import QueryGeneratorAgent
from sql_validator_agent import SQLValidatorAgent
from table_agent import TableAgent
from retriever_agent import RetrieverAgent
from synthesis_agent import SynthesisAgent
from audit_feedback_agent import AuditFeedbackAgent

def main():
    print("\n🎓 AIML Department Academic Chatbot — Phase 1")
    print("Ask your academic question below (e.g. 'Show my 3rd sem results', 'List internships', 'Show faculty list')\n")

    query = input("🔍 Your Query: ")

    intent_agent = IntentAgent()
    query_gen = QueryGeneratorAgent()
    validator = SQLValidatorAgent()
    table_agent = TableAgent()
    retriever = RetrieverAgent()
    synthesis = SynthesisAgent()
    audit = AuditFeedbackAgent()

    intent = intent_agent.identify_intent(query)
    sql = query_gen.generate_sql(intent, query)
    validated_sql = validator.validate(sql)
    data = table_agent.execute(validated_sql)
    context = retriever.get_context(intent)
    response = synthesis.create_response(data, context)

    print("\n" + "=" * 60)
    print("🤖 Chatbot Response:\n")
    print(response)
    print("=" * 60 + "\n")

    audit.log_interaction(query, response)

if __name__ == "__main__":
    main()







































