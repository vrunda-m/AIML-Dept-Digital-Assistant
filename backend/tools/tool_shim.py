# backend/tools/tool_shim.py
from crewai.tools.base_tool import BaseTool

def tool(name=None, description=None):
    """
    Decorator that converts a normal Python function into a valid CrewAI BaseTool instance.
    Works for CrewAI 1.3.0 with Pydantic v2.
    """
    def decorator(fn):
        _name = name or fn.__name__
        _description = description or (fn.__doc__ or "")

        class DynamicTool(BaseTool):
            name: str = _name
            description: str = _description

            def _run(self, *args, **kwargs):
                return fn(*args, **kwargs)

        return DynamicTool()

    return decorator
