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
                print(t)
                print("Now you have {} tasks in the list.".format(len(list_of_task)-1))
        
        elif break_task[0] == "deadline":
            if len(break_task) < 5:
                print(config.missing_arg_msg)
                continue
            else:
                print(config.taskOk_msg)
                d = task.Task(break_task[0])
                d.setTaskName(break_task[1])
                d.setTaskCatagory(break_task[2])
                d.set_DeadLine(break_task[3],break_task[4])
                list_of_task.append(d) # type: ignore
                id = list_of_task.index(d) # type: ignore
                d.setId(id)
                print(d)
                print("Now you have {} tasks in the list.".format(len(list_of_task)-1))
                
        
        elif break_task[0] == "event":
            if len(break_task) < 8:
                print(config.missing_arg_msg)
                continue
            else:
                print(config.taskOk_msg)
                e = task.Task(break_task[0])
                e.setTaskName(break_task[1])
                e.setTaskCatagory(break_task[2])
                e.set_start_and_end(break_task[3],break_task[4],break_task[5],break_task[6],break_task[7])
                list_of_task.append(e) # type: ignore
                id = list_of_task.index(e) # type: ignore
                e.setId(id)
                print(e)
                print("Now you have {} tasks in the list.".format(len(list_of_task)-1))
        
        elif break_task[0] == "list":
            if len(list_of_task) <= 1:
                print(config.list_msg)
                continue
            else:
                for i in range(1,len(list_of_task)):
                    print(i,"." + str(list_of_task[i]))# type: ignore 
        
        elif break_task[0] == "mark":
            if len(list_of_task) <= 1:
                continue
            id = int(break_task[1])
            task.markObj(list_of_task[id])  # type: ignore
            print(config.marked_msg)
            print(list_of_task[id])
            
        elif break_task[0] == "unmark":
            if len(list_of_task) <= 1:
                continue
            id = int(break_task[1])
            task.unmarkObj(list_of_task[id])  # type: ignore
            print(config.unmark_msg)
            print(list_of_task[id])
            
        elif break_task[0] == "find":
            if len(list_of_task) <= 1:
                continue
            for i in range(1,len(list_of_task)):
                if list_of_task[i].taskCatagory == break_task[1]: # type: ignore
                    print(list_of_task[i])
            
        elif break_task[0] == "delete": # update the the whole database not efficient at all should use with hashcode
            pass
         
        else:
            print(config.falseCommand)

       
        print(" ")
        print(config.dotted)  
        print(" ")      
        cmd = str(input("> "))
    
    end.end()    
    
    
    
    