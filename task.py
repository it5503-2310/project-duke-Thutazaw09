import config
class Task():

    def __init__(self,command:str) -> None:
        self.command = command
        self.taskId = id
        self.taskName = None
        self.taskCatagory = None
        self.marked = False
        self.deadLine = None
        self.plan = None
      

    def setTaskName(self,task:str) -> None:
        self.taskName = task

    def setTaskCatagory(self,item:str) -> None:
        self.taskCatagory = item
         
    def setId(self,newId:int) -> None:
        self.taskId = newId

    def __str__(self) -> str: 
        if self.command == "todo":
            return "    [{}][{}] {} {}".format(config.todo_symbol,config.mark_symbol if self.marked else " ",self.taskName,self.taskCatagory)
        elif self.command == "deadline":
            return "    [{}][{}] {} {} {}".format(config.deadline_symbol,config.mark_symbol if self.marked else " ",self.taskName,self.taskCatagory,self.deadLine)
        elif self.command == "event":
            return "    [{}][{}] {} {} {}".format(config.event_symbol,config.mark_symbol if self.marked else " ",self.taskName,self.taskCatagory,self.plan)
        else:
            return " Error "
        
    def set_DeadLine(self,artical:str,duedate:str)-> None:
        art = artical[1:]
        self.deadLine = "("+art+": "+duedate+")"
    
    def set_start_and_end(self,art1:str,day:str,time_1:str,art2:str,time_2:str):
        a1 = art1[1:]
        a2 = art2[1:]
        self.plan = "("+a1+": "+day+" "+time_1+" "+a2+": "+time_2+")"
        
        

def markObj(obj:Task)->None:
    obj.marked = True
        
def unmarkObj(obj:Task)->None:
    obj.marked = False
        

# data structure fixing is required  
# delete 
# type problem needed to fix
