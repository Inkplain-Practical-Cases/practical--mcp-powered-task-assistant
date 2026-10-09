# Beginner-friendly deterministic intent interpreter, not a hosted LLM.
# Important: ambiguous user requests are rejected; no unsupported actions run.
import re
from datetime import date, timedelta
from app.features.feature_assistant.schemas.action_plan import Action, ActionPlan

def service_interpret_request(message: str) -> ActionPlan:
    text = message.strip()
    lowered = text.lower()
    actions: list[Action] = []
    if "task" in lowered and any(word in lowered for word in ("create", "add")):
        # Capture only the task phrase; do not put calendar instructions in a title.
        match = re.search(r"(?:create|add)\s+(?:a\s+)?task\s+(?:to\s+)?(.+?)(?=\s+and\s+(?:show|list)\b|$)", text, re.I)
        if match is None:
            raise ValueError("Please specify a task title after 'create task'")
        title = re.sub(r"\b(today|tomorrow)\b", "", match.group(1), flags=re.I).strip(" .")
        if len(title) < 3:
            raise ValueError("Task title is too short")
        day = date.today() + timedelta(days=1 if "tomorrow" in lowered else 0)
        actions.append(Action(name="create_task", arguments={
            "title": title, "due_date": day.isoformat(), "priority": "normal"
        }))
    if any(word in lowered for word in ("meeting", "calendar", "events")) and any(
        word in lowered for word in ("show", "list", "upcoming")
    ):
        actions.append(Action(name="list_calendar_events", arguments={"limit": 3}))
    if not actions:
        raise ValueError("Request does not match supported task/calendar intentions")
    return ActionPlan(actions=actions)
