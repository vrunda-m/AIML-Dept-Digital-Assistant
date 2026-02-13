# backend/tools/audit_tools.py

from pathlib import Path
import json
import time
from backend.tools.tool_shim import tool

# Root-level data/audit directory
BASE_DIR = Path(__file__).resolve().parents[2]
AUDIT_DIR = BASE_DIR / "data" / "audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = AUDIT_DIR / "events.jsonl"

@tool("log_event")
def log_event(event_json: str) -> str:
    """
    Append a JSON line to audit log.
    Accepts a JSON string. If invalid JSON, stores as plain message.
    """
    try:
        data = json.loads(event_json)
    except Exception:
        data = {"message": event_json}

    data["ts"] = time.time()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

    return "LOGGED"
