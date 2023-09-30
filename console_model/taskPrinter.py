from console_model import config

from database_model import dataBase


from typing import Any


def printTask(task: Any) -> str:
    taskType: str = task.getType()
    if taskType == "todo":
        symbol: str = task.getSymbol()
        done: bool = task.getDoneCondition()
        taskTitle: str = task.getTitle()
        doneSymbol: str = config.markedSymbol if done else config.space
        return "  [{}][{}] {} {}".format(symbol, doneSymbol, taskType, taskTitle)

    elif taskType == "deadline":
        symbol: str = task.getSymbol()
        done: bool = task.getDoneCondition()
        taskType: str = task.getType()
        taskTitle: str = task.getTitle()
        doneSymbol: str = config.markedSymbol if done else config.space
        dueTime: str = f"(by: {task.getDueTime()})"
        return "  [{}][{}] {} {} {}".format(symbol, doneSymbol, taskType, taskTitle, dueTime)

    else:
        symbol: str = task.getSymbol()
        done: bool = task.getDoneCondition()
        taskType: str = task.getType()
        taskTitle: str = task.getTitle()
        doneSymbol: str = config.markedSymbol if done else config.space
        startTime: str = task.getStartTime()
        endTIme: str = task.getEndTime()
        plan: str = f"(from: {startTime} to: {endTIme})"
        return "  [{}][{}] {} {} {}".format(symbol, doneSymbol, taskType, taskTitle, plan)


def dataBasePrinter(db: dataBase.DB) -> str:
    return f"Now you have {db.getCount()} tasks in the list."


def printingDottedLine() -> None:
    print(config.dottedLine)


def spaceDottedSpace() -> None:
    print(config.space)
    print(config.dottedLine)
    print(config.space)


def unknowCommand() -> None:
    print(config.unknownCommandMessage)
