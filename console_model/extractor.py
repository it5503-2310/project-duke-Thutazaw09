from console_model import config


def textSeparater(command: str) -> list[str]:
    return command.split(config.space)


def extractCommandType(lst: list[str]) -> str:
    return lst[0]


def extractCommandTitle(lst: list[str]) -> str:
    return lst[1] + " " + lst[2]


def extractDeadLine(lst: list[str]) -> str:
    return lst[4]


def extractStartTimeForPlan(lst: list[str]) -> str:
    return lst[4] + " " + lst[5]


def extractEndTimeForPlan(lst: list[str]) -> str:
    return lst[7]


def extractTargetIdOfTask(lst: list[str]) -> int:
    return int(lst[1]) - 1


def extractKeyWordOfTask(lst: list[str]) -> str:
    return lst[1]


def extractItem(lst: list[str]) -> str:
    return lst[1]
