from agentic_framework.tools.tool import BaseTool


class CurrentTimeTool(BaseTool):
    name = "current_time"
    description = "Returns the current time"
    args_schema = None  # No input is required

    def _run(self) -> dict:
        from datetime import datetime

        current_time = datetime.now().isoformat()
        return {"current_time": current_time}
