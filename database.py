import task

class DB: # database of object
    def __init__(self) -> None:
        self.storage = [task.Task]
        self.count = 0
        
    def countTask(self) -> str:
        return "Now you have {} tasks in the list.".format(len(self.storage)-1) # type: ignore
    
    def addTask(self,obj:task.Task) -> None:
        self.storage.append(obj)  # type: ignore
        self.count += 1
    
    def removeTask(self,id:int) -> task.Task:
        self.count -= 1
        return self.storage.pop(id) # type: ignore
    
    def accessTask(self,id:int) -> task.Task:
        return self.storage[id] # type: ignore
        
    def listTask(self) -> None:
        for i in range(1,len(self.storage)):
            print(i,"." + str(self.storage[i]))
    
    def getCount(self) -> int:
        return self.count
    
    def findByKeyword(self,kwad:str)-> None: # print 
        for i in range(1,len(self.storage)):
            if self.storage[i].taskCatagory == kwad: # type: ignore
                print(self.storage[i])
            