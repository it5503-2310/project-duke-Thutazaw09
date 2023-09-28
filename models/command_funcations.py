import config
from converter import *
from task import *
from database import DB

def TodoFunction() -> None:
    def helper(DataStorage:DB,lst:list[str]) -> None:
        if len(lst) < 3:
            print(config.emptyDescriptionTodoMessage)
         
        else:
            print(config.taskAddedMessage)
            command = extractCommand(lst)
            action  = extractAction(lst)
            item    = extractItem(lst)
            tsk = Task()
            
            tsk.setCommand(command)
            tsk.setAction(action)
            tsk.setItem(item)
            tsk.setSymbol(config.todoSymbol)
            DataStorage.addItem(tsk)
            print(tsk)
            print(DataStorage)
            
    return lambda x,y: helper(x,y)
        
def deadLineFunction()-> None:
    def helper(DataStorage:DB,lst:list[str]) -> None:
        if len(lst) < 5:
            print(config.missingArgumentMessage)
        else:
            print(config.taskAddedMessage)
            command = extractCommand(lst)
            action  = extractAction(lst)
            item    = extractItem(lst)
            deadLine= extractDeadLine(lst)
            
            tsk = TaskWithDeadLine()
            tsk.setCommand(command)
            tsk.setAction(action)
            tsk.setItem(item)
            tsk.setDeadLine(deadLine)
            tsk.setSymbol(config.deadlineSymbol)
            
            DataStorage.addItem(tsk)
            print(tsk)
            print(DataStorage)
            
    return lambda x,y: helper(x,y)


def eventFunction() -> None:
    def helper(DataStorage:DB,lst:list[str]) -> None:
        if len(lst) < 8:
            print(config.missingArgumentMessage)
               
        else:
            print(config.taskAddedMessage)
            command     = extractCommand(lst)
            action      = extractAction(lst)
            item        = extractItem(lst)
            planDay     = extractDayForPlan(lst)
            startTime   = extractStartTimeForPlan(lst)
            endTime     = extractEndTimeForPlan(lst)
            
            tsk = TaskWithPlan()
            tsk.setCommand(command)
            tsk.setAction(action)
            tsk.setItem(item)
            tsk.setPlanTime(planDay,startTime,endTime) 
            tsk.setSymbol(config.eventSymbol)
            
            DataStorage.addItem(tsk)
            print(tsk)
            print(DataStorage)
        
    return lambda x,y: helper(x,y)
        
def listFunction() -> None:
    def helper(DataStorage:DB,lst:list[str]) -> None:
        dataCount = DataStorage.getCount()
        if  dataCount < 1:
            print(config.listMessage)
        else:
            print(config.listMessage)
            for position in range(dataCount):
                number = position + 1
                orderString = "{}.".format(number)
                taskString  = str(DataStorage.getItem(position))
                print(orderString+taskString)
                
    return lambda x,y: helper(x,y)

def markedFunction() -> None:
    
    def helper(DataStorage:DB,lst:list[str]) -> None:
        
        if DataStorage.getCount() < 1:
            print(config.errorMessage)
            
        position = extractTargetIdOfTask(lst)
        tsk = DataStorage.getItem(position)
        tsk.markedTask()
        
        print(config.markedMessage)
        print(tsk)
        
    return lambda x,y: helper(x,y)

def unmarkedFunction() -> None:
    
    def helper(DataStorage:DB,lst:list[str]) -> None:
        if DataStorage.getCount() < 1:
            print(config.errorMessage)
            
        position = extractTargetIdOfTask(lst)
        tsk = DataStorage.getItem(position)
        tsk.unmarkedTask()
        
        print(config.unmarkedMessage)
        print(tsk)
    return lambda x,y: helper(x,y)

def findFunction() -> None:
   
    def helper(DataStorage:DB,lst:list[str]) -> None:
        dataCount = DataStorage.getCount()
        if  dataCount < 1:
            print(config.errorMessage)
        else:
            print(config.findMessage)
            keyword = extractKeyWordOfTask(lst)
            for position in range(dataCount):
                tsk = DataStorage.getItem(position)
                if keyword == tsk.getItem():
                    print(tsk)
                
    return lambda x,y: helper(x,y)

def deleteFunction() -> None:
    
    def helper(DataStorage:DB,lst:list[str]) -> None:
        if DataStorage.getCount() < 1:
            print(config.errorMessage)
            
        position = extractTargetIdOfTask(lst)
        tsk = DataStorage.remmoveItem(position)
        print(config.deleteMessage)
        print(tsk)
        print(DataStorage)
    
    return lambda x,y: helper(x,y)

    