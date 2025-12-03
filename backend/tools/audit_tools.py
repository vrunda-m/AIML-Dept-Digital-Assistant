# backend/tools/audit_tools.py
from tools.tool_shim import tool
import time, json, os

os.makedirs("./backend/data/audit", exist_ok=True)
LOG_FILE = "./backend/data/audit/events.jsonl"

@tool("log_event")
def log_event(event_json: str) -> str:
    """
    Append a JSON line to audit log. Accepts JSON string.
    """
    try:
        data = json.loads(event_json)
    except Exception:
        data = {"message": event_json}
    data["ts"] = time.time()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
    return "LOGGED"
