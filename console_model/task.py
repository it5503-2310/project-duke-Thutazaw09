class Task():

    __type: str
    __title: str
    __done: bool
    __symbol: str
    __id: int

    def __init__(self) -> None:
        self.__id = 0
        self.__type = ""
        self.__title = ""
        self.__done = False
        self.__symbol = ""

    # setter
    def setType(self, cmd: str) -> None:  # todo borwoo book
        self.__type = cmd

    def setTitle(self, act: str) -> None:
        self.__title = act

    def setSymbol(self, syb: str) -> None:
        self.__symbol = syb

    def markedTask(self) -> None:
        self.__done = True

    def unmarkedTask(self) -> None:
        self.__done = False

    def setId(self, id: int) -> None:
        self.__id = id

    # getter
    def getType(self) -> str:
        return self.__type

    def getTitle(self) -> str:
        return self.__title

    def getSymbol(self) -> str:
        return self.__symbol

    def getDoneCondition(self) -> bool:
        return self.__done

    def getId(self) -> int:
        return self.__id


class TaskWithDueTime(Task):
    __dueTime: str

    def __init__(self) -> None:
        super().__init__()
        self.__dueTime = ""

    # setter
    def setDueTime(self, dueTime: str) -> None:
        self.__dueTime = dueTime

    # getter
    def getDueTime(self) -> str:
        return self.__dueTime


class TaskWithPlan(Task):
    __startTime: str
    __endTime: str

    def __init__(self) -> None:
        super().__init__()
        self.__startTime = ""
        self.__endTime = ""

    # setter
    def setStartTime(self, startTime: str) -> None:
        self.__startTime = startTime

    def setEndTime(self, endTime: str) -> None:
        self.__endTime = endTime

    # getter
    def getStartTime(self) -> str:
        return self.__startTime

    def getEndTime(self) -> str:
        return self.__endTime
