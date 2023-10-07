from typing import Any


def markTask(task: Any) -> None:
    task.markedTask()


def unmarkTask(task: Any) -> None:
    task.unmarkedTask()
