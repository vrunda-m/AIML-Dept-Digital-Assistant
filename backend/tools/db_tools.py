# backend/tools/db_tools.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from tools.tool_shim import tool
import os

load_dotenv()
DB_URL = os.getenv("DB_URL", "sqlite:///./backend/academic.db")
engine = create_engine(DB_URL, echo=False)

@tool("run_sql")
def run_sql(sql: str) -> str:
    """
    Execute a SELECT-only SQL and return TSV (first line header).
    """
    s = sql.strip().lower()
    if not s.startswith("select"):
        return "[DB ERROR] Only SELECT queries are allowed."
    try:
        with engine.connect() as conn:
            res = conn.execute(text(sql))
            cols = list(res.keys())
            lines = ["\t".join(cols)]
            for row in res.fetchall():
                vals = ["" if v is None else str(v) for v in row]
                lines.append("\t".join(vals))
        return "\n".join(lines)
    except Exception as e:
        return f"[DB ERROR] {e}"
