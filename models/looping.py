import end
import config
from task import *
from database import DB
from converter import textSeparater,extractCommand
from command_data import choice,extractFunction

def Looping(cmd:str):
    
    inputStringToList : list[str]
  
    storage = DB()
    
    while cmd != "bye":
        print(config.dottedLine)  
        inputStringToList = textSeparater(cmd)
        
        if len(inputStringToList) == 0:
            print(config.unknownCommandMessage)
            continue
        command = extractCommand(textSeparater(cmd))
        
        if command not in choice:
            print(config.unknownCommandMessage)
            continue

        fun = extractFunction(choice,command)
        fun(storage,inputStringToList)
        
        print(config.space)
        print(config.dottedLine)  
        print(config.space)
        cmd = str(input(config.inputSign))

    end.end()    
    
    
    
    