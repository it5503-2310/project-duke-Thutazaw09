from typing import Any
from task_model import task
from database_model import dataBase


def taskToDict(task: task.Task) -> Any:
    type: str = task.getType()
    title: str = task.getTitle()
    done: bool = task.getDoneCondition()
    id: int = task.getId()
    taskDict: Any
    taskDict = {
        "type": type,
        "title": title,
        "done": done,
        "id": id
    }
    return taskDict


def taskWithDueTimeToDict(task: task.TaskWithDueTime) -> Any:
    type: str = task.getType()
    title: str = task.getTitle()
    done: bool = task.getDoneCondition()
    dueTime: str = task.getDueTime()
    id: int = task.getId()
    taskDict: Any
    taskDict = {
        "type": type,
        "title": title,
        "done": done,
        "due_time": dueTime,
        "id": id
    }
    return taskDict


def taskWithPlanToDict(task: task.TaskWithPlan) -> Any:
    type: str = task.getType()
    title: str = task.getTitle()
    done: bool = task.getDoneCondition()
    startTime: str = task.getStartTime()
    endTime: str = task.getEndTime()
    id: int = task.getId()
    taskDict: Any
    taskDict = {
        "type": type,
        "title": title,
        "done": done,
        "start_time": startTime,
        "end_time": endTime,
        "id": id
    }
    return taskDict


def objToDict(obj: Any) -> Any:
    objType = obj.getType()
    if objType == "todo":
        return taskToDict(obj)

    elif objType == "deadline":
        return taskWithDueTimeToDict(obj)

    elif objType == "event":
        return taskWithPlanToDict(obj)


def makeDictsList(Storage: dataBase.DB) -> list[dict[str, Any]]:
    listOfObjs = Storage.getStorage()
    listOfDicts: list[Any] = []
    for obj in listOfObjs:
        listOfDicts.append(objToDict(obj))
    return listOfDicts
