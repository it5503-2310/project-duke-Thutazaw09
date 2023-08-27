import end
import config
import task

def Looping(cmd:str):

    list_of_task = [object]
    while cmd != "bye":
        print(config.dotted)
        
        break_task = cmd.split(" ")
        if len(break_task) == 0:
            print(config.falseCommand)
            
        
        elif break_task[0] == "todo":
            
            if len(break_task) < 3:
                print(config.emptyDescription_msg)
            else:
                print(config.taskOk_msg)
              
                t = task.Task(break_task[0])
                t.setTaskName(break_task[1])
                t.setTaskCatagory(break_task[2])
                list_of_task.append(t) # type: ignore
                id = list_of_task.index(t) # type: ignore
                t.setId(id)

               
        
             
        else:
            print(config.falseCommand)

        print(" ")
        print(config.dotted)  
        print(" ")      
        cmd = str(input("> "))
    
    end.end()    
    
    
    
    