from console_model import config,extractor,task,taskPrinter
from database_model import dataBase


def TodoFunction() -> None:
    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        if len(lst) < 3:
            print(config.emptyDescriptionTodoMessage)
        else:
            print(config.taskAddedMessage)
            commandType = extractor.extractCommandType(lst)
            commandTitle = extractor.extractCommandTitle(lst)
            tsk = task.Task()
            tsk.setType(commandType)
            tsk.setTitle(commandTitle)
            tsk.setSymbol(config.todoSymbol)
            DataStorage.addItem(tsk)
            print(taskPrinter.printTask(tsk))
            print(taskPrinter.dataBasePrinter(DataStorage))

    return lambda x, y: helper(x, y)


def deadLineFunction() -> None:
    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        if len(lst) < 5:
            print(config.missingArgumentMessage)
        else:
            print(config.taskAddedMessage)
            commandType = extractor.extractCommandType(lst)
            commandTitle = extractor.extractCommandTitle(lst)
            dueTime = extractor.extractDeadLine(lst)

            tsk = task.TaskWithDueTime()
            tsk.setType(commandType)
            tsk.setTitle(commandTitle)
            tsk.setSymbol(config.deadlineSymbol)
            tsk.setDueTime(dueTime)

            DataStorage.addItem(tsk)
            print(taskPrinter.printTask(tsk))
            print(taskPrinter.dataBasePrinter(DataStorage))

    return lambda x, y: helper(x, y)


def eventFunction() -> None:
    def helper(DataStorage:dataBase.DB, lst: list[str]) -> None:
        if len(lst) < 8:
            print(config.missingArgumentMessage)

        else:
            print(config.taskAddedMessage)
            commandType = extractor.extractCommandType(lst)
            commandTitle = extractor.extractCommandTitle(lst)
            startTime = extractor.extractStartTimeForPlan(lst)
            endTime = extractor.extractEndTimeForPlan(lst)

            tsk = task.TaskWithPlan()
            tsk.setType(commandType)
            tsk.setTitle(commandTitle)
            tsk.setSymbol(config.eventSymbol)
            tsk.setStartTime(startTime)
            tsk.setEndTime(endTime)

            DataStorage.addItem(task)
            print(taskPrinter.printTask(tsk))
            print(taskPrinter.dataBasePrinter(DataStorage))

    return lambda x, y: helper(x, y)


def listFunction() -> None:
    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        dataCount = DataStorage.getCount()
        if dataCount < 1:
            print(config.listMessage)
        else:
            print(config.listMessage)
            for position in range(dataCount):
                number = position + 1
                orderString = "{}.".format(number)
                taskString = taskPrinter.printTask(DataStorage.getItem(position))
                print(orderString+taskString)

    return lambda x, y: helper(x, y)


def markedFunction() -> None:

    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:

        if DataStorage.getCount() < 1:
            print(config.errorMessage)

        position = extractor.extractTargetIdOfTask(lst)
        task = DataStorage.getItem(position)
        task.markedTask()

        print(config.markedMessage)
        print(taskPrinter.printTask(task))

    return lambda x, y: helper(x, y)


def unmarkedFunction() -> None:

    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        if DataStorage.getCount() < 1:
            print(config.errorMessage)

        position = extractor.extractTargetIdOfTask(lst)
        task = DataStorage.getItem(position)
        task.unmarkedTask()

        print(config.unmarkedMessage)
        print(taskPrinter.printTask(task))
    return lambda x, y: helper(x, y)


def findFunction() -> None:

    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        dataCount = DataStorage.getCount()
        if dataCount < 1:
            print(config.errorMessage)
        else:
            print(config.findMessage)
            keyword = extractor.extractKeyWordOfTask(lst)
            for position in range(dataCount):
                task = DataStorage.getItem(position)
                temp = extractor.textSeparater(task.getTitle())
                if keyword == extractor.extractItem(temp):
                    print(taskPrinter.printTask(task))

    return lambda x, y: helper(x, y)


def deleteFunction() -> None:

    def helper(DataStorage: dataBase.DB, lst: list[str]) -> None:
        if DataStorage.getCount() < 1:
            print(config.errorMessage)

        position = extractor.extractTargetIdOfTask(lst)
        task = DataStorage.remmoveItem(position)
        print(config.deleteMessage)
        print(taskPrinter.printTask(task))
        print(taskPrinter.dataBasePrinter(DataStorage))

    return lambda x, y: helper(x, y)
