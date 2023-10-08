# Documentation for project Duke (Developer guide)

## Console Application (duke-cli)

- The entry point of the console application is duke-cli.py.  
- Application can be initialized by running the following command.  
```
python duke-cli.py
```
- That will run the program and call the "start()" function to print the greeting message.  
- And the program will initialize the Storage for tasks.  
- The Storage object is created by using a "class DB" from "database_model/dataBase.py".  
- A list with name "inputStringToList" is initialized to serve as a temp storage for incoming command.  
- A while loop is started and request for the input from the user.  
- While loop will run as long as the command "bye" is given.  
- The incoming text string is sparated by using "textSeparater()" function and then stored in the "inputStringToList" list.  
- Get the command Type from the "inputStringToList" with the help of "extractCommandType()" function.  
- Check for command Type and if wrong, call the "unknowCommand()" function to acknowledge the user and ask for the command again.  
- If the command is appropriate, call the function with respect to the command Type by using the "extractFunction()" function.  
- Call "spaceDottedSpace()" function for printing the separation between command.  
- When the user input the command "bye", the loop is exit and call the "end()" function at the end for printing the ending texts to the user.  

### Remark
- All the modules related to console application are stored in the console_model folder.  
- All the texts are saved in "config.py" inside the console_model folder.  

### Functions 
#### start.py 
- start()   -> Print the Greeting message.
#### end.py
- end()     -> Print Good Bye message
#### taskPrinter.py
- printingDottedLine()  -> Print dotted line.
- spaceDottedSpace()    -> Skip one line and print dotted line.
- unknowCommand()       -> Print the unknown command message.
- dataBasePrinter()     -> Take database object and print the count of the database.
- printTask()           -> Take the task object and print in format accordingly.
#### extractor.py
- textSeparater()           -> Take the incoming command text, split it by "space" and return the list of string of command.
- extractCommandType()      -> Take the list of string of command and return the command type.
- extractCommandTitle()     -> Take the list of string of command and return the command title.
- extractDeadLine()         -> Take the list of string of command and return the due_time.
- extractStartTimeForPlan() -> Take the list of string of command and return the start_time.
- extractEndTimeForPlan()   -> Take the list of string of command and return the end_time.
- extractTargetIdOfTask()   -> Take the list of string of command and return the id from command.
- extractKeyWordOfTask()    -> Take the list of string of command and return the keyword that user want to find.
- extractItem()             -> Take the command title and return the item name.
#### command_data.py

#### command_functions.py







## Web Application (duke-web)
- The entry point of the web application is duke-web.py.  
- Application can be initialized by running the following command.  
```
flask --app duke-web.py run
```

### Remark

### Functions 









## Classes
The applications are created 

### Task Class

### Task with DueTime
### Task with plan

### Database Class