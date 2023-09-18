import config
class Task():
    command     : str
    action      : str
    item        : str
    marked      : bool
    symbol      : str

    def __init__(self) -> None:
        self.command        = ""
        self.action         = ""
        self.item           = ""
        self.marked         = False
        self.symbol         = ""
        
    def setCommand(self,cmd:str) -> None: # todo borwoo book 
        self.command = cmd

    def setAction(self,act:str) -> None:
        self.action = act
    
    def setSymbol(self,syb:str) -> None:
        self.symbol = syb
        
    def setItem(self,itm:str) -> None:
        self.item = itm
        
    def getItem(self) -> str:
        return self.item
    
    def markedTask(self) -> None:
        self.marked = True
    
    def unmarkedTask(self) -> None:
        self.marked = False
    
    def symbolGenertor(self) -> str:
        return config.markedSymbol if self.marked else config.space
        
    def __str__(self) -> str:
        return "  [{}][{}] {} {}".format(self.symbol,self.symbolGenertor(),self.action,self.item)
         
    
class TaskWithDeadLine(Task):
    deadLine    : str
    hasDeadLine : bool
    
    def __init__(self) -> None:
        super().__init__()
        self.deadLine    = ""
        self.hasDeadLine = False
    
    def setDeadLine(self,date:str) -> None:
        self.deadLine = f"(by: {date})"
        self.hasDeadLine = True
        
    def __str__(self) -> str:
        return "  [{}][{}] {} {} {}".format(self.symbol,self.symbolGenertor(),self.action,self.item,self.deadLine)
        
class TaskWithPlan(Task):
    planTime    : str
    hasPlan     : bool
    
    def __init__(self) -> None:
        super().__init__()
        self.planTime = ""
        self.hasPlan  = False
        
    def setPlanTime(self,day:str,start:str,end:str) -> None:
        self.planTime = f"(from: {day} {start} to: {end})"
        self.hasPlan  = True
    
    def __str__(self) -> str:
        return "  [{}][{}] {} {} {}".format(self.symbol,self.symbolGenertor(),self.action,self.item,self.planTime)
    

# class for Task viewer
# controller has view 

