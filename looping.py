import end
import config


def Looping(cmd:str):
    count = 0
    while cmd != "bye":
        print(config.dotted)
        
        break_task = cmd.split(" ")
        
        if len(break_task) == 0:
            print(config.falseCommand)
            
        
        elif break_task[0] == "todo":
            if len(break_task) < 1:
                print(config.emptyDescription_msg)
            else:
                print(config.taskOk_msg)
                count += 1
             
        else:
            print(config.falseCommand)
                
        cmd = str(input("> "))
    
    end.end()    
    
    
    
    