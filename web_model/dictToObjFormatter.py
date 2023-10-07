from typing import Any
from task_model import task
from console_model import config


def dictToObj(data: dict[str, Any]) -> Any:
    taskType = data["type"]
    if taskType == "todo":
        tsk = task.Task()
        tsk.setId(data["id"])
        tsk.setSymbol(config.todoSymbol)
        tsk.setType(data["type"])
        tsk.setTitle(data["title"])
        return tsk

    elif taskType == "deadline":
        tsk = task.TaskWithDueTime()
        tsk.setId(data["id"])
        tsk.setSymbol(config.deadlineSymbol)
        tsk.setType(data["type"])
        tsk.setTitle(data["title"])
        tsk.setDueTime(data["due_time"])
        return tsk

    elif taskType == "event":
        tsk = task.TaskWithPlan()
        tsk.setId(data["id"])
        tsk.setSymbol(config.eventSymbol)
        tsk.setType(data["type"])
        tsk.setTitle(data["title"])
        tsk.setStartTime(data["start_time"])
        tsk.setEndTime(data["end_time"])
        return tsk
