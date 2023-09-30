from database_model import dataBase
from console_model import config, start, end, taskPrinter, extractor, command_data


if __name__ == "__main__":
    start.start()
    Storage = dataBase.DB()
    inputStringToList: list[str]
    while True:
        command = str(input(config.inputSign))
        if command == "bye":
            break
        taskPrinter.printingDottedLine()

        inputStringToList = extractor.textSeparater(command)

        if len(inputStringToList) == 0:
            taskPrinter.unknowCommand()
            continue
        commandType = extractor.extractCommandType(inputStringToList)
        if commandType not in command_data.choice:
            taskPrinter.unknowCommand()
            continue
        action = command_data.extractFunction(command_data.choice, commandType)  # type: ignore
        action(Storage, inputStringToList)
        taskPrinter.spaceDottedSpace()
    end.end()
