import end
import config
import task
from database import DB
def Looping(cmd:str):

    storage = DB()
    while cmd != "bye":
        print(config.dotted)
        
        break_task = cmd.split(" ")
        main_cmd = break_task[0]
        if len(break_task) == 0:
            print(config.falseCommand)
        elif main_cmd == "todo":
            if len(break_task) < 3:
                print(config.emptyDescription_msg)
            else:
                print(config.taskOk_msg)
                t = task.Task(break_task[0])
                t.setTaskName(break_task[1])
                t.setTaskCatagory(break_task[2])
                storage.addTask(t)
                print(t)
                print(storage.countTask())
        
        elif main_cmd == "deadline":
            if len(break_task) < 5:
                print(config.missing_arg_msg)
                continue
            else:
                print(config.taskOk_msg)
                d = task.Task(break_task[0])
                d.setTaskName(break_task[1])
                d.setTaskCatagory(break_task[2])
                d.set_DeadLine(break_task[3],break_task[4])
                storage.addTask(d)
                print(d)
                print(storage.countTask())
                      
        elif main_cmd == "event":
            if len(break_task) < 8:
                print(config.missing_arg_msg)
                continue
            else:
                print(config.taskOk_msg)
                e = task.Task(break_task[0])
                e.setTaskName(break_task[1])
                e.setTaskCatagory(break_task[2])
                e.set_start_and_end(break_task[3],break_task[4],break_task[5],break_task[6],break_task[7])
                storage.addTask(e)
                print(e)
                print(storage.countTask())
                
        
        elif main_cmd == "list":
            if storage.getCount() < 1:
                print(config.list_msg)
                continue
            else:
                print(config.list_msg)
                storage.listTask()
        
        elif main_cmd == "mark":
            if storage.getCount() < 1:
                print(config.error_msg)
            id = int(break_task[1])
            task.markObj(storage.accessTask(id)) 
            print(config.marked_msg)
            print(storage.accessTask(id))
            
        elif main_cmd == "unmark":
            if storage.getCount() < 1:
                continue
            id = int(break_task[1])
            task.unmarkObj(storage.accessTask(id))  # type: ignore
            print(config.unmark_msg)
            print(storage.accessTask(id))
            
        elif main_cmd == "find": 
            if storage.getCount() < 1:
                continue
            else:
                print(config.find_msg)
                storage.findByKeyword(break_task[1])
            
        elif main_cmd == "delete": 
            if storage.getCount() < 1:
                continue
            id = int(break_task[1])
            tsk = storage.removeTask(id)
            print(config.delete_msg)
            print(tsk)
            print(storage.countTask())
            
        else:
            print(config.falseCommand)

        print(config.space)
        print(config.dotted)  
        print(config.space)
        cmd = str(input(config.inputting_sign))
    
    end.end()    
    
    
    
    