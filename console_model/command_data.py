
from console_model import command_funcations
from typing import Any
choice = {"todo": command_funcations.TodoFunction(), "deadline": command_funcations.deadLineFunction(), "event": command_funcations.eventFunction(), "find": command_funcations.findFunction(), "list": command_funcations.listFunction(),
          "mark": command_funcations.markedFunction(), "unmark": command_funcations.unmarkedFunction(), "delete": command_funcations.deleteFunction()}


def extractFunction(choiceDict: Any, key: str) -> Any:
    return choiceDict[key]
