from llm_instance import get_llm

class SQLValidatorAgent:
    def __init__(self):
        self.llm = get_llm()

    def validate(self, sql_query: str) -> str:
        u = sql_query.upper()
        if "DROP" in u or "DELETE" in u or "ALTER" in u:
            return "-- BLOCKED_UNSAFE_QUERY"
        if sql_query.strip() == "" or sql_query.startswith("--"):
            return "-- NO_VALID_SQL"
        return sql_query















