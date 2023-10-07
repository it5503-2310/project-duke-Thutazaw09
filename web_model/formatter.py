from typing import Any


def dataFormatter(data: Any, id: int) -> Any:
    responseDict: dict[str, Any] = {}
    requestPayload: list[str] = ["due_time", "start_time", "end_time"]

    commandType: str = data["type"]
    commandPayload: dict[str, Any] = data["payload"]
    commandTitle: str = commandPayload["title"]

    responseDict["id"] = id
    responseDict["type"] = commandType
    responseDict["title"] = commandTitle
    responseDict["done"] = False  # default

    for name in requestPayload:
        if name in commandPayload:
            responseDict[name] = commandPayload[name]

    return responseDict
