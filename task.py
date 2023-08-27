
class Task():

    def __init__(self,command:str) -> None:
        self.command = command
        self.taskId = id
        self.taskName = None
        self.taskCatagory = None
        self.deadLine = None
        self.event = None
        self.marked = False

    def setTaskName(self,task:str) -> None:
        self.taskName = task

    def setTaskCatagory(self,item:str) -> None:
        self.taskCatagory = item
         
    def setId(self,newId:int) -> None:
        self.taskId = newId


    def __str__(self) -> str:
        return str(self.taskName)

  
        


