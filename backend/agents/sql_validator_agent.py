class SQLValidatorAgent:
    def validate(self, sql):
        blacklist = ["DROP", "DELETE", "ALTER"]
        if any(word in sql.upper() for word in blacklist):
            return False, "Unsafe SQL detected"
        return True, "Query validated"
