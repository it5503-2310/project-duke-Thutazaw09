
class Task():

    def __init__(self,command:str) -> None:
        self.command = command
        self.taskId = id
        self.task = None
        self.Item = None
        self.deadLine = None
        self.event = None
        self.marked = False

    def setTask(self,task:str) -> None:
        self.task = task

    def setItem(self,item:str) -> None:
        self.Item = item
         
    def changeId(self,newId:int) -> None:
        self.taskId = newId

    def __str__(self) -> str:
        return str(self.task)

  
        


