from command_funcations import *

choice = {"todo":TodoFunction(),"deadline":deadLineFunction(),"event":eventFunction(),"find":findFunction(),"list":listFunction(),
              "mark":markedFunction(),"unmark":unmarkedFunction(),"delete":deleteFunction()}


def extractFunction(choiceDict:dict,key:str) -> any:
    return choiceDict[key]
